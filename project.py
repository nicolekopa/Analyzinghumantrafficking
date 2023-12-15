import pandas as pd
import streamlit as st
import altair as alt
import subprocess

subprocess.run(["pip", "install", "plotly"])

# Load data function
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

# List of file paths for human trafficking data
file_paths = [
    "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-1.csv",
    "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-2.csv",
    "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-3.csv",
    "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-4.csv"
]

# Create a dictionary to hold the dataframes
dfs = {}

# Loop through the file paths and read each file into a dataframe
for i, file in enumerate(file_paths):
    df = load_data(file)
    dfs[f'df{i+1}'] = df

# Combine all dataframes into one
combined_df = pd.concat(dfs.values())

# Streamlit App
st.title("Human Trafficking Analysis")

# Sidebar
selected_tab = st.sidebar.selectbox("Select a Tab", ["Data Table", "Scatter Plot", "Bar Chart"])

# Display data table
if selected_tab == "Data Table":
    st.subheader('Data Table')
    st.dataframe(combined_df)

# Scatter Plot Tab
elif selected_tab == "Scatter Plot":
    st.subheader('Scatter Plot')
    st.dataframe(combined_df)

    x_val = st.sidebar.selectbox("Pick your x-axis", combined_df.columns)
    y_val = st.sidebar.selectbox("Pick your y-axis", combined_df.columns)

    scatter = alt.Chart(combined_df).mark_point().encode(
        alt.X(x_val, title=f'{x_val}'),
        alt.Y(y_val, title=f'{y_val}'),
        tooltip=list(combined_df.columns), size='Offenses'
    ).configure_mark(
        opacity=0.5,
        color='blue'
    )

    st.altair_chart(scatter, theme="streamlit", use_container_width=True)

# Bar Chart Tab
elif selected_tab == "Bar Chart":
    st.subheader('Bar Chart')
    st.dataframe(combined_df)

    z_val = st.sidebar.selectbox("Pick your issue to evaluate", combined_df.columns)
    count_input = st.sidebar.number_input(f"Enter a value for the number of top {z_val} values to display", min_value=1, max_value=len(combined_df), value=10, step=1)

    # Bar chart without 'Total' column
    bar_chart = alt.Chart(combined_df.nlargest(count_input, z_val)).mark_bar().encode(
        y=alt.Y('State', title='State', sort='-x'),
        x=alt.X(z_val, title=f'{z_val}'),
        tooltip=['State', z_val]  # Updated tooltip to exclude 'Offenses'
    ).transform_window(
        rank='rank(z_val)', sort=[alt.SortField(z_val, order='descending')]
    ).transform_filter(
        (alt.datum.rank <= count_input)
    )

    st.altair_chart(bar_chart, use_container_width=True)




