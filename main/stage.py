import streamlit as st

home_page = st.Page('streamlit-inter.py',title = 'Home', icon = '🏠')

analysis_page = st.Page('pages/02_⚙️_analysis2.py', title='Deep Dive', icon = '📈')

# pg = st.navigation([home_page,analysis_page])

pg = st.navigation({
    "General": [home_page],
    "Reports": [analysis_page]
})
pg.run()