# app.py
import streamlit as st
from stuff import summarize_with_stuff
from map import summarize_with_map

def main():
    st.title("📄 Blog Summarizer with LangChain & Groq")

    url = st.text_input("Enter a blog or article URL:", "https://lilianweng.github.io/posts/2023-06-23-agent/")
    if st.button("Summarize"):
        if not url:
            st.warning("Please enter a valid URL")
            return

        st.info("Summarizing using STUFF method...")
        stuff_summary = summarize_with_stuff(url)
        st.success("Stuff Method Summary")
        st.write(stuff_summary)

        st.info("Summarizing using MAP-REDUCE method...")
        map_summary = summarize_with_map(url)
        st.success("Map-Reduce Method Summary")
        st.write(map_summary)

if __name__ == "__main__":
    main()