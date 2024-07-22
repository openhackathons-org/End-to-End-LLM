# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nemoguardrails import LLMRails
from nemoguardrails.actions import action
from nemoguardrails.actions.actions import ActionResult
from nemoguardrails.utils import new_event_dict


@action(is_system_action=True)
async def generate_user_intent():
    return ActionResult(events=[{"type": "UserIntent", "intent": "ask question"}])


@action(is_system_action=True)
async def generate_next_step():
    return ActionResult(events=[{"type": "BotIntent", "intent": "respond to question"}])


@action(is_system_action=True)
async def generate_bot_message():
    return ActionResult(
        events=[new_event_dict("StartUtteranceBotAction", script="How are you doing?")],
    )


def init(app: LLMRails):
    app.register_action(generate_user_intent)
    app.register_action(generate_next_step)
    app.register_action(generate_bot_message)
