import streamlit as st


def page_model_performance_body():
    st.title("Model Performance")

    st.write(
        "The models exhibited promising performance in predicting lead "
        "conversion, with the Random Forest model showing particularly "
        "high accuracy on the training data. However, there was a slight "
        "decline in performance on the testing data, indicating the need "
        "for further optimization. The initial decision tree model "
        "provided insights into the importance of various features in "
        "predicting lead conversion. However, it exhibited signs of "
        "overfitting, as indicated by the significant difference in "
        "performance between the training and testing data. This suggests "
        "that the model might have memorized the training data rather than "
        "generalizing well to new, unseen data. To address the overfitting "
        "issue, hyperparameter tuning was performed using GridSearchCV, "
        "and the class_weight hyperparameter was adjusted to account for "
        "the class imbalance in the data. This resulted in an improved "
        "decision tree model that showed better balance and consistency "
        "in performance between the training and testing data."
    )

    image_path = (
        "assets/images/feature_importance.png"
    )
    st.image(image_path, caption="Feature Importance")

    st.write(
        "The top factors driving lead conversion include time spent on "
        "the website, first interaction being through the website, profile "
        "completion (particularly in the medium range), age, and last "
        "activity being website activity. These features demonstrate their "
        "influence on the lead conversion process and can be used to "
        "identify leads with a higher likelihood of conversion. Based on "
        "the available data, certain profiles of leads are more likely to "
        "convert. Professionals emerged as the most likely demographic to "
        "be converted, followed by students and the unemployed. Age also "
        "plays a role, with older individuals tending to have a higher "
        "likelihood of conversion. Moreover, leads who have completed a "
        "higher proportion of their profiles, last interacted on the "
        "website, used print media types 1 and 2, utilized digital media, "
        "did not use educational channels, or were referred have a higher "
        "probability of conversion. To create a profile of leads who are "
        "likely to convert, we can consider the characteristics that were "
        "found to be influential. The ideal lead profile would include "
        "professionals or individuals in stable occupations, who have a "
        "higher age, have completed a significant portion of their "
        "profiles, and have shown engagement with the website."
    )
