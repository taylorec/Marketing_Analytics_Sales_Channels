import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('SC_model.joblib')


Fresh = st.number_input("Customers annual spend on fresh produce", min_value=1)
Milk = st.number_input("Customers annual spend on milk", min_value=1)
Frozen = st.number_input("Customers annual spend on frozen foods", min_value=1)
Grocery	= st.number_input("Customers annual spend on other groceries", min_value=1)
Detergents_Paper = st.number_input("Customers annual spend on detergent papers", min_value=1)
Delicatessen = st.number_input("Customers annual spend on delicatessen", min_value=1)

prediction = model.predict([[Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicatessen]])

if prediction == 0:
    prediction = 'Retail'
elif prediction == 1:
    prediction = 'Roadshow'
elif prediction == 2:
    prediction = 'Social Media'
elif prediction == 3:
    prediction = 'Television'

st.write('The most effective channel that can be used to target this customer is {}'.format(prediction))





