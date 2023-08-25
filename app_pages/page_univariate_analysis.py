import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('/workspaces/advertising_analysis/'
                   'jupyter_notebooks/advertising_dataset.csv')

# Function to plot a boxplot and a histogram along the same scale.


def histogram_boxplot(data, feature):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    sns.histplot(data=data, x=feature, bins=20, kde=True, ax=axes[0])
    axes[0].set_xlabel(feature)
    axes[0].set_ylabel("Frequency")
    axes[0].set_title(f"Histogram of {feature}")

    sns.boxplot(data=data, y=feature, ax=axes[1])
    axes[1].set_ylabel(feature)
    axes[1].set_title(f"Boxplot of {feature}")

    plt.tight_layout()
    st.pyplot(fig)

# Function to create labeled barplots with consistent image size and text size


def labeled_barplot(data, feature, perc=False, n=None):
    total = len(data[feature])

    fig, ax = plt.subplots(figsize=(10, 5))  # Use consistent figsize

    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=15)
    sns.countplot(data=data, x=feature, palette="Paired",
                  order=data[feature].value_counts().index[:n].sort_values(),
                  ax=ax)

    for p in ax.patches:
        if perc:
            label = "{:.1f}%".format(100 * p.get_height() / total)
        else:
            label = p.get_height()

        x = p.get_x() + p.get_width() / 2
        y = p.get_height()

        ax.annotate(
            label,
            (x, y),
            ha="center",
            va="center",
            size=12,
            xytext=(0, 5),
            textcoords="offset points",
        )

    st.pyplot(fig)

# Streamlit app


def page_univariate_analysis_body():
    st.title("Univariate Analysis")

    # Display observations on age
    st.subheader("Observations on Age")
    st.write("Observation of age shows an average of approximately 46 years, "
             "with a standard deviation of 13.16. The minimum age is 18, and "
             "the maximum age is 63. This is shown visually below:")
    histogram_boxplot(data, "age")

    # Display observations on website visits
    st.subheader("Observations on Website Visits")
    st.write("On average, each individual has 3.57 website visits, "
             "with a standard deviation of 2.83. "
             "The maximum number of visits is 30 as shown below:")
    histogram_boxplot(data, "website_visits")

    # Display the number of leads that haven't visited the website
    not_visited = data[data["website_visits"] == 0].shape[0]
    st.write("Number of leads who haven't visited the website:", not_visited)

    # Display observations on time spent on website
    st.subheader("Observations on Time Spent on Website")
    st.write("The average time spent on the website is 724.01 units (time "
             "unit not specified), with a standard "
             " deviation of 743.83. The minimum time spent is 0, the maximum "
             "time spent is 2,537 units. This is evidenced below:")
    histogram_boxplot(data, "time_spent_on_website")

    # Display observations on page views per visit
    st.subheader("Observations on Page Views per Visit")
    st.write("Page Views per visit on average results in 3.03 page views and, "
             "a standard deviation of 1.97. The maximum is 18.43 as shown:")
    histogram_boxplot(data, "page_views_per_visit")

    # Display labeled barplots with consistent image size and text size
    st.subheader("Observations on Current Occupation")
    st.write("A breakdown of demographics is shown visually in bar graphs "
             "below:")
    labeled_barplot(data, "current_occupation", perc=True)

    st.subheader("Observations on First Interaction")
    st.write("First Interaction:")
    labeled_barplot(data, "first_interaction", perc=True)

    st.subheader("Observations on Profile Completed")
    st.write("Profile Completion:")
    labeled_barplot(data, "profile_completed", perc=True)

    st.subheader("Observations on Last Activity")
    st.write("Last Activity:")
    labeled_barplot(data, "last_activity", perc=True)

    st.subheader("Observations on Print Media Type 1")
    st.write("Media Usage:")
    labeled_barplot(data, "print_media_type1", perc=True)

    st.subheader("Observations on Print Media Type 2")
    st.write("Media Usage:")
    labeled_barplot(data, "print_media_type2", perc=True)

    st.subheader("Observations on Digital Media")
    st.write("Media Usage:")
    labeled_barplot(data, "digital_media", perc=True)

    st.subheader("Observations on Educational Channels")
    st.write("Educational Channels:")
    labeled_barplot(data, "educational_channels", perc=True)

    st.subheader("Observations on Referral")
    st.write("Referral:")
    labeled_barplot(data, "referral", perc=True)

    st.subheader("Observations on Status")
    st.write("Status:")
    labeled_barplot(data, "status", perc=True)


# Call the function to display the page
page_univariate_analysis_body()
