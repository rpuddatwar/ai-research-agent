
# AI Research Agent

This project is a Deep Research AI Agentic System. It automates deep online research using Tavily, organizes the information with LangGraph & LangChain, and drafts detailed answers using Hugging Face models.

✨ **Features**
- 📚 **Research Agent**: Crawls the web for information using Tavily API.
- ✍️ **Answer Drafter Agent**: Drafts detailed answers from the research context using Hugging Face models.
- 🔗 **Agent Orchestration**: Built using LangGraph and LangChain for smooth multi-agent flow.

⚙️ **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-research-agent.git
   cd ai-research-agent
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file (or copy from `.env.example`) and add your API keys:
     ```
     TAVILY_API_KEY=your_tavily_api_key_here
     HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
     ```

5. **Run the project**:
   ```bash
   python agent_flow.py
   ```

📋 **Environment Variables**

| Variable                   | Description                                                   |
|----------------------------|---------------------------------------------------------------|
| `TAVILY_API_KEY`            | API Key for Tavily Search                                     |
| `HUGGINGFACEHUB_API_TOKEN`  | Hugging Face Hub Token for model access                       |


🔥 **How it Works**

1. User provides a research query.
2. `research_agent.py` fetches information from the web using Tavily.
3. `answer_agent.py` generates an intelligent answer based on the research context.
4. Results are printed to the console.

📜 **Example**

**Query:** What does a UI/UX designer do?

**Final Answer:** A UI/UX designer focuses on enhancing user satisfaction by improving the usability, accessibility, and overall interaction between the user and the product.

🛠️ **Tech Stack**

- Python 3
- Tavily API
- Hugging Face Transformers
- LangGraph
- LangChain
- dotenv
