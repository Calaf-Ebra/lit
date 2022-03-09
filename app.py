import streamlit as st
st.header("LWP")
st.subheader("Automation Solutions")

a='cass'

number = st.number_input('Insert a number')


option = st.selectbox(
     'How would you like to be contacted?',
     ('hhh',a, 'Home phone', 'Mobile phone'))

if option==a:
     st.write(number*2)
     

st.write('You selected:', option)
