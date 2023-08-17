import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_bp_overview import page_bp_overview_body
from app_pages.page_data_summary import page_data_summary_body
from app_pages.page_eda_results import page_eda_results_body
from app_pages.page_data_preprocessing import page_data_preprocessing_body
from app_pages.page_model_performance import page_model_performance_body
from app_pages.page_conclusion_recommend import page_conclusion_recommend_body
from app_pages.page_cluster import page_cluster_body

app = MultiPage(app_name="Churnometer")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Customer Base Churn Study", page_churned_customer_study_body)
app.add_page("Prospect Churnometer", page_prospect_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Prospect Churn", page_predict_churn_body)
app.add_page("ML: Prospect Tenure", page_predict_tenure_body)
app.add_page("ML: Cluster Analysis", page_cluster_body)

app.run()  # Run the  app
