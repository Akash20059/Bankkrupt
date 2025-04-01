import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("bankrupt_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI
st.title("Bankruptcy Prediction Model")

st.write("Enter financial details to predict if the company is bankrupt or not.")

# Input fields
feature1 = st.number_input("Current assets", value=0.0)
feature2 = st.number_input("Cost of goods sold", value=0.0)
feature3 = st.number_input("Depreciation and amortization", value=0.0)
feature4 = st.number_input("EBITDA", value=0.0)
feature5 = st.number_input("Inventory", value=0.0)
feature6 = st.number_input("Net Income", value=0.0)
feature7 = st.number_input("Net sales", value=0.0)
feature8 = st.number_input("Total assets", value=0.0)
feature9 = st.number_input("Total Long-term debt", value=0.0)
feature10= st.number_input("EBIT", value=0.0)
feature11 = st.number_input("Gross Profit", value=0.0)
feature12 = st.number_input("Total Current Liabilities", value=0.0)
feature13 = st.number_input("Retained Earnings", value=0.0)
feature14 = st.number_input("Total Revenue", value=0.0)
feature15 = st.number_input("Total Liabilities", value=0.0)


# Predict button
if st.button("Predict"):
    features = np.array([[feature1, feature2, feature3, feature4,feature5, feature6, feature7, feature8,feature9, feature10, feature11, feature12,feature13, feature14,feature15]])
    prediction = model.predict(features)
    
    result = "Bankrupt" if prediction[0] == 1 else "Not Bankrupt"
    st.success(f"Prediction: {result}")
