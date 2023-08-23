import streamlit as st


def page_jws_requirements_body():
    st.title("JWS Business Requirement")

    st.markdown("## Objective")
    st.write("JWS is an initial stage startup that offers programs on cutting-edge technologies to students and professionals "
             "to help them upskill/reskill. With a large number of leads being generated regularly, one of the issues faced "
             "is to identify which of the leads are more likely to convert so that they can allocate resources accordingly. "
             "The objective is to:")

    st.write("- Analyze and build an ML model to help identify which leads are more likely to convert to paid customers,")
    st.write("- Find the factors driving the lead conversion process")
    st.write("- Create a profile of the leads which are likely to convert")


# Call the function to display the page content
page_jws_requirements_body()
