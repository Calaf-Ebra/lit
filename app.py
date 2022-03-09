import streamlit as st
import pandas as pd

st.header("LWP")
st.subheader("Automation Solutions")


                          
a='cass'

number = st.number_input('Number of Items')
options = st.selectbox(
     'Item Name?',
     ('Farida',a, 'Holland'))
if options==a:
     st.write(number*2)
     

st.write('You selected:', options)
