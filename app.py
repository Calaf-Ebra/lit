import streamlit as st
st.header("LWP")
st.subheader("Automation Solutions")

a='cass'

number = st.number_input('Number of Items')
option = st.selectbox(
     'Item Name?',
     ('Farida',a, 'Holland))

st.write('You selected:', option)
if options==a:
     st.write(number*2)
     

st.write('You selected:', options)
