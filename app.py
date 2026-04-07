import streamlit as st
import requests
from charts import plot_chart

st.title("🚀 Elite Financial AI")

files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
query = st.text_input("Ask your question")

if files and query:
    
    req_files = [("files", (f.name, f, "application/pdf")) for f in files]
    
    res = requests.post(
        "http://127.0.0.1:8000/analyze",
        files=req_files,
        params={"query": query}
    )
    
    data = res.json()
    
    st.write("### 🧠 Answer")
    st.write(data["answer"])
    
    st.write("### 📊 Ratios")
    st.json(data["ratios"])
    
    st.write("### 📉 Chart")
    fig = plot_chart()
    st.pyplot(fig)