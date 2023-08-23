import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_jws_requirements import page_jws_requirements_body
from app_pages.page_data_overview import page_data_overview_body
from app_pages.page_univariate_analysis import page_univariate_analysis_body
from app_pages.page_bivariate_analysis import page_bivariate_analysis_body
from app_pages.page_decision_tree import page_decision_tree_body
from app_pages.page_random_forest import page_random_forest_body
from app_pages.page_model_performance import page_model_performance_body

# Create an instance of the app
app = MultiPage(app_name="advertising_analysis")

# App pages
app.add_page("JWS Business Requirement", page_jws_requirements_body)
app.add_page("Data Overview ", page_data_overview_body)
app.add_page("Univariate Analysis", page_univariate_analysis_body)
app.add_page("Bivariate Analysis", page_bivariate_analysis_body)
app.add_page("Decision Tree", page_decision_tree_body)
app.add_page("Random Forest", page_random_forest_body)
app.add_page("Model Performace", page_model_performance_body)

app.run()  # Run the  app
