import streamlit as st

st.title('chatbot')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt:= st.chat_input('What is life?'):
    st.session_state.messages.append({'role':'user','content':prompt})

    with st.chat_message('user'):# this is used because right now we just append the prompt message to the session_state but we still on line 14 so after next message it would show to avoid that we write the message instantly
        st.markdown(prompt)
    response = f"I heard you say: {prompt}"
    st.session_state.messages.append({'role':'assistant','content':response})
    with st.chat_message('assistant'):
        st.markdown(response)