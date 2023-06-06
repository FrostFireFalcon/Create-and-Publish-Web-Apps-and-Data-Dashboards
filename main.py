
import streamlit as st
import pandas as pd

data = {
  "Series_1": [1, 3, 4, 5, 7],
  "Series_2": [10, 30, 40, 100, 250]
}

df = pd.DataFrame(data)

st.title("My Learning App")
st.subheader("Introducing Streamlit in Automate Everything with Python")
st.write("""
This is my learning Web App.
Enjoy! :)
""")
st.write(df)
st.line_chart(df)
st.area_chart(df)

my_slider = st.slider("Celsius")
st.write(my_slider, "in Fahrenheit is", my_slider * 9/5 + 32)
