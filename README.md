# Agentorithm 🧑‍💻

Agentorithm is a sophisticated, multi-agent AI system designed to solve Data Structures and Algorithms (DSA) problems. Built with Microsoft's `AutoGen` framework, it leverages a collaborative team of AI agents to write, execute, and explain Python code for complex algorithmic challenges. The system ensures safe code execution by running all generated code within a secure Docker container.

This project offers two distinct ways to interact with the agent team:
1.  A command-line interface (`main.py`) for direct, scripted queries.
2.  An interactive web application (`app.py`) built with Streamlit for a dynamic, user-friendly experience.

---
## ✨ Key Features

* **Multi-Agent Collaboration:** Employs a `DSA_Problem_Solver_Agent` that designs the algorithm and a `CodeExecutorAgent` that safely runs the code in a Docker container.
* **Secure Code Execution:** All Python code is executed inside an isolated Docker environment, preventing any potential harm to the host machine.
* **Optimal Solutions:** The solver agent is designed to provide solutions with the best possible time complexity for any given DSA problem.
* **Interactive Web UI:** A user-friendly interface built with Streamlit allows you to input any DSA problem and watch the agents collaborate in real-time.
* **Modular Architecture:** The project is organized into a clean, modular structure, separating agents, configuration, and application logic for better maintainability.
* **Automated Testing:** The solver agent automatically generates multiple test cases to validate the correctness of its proposed solution.

---
## 🎬 Demo

Watch a live demo of Agentorithm solving a DSA problem through the Streamlit interface. Click the image below to view the video.

[![Agentorithm Demo Video](https://drive.google.com/uc?export=view&id=19P-IuUSICaEsI1ALYbLSO6ISLPLwbkTS)](https://drive.google.com/file/d/14do1V-5zKVW2YuqoAv6P7HRZvvki3cmi/view?usp=sharing)

---
## 🛠️ Getting Started

Follow these steps to set up and run the Agentorithm project on your local machine.

### Prerequisites

* [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* An [OpenAI API key](https://platform.openai.com/api-keys).

### 1. Clone the Repository

First, clone the project repository from GitHub.

```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/Agentorithm.git](https://github.com/YOUR_GITHUB_USERNAME/Agentorithm.git)
cd Agentorithm
```
**Note:** Remember to replace `YOUR_GITHUB_USERNAME` with your actual GitHub username.

### 2. Create and Activate Conda Environment

Create a dedicated Conda environment for the project using Python 3.12.

```bash
conda create -n agentorithm python=3.12 -y
conda activate agentorithm
```

### 3. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

You need to provide your OpenAI API key for the agents to function.

1.  Create a file named `.env` in the root directory of the project.
2.  Add your OpenAI API key to the file as shown below:

```env
OPENAI_API_KEY="sk-..."
```

---
## 🚀 Usage

Agentorithm can be run in two different modes.

### 1. Terminal Mode (`main.py`)

This mode runs a hardcoded DSA task directly in your terminal. It's useful for quickly testing the core agent logic. By default, the task is to "Write a python code to add two numbers."

To run it, execute the `main.py` script from the root directory:

```bash
python main.py
```

The script will stream the conversation between the agents as they solve the problem.

### 2. Interactive Web App (`app.py`)

This is the recommended way to use Agentorithm. It launches a local web server with a user-friendly Streamlit interface.

To start the web application, run the following command in your terminal from the root directory:

```bash
streamlit run app.py
```

This will open a new tab in your web browser at **http://localhost:8501**. You can then enter any DSA problem statement and click "Run" to see the agents work their magic.

---
## 📂 Project Structure

The project follows a modular structure to keep the code organized and maintainable.

```
Agentorithm/
├── agents/
│   ├── __pycache__/
│   ├── code_executor_agent.py
│   └── problem_solver.py
├── config/
│   ├── __pycache__/
│   ├── constant.py
│   ├── docker_executor.py
│   ├── docker_utils.py
│   └── settings.py
├── dir/
│   └── ... (working directory for the code executor)
├── team/
│   ├── __pycache__/
│   └── dsa_team.py
├── .env
├── app.py
├── main.py
└── requirements.txt
