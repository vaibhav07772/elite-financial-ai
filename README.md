# elite-financial-ai
AI-powered financial RAG system using Hinglish LLM

# 🚀 Elite Financial AI (Hinglish RAG System)

## 📌 Overview

Elite Financial AI ek **AI-powered financial analysis system** hai jo company ke **annual reports (PDFs)** ko read karta hai aur user ke questions ka **Hinglish me intelligent answer** deta hai.

👉 Ye system ek **AI Financial Analyst** ki tarah kaam karta hai.

---

## 💡 Features

* 📄 PDF upload (single + multiple)
* 🧠 RAG-based intelligent search
* 🤖 Hinglish AI responses
* 📊 Financial ratio estimation
* 📉 Basic financial visualization (charts)
* 🌐 FastAPI backend + Streamlit UI

---

## 🧠 How It Works

```text
PDF → Text Extraction → Chunking → Embeddings → FAISS Search → LLM → Answer
```

### Step-by-step flow:

1. PDF upload hota hai
2. Text extract hota hai
3. Text chunks me split hota hai
4. Embeddings create hote hain
5. Relevant data search hota hai
6. LLM answer generate karta hai

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **LLM:** Fine-tuned Hinglish Model
* **Embeddings:** Sentence Transformers
* **Vector DB:** FAISS
* **PDF Processing:** pdfplumber
* **Visualization:** Matplotlib

---

## 📂 Project Structure

```
elite_finance_ai/
│── app.py
│── api.py
│── rag.py
│── utils.py
│── finance_utils.py
│── charts.py
│── requirements.txt
│── data/
│── model/
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/vaibhav07772/elite-financial-ai.git
cd elite-finance_ai
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 1️⃣ Start Backend

```
uvicorn api:app --reload
```

### 2️⃣ Start Frontend

```
streamlit run app.py
```

---

## 📊 Usage

1. Open Streamlit UI
2. Upload financial PDF reports
3. Ask questions like:

```
Company ka debt kaisa hai?
Risk high hai kya?
Financial condition explain karo
```

4. Get answers in Hinglish 🎯

---

## 📁 Dataset

### PDF Sources:

* Company Annual Reports
* Examples:

  * Tata
  * Reliance
  * HDFC Bank
  * ICICI Bank

👉 Google search:

```
"Tata annual report pdf"
```

---

## 🧠 Example Output

**Question:**
Company ka debt kaisa hai?

**Answer:**
Company ka debt moderate hai aur liabilities controlled level par hai...

---

## ⚠️ Limitations

* Financial ratios approximate hain
* PDF tables accurately parse nahi hote
* Model hallucination possible hai

---

## 🚀 Future Improvements

* 📊 Accurate table extraction (balance sheet parsing)
* 📈 Real financial ratio calculation
* 📡 Live stock market integration
* 🤖 Multi-agent reasoning system
* ☁️ Cloud deployment (Docker + Kubernetes)

---

## 🧑‍💻 Author

Vaibhav Singh

👉 Perfect for Data Scientist / NLP Engineer roles 🚀
