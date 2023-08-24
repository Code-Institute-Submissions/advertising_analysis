import streamlit as st
import pandas as pd

# Load your data here, replace 'data.csv' with your actual data source
data = pd.read_csv(
    '/workspaces/advertising_analysis/jupyter_notebooks/advertising_dataset.csv')


def page_data_overview_body():
    st.title("Data Overview")  # Fixed the string closing quotation mark

    # Display the first 5 rows of the loaded data
    st.write("Top 5 rows of the data:")
    st.dataframe(data.head(5))


# Call the function to display the page
page_data_overview_body()
