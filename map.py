import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document
from langchain.chains.combine_documents.reduce import (
    split_list_of_docs,
    acollapse_docs,
)

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192", temperature=0)

map_prompt = ChatPromptTemplate.from_messages([
    ("system", "Write a concise summary of the following:\n\n{context}")
])

reduce_prompt = ChatPromptTemplate.from_messages([
    ("human", "The following is a set of summaries:\n{docs}\nTake these and distill it into a final, consolidated summary of the main themes.")
])

def length_function(documents):
    return sum(llm.get_num_tokens(doc.page_content) for doc in documents)

async def _reduce(input: dict) -> str:
    prompt = reduce_prompt.invoke(input)
    response = await llm.ainvoke(prompt)
    return response.content

async def map_reduce_summary(url: str) -> str:
    loader = WebBaseLoader(url)
    docs = loader.load()

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000, chunk_overlap=0)
    split_docs = text_splitter.split_documents(docs)

    # Step 1: Map
    summaries = []
    for chunk in split_docs:
        prompt = map_prompt.invoke(chunk.page_content)
        response = await llm.ainvoke(prompt)
        summaries.append(Document(page_content=response.content))

    # Step 2: Reduce (Collapse)
    doc_lists = split_list_of_docs(summaries, length_function, 1000)
    reduced_docs = []
    for doc_list in doc_lists:
        reduced_docs.append(await acollapse_docs(doc_list, _reduce))

    # Final Reduce
    final_summary = await _reduce({"docs": [doc.page_content for doc in reduced_docs]})
    return final_summary

def summarize_with_map(url: str) -> str:
    import asyncio
    return asyncio.run(map_reduce_summary(url))

if __name__ == "__main__":
    test_url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
    summary = summarize_with_map(test_url)
    print("\nMap-Reduce Summary:\n",summary)
