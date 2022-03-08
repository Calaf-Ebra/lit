import streamlit as st

a='jj'

option = st.selectbox(
     'How would you like to be contacted?',
     (a, 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
