# answer_agent.py
from transformers import pipeline
import os
from dotenv import load_dotenv
from huggingface_hub import login

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face API token from the .env file
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Ensure Hugging Face API token exists
if not hf_token:
    raise ValueError("Hugging Face API token is missing in the environment variables.")

# Authenticate with the Hugging Face Hub
login(token=hf_token)

# Choose the model dynamically (you can replace this with another model name)
model_name = os.getenv("MODEL_NAME", "gpt2")
qa_model = pipeline("text-generation", model=model_name)

def draft_answer(state: dict) -> dict:
    context = state.get("context", "")
    question = "What is the main idea of this research?"
    prompt = f"Use the following context to answer the question:\nContext: {context}\nQuestion: {question}\nAnswer:"
    try:
        # Generate text with the model
        output = qa_model(prompt, max_new_tokens=300, do_sample=True)[0]["generated_text"]
        # print("29output", output)
        
        # Extract the answer part from the generated text
        answer = output.split("Answer:")[-1].strip()
        # print("33answer", answer)
        
        return {
            **state,
            "answer": answer if answer else "I'm sorry, I couldn't generate a relevant answer."
        }
    except Exception as e:
        print(f"Error during text generation: {e}")
        return {
            **state,
            "answer": "An error occurred while generating the answer."
        }
    
    
# if __name__ == "__main__":
#     # Test context and question
#     test_context = (
#         "AI research is progressing quickly with new innovations in machine learning and neural networks. "
#         "Transformers and reinforcement learning are particularly popular."
#     )
#     test_question = "What are the current trends in AI research?"
    
#     # Generate and print the answer
#     answer = draft_answer(test_context, test_question)
#     print("\nGenerated Answer:\n", answer)

# if __name__ == "__main__":
#     # Test context and question
#     test_context = (
#         "The process of photosynthesis in plants involves converting light energy into chemical energy. "
#         "It takes place primarily in the chloroplasts of plant cells."
#     )
#     test_question = "How do plants convert light into energy?"

#     # Generate and print the answer
#     answer = draft_answer(test_context, test_question)
#     print("\nGenerated Answer:\n", answer)



# import os
# import test_openai_api_call
# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# class AnswerAgent:
#     def __init__(self):
#         self.token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
#         if not self.token:
#             raise ValueError("API token is required.")
        
#         # Set OpenAI API key
#         test_openai_api_call.api_key = self.token  # Use the same token for OpenAI API key
        
#     def generate_answer(self, input_text):
#         """Generate an answer using GPT-3.5-turbo."""
#         try:
#             response = test_openai_api_call.Completion.create(
#                 model="gpt-3.5-turbo",  # Use OpenAI's model identifier
#                 prompt=input_text,
#                 max_tokens=150
#             )
#             return response.choices[0].text.strip()
#         except Exception as e:
#             return f"Error: {str(e)}"

# # Example usage:
# if __name__ == "__main__":
#     # Initialize Answer Agent
#     agent = AnswerAgent()

#     # Sample input (this should be the research data or a question)
#     question = "What is artificial intelligence?"

#     # Generate answer
#     answer = agent.generate_answer(question)
#     print("Answer generated:", answer)



# # answer_agent.py
# import os
# from dotenv import load_dotenv
# from langchain_huggingface import HuggingFaceEndpoint  # Using langchain_huggingface directly
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# load_dotenv()  # Load environment variables

# # Initialize the Hugging Face LLM (free)
# llm = HuggingFaceEndpoint(
#     repo_id="tiiuae/falcon-7b-instruct",  # or another text-generation-supported model
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#     temperature=0.5,
#     max_new_tokens=256
# )

# def draft_answer(context: str) -> str:
#     try:
#         prompt = PromptTemplate(
#             input_variables=["context"],
#             template=""" 
#             Based on the following research results, draft a clear and concise answer to the user's query.
#             Research Results: {context}
#             Answer:
#             """
#         )

#         # Create an LLMChain with the prompt and LLM
#         chain = LLMChain(llm=llm, prompt=prompt)

#         # Use the LLMChain to generate the response
#         response = chain.run({"context": context})
        
#         return response.strip()
#     except Exception as e:
#         print(f"❌ Error in drafting answer: {e}")
#         return "Sorry, I couldn't generate an answer at the moment."

# if __name__ == "__main__":
#     test_context = """
#     AI research is rapidly advancing, with new models and algorithms emerging.
#     Recent studies focus on reinforcement learning and generative models.
#     """
#     answer = draft_answer(test_context)
#     print(f"Generated Answer: {answer}")



# import os
# from dotenv import load_dotenv
# # from langchain_community.llms import HuggingFaceHub
# from langchain_huggingface import HuggingFaceEndpoint
# from langchain.prompts import PromptTemplate

# # from langchain.chat_models import ChatOpenAI
# # from langchain_community.chat_models import ChatOpenAI
# # from langchain_openai import ChatOpenAI

# # from langchain.schema import HumanMessage, SystemMessage
# # from langchain.prompts import PromptTemplate
# # from langchain.chains import LLMChain

# load_dotenv()  # Load environment variables

# # Initialize the OpenAI LLM (e.g., GPT-4)
# # llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
# # print("open api instance", llm)
# # print("open api Key", os.getenv("OPENAI_API_KEY"))

# # Initialize the Hugging Face LLM (free)
# # llm = HuggingFaceHub(
# #     repo_id="google/flan-t5-large",  # You can try "tiiuae/falcon-7b-instruct" or others too
# #     model_kwargs={"temperature": 0.5, "max_new_tokens": 256}
# # )
# llm = HuggingFaceEndpoint(
#     repo_id="tiiuae/falcon-7b-instruct",  # or any text-generation-supported model
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#     temperature=0.5,
#     max_new_tokens=256
# )

# def draft_answer(context: str) -> str:
#     try:
#         prompt = PromptTemplate(
#             input_variables=["context"],
#             template="""
#             Based on the following research results, draft a clear and concise answer to the user's query.
#             Research Results: {context}

#             Answer:
#             """
#         )
#         chain = prompt | llm
#         response = chain.invoke({"context": context})
#         return response.strip()
#     except Exception as e:
#         print(f"❌ Error in drafting answer: {e}")
#         return "Sorry, I couldn't generate an answer at the moment."

# if __name__ == "__main__":
#     test_context = """
#     AI research is rapidly advancing, with new models and algorithms emerging.
#     Recent studies focus on reinforcement learning and generative models.
#     """
#     answer = draft_answer(test_context)
#     print(f"Generated Answer: {answer}")