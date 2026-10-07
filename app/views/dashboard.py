import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from datetime import datetime


# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

FLIGHT_DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "flights_processed.csv"
)

HOTEL_DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "hotels_processed.csv"
)


# ==========================================================
# Load Data
# ==========================================================

@st.cache_data
def load_data():

    flights = pd.read_csv(FLIGHT_DATA_PATH)

    hotels = pd.read_csv(HOTEL_DATA_PATH)

    return flights, hotels


# ==========================================================
# Dashboard
# ==========================================================

def dashboard_page():

    st.title("📊 Travel Intelligence Dashboard")

    st.caption(
        "Analytics Dashboard for Flights and Hotels"
    )

    flights, hotels = load_data()

    st.markdown("---")

    # ======================================================
    # Sidebar Filters
    # ======================================================

    st.sidebar.header("Dashboard Filters")

    airline = st.sidebar.selectbox(
        "Airline",
        ["All"] + sorted(
            flights["agency"].unique().tolist()
        )
    )

    destination = st.sidebar.selectbox(
        "Destination",
        ["All"] + sorted(
            flights["to"].unique().tolist()
        )
    )

    flight_type = st.sidebar.selectbox(
        "Flight Type",
        ["All"] + sorted(
            flights["flightType"].unique().tolist()
        )
    )

    hotel_name = st.sidebar.selectbox(
        "Hotel",
        ["All"] + sorted(
            hotels["name"].unique().tolist()
        )
    )

    # ======================================================
    # Apply Filters
    # ======================================================

    filtered_flights = flights.copy()

    filtered_hotels = hotels.copy()

    if airline != "All":

        filtered_flights = filtered_flights[
            filtered_flights["agency"] == airline
        ]

    if destination != "All":

        filtered_flights = filtered_flights[
            filtered_flights["to"] == destination
        ]

    if flight_type != "All":

        filtered_flights = filtered_flights[
            filtered_flights["flightType"] == flight_type
        ]

    if hotel_name != "All":

        filtered_hotels = filtered_hotels[
            filtered_hotels["name"] == hotel_name
        ]

    # ======================================================
    # KPI Cards
    # ======================================================

    st.subheader("📈 Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "✈ Flights",
            f"{len(filtered_flights):,}"
        )

    with col2:

        st.metric(
            "🏨 Hotels",
            f"{len(filtered_hotels):,}"
        )

    with col3:

        if "price" in filtered_flights.columns:

            avg_flight = filtered_flights["price"].mean()

            st.metric(
                "💰 Avg Flight Fare",
                f"₹ {avg_flight:,.0f}"
            )

        else:

            st.metric(
                "💰 Avg Flight Fare",
                "N/A"
            )

    with col4:

        if "total" in filtered_hotels.columns:

            avg_hotel = filtered_hotels["total"].mean()

            st.metric(
                "🏨 Avg Hotel Cost",
                f"₹ {avg_hotel:,.0f}"
            )

        else:

            st.metric(
                "🏨 Avg Hotel Cost",
                "N/A"
            )

    st.markdown("---")
    # ======================================================
    # Flight Price Distribution
    # ======================================================

    if "price" in filtered_flights.columns:

        st.subheader("✈ Flight Price Distribution")

        fig = px.histogram(
            filtered_flights,
            x="price",
            nbins=40,
            title="Flight Price Distribution"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # Hotel Cost Distribution
    # ======================================================

    if "total" in filtered_hotels.columns:

        st.subheader("🏨 Hotel Cost Distribution")

        fig = px.histogram(
            filtered_hotels,
            x="total",
            nbins=40,
            title="Hotel Booking Cost Distribution"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # Top Airlines & Destinations
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✈ Top Airlines")

        airline_df = (
            filtered_flights["agency"]
            .value_counts()
            .reset_index()
        )

        airline_df.columns = [
            "Airline",
            "Flights"
        ]

        fig = px.bar(
            airline_df,
            x="Airline",
            y="Flights",
            text="Flights",
            title="Top Airlines"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("🌍 Top Destinations")

        destination_df = (
            filtered_flights["to"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        destination_df.columns = [
            "Destination",
            "Flights"
        ]

        fig = px.bar(
            destination_df,
            x="Destination",
            y="Flights",
            text="Flights",
            title="Top Destinations"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # Flight Type & Hotel Brands
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🛫 Flight Type Distribution")

        flight_type_df = (
            filtered_flights["flightType"]
            .value_counts()
            .reset_index()
        )

        flight_type_df.columns = [
            "Flight Type",
            "Count"
        ]

        fig = px.pie(
            flight_type_df,
            names="Flight Type",
            values="Count",
            hole=0.45,
            title="Flight Types"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("🏨 Hotel Brands")

        hotel_df = (
            filtered_hotels["name"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        hotel_df.columns = [
            "Hotel",
            "Bookings"
        ]

        fig = px.bar(
            hotel_df,
            x="Hotel",
            y="Bookings",
            text="Bookings",
            title="Top Hotel Brands"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # Average Flight Price by Airline
    # ======================================================

    if (
        "agency" in filtered_flights.columns and
        "price" in filtered_flights.columns
    ):

        st.subheader("💰 Average Flight Price by Airline")

        avg_airline = (
            filtered_flights
            .groupby("agency")["price"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        avg_airline.columns = [
            "Airline",
            "Average Fare"
        ]

        fig = px.bar(
            avg_airline,
            x="Airline",
            y="Average Fare",
            text="Average Fare",
            title="Average Flight Fare by Airline"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # Average Hotel Cost by Destination
    # ======================================================

    if (
        "place" in filtered_hotels.columns and
        "total" in filtered_hotels.columns
    ):

        st.subheader("🏨 Average Hotel Cost by Destination")

        avg_hotel = (
            filtered_hotels
            .groupby("place")["total"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        avg_hotel.columns = [
            "Destination",
            "Average Cost"
        ]

        fig = px.bar(
            avg_hotel,
            x="Destination",
            y="Average Cost",
            text="Average Cost",
            title="Average Hotel Cost by Destination"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # Dataset Summary
    # ======================================================

    st.subheader("📋 Dataset Summary")

    left, right = st.columns(2)

    with left:

        st.info(
            f"""
**Flights Dataset**

• Total Records : {len(filtered_flights):,}

• Airlines : {filtered_flights['agency'].nunique()}

• Destinations : {filtered_flights['to'].nunique()}

• Flight Types : {filtered_flights['flightType'].nunique()}
"""
        )

    with right:

        st.info(
            f"""
**Hotels Dataset**

• Total Records : {len(filtered_hotels):,}

• Hotels : {filtered_hotels['name'].nunique()}

• Destinations : {filtered_hotels['place'].nunique()}
"""
        )

    st.markdown("---")

    # ======================================================
    # Project Information
    # ======================================================

    st.subheader("🚀 Project Information")

    st.success(
        """
✔ End-to-End MLOps Pipeline

✔ Apache Airflow Workflow

✔ Jenkins CI/CD Pipeline

✔ MLflow Experiment Tracking

✔ Docker Containerization

✔ FastAPI REST API

✔ Streamlit Web Application

✔ Flight Price Prediction

✔ Hotel Price Prediction
"""
    )

    st.markdown("---")

    # ======================================================
    # Last Refresh
    # ======================================================

    st.caption(
        f"Dashboard refreshed on: {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}"
    )

    st.caption(
        "Travel Intelligence MLOps • Built with Streamlit, FastAPI, MLflow, Docker, Jenkins & Airflow"
    )
