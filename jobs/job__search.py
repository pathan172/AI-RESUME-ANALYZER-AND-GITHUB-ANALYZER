import streamlit as st

def render_job_search():
    st.title("🔍 Job Search")

    keyword = st.text_input("Job Title")
    location = st.text_input("Location")

    if st.button("Search Jobs"):
        st.success(f"Searching jobs for '{keyword}' in '{location}'...")
