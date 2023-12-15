import pandas as pd
import streamlit as st
import altair as alt
import os

# Load data function
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df


# Define the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# List of file paths for human trafficking data
file_paths = [
    os.path.join(current_dir, "table-1.csv"),
    os.path.join(current_dir, "table-2.csv"),
    os.path.join(current_dir, "table-3.csv"),
    os.path.join(current_dir, "table-4.csv")
]

# Initialize an empty dictionary to store the dataframes
dfs = {}

# Loop through the file paths and read each file into a dataframe
for i, file in enumerate(file_paths):
    df = load_data(file)
    dfs[f'df{i+1}'] = df

# Combine all dataframes into one
combined_df = pd.concat(dfs.values())

# Remove leading and trailing spaces from column names
combined_df.columns = combined_df.columns.str.strip()

# Convert 'State' column to string type
combined_df['State'] = combined_df['State'].astype(str)


# Initialize an empty dictionary to store the dataframes
dfs = {}

# Loop through the file paths and read each file into a dataframe
for i, file in enumerate(file_paths):
    df = load_data(file)
    dfs[f'df{i+1}'] = df

# Combine all dataframes into one
combined_df = pd.concat(dfs.values())

# Remove leading and trailing spaces from column names
combined_df.columns = combined_df.columns.str.strip()

# Convert 'State' column to string type
combined_df['State'] = combined_df['State'].astype(str)

# Streamlit App
st.title("Analyzing human trafficking in the US")  # Added title

# Sidebar
selected_tab = st.sidebar.selectbox("Select a Tab", ["Data Table", "Bar Chart"])

# Display data based on the selected tab
if selected_tab == "Data Table":
    st.subheader('Data Table')
    st.dataframe(combined_df)

elif selected_tab == "Bar Chart":
    st.subheader('Bar Chart')
    st.dataframe(combined_df)

    z_val = st.sidebar.selectbox("Pick your issue to evaluate", combined_df.columns)
    count_input = st.sidebar.number_input(f"Enter a value for the number of top {z_val} values to display", min_value=1, max_value=len(combined_df), value=10, step=1)

    # Bar chart without 'Total' column
    bar_chart = alt.Chart(combined_df.nlargest(count_input, z_val, 'all')).mark_bar().encode(
        y=alt.Y('State:N', title='State', sort='-x'),  # Use nominal type for 'State'
        x=alt.X(f'`{z_val}`:Q', title=f'{z_val}'),  # Updated X encoding
        tooltip=['State', z_val]  # Updated tooltip to exclude 'Offenses'
    ).transform_window(
        rank='rank(z_val)', sort=[alt.SortField(z_val, order='descending')]
    ).transform_filter(
        (alt.datum.rank <= count_input)
    )

    st.altair_chart(bar_chart, use_container_width=True)
    # Bar chart for all data
    bar_chart_all = alt.Chart(combined_df).mark_bar().encode(
        x=alt.X('State:N', title='State'),
        y=alt.Y('Offenses:Q', title='Offenses'),
        tooltip=['State', 'Offenses']
    ).configure_mark(
        color='blue'
    )

    st.subheader('Bar Chart - All Data')
    st.altair_chart(bar_chart_all, use_container_width=True)
















