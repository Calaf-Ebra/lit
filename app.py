import streamlit as st
st.header("LWP")
st.subheader("Automation Solutions")

a='cass'

number = st.number_input('Number of Items')


option = st.selectbox(
     'product Name?',
     ('BG',a, 'Farida', 'Holland'))

if option==a:
     st.write(number*2)
     

st.write('You selected:', option)
