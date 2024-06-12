import streamlit as st

st.title("Чат бот")


if user_prompt := st.chat_input():
    st.toast(user_prompt)

