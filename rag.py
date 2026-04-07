from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from utils import extract_text, chunk_text
from finance_utils import calculate_ratios

# Load embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your fine-tuned model
model_path = "microsoft/phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_path)
llm = AutoModelForCausalLM.from_pretrained(model_path)

def build_index(chunks):
    embeddings = embed_model.encode(chunks)
    
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    
    return index

def search(query, index, chunks):
    query_vec = embed_model.encode([query])
    
    D, I = index.search(query_vec, k=5)
    
    return [chunks[i] for i in I[0]]

def generate_answer(query, context):
    prompt = f"""
    Tum ek financial expert ho.

    Context:
    {context}

    Question:
    {query}

    Hinglish me answer do.
    """

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = llm.generate(**inputs, max_new_tokens=150)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def run_rag(pdf_paths, query):
    all_chunks = []
    full_text = ""
    
    for pdf in pdf_paths:
        text = extract_text(pdf)
        full_text += text
        
        chunks = chunk_text(text)
        all_chunks.extend(chunks)
    
    index = build_index(all_chunks)
    context = search(query, index, all_chunks)
    
    answer = generate_answer(query, "\n".join(context))
    
    ratios = calculate_ratios(full_text)
    
    return answer, ratios