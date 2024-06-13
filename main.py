import streamlit as st
from protochat_api import get_access_token, send_prompt

st.title("Чат бот")

if "access_token" not in st.session_state:
    try:
        st.session_state.access_token = get_access_token()
        st.toast("Токен получен")
    except Exception as e:
        st.toast(f"Не удалось получить токен: {e}")

if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "ai", "content": "Что я могу для вас сделать?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if user_prompt := st.chat_input():
    st.chat_message("user").write(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner("В процессе..."):
        response = send_prompt(user_prompt, st.session_state.access_token)
        st.toast(response)



        st.chat_message("ai").write(response)
        st.session_state.messages.append({"role": "ai", "content": response})

