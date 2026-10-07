import streamlit as st
from datetime import date, time

from utils.api_client import predict_flight
from utils.distance_mapping import CITY_DISTANCE


# -------------------------------------------------
# Airline Frequency Mapping
# Replace these values with your actual frequencies
# -------------------------------------------------

COMPANY_FREQUENCY = {
    "4You": 120,
    "Acme Factory": 110,
    "Monsters CYA": 95,
    "Umbrella LTDA": 150,
    "Wonka Company": 130
}

# -------------------------------------------------
# Display Names
# -------------------------------------------------

AIRLINE_DISPLAY = {
    "4You Airlines": "4You",
    "Acme Airlines": "Acme Factory",
    "Monsters Airways": "Monsters CYA",
    "Umbrella Airways": "Umbrella LTDA",
    "Wonka Airlines": "Wonka Company"
}

FLIGHT_CLASS_DISPLAY = {
    "Economy": "economic",
    "Premium Economy": "premium",
    "First Class": "firstClass"
}

# -------------------------------------------------
# Automatic Age Group
# -------------------------------------------------

def get_age_group(age):

    if age < 25:
        return "Young Adult"

    elif age < 45:
        return "Adult"

    elif age < 60:
        return "Middle Age"

    return "Senior"


# -------------------------------------------------
# Flight Prediction Page
# -------------------------------------------------

def flight_prediction_page():

    st.title("✈ Flight Price Prediction")
    st.caption("Enter your travel details to estimate your flight fare.")

    st.markdown("---")

    # ============================================
    # Passenger Information
    # ============================================

    st.subheader("👤 Passenger Details")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            [
                "male",
                "female",
                "none"
            ]
        )

    with col2:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30,
            step=1
        )

    age_group = get_age_group(age)

    st.markdown("---")

    # ============================================
    # Flight Information
    # ============================================

    st.subheader("🛫 Flight Details")

    col1, col2 = st.columns(2)

    with col1:

        selected_airline = st.selectbox(
            "✈ Airline",
            list(AIRLINE_DISPLAY.keys())
        )

        company = AIRLINE_DISPLAY[selected_airline]

        from_city = st.selectbox(
            "🛫 From",
            [
                "Brasilia (DF)",
                "Rio de Janeiro (RJ)",
                "Sao Paulo (SP)",
                "Recife (PE)",
                "Natal (RN)",
                "Campo Grande (MS)",
                "Aracaju (SE)",
                "Salvador (BH)",
                "Florianopolis (SC)"
            ]
        )

        flight_date = st.date_input(
            "Departure Date",
            value=date.today(),
            min_value=date.today()
        )

    with col2:

        selected_class = st.selectbox(
            "💺 Cabin Class",
            list(FLIGHT_CLASS_DISPLAY.keys())
        )

        flight_type = FLIGHT_CLASS_DISPLAY[selected_class]

        available_destinations = [
            city for city in [
                "Brasilia (DF)",
                "Rio de Janeiro (RJ)",
                "Sao Paulo (SP)",
                "Recife (PE)",
                "Natal (RN)",
                "Campo Grande (MS)",
                "Aracaju (SE)",
                "Salvador (BH)",
                "Florianopolis (SC)"
            ]
            if city != from_city
        ]

        to_city = st.selectbox(
            "🛬 To",
            available_destinations
        )

        departure_time = st.time_input(
            "🕒 Departure Time",
            value=time(9, 0)
        )

    st.markdown("---")

    # ============================================
    # Automatic Feature Generation
    # ============================================

    travel_year = flight_date.year

    travel_month = flight_date.month

    travel_day = flight_date.day

    travel_weekday = flight_date.strftime("%A")

    is_weekend = 1 if flight_date.weekday() >= 5 else 0

    company_frequency = COMPANY_FREQUENCY.get(
        company,
        100
    )

    distance = CITY_DISTANCE.get(
        (from_city, to_city),
        1500
    )

    flight_minutes = (
        departure_time.hour * 60
        + departure_time.minute
    )

    

    st.markdown("---")
    if st.button(
        "💰 Calculate Flight Fare",
        use_container_width=True
    ):

        payload = {

            "gender": gender,
            "age": age,
            "age_group": age_group,
            "company_frequency": company_frequency,
            "company": company,
            "from_city": from_city,
            "to_city": to_city,
            "flight_type": flight_type,
            "time": flight_minutes,
            "distance": distance,
            "travel_year": travel_year,
            "travel_month": travel_month,
            "travel_day": travel_day,
            "travel_weekday": travel_weekday,
            "is_weekend": is_weekend

        }

        try:

            with st.spinner("Calculating your flight price..."):

                result = predict_flight(payload)

            predicted_price = result["predicted_price"]

            st.success("✅ Prediction Completed")

            st.markdown("### 🎫 Flight Fare Summary")

            summary_container = st.container(border=True)

            with summary_container:

                col1, col2 = st.columns([1, 1])

                with col1:

                    st.metric(
                        label="💰 Estimated Fare",
                        value=f"₹ {predicted_price:,.2f}"
                    )

                    st.markdown("### ✈ Airline")
                    st.success(selected_airline)

                    st.markdown("### 💺 Cabin Class")
                    st.success(selected_class)

                

                with col2:

                    st.markdown("### 🛫 From")
                    st.info(from_city)

                    st.markdown("### 🛬 To")
                    st.info(to_city)

                    st.markdown("### 📅 Journey Date")
                    st.info(flight_date.strftime("%d %B %Y"))

                    st.markdown("### 🕒 Departure Time")
                    st.info(departure_time.strftime("%I:%M %p"))

                    st.markdown("### 📍 Distance")
                    st.info(f"{distance:,} KM")
                st.markdown("---")

                st.caption(
                    "This fare is generated using the trained Machine Learning model based on the selected travel details."
                )
        except Exception as e:

            st.error("❌ Prediction Failed")
            st.error(str(e))
