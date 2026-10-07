import sys
from pathlib import Path
from views.dashboard import dashboard_page
# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from views.home import home_page
from views.flight_prediction import flight_prediction_page
from views.hotel_prediction import hotel_prediction_page
from views.about import about_page

# ------------------ Page Configuration ------------------ #

st.set_page_config(
    page_title="Travel Intelligence MLOps",
    page_icon="✈️",
    layout="wide"
)

# ------------------ Load CSS ------------------ #

css_file = Path(__file__).parent / "styles" / "style.css"

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    ) 

# ------------------ Sidebar ------------------ #

st.sidebar.title("Travel Intelligence")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "✈ Flight Price Prediction",
        "🏨 Hotel Price Prediction",
        "📊 Dashboard",
        "ℹ About"
    ]
)

# ------------------ Navigation ------------------ #

if page == "🏠 Home":
    home_page()

elif page == "✈ Flight Price Prediction":
    flight_prediction_page()

elif page == "🏨 Hotel Price Prediction":
    hotel_prediction_page()

elif page == "📊 Dashboard":
    dashboard_page()
    
elif page == "ℹ About":
    about_page()
