import streamlit as st


st.title("interactive counter")

if 'count'not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1

def reset():
    st.session_state.count = 0

col1,col2 = st.columns(2)
col1 = st.button('click me to increase count', on_click=increment)
col2 = st.button('click to reset', on_click=reset)
# if col1:
#     increment()
# if col2:
#     reset()

st.header(st.session_state.count)