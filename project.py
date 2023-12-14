import streamlit as st
import pandas as pd
import altair as alt

alt.data_transformers.disable_max_rows()

st.header('Analyzing Human Trafficking')

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

table_paths = [
    "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-1.csv",
    "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-2.csv",
    "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-3.csv",
    "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-4.csv"
]

# Let users select a table
selected_table_path = st.selectbox("Select a Table", table_paths)

# Load the selected table
project = load_data(selected_table_path)

# Display the selected table
st.subheader(f'Table {table_paths.index(selected_table_path) + 1}')
st.dataframe(project)





