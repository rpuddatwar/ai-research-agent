# research_agent.py

import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()  # Load API keys from .env

# Initialize Tavily client
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def perform_research(state: dict) -> dict:
    query = state.get("query", "")
    try:
        print(f"🔍 Running Tavily search for: {query}")
        search_results = tavily.search(query, max_results=5)

        # Combine content from results into context
        context = "\n".join([res.get("content", "") for res in search_results.get("results", [])])

        return {
            "query": query,
            "context": context,
            "answer": ""
        }

    except Exception as e:
        print(f"❌ Tavily API Error: {e}")
        return {
            "query": query,
            "context": "",
            "answer": "Error occurred during research."
        }

# Test query
# query = "latest AI research"
# query = "terror attack"
# results = perform_research(query)

# if results:
#     print(f"Found {len(results)} results:")
#     for i, result in enumerate(results, start=1):
#         print(f"{i}. {result['title']} - {result['url']}")
# else:
#     print("No results found.")