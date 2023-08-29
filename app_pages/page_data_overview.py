import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('jupyter_notebooks/advertising_dataset.csv')


def page_data_overview_body():
    st.title("Data Overview")

    st.write("The dataset (15 columns) that was analyzed:")

    st.write("- ID")
    st.write("- Age")
    st.write("- Current Occupation")
    st.write("- First Interaction")
    st.write("- Profile Completed")
    st.write("- Website Visits")
    st.write("- Time Spent on Website")
    st.write("- Page Views per Visit")
    st.write("- Last Activity")
    st.write("- Print Media Type1 - Ads in Newpapers")
    st.write("- Print Media Type2 - Ads in Magazines")
    st.write("- Digital Media - Ads online")
    st.write("- Educational Channels - Ads on forums, threads, newsletters")
    st.write("- Referral - referred to JWS or not")
    st.write("- Status - converted to a paid customer or not")

    st.write("The dataset contains information on 4,612 records with 0 "
             "duplicates.")

    # Display the first and last 5 rows of the loaded data
    st.write("Top 5 rows of the data:")
    st.dataframe(data.head(5))

    st.write("Last 5 rows of the data:")
    st.dataframe(data.tail(5))

    # Display the statistical summary
    st.write("The statistical summary of the data is as follows:")
    st.dataframe(data.describe())


# Call the function to display the page
page_data_overview_body()
