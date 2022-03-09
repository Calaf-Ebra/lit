import streamlit as st
import pandas as pd

st.header("LWP")
st.subheader("Automation Solutions")


sheet_url = "https://docs.google.com/spreadsheets/d/1IXe_43DiORo36E9D7OgUiCQQD9JeYOtIl0HimoStOyA/edit#gid=0"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
pd.read_csv(url_1)
                          
                          
a='cass'

number = st.number_input('Number of Items')
options = st.selectbox(
     'Item Name?',
     ('Farida',a, 'Holland'))
if options==a:
     st.write(number*2)
     

st.write('You selected:', options)
