import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report, confusion_matrix,
    recall_score, make_scorer
)
from sklearn.model_selection import GridSearchCV

# Load the data
data = pd.read_csv('jupyter_notebooks/advertising_dataset.csv')

# Data processing and preparation steps

X = data.drop(["status"], axis=1)
Y = data['status']

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.30, random_state=1
)

# Random Forest model building
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Random Forest evaluation
y_pred_train1 = rf_model.predict(X_train)
y_pred_test = rf_model.predict(X_test)

# Hyperparameter tuning
rf_model_tuned = RandomForestClassifier(
    random_state=7, class_weight={0: 0.3, 1: 0.7})

parameters = {
    'n_estimators': [100, 150],
    'max_depth': [6, 7],
    'min_samples_leaf': [20, 25],
    'max_features': ['auto', 'sqrt'],
    'bootstrap': [True, False]
}

scorer = make_scorer(recall_score, pos_label=1)
grid_obj = GridSearchCV(rf_model_tuned, parameters, scoring=scorer, cv=5)
grid_obj = grid_obj.fit(X_train, y_train)
rf_model_tuned = grid_obj.best_estimator_
rf_model_tuned.fit(X_train, y_train)

# Random Forest evaluation after tuning
y_pred_train2 = rf_model_tuned.predict(X_train)
y_pred_test2 = rf_model_tuned.predict(X_test)

# Streamlit UI


def metrics_score(actual, predicted):
    st.text(classification_report(actual, predicted))
    cm = confusion_matrix(actual, predicted)
    plt.figure(figsize=(8, 5))
    sns.heatmap(cm, annot=True, fmt='.2f', xticklabels=[
                'Not Converted', 'Converted'],
                yticklabels=['Not Converted', 'Converted'])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    st.pyplot(plt.gcf())


def page_random_forest_body():
    st.title("Random Forest")

    st.title("Data Preparation for modeling")
    st.write("We want to predict which lead is more likely to be converted.")
    st.code("X_train shape: " + str(X_train.shape))
    st.code("X_test shape: " + str(X_test.shape))

    st.title("Building Classification Models")
    st.title("Random Forest Model Evaluation - Before Tuning")
    st.subheader("Performance on the training data:")
    metrics_score(y_train, y_pred_train1)
    st.subheader("Performance on the testing data:")
    metrics_score(y_test, y_pred_test)

    st.title("Random Forest - Hyperparameter Tuning")
    st.write(
        "We will use the class_weight hyperparameter with the value equal to "
        "{0: 0.3, 1: 0.7} which is approximately the opposite of the "
        "imbalance in the original data.")
    st.write("Best parameters:", grid_obj.best_params_)
    st.title("Random Forest Model Evaluation - After Tuning")
    st.subheader("Performance on the training data:")
    metrics_score(y_train, y_pred_train2)
    st.subheader("Performance on the testing data:")
    metrics_score(y_test, y_pred_test2)

    st.write("In summary, the initial model showed high accuracy and perfect "
             "scores on the training data, but the testing data performance "
             "indicated some imbalance-related issues, particularly in terms "
             "of recall for class 1. After hyperparameter tuning, the model's "
             "overall performance improved, with better balance between "
             "precision and recall for both classes. While the final model's "
             "accuracy increased slightly, it still faces challenges in "
             "accurately predicting conversions. Further experimentation and "
             "feature engineering might be beneficial for improving this "
             "model's performance.")


# Call the page_random_forest_body function to display the content
page_random_forest_body()
