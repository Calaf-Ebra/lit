import streamlit as st

a='cass'

option = st.selectbox(
     'How would you like to be contacted?',
     (a, 'Home phone', 'Mobile phone'))

if option==a:
     st.header("We are done")
     

st.write('You selected:', option)
