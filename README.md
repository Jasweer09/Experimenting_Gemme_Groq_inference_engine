# Gemma Model Q&A ChatBot

## Overview
This is a **user-friendly Q&A chatbot** built with **Streamlit** that answers questions based on PDF documents stored in the `us_census` folder. It uses the **Gemma2-9B-IT** model powered by **Groq** for fast and accurate responses, along with **Google Generative AI Embeddings** to process and understand documents. The app splits documents into smaller chunks, stores them in a **FAISS vector store**, and retrieves relevant information to answer your queries.

---

## Why Groq is Awesome Compared to Ollama
- **Super Fast**: Groq’s special hardware (LPU) answers questions in a flash—up to **800+ words per second**! Ollama, running on your computer, is slower, especially without a powerful GPU.
- **No Fancy Hardware Needed**: Groq works in the cloud, so you don’t need an expensive computer. Ollama needs a strong PC or laptop to run big models like Gemma.
- **Easy to Scale**: Groq handles lots of users and big document sets without slowing down. Ollama struggles with heavy tasks on regular computers.
- **Simple to Use**: Groq’s API is easy to plug into apps like this one. Ollama requires setting up models locally, which can be tricky.
- **Affordable Power**: Groq offers fast responses at low cost (as little as $0.10 per million words). Ollama is free but needs costly hardware for big models.
- **Accurate Answers**: Groq keeps the Gemma model’s quality high without compromises. Ollama’s smaller models might lose some accuracy.

**In short**: Groq makes this chatbot **fast**, **easy**, and **reliable** for answering your questions, no matter how many documents or users!

---

## Features
- **Load PDFs**: Reads PDF files from the `us_census` folder.
- **Smart Search**: Finds the right document parts to answer your questions.
- **Fast Answers**: Uses Groq’s Gemma2-9B-IT model for quick, accurate replies.
- **Interactive App**: Type your question in the Streamlit app and see answers with document context.
- **Secure Setup**: Keeps API keys safe in a `.env` file.

---

## What You Need
- **Python**: Version 3.8 or higher.
- **Libraries**: Install `streamlit`, `langchain`, `langchain-groq`, `langchain-community`, `langchain-google-genai`, `faiss-cpu`, `PyPDF2`, and `python-dotenv`.
- **API Keys**:
  - Groq API key (for the Gemma model).
  - Google API key (for document embeddings).
- **PDFs**: Place your PDF files in a folder named `us_census`.

---

## How to Set Up
1. **Clone the Project**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Install Libraries**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Add API Keys**:
   - Create a `.env` file in the project folder.
   - Add your keys like this:
     ```bash
     GROQ_API_KEY=your-groq-api-key
     GOOGLE_API_KEY=your-google-api-key
     ```
4. **Add PDFs**: Put your PDF files in the `us_census` folder.

---

## How to Run
1. Start the app:
   ```bash
   streamlit run app.py
   ```
2. Open the link in your browser (like `http://localhost:8501`).
3. Click **"Creating Vector Store"** to process the PDFs.
4. Type a question (e.g., “What’s the US population growth rate?”).
5. Get the answer and see the document parts used!
_Landing_UI_
![Screen_shot](Landing_UI)

---

## Project Files
- `app.py`: The main app code.
- `us_census/`: Folder for your PDF files.
- `.env`: Stores your API keys (keep it secret!).
- `requirements.txt`: Lists all needed libraries.

---

## Tips
- The app saves the document data in memory to avoid reprocessing.
- Make sure your internet is on for Groq and Google APIs.
- For big PDF collections, give the app some time to build the vector store.

---

## Example
**Question**: “What’s the latest US population data?”
**Answer**: The chatbot finds the right info from the `us_census` PDFs and gives a clear answer, fast!

Enjoy asking questions with your super-speedy Groq-powered chatbot! 🚀