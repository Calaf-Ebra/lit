import streamlit as st
st.header("LWP")
st.subheader("Automation Solutions")

a='cass'

number = st.number_input('Number of Items')

options = st.multiselect(
     'Product Name',
     ['Holalnd',a, 'Farida', 'BG', 'Extra'],
     ['Janov', 'DC'])

if option==a:
     st.write(number*2)
     

st.write('You selected:', option)
