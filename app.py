import streamlit as st
from predict_page import show_predict_page

prediction = show_predict_page()
st.write('Prediction of house price:', prediction)
