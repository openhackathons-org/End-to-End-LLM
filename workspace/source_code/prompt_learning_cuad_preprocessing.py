# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
import json
from tqdm import tqdm
"""
Dataset preprocessing script for the CUAD dataset: 
Converts the dataset into a jsonl format that can be used for p-tuning/prompt tuning in NeMo. 
Inputs:
    data-dir: (str) The directory where the cuad dataset was downloaded, files will be saved here
    train-file: (str) Name of train set file
    dev-file: (str) Name of dev set file
    save-name-base: (str) The base name for each of the train, val, and test files. If save-name-base were 'cuad' for
                    example, the files would be saved as cuad_train.jsonl, cuad_val.jsonl, and cuad_test.jsonl
    include-topic-name: Whether to include the topic name for the paragraph in the data json. See the cuad explaination
                        below for more context on what is meant by 'topic name'.
    random-seed: (int) Random seed for repeatable shuffling of train/val/test splits. 
Saves train, val, and test files for the cuad dataset. The val and test splits are the same data, because the given test
split lacks ground truth answers. 
An example of the processed output written to file:
    {
"taskname": "cuad", 
"context": "Exhibit 10.2 PORTIONS OF THIS EXHIBIT MARKED BY [**] HAVE BEEN OMITTED PURSUANT TO RULE 601(B)(10) OF REGULATION S-K. THE OMITTED INFORMATION IS (I) NOT MATERIAL AND (II) WOULD LIKELY CAUSE COMPETITIVE HARM TO THE REGISTRANT IF PUBLICLY DISCLOSED. EXECUTION VERSION STRATEGIC ALLIANCE AGREEMENT STRATEGIC ALLIANCE AGREEMENT, dated as of December 20, 2019 (as amended, supplemented or otherwise modified from time to time, this \"Agreement\"), by and among Farids & Co. LLC, a Delaware limited liability company (\"Farids\"), Edible Arrangements, LLC, a Delaware limited liability company (\"EA\"), and Rocky Mountain Chocolate Factory, Inc., a Delaware corporation (the \"Company\"). W I T N E S S E T H: WHEREAS, the Company is an international franchisor, confectionery manufacturer and retail operator; WHEREAS, Farids is a holding company and, together with TF (as defined below), indirectly controls EA; WHEREAS, EA is a US-based franchisor that specializes in fresh fruit arrangements and specialty fruit gift items; WHEREAS, the Company desires to issue and sell,...If the foregoing applies, the Parties shall use all reasonable endeavours to agree within a reasonable time upon any lawful and reasonable  variations to the     18\n\n\n\n\n\n     Agreement which may be necessary in order to achieve, to the greatest extent possible, the same effect as would have been achieved by  the Clause, or the part of the Clause, in question.     22 GOVERNING LAW     22.1 This Agreement is governed by English law.     22.2 The Parties submit to the non-exclusive jurisdiction of the courts of England and Wales.     This Agreement shall come into force on the date given at the beginning of this Agreement.\n\n   19\n\nSIGNED by\n\n   )        )  (name),                     )   a duly authorised signatory of     ) (signature)  SHBV (HONG KONG) LTD            )\n\nSIGNED by\n\n      )           )  (name),\n\n\n\n\n\n     )\n\na duly authorised signatory of     ) (signature)  WASTE2ENERGY GROUP HOLDINGS PLC      )", 
"question": "Highlight the parts (if any) of this contract related to \"Document Name\" that should be reviewed by a lawyer. Details: The name of the contract",
"answer": "STRATEGIC ALLIANCE AGREEMENT, d"
    },
"""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, default=".")
    parser.add_argument("--train-file", type=str, default="train_dataset.json")
    parser.add_argument("--dev-file", type=str, default="test_dataset.json")
    parser.add_argument("--save-name-base", type=str, default="cuad")
    parser.add_argument("--include-topic-name", action='store_true')
    parser.add_argument("--random-seed", type=int, default=1234)
    parser.add_argument("--sft-format", action='store_true')
    args = parser.parse_args()
    train_data_dict = json.load(open(f"{args.data_dir}/{args.train_file}"))
    dev_data_dict = json.load(open(f"{args.data_dir}/{args.dev_file}"))
    train_data = train_data_dict['data']
    val_data = dev_data_dict['data']
    save_name_base = f"{args.data_dir}/{args.save_name_base}"
    process_data(train_data, val_data, save_name_base, args.include_topic_name, args.sft_format)
def process_data(train_data, val_data, save_name_base, include_topic, sft_format):
    train_set = extract_questions(train_data, include_topic, sft_format, split="train")
    val_set = extract_questions(val_data, include_topic, sft_format, split="val")
    test_set = extract_questions(val_data, include_topic, sft_format, split="test")
    gen_file(train_set, save_name_base, 'train', sft_format)
    gen_file(val_set, save_name_base, 'val', sft_format)
    gen_file(test_set, save_name_base, 'test', sft_format, make_ground_truth=True)
    gen_file(test_set, save_name_base, 'test', sft_format, make_ground_truth=False)
def extract_questions(data, include_topic, sft_format, split):
    processed_data = []
    # Iterate over topics, want to keep them seprate in train/val/test splits
    for question_group in data:
        processed_topic_data = []
        topic = question_group['title']
        questions = question_group['paragraphs']
        # Iterate over paragraphs related to topics
        for qa_group in questions:
            context = qa_group['context']
            qas = qa_group['qas']
            # Iterate over questions about paragraph
            for qa in qas:
                question = qa['question']
                try:
                    # Dev set has multiple right answers. Want all possible answers in test split ground truth
                    if split == "test":
                        answers = [qa['answers'][i]['text'] for i in range(len(qa['answers']))]
                    # Choose one anser from dev set if making validation split, train set only has one answer
                    else:
                        answers = qa['answers'][0]["text"]
                except IndexError:
                    continue
                if sft_format:
                    example_json = {
                        "input": f"User: Context:{context} Question:{question}\n\nAssistant:",
                        "output": answers,
                    }
                else:
                    example_json = {"taskname": "cuad", "context": context, "question": question, "answer": answers}
                if include_topic:
                    example_json["topic"] = topic
                processed_topic_data.append(example_json)
        processed_data.extend(processed_topic_data)
    return processed_data
def gen_file(data, save_name_base, split_type, sft_format, make_ground_truth=False):
    save_path = f"{save_name_base}_{split_type}.jsonl"
    if make_ground_truth:
        save_path = f"{save_name_base}_{split_type}_ground_truth.jsonl"
    print(f"Saving {split_type} split to {save_path}")
    with open(save_path, 'w') as save_file:
        for example_json in tqdm(data):
            # Dont want labels in the test set
            if split_type == "test" and not make_ground_truth:
                if sft_format:
                    example_json["output"] = ""
                else:
                    del example_json["answer"]
            save_file.write(json.dumps(example_json) + '\n')
if __name__ == "__main__":
    main()









