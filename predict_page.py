import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('linear_regression_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model
data = load_model()

def show_predict_page():
    st.title("Bangalore House Price Prediction")
    st.write("""### We need some input information to predict the house price""")

    bath = st.number_input('no.of bathrooms:', value = 0)
    balcony = st.number_input('no.of balconies:', value = 0)
    total_sqft = st.number_input('total sqaure feet:', value=00.00)
    bhk = st.number_input('no.of bed rooms:', value=0)

    input_data = [[bath, balcony, total_sqft, bhk]]
    prediction = data.predict(input_data)
    return prediction