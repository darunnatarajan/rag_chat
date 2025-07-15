import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.schema import Document

# Load environment variables
load_dotenv()

# 1. CREATE SAMPLE FILES DYNAMICALLY
print("1. Creating sample documents...")

# Create documents directory if it doesn't exist
if not os.path.exists("./documents"):
    os.makedirs("./documents")

# Sample content
sample_files = {
    "python_basics.txt": """
Python is a high-level programming language known for its simplicity and readability.
It was created by Guido van Rossum and first released in 1991.
Python is widely used in web development, data science, artificial intelligence, and automation.
The language emphasizes code readability and uses indentation to define code blocks.
""",
    
    "machine_learning.txt": """
Machine learning is a subset of artificial intelligence that enables computers to learn from data.
It involves algorithms that can identify patterns and make predictions without being explicitly programmed.
Common types include supervised learning, unsupervised learning, and reinforcement learning.
Popular applications include image recognition, natural language processing, and recommendation systems.
""",
    
    "rag_technology.txt": """
RAG stands for Retrieval Augmented Generation.
It is a technique that combines information retrieval with text generation.
RAG systems first retrieve relevant documents from a knowledge base.
Then they use this context to generate more accurate and informed responses.
This approach helps reduce hallucinations in AI-generated content.
"""
}

# Create the files
for filename, content in sample_files.items():
    file_path = os.path.join("./documents", filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content.strip())
    print(f"Created: {filename}")

# 2. DOCUMENT LOADER - Load the created files
print("\n2. Loading documents...")
documents = []

for filename in os.listdir("./documents"):
    if filename.endswith(".txt"):
        file_path = os.path.join("./documents", filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            doc = Document(page_content=content, metadata={"source": filename})
            documents.append(doc)
            print(f"Loaded: {filename}")

print(f"Total loaded: {len(documents)} documents")

# 3. TEXT SPLITTER - Split documents into chunks
print("\n3. Splitting text...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
splits = text_splitter.split_documents(documents)
print(f"Created {len(splits)} text chunks")

# 4. EMBEDDINGS - Convert text to vectors
print("\n4. Creating embeddings...")
embeddings = OpenAIEmbeddings()

# 5. VECTOR STORE - Store embeddings in database
print("\n5. Creating vector store...")
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings
)

# 6. LLM - Set up the language model
print("\n6. Setting up LLM...")
llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")

# 7. QA CHAIN - Connect everything together
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# 8. EXECUTE - Ask questions
print("\n" + "="*50)
print("RAG System Ready! Ask your questions:")
print("Available topics: Python, Machine Learning, RAG")
print("="*50)

# Sample questions to try
sample_questions = [
    "What is Python?",
    "What is machine learning?", 
    "What does RAG stand for?",
    "Who created Python?",
    "What are types of machine learning?"
]

print("\nSample questions you can ask:")
for i, q in enumerate(sample_questions, 1):
    print(f"{i}. {q}")

while True:
    question = input("\nQuestion: ")
    if question.lower() == 'quit':
        break
    
    answer = qa_chain.invoke({"query": question})
    print(f"Answer: {answer['result']}")