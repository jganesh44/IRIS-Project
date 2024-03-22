# IMPORT PACKAGES
import numpy as np
import pandas as pd
import pickle
import streamlit as st

# PROVIDE HEADER NAME TO BROWSER
st.set_page_config(page_title='IRIS PROJECT - JGN',layout='wide')

# ADD A TITLE IN BODY OF BROWSER
st.title('IRIS PROJECT - JGN')

# Take sepal length, sepal width, petal length and petal width as input from user
sep_len = st.number_input('Sepal Length : ', min_value=0.00, step=0.01)
sep_wid = st.number_input('Sepal Width : ', min_value=0.00, step=0.01)
pet_len = st.number_input('Petal Length : ', min_value=0.00, step=0.01)
pet_wid = st.number_input('Petal Width : ', max_value=0.00, step=0.01)

# ADD BUTTON FOR PREDICTION
submit = st.button('Predict')

# ADD SUBHEADER FOR PREDICTION
st.subheader('Prediction Are: ')

# Create a function to predict species along with probability
def predict_species(scaler_path, model_path):
    # Load the scaler object
    with open(scaler_path, 'rb') as file1:
        scaler = pickle.load(file1)
    # Load the model object
    with open(model_path, 'rb') as file2:
        model = pickle.load(file2)
    # Convert sep_len, sep_wid and other inputs in dataframe format
    dct = {'sepal_length':[sep_len],
           'sepal_width':[sep_wid],
           'petal_length':[pet_len],
           'petal_width':[pet_wid]}
    xnew = pd.DataFrame(dct)
    # Apply scaler on the xnew
    xnew_pre = scaler.transform(xnew)
    # Give the predictions with model
    pred = model.predict(xnew_pre)
    # Get the probability
    probs = model.predict_proba(xnew_pre)
    # Get max probabililty
    max_prob = np.max(probs)
    return pred, max_prob

# Show the results in streamlit
if submit:
    scaler_path = 'Notebook/scaler.pkl'
    model_path = 'Notebook/model.pkl'
    pred, max_prob = predict_species(scaler_path, model_path)
    st.subheader(f'Predicted Species is : {pred[0]}')
    st.subheader(f'Probability of Prediction : {max_prob:.4f}')
    st.progress(max_prob)