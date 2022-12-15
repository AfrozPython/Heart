# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:29:34 2022

@author: Afroz
"""

import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Company Profit")


Research = st.number_input('R&D Spend')                         

Administration = st.number_input('Administration')                                        
 
Marketing = st.number_input('Marketing')                             

State = st.selectbox('State',df['State'].unique())


if st.button('Predict Price'):
    query = np.array([Research,Administration,Marketing,State])

    query = query.reshape(1,4)
    st.title("The Profit of the company is " + str(int(np.exp(pipe.predict(query)[0]))))
 
 
 
 
