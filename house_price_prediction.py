import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the saved model
model_path = 'Model/svr_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

st.markdown("<h1 style='text-align: center; color: black;'>House Price Prediction App</h1>", unsafe_allow_html=True)
st.info('Enter the following details to predict the house price')

# Input layout
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        bedrooms = st.slider("Bedrooms:", 1, 6, 1)
        parking = st.slider("Parking:", 0, 3, 1)
        area = st.number_input('Area (in square feet)', min_value=0.0)
        basement = st.selectbox('Basement', ['Yes', 'No'])
        air_conditioning = st.selectbox('Air Conditioning', ['Yes', 'No'])

    with col2:
        bathrooms = st.slider("Bathrooms:", 1, 4, 1)
        stories = st.slider('Stories:', 1, 5, 1)
        furnishing_status = st.selectbox('Furnishing Status', ['unfurnished', 'semi-furnished', 'furnished'])
        hot_water_heating = st.selectbox('Hot Water Heating', ['Yes', 'No'])
        pref_area = st.selectbox('Preference Area', ['Yes', 'No'])

# Encode categorical features
furnishingstatus = {'unfurnished': 0, 'semi-furnished': 1, 'furnished': 2}[furnishing_status]
basement_yes = 1 if basement == 'Yes' else 0
hotwaterheating_yes = 1 if hot_water_heating == 'Yes' else 0
airconditioning_yes = 1 if air_conditioning == 'Yes' else 0
prefarea_yes = 1 if pref_area == 'Yes' else 0


def predict_price():
    # Prepare input data as a DataFrame with matching feature names
    input_data = pd.DataFrame({
        'area': [np.log(area + 1)],               
        'bedrooms': [np.log(bedrooms + 1)],
        'bathrooms': [np.log(bathrooms + 1)],
        'stories': [np.log(stories + 1)],
        'parking': [np.log(parking + 1)],
        'furnishingstatus': [furnishingstatus],    
        'basement_yes': [basement_yes],
        'hotwaterheating_yes': [hotwaterheating_yes],
        'airconditioning_yes': [airconditioning_yes],
        'prefarea_yes': [prefarea_yes]
    })
    
    # Print the input data columns for debugging
    print("Input data columns:", input_data.columns)

    # Predict the log-transformed price
    log_predicted_price = model.predict(input_data)[0]
    
    # Convert the log price back to the original scale
    predicted_price = np.exp(log_predicted_price)

    return predicted_price

# Add button to make the prediction
if st.button('Predict House Price'):
    predicted_price = predict_price()
    st.success(f'The predicted house price is: ${predicted_price:.2f} million')
