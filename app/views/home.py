import streamlit as st


def home_page():

    st.title("🌍 Travel Intelligence MLOps")

    st.markdown("---")

    st.header("Welcome")

    st.write(
        """
        Welcome to the Travel Intelligence MLOps Platform.

        This application demonstrates a complete production-ready
        Machine Learning pipeline for travel analytics.

        ### Available Modules

        ✈ Flight Price Prediction

        🏨 Hotel Price Prediction

        🌍 Travel Recommendation

        📊 ML-powered Analytics

        🚀 FastAPI Backend

        📈 MLflow Experiment Tracking
        """
    )
