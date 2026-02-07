import streamlit as st

home_page = st.Page('streamlit-inter.py',title = 'Home', icon = '🏠')

analysis_page = st.Page('pages/02_⚙️_analysis2.py', title='Deep Dive', icon = '📈')

# pg = st.navigation([home_page,analysis_page])
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


def login():
    if st.session_state.password_input =='secret123':
        st.session_state['logged_in'] = True
    else:
        st.write('Wrong Password!!!!')


if not st.session_state['logged_in']:
    st.text_input('Enter pasword',type ='password', key = 'password_input',on_change= login)
    st.button('Submit Password', on_click = login)

else:
    pg = st.navigation({
        "General": [home_page],
        "Reports": [analysis_page]
    })
    pg.run()
    if st.button('Log out'):
        st.session_state['logged_in'] = False
        st.rerun()