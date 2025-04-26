AI Research Agent
This project is a Deep Research AI Agentic System developed as part of a Qualifying Assignment.
It automates deep online research using Tavily, organizes the information with LangGraph & LangChain, and drafts detailed answers using Hugging Face models.

✨ Features
📚 Research Agent: Crawls the web for information using Tavily API.
✍️ Answer Drafter Agent: Drafts detailed answers from the research context using Hugging Face models.
🔗 Agent Orchestration: Built using LangGraph and LangChain for smooth multi-agent flow.
🛡️ Environment Variables: Securely managed via .env file (example provided).

⚙️ Setup Instructions

Clone the repository:
git clone https://github.com/your-username/ai-research-agent.git
cd ai-research-agent

Create and activate a virtual environment:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Set up environment variables:
Create a .env file (or copy from .env.example) and add your API keys:
TAVILY_API_KEY=your_tavily_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here

Run the project:
python agent_flow.py

📋 Environment Variables

Variable	Description
TAVILY_API_KEY	API Key for Tavily Search
HUGGINGFACEHUB_API_TOKEN	Hugging Face Hub Token for model access
MODEL_NAME (optional)	Model name from Hugging Face (default: gpt2)

🔥 How it Works
Step 1: User provides a research query.
Step 2: research_agent.py fetches information from the web using Tavily.
Step 3: answer_agent.py generates an intelligent answer based on the research context.
Step 4: Results are printed to the console.

📜 Example
Query: What does a UI/UX designer do?
Final Answer: A UI/UX designer focuses on enhancing user satisfaction by improving the usability, accessibility, and overall interaction between the user and the product.

🛠️ Tech Stack
Python 3
Tavily API
Hugging Face Transformers
LangGraph
LangChain
dotenv

📎 License
This project is for educational/demo purposes only.
Feel free to improve or extend it! 🚀