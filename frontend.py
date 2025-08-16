import streamlit as st
import pandas as pd
import pickle
st.set_page_config(page_title='Car Price Prediction', page_icon='car icon.png')
st.header('🚗 Welcome to Car Price Predictor')
df = pd.read_csv("copied.csv")
with open("LinearModel.pkl", "rb") as file:
    model = pickle.load(file)
col1, col2 = st.columns(2)
make = col1.selectbox("Car Brand", options=sorted(df["Make"].unique()))
model_name = col2.selectbox("Car Model", options=sorted(df["Model"].unique()))
fuel = col1.selectbox("Fuel Type", options=sorted(df["Fuel Type"].unique()))
trans = col2.selectbox("Transmission", options=sorted(df["Transmission"].unique()))
year = col1.number_input("Year of Manufacture", min_value=int(df["Year"].min()), max_value=int(df["Year"].max()), step=1)
engine_size = col2.number_input("Engine Size (L)", min_value=float(df["Engine Size"].min()), max_value=float(df["Engine Size"].max()), step=0.1)
mileage = col1.number_input("Mileage in (km)", min_value=int(df["Mileage"].min()), max_value=int(df["Mileage"].max()), step=1000)
makes = sorted(df["Make"].unique())
models = sorted(df["Model"].unique())
fuels = sorted(df["Fuel Type"].unique())
trans_list = sorted(df["Transmission"].unique())
input_values = [[
    makes.index(make),
    models.index(model_name),
    year,
    engine_size,
    mileage,
    fuels.index(fuel),
    trans_list.index(trans)
]]

c1, c2, c3 = st.columns([1.6, 1.5, 1])
if c2.button("Predict Car Price 💰"):
    out = model.predict(input_values)
    st.subheader(f"Estimated Price: ₹ {out[0]:,.2f}")
