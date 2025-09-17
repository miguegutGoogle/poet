# AI Poetic Collaborator

## Overview

The **AI Poetic Collaborator** is an advanced, multi-agent system designed to guide users through the complete creative process of writing a poem. It transforms a simple theme or idea into a polished, final piece by orchestrating a team of five specialized AI **sub-agents**.

This agent is built to make the complex process of creative writing structured and collaborative, providing expert assistance at every stage: from initial brainstorming to critical review and final refinement.

### The Five-Agent Creative Process

The collaborator works through a structured, five-step workflow, with the user providing feedback and approvals after each step:

1.  **Brainstorming & Inspiration:** The **Muse Agent** generates creative concepts based on the user's initial theme, topic, or mood.
2.  **Designing the Blueprint:** The **Architect Agent** takes the concept and designs a poetic structure (e.g., meter, rhyme scheme, stanza count) to serve as the poem's foundation.
3.  **Writing the First Draft:** The **Scribe Agent** synthesizes the concept and the blueprint to produce the first draft of the poem.
4.  **Critical Review:** The **Critic Agent** analyzes the draft, providing detailed feedback on its strengths and areas for improvement.
5.  **Polishing the Poem:** The **Wordsmith Agent** uses the original draft and the critic's feedback to produce the final, polished version.

---

## Agent Details

The **AI Poetic Collaborator** is designed for an easy-to-use, conversational experience.

| Feature | Description |
| :--- | :--- |
| **Interaction Type** | Conversational |
| **Complexity** | Easy |
| **Agent Type** | Multi-Agent (5 sub-agents) |
| **Components** | No external tools required |
| **Vertical** | Education / Creative Writing |

### Agent Architecture

This diagram illustrates the detailed architecture of the main collaborator agent and its five sub-agents:

<img src="poetic-collaborator.svg" alt="AI Poetic Collaborator Architecture" width="800"/>

---

## Setup and Installation

### 1. Prerequisites

* **Python 3.11+**
* **Poetry**
    * For dependency management and packaging. Please follow the instructions on the official [Poetry website](https://python-poetry.org/docs/) for installation.

    ```bash
    pip install poetry
    ```

* A project on **Google Cloud Platform**
* **Google Cloud CLI**
    * For installation, please follow the instruction on the official [Google Cloud website](https://cloud.google.com/sdk/docs/install).

### 2. Installation

```bash
# Clone this repository.
git clone [https://github.com/miguegutGoogle/poet.git](https://github.com/miguegutGoogle/poet.git)
cd poet/python/agents/poetic-collaborator # Assuming the agent is located here inside the 'poet' repo
# Install the package and dependencies.
# Note for Linux users: If you get an error related to `keyring` during the installation, you can disable it by running the following command:
# poetry config keyring.enabled false
# This is a one-time setup.
poetry install
