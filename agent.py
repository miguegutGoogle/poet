# Copyright 2025 Google LLC
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

"""Poet coordinator: create beautiful poetry from simple descriptions"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.muse import muse_agent
from .sub_agents.architect import architect_agent
from .sub_agents.scribe import scribe_agent
from .sub_agents.critic import critic_agent
from .sub_agents.wordsmith import wordsmith_agent

MODEL = "gemini-2.5-pro"


poet_coordinator = LlmAgent(
    name="poet_coordinator",
    model=MODEL,
    description=(
        "guides users through structured process to create a poem"
        "by orchestrating a series of expert subagents"
    ),
    instruction=prompt.POET_COORDINATOR_PROMPT,
    output_key="poet_coordinator_output",
    tools=[
        AgentTool(agent=muse_agent),
        AgentTool(agent=architect_agent),
        AgentTool(agent=scribe_agent),
        AgentTool(agent=critic_agent),
        AgentTool(agent=wordsmith_agent),
    ],
)

root_agent = poet_coordinator
