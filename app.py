import streamlit as st
st.header("LWP")
st.subheader("Automation Solutions")

a='cass'

number = st.number_input('Number of Items')
options = st.selectbox(
     'Item Name?',
     ('Farida',a, 'Holland'))

st.write('You selected:', options)
if options==a:
     st.write(number*2)
     

st.write('You selected:', options)
