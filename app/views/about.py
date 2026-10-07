import streamlit as st


def about_page():

    st.title("ℹ About")

    st.write(
        """
        Travel Intelligence MLOps

        Version: 1.0

        Built using:

        • Python

        • Streamlit

        • FastAPI

        • Scikit-learn

        • MLflow

        • XGBoost
        """
    )
