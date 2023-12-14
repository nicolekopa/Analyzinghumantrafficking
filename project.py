import streamlit as st
import pandas as pd
import altair as alt

# Streamlit General
st.set_page_config(layout='wide')
st.title('Analyzing Human Trafficking by State')
st.sidebar.title('Page Settings')

# Data Wrangling
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv, skiprows=6)  # Skip the first 6 rows in each CSV file
    return df

def main():
    table_paths = [
        "C:\\Users\\nicol\\OneDrive\\Documents\\HCIP 5122\\Streamlit\\Analyzinghumantrafficking\\table-1.csv"
    ]

    # Combine tables into a single DataFrame
    combined_data = pd.concat([load_data(table_path) for table_path in table_paths], ignore_index=True)

    # Ensure the "State" column is of the correct data type
    if 'State' in combined_data.columns:
        combined_data['State'] = combined_data['State'].astype(str)

        # Create a bar chart for Total Offenses by State
        chart_total_offenses = alt.Chart(combined_data).mark_bar().encode(
            x=alt.X('State:N', axis=alt.Axis(labelAngle=-45)),  # Specify that 'State' is a nominal variable
            y='Total - Offenses',
            color='State',
            tooltip=['State:N', 'Total - Offenses']
        ).properties(
            width=800,
            height=400,
            title='Total Offenses by State'
        )

        # Display the chart
        st.subheader('Total Offenses by State')
        st.altair_chart(chart_total_offenses, use_container_width=True)

        # Display the raw data for debugging
        st.subheader('Raw Data')
        st.dataframe(combined_data)

if __name__ == '__main__':
    main()




