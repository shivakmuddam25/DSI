import streamlit as st
import pandas as pd
import pickle

st.header("Welcome to Data Visualization")
#df = pd.read_csv("../LifeExpectancyData.csv")


# with open("data.sav", 'wb') as f:
#     pickle.dump(df, f)

df = pickle.load(open('../data.sav', 'rb'))


#st.dataframe(df)
st.write(df)
# Display the various charts

