import streamlit as st
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
for x in option:
     if option=='Email'
       print("hh")

st.write('You selected:', option)
