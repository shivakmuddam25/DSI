import streamlit as st
import pandas as pd
import pickle

st.header("Welcome to Data Visualization")
df = pd.read_csv("../LifeExpectancyData.csv")
st.write(df)

# with open("data.sav", 'wb') as f:
#     pickle.dump(df, f)

#df = pickle.load(open('../data.sav', 'rb'))


#st.dataframe(df)

# Display the various charts

