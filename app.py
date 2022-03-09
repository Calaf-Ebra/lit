import streamlit as st
import pandas as pd

st.header("LWP")
st.subheader("Automation Solutions")


sheet_id = "/1IXe_43DiORo36E9D7OgUiCQQD9JeYOtIl0HimoStOyA/edit#gid=0”
sheet_name = “Leave with Python”
url = f”https://docs.google.com/spreadsheets/d/1IXe_43DiORo36E9D7OgUiCQQD9JeYOtIl0HimoStOyA/edit#gid=0"
  pd.read_csv(url)
                          
a='cass'

number = st.number_input('Number of Items')
options = st.selectbox(
     'Item Name?',
     ('Farida',a, 'Holland'))
if options==a:
     st.write(number*2)
     

st.write('You selected:', options)
