import streamlit as st

from src.pipeline.hotel_recommendation_pipeline import (
    HotelRecommendationPipeline
)

pipeline = HotelRecommendationPipeline()

st.title("🏨 Travel Recommendation")

destination = st.selectbox(
    "Select Destination",
    sorted(pipeline.dataset["place"].unique())
)

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=2
)

if st.button("Recommend Hotels"):

    hotels = pipeline.recommend(
        destination=destination,
        days=days
    )

    if hotels.empty:
        st.warning("No hotels found.")
    else:

        st.success(f"{len(hotels)} hotel(s) found")

        for _, row in hotels.iterrows():

            with st.container():

                st.subheader(row["name"])

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Destination:** {row['place']}")
                    st.write(f"**Price / Night:** ₹{row['price']:.2f}")

                with col2:
                    st.write(f"**Days:** {days}")
                    st.write(f"**Total Cost:** ₹{row['total_cost']:.2f}")

                st.divider()
