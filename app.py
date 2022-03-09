import streamlit as st
st.header("LWP")
st.subheader("Automation Solutions")

a='cass'

number = st.number_input('Number of Items')
options = st.multiselect(
     'What are your favorite colors',
     ['Farida',a, 'BG', 'Janov'],
     ['Extra', 'KF'])

if options==a:
     st.write(number*2)
     

st.write('You selected:', options)
