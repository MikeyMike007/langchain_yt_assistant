"""A sample streamlit app"""

import textwrap
import streamlit as st
import langchain_helper as lch

st.title("Youtube Video Q&A Assistant")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.text_area(label="Insert Youtube Video Url", max_chars=50)
        query = st.text_area(
            label="Ask a question about the video", max_chars=50, key="query"
        )
        submit_button = st.form_submit_button(label="Submit")

if query and youtube_url:
    db = lch.create_db_from_youtube_video_url(youtube_url)
    response = lch.get_response_from_query(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=85))
