import streamlit as st

st.title('Hello, streamlit')
st.write('This is my first app. hello app')

st.header('hello but smaller')
st.write('This is hello from h2')

st.subheader('smallest hello')

st.markdown("#### Heading 4(smaller than h3)")
st.markdown("This :green[text] is :red[abhishek].")

st.markdown("Here's a bouquet &mdash;\
:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


import numpy as np
import pandas as pd


df = pd.DataFrame({
    'Month':['Jan','Feb','Mar'],
    'Sales':[100,200,300],
    'Customers':[20,35,30]
})

print(df[['Sales']].sum())


#Add sidebar Filters
st.sidebar.header('settings')
show_table = st.sidebar.checkbox('Show raw data')

col1, col2 = st.columns(2)
col1.metric("Total Sales",df[['Sales']].sum(),"12%")
col2.metric("YTD Sales","$100","-14%")

st.subheader('Sales Trend')
st.line_chart(df.set_index('Month')['Sales'])

if show_table:
    st.write(df)