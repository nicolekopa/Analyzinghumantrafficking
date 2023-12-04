import streamlit as st
import pandas as pd
import altair as alt
alt.data_transformers.disable_max_rows()
st.header('Analyzing Human Trafficking')
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
    project= load_data("table-1.csv")