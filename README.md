## 📚 RAG Chat Bot

A simple Retrieval-Augmented Generation (RAG) chatbot using LangChain, HuggingFace embeddings, and the Groq LLM. It indexes local `.txt` files and answers questions based only on the content of those files.

---

### 📦 Features

* Loads `.txt` documents from a folder
* Splits content into chunks
* Generates vector embeddings using HuggingFace
* Stores embeddings in memory
* Uses Groq LLM for answering questions
* Returns document-based answers (with optional fallback to LLM if needed)

---

### 🏗️ Project Structure

```
rag_chat_bot/
│
├── rag_demo.py           # Main script to run the RAG chatbot
├── documents/            # Folder containing your .txt files
│   ├── python_basics.txt
│   ├── machine_learning.txt
│   └── rag_technology.txt
├── .venv/                # Optional: Your virtual environment
└── README.md             # This file
```

---

### ⚙️ Setup Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/darunnatarajan/rag_chat_bot.git
cd rag_chat_bot
```

#### 2. Create a virtual environment and activate it

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can use:

```bash
pip install langchain langchain-huggingface huggingface-hub groq
```

---

### 🔑 Environment Variables

Create a `.env` file or set environment variables manually with your API key for Groq.

```bash
export GROQ_API_KEY="your-groq-api-key"
```

Or on Windows (PowerShell):

```powershell
$env:GROQ_API_KEY = "your-groq-api-key"
```

---

### 🚀 Run the Chat Bot

```bash
python rag_demo.py
```

You will see:

```
==================================================
RAG System Ready! Ask your questions:
Available topics: Python, Machine Learning, RAG
==================================================
```

Example prompts:

* What is Python?
* Who created Python?
* What does RAG stand for?

Type `'quit'` to exit the chat.

---

### 🧠 How It Works

1. **Document Loading**: Loads `.txt` files from the `documents/` folder.
2. **Chunking**: Breaks each file into manageable pieces.
3. **Embedding**: Converts text chunks into vectors using HuggingFace embeddings.
4. **Vector Store**: Stores those vectors in memory for fast retrieval.
5. **Querying**: When you ask a question, it:

   * Retrieves the most relevant chunks
   * Passes them to the Groq LLM to generate an answer

---

### 📝 Add Your Own Files

Place your `.txt` files into the `documents/` folder. The bot will automatically load and index them on startup.

---

### ✅ Example Output

```
Question: What is Python?
Answer: Python is a high-level programming language known for its simplicity and readability.
```

---

### 📌 Notes

* The LLM (Groq) may fall back to its own internal knowledge **only** if nothing is retrieved — this can be disabled if you want document-only answers.
* You can customize chunk size, embedding model, or LLM settings in the script.

---

### 📄 License

MIT License.