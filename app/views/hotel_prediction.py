import streamlit as st
import pandas as pd
from datetime import date
from pathlib import Path

from utils.api_client import predict_hotel


# ==========================================================
# Project Root
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]


# ==========================================================
# Data Path
# ==========================================================

HOTEL_DATA_PATH = BASE_DIR / "data" / "processed" / "hotels_processed.csv"


# ==========================================================
# Load Hotel Data
# ==========================================================

@st.cache_data
def load_hotels():

    df = pd.read_csv(HOTEL_DATA_PATH)

    return (
        df[["name", "place"]]
        .drop_duplicates()
        .sort_values("name")
    )


# ==========================================================
# Hotel Prediction Page
# ==========================================================

def hotel_prediction_page():

    st.title("🏨 Hotel Price Prediction")

    st.caption(
        "Enter your hotel booking details to estimate the total booking cost."
    )

    st.markdown("---")

    hotels = load_hotels()

    # ======================================================
    # Booking Details
    # ======================================================

    st.subheader("🏨 Booking Details")

    col1, col2 = st.columns(2)

    with col1:

        hotel_name = st.selectbox(
            "🏨 Select Hotel",
            hotels["name"].unique()
        )

        stay_date = st.date_input(
            "📅 Check-in Date",
            value=date.today()
        )

    with col2:

        place = hotels.loc[
            hotels["name"] == hotel_name,
            "place"
        ].iloc[0]

        st.text_input(
            "📍 Destination",
            value=place,
            disabled=True
        )

        days = st.number_input(
            "🌙 Number of Nights",
            min_value=1,
            max_value=30,
            value=1,
            step=1
        )

    st.markdown("---")

    # ======================================================
    # Prediction
    # ======================================================

    if st.button(
        "💰 Predict Hotel Cost",
        use_container_width=True
    ):

        payload = {

            "name": hotel_name,

            "place": place,

            "stay_weekday": stay_date.strftime("%A"),

            "days": int(days),

            "stay_year": stay_date.year,

            "stay_month": stay_date.month,

            "stay_day": stay_date.day

        }

        try:

            with st.spinner("Calculating hotel booking cost..."):

                result = predict_hotel(payload)

            prediction = result["predicted_total_cost"]

            st.success("✅ Prediction Completed")

            st.markdown("## 🏨 Hotel Cost Summary")

            summary = st.container(border=True)

            with summary:

                left, right = st.columns(2)

                with left:

                    st.metric(
                        label="💰 Estimated Cost",
                        value=f"₹ {prediction:,.2f}"
                    )

                    st.markdown("### 🏨 Hotel")

                    st.success(hotel_name)

                    st.markdown("### 🌙 Nights")

                    st.success(f"{days} Night(s)")

                with right:

                    st.markdown("### 📍 Destination")

                    st.info(place)

                    st.markdown("### 📅 Check-in Date")

                    st.info(
                        stay_date.strftime("%d %B %Y")
                    )

                    st.markdown("### 📆 Stay Weekday")

                    st.info(
                        stay_date.strftime("%A")
                    )

            st.markdown("---")

            st.caption(
                "This prediction is generated using the deployed Machine Learning model served through FastAPI."
            )

        except Exception as e:

            st.error("❌ Prediction Failed")

            st.error(str(e))
