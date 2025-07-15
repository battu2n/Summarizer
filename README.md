# Summarizer
A Streamlit-based tool that summarizes blog articles using LangChain with Groq’s LLMs, supporting both Stuff and Map-Reduce summarization methods.

## 📄 Blog Summarizer using LangChain & Groq

A powerful and intelligent application that takes any blog or article URL and returns concise, meaningful summaries using large language models. This project uses LangChain with Groq’s blazing-fast LLaMA 3.1 model and implements both `Stuff` and `Map-Reduce` summarization strategies.

---

## 🚀 Features

- 🔗 Input any blog or article URL
- 🧠 Summarization powered by **LangChain + Groq**
- 🧾 Supports both **Stuff** and **Map-Reduce** summarization methods
- 📚 Extracts and processes the blog content dynamically
- 📥 Clean, readable summaries designed for quick understanding

---

## 📊 Summary Methods

### 📌 Stuff Method
Processes the entire article in a single prompt. Best for short/medium-sized content. Provides a precise breakdown of the content's structure and components.

### 🔁 Map-Reduce Method
Breaks the article into chunks, summarizes each, then combines the summaries. Suitable for long-form blogs or complex content. Offers a thematic overview and identifies broader insights.

---

## 🛠️ Tech Stack

| Component        | Tool/Library                   |
|------------------|------------------------------- |
| Language Model   | Groq (LLaMA 3.1-8B-Instant)    |
| Framework        | LangChain                      |
| Summarization    | Stuff / MapReduce Chains       |
| Programming Lang | Python                         |

---

## 📂 Project Structure

blog_summarizer
├── main.py # 
├── stuff.py # 
├── map.py # 
├── requirements.txt # 
├── README.md 

---

### 🔧 Setup Instructions

## 1. **Clone the repo**
   git clone https://github.com/your-username/blog-summarizer.git
   cd blog-summarizer

## 2 Create a virtual environment

python -m venv venv
venv\Scripts\activate

## 3 Install dependencies

pip install -r requirements.txt
Set up environment variables
Create a .env file:

GROQ_API_KEY=your_api_key_here

### Run the summarizer

Streamlit run main.py
🧪 Example Usage

Enter a blog URL: https://lilianweng.github.io/posts/2023-06-23-agent/
# Stuff Method Summary:

The article discusses how LLM agents plan, store memory, and use tools. It explains techniques like ReAct and Reflexion to refine performance.

# Map-Reduce Summary:

The article highlights both the power and challenges of LLM agents, such as limited memory and tool use, and reviews solutions like HuggingGPT and Algorithm Distillation.

