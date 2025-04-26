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

