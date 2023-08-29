import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    classification_report, confusion_matrix,
    recall_score, make_scorer
)
from sklearn.model_selection import GridSearchCV
from sklearn import tree

# Load the data
data = pd.read_csv('/workspaces/advertising_analysis/'
                   'jupyter_notebooks/advertising_dataset.csv')

# Data processing and preparation steps

X = data.drop(["status"], axis=1)
Y = data['status']

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.30, random_state=1)

# Decision Tree model building
d_tree = DecisionTreeClassifier()
d_tree.fit(X_train, y_train)

# Decision Tree evaluation
y_pred_train1 = d_tree.predict(X_train)
y_pred_test = d_tree.predict(X_test)

# Hyperparameter tuning
d_tree_tuned = DecisionTreeClassifier(
    random_state=7, class_weight={0: 0.3, 1: 0.7})

parameters = {
    'max_depth': np.arange(2, 10),
    'criterion': ['gini', 'entropy'],
    'min_samples_leaf': [5, 10, 20, 25]
}

scorer = make_scorer(recall_score, pos_label=1)
grid_obj = GridSearchCV(d_tree_tuned, parameters, scoring=scorer, cv=5)
grid_obj = grid_obj.fit(X_train, y_train)
d_tree_tuned = grid_obj.best_estimator_
d_tree_tuned.fit(X_train, y_train)

# Decision Tree evaluation after tuning
y_pred_train2 = d_tree_tuned.predict(X_train)
y_pred_test2 = d_tree_tuned.predict(X_test)

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


def page_decision_tree_body():
    st.title("Decision Tree")

    st.title("Outlier Check")
    numeric_columns = data.select_dtypes(include=np.number).columns.tolist()
    numeric_columns.remove("status")
    plt.figure(figsize=(15, 12))
    for i, variable in enumerate(numeric_columns):
        plt.subplot(4, 4, i + 1)
        plt.boxplot(data[variable], whis=1.5)
        plt.tight_layout()
        plt.title(variable)
    st.pyplot(plt.gcf())
    st.write("As is evidenced above there are significant outliers in data "
             "concerning website visits and page views per visit.")

    st.title("Data Preparation for modeling")
    st.write("We want to predict which lead is more likely to be converted.")
    st.code("X_train shape: " + str(X_train.shape))
    st.code("X_test shape: " + str(X_test.shape))

    st.title("Building Classification Models")
    st.title("Decision Tree Model Evaluation - Before Tuning")
    st.subheader("Performance on the training data:")
    metrics_score(y_train, y_pred_train1)
    st.subheader("Performance on the testing data:")
    st.text(classification_report(y_test, y_pred_test))

    # Heatmap visualization
    plt.figure(figsize=(8, 5))
    sns.heatmap(confusion_matrix(y_test, y_pred_test2), annot=True, fmt='.2f',
                xticklabels=['Not Converted', 'Converted'],
                yticklabels=['Not Converted', 'Converted'])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    st.pyplot(plt.gcf())

    st.title("Decision Tree - Hyperparameter Tuning")
    st.write(
        "We will use the class_weight hyperparameter with the value equal to "
        "{0: 0.3, 1: 0.7} which is approximately the opposite of the "
        "imbalance in the original data.")
    st.write("Best parameters:", grid_obj.best_params_)
    st.title("Decision Tree Model Evaluation - After Tuning")
    st.subheader("Performance on the training data:")
    metrics_score(y_train, y_pred_train2)
    st.subheader("Performance on the testing data:")
    metrics_score(y_test, y_pred_test2)

    st.title("Visualizing the Decision Tree")
    features = list(X.columns)
    plt.figure(figsize=(30, 25))
    tree.plot_tree(d_tree_tuned, feature_names=features,
                   filled=True, fontsize=12, node_ids=True, class_names=True)
    st.pyplot(plt.gcf())

    st.write("Note: Blue leaves represent the converted leads, while the "
             "orange leaves represent the unconverted leads. The more the "
             "number of observationns in a leaf, the darker its colour gets.")

    st.write("In summary, the Decision Tree model, showed initial high "
             "accuracy and perfect scores on the training data. After "
             "hyperparameter tuning, the model's overall performance became  "
             "more balanced but still faced challenges in accurately "
             "predicting conversions. Further work on feature engineering "
             " and possibly handling outliers could contribute to "
             "improved model performance.")


# Call the page_decision_tree_body function to display the content
page_decision_tree_body()
