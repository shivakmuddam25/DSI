import streamlit as st
import pandas as pd
import numpy as np

st.header("Welcome to Data Visualization")
df = pd.read_csv("./LifeExpectancyData.csv")
st.dataframe(df)

# Display the various charts

