## Developmet Team - LLMs for coding

## Introduction

This project utilizes large language models (LLMs) and conversational AI frameworks to create coding assistants and collaborative teams. It offers different tools and approaches to help developers with various tasks, from suggesting code fixes to generating code snippets based on natural language descriptions.

## Usage

This project primarily consists of Jupyter Notebooks and Python scripts. Here's a general usage guide:

**1. Prerequisites:**

* Ensure you have Python 3 installed.
* Create a virtual environment (recommended) and activate it.
* Install the required libraries:

```bash
pip install -r requirements.txt
```

* Set environment variables:
    * Create a `.env` file in the project root directory.
    * Add the following lines, replacing placeholders with your actual values:
        ```
        OPENAI_API_KEY=your_openai_api_key
        # Add other environment variables as needed
        ```
    * Load the environment variables using `import os` and `os.getenv` in your scripts.

**2. Choose a Script/Notebook:**

* **LinuxKernelLangchain.ipynb:** Explore LLM-based solutions for Linux kernel tasks.
* **LinuxKernelRag.ipynb:** Experiment with RAG-powered agents for Linux kernel development assistance.
* **LinuxKernelTeam.py:** Run a simulated team chat for collaborative Linux kernel problem-solving.
* **SettelmentChatTeam.ipynb:** Utilize SettlementChat for team-like code development conversations.
    * **Note:** This notebook might require additional setup or dependencies.

**3. Follow Notebook/Script Instructions:**

Each notebook and script has its own specific instructions within the file. Carefully read and follow them for proper execution.

**4. Input and Prompts:**

* Some components may require user input or prompts to guide the LLMs. Provide clear and relevant information to achieve desired outcomes.

**5. Output and Results:**

Each component produces its own output, such as code suggestions, answers to questions, or conversation summaries. Interpret and utilize the results based on your task and goals.

## Dependencies

* Refer to the `requirements.txt` file for a complete list of dependencies.

## .env File and CONFIG_FILE.json

* **.env file:** Stores sensitive information like API keys for secure management.
* **CONFIG_FILE.json:** Contains configuration options for LLM models, agents, and other elements. See individual notebooks/scripts for details.

## Project Structure

This project is organized into several folders:

* **notebooks:**
    * Explore LLM solutions for specific tasks.
    * Utilize SettlementChat for team collaborations.
    * Run a simulated team chat for collaborative problem-solving.
* **configs:**
    * Securely manage API keys and other sensitive information.
    * Configure LLM models, agents, and other elements.
* **prompts:**
    * Text prompts to guide LLMs for various tasks.
* **rag:**
    * Content used by RAG components, including documentation and knowledge sources.
* **outputs:**
    * Content used by RAG components, including documentation and knowledge sources.