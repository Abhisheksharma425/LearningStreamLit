
import time
import pandas as pd
import streamlit as st




# df = pd.DataFrame({'Month':['Jan','Feb','Mar'],'Fruits':['Apple','Mango','Banana'],'Amount':[20,30,50]})
# st.write('Monthly data for fruits:')
# st.write(df)
@st.cache_data #this cache skips the delay and store the df result in a ram in the form of cacheqw
def get_data():
    df = pd.DataFrame({'Month':['Jan','Feb','Mar'],'Fruits':['Apple','Mango','Ban'],'Amount':[20,30,50]})
    return df
df = get_data()
col1,col2 = st.columns(2)

selected_fruits = st.sidebar.multiselect('Select fruits', df['Fruits'].unique())
filtered_df = df[df['Fruits'].isin(selected_fruits)] if selected_fruits else df


with col1:
    st.write(filtered_df)

with col2:
    st.bar_chart(filtered_df.set_index('Month'))

if 'count' not in st.session_state:
    st.session_state['count'] = 0




def increment():
    st.session_state['count']+=1


st.button('increment',on_click=increment)
st.write(st.session_state['count'])

