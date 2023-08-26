import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('/workspaces/advertising_analysis/'
                   'jupyter_notebooks/advertising_dataset.csv')


def page_bivariate_analysis_body():
    st.title("Bivariate Analysis")

    # Display a brief description or introduction
    st.write("In this section, we will explore the relationships between "
             "different variables using bivariate analysis.")

    # Choose variables for analysis
    selected_columns = st.multiselect(
        "Select columns for analysis", data.columns)

    if len(selected_columns) >= 2:
        # Display a scatter plot for selected variables
        sns.set(style="whitegrid")
        pairplot = sns.pairplot(data[selected_columns])
        st.pyplot(pairplot.fig)  # Pass the figure explicitly to st.pyplot()

        # Display the heatmap of correlations
        cols_list = data[selected_columns].select_dtypes(
            include=np.number).columns.tolist()
        heatmap_fig, heatmap_ax = plt.subplots(figsize=(12, 7))
        sns.heatmap(
            data[selected_columns][cols_list].corr(), annot=True, vmin=-1,
            vmax=1, fmt=".2f", cmap="Spectral",
            ax=heatmap_ax
        )
        st.pyplot(heatmap_fig)  # Pass the figure explicitly to st.pyplot()

    else:
        st.write("Select at least two columns for bivariate analysis.")


# Run the Streamlit app
if __name__ == "__main__":
    page_bivariate_analysis_body()
