import streamlit as st
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone','GGG'))

d=int(input("hhhhh "))


st.write('You selected:', option)
