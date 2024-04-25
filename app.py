# import the streamlit library
import streamlit as st
import numpy as np
import pickle


region_to_number = {
   'FATICK': 2, 
   'DAKAR': 0, 
   'LOUGA': 7, 
   'TAMBACOUNDA': 12, 
   'KAOLACK': 4,
   'THIES': 13, 
   'SAINT-LOUIS': 10, 
   'KOLDA': 6, 
   'KAFFRINE': 3, 
   'DIOURBEL': 1,
   'ZIGUINCHOR': 14, 
   'MATAM': 8, 
   'SEDHIOU': 11, 
   'KEDOUGOU': 5, 
   'Other': 9
}

tenure_to_number = {
    '3-6 month' : 0, 
    '6-9 month' : 1, 
    '9-12 month': 2, 
    '12-15 month': 3, 
    '15-18 month': 4, 
    '18-21 month': 5, 
    '21-24 month': 6, 
    '> 24 month': 7
}

yes_churn = 'The client is expected to churn'
no_churn = 'The client is not expected to churn'

default_value = 0.00

def churn_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
        return no_churn
    else:
        return yes_churn

# give a title to our app
st.title('Welcome to Churn Identifier')

# Region
region = st.selectbox("Location: ", ['Select an option'] + list(region_to_number.keys()) )

tenure = st.selectbox('Duration in the Network: ', ['Select an option'] + list(tenure_to_number.keys()))

top_up = st.number_input("Top-up amount:", value=default_value)

client_income = st.number_input("Monthly Income:", value=default_value)

number_of_connections = st.number_input("Number of connections:", value=default_value)

regularity = st.number_input("Number of times for being active within 90 days:", value=default_value)

frequency_top_pack = st.number_input("Number of times for activating the most active packs:", value=default_value)

try:
    if (st.button('Calculate Churn Probability')):
        # Map the selected option to its corresponding number
        region_number = region_to_number.get(region, '')
        tenure_number = tenure_to_number.get(tenure, '')
        
        try:
            if top_up == default_value:
                raise ValueError('to input a value')
            elif client_income == default_value:
                raise ValueError('to input a value')
            elif number_of_connections == default_value:
                raise ValueError('to input a value')
            elif regularity == default_value:
                raise ValueError('to input a value')
            elif frequency_top_pack == default_value:
                raise ValueError('to input a value')
            result = churn_prediction([top_up, client_income, number_of_connections, regularity, frequency_top_pack, region_number, tenure_number ])
            if result == yes_churn:
                st.error(result)
            else:
                st.success(result)
        except ValueError:
            'Please: Fill all the inputs.'
except ValueError:
    'Please: Fill all the inputs.'
