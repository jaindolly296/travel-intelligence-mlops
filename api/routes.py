from fastapi import APIRouter

from api.schemas import (
    FlightPredictionRequest,
    FlightPredictionResponse,
    HotelPredictionRequest,
    HotelPredictionResponse,
)

from src.components.custom_data import CustomData
from src.pipeline.prediction_pipeline import PredictPipeline
from src.pipeline.hotel_prediction_pipeline import HotelPredictionPipeline


router = APIRouter()

predictor = PredictPipeline()
hotel_predictor = HotelPredictionPipeline()


# ==========================================================
# Home
# ==========================================================

@router.get("/")
def home():

    return {
        "message": "Travel Intelligence MLOps API is running successfully."
    }


# ==========================================================
# Health Check
# ==========================================================

@router.get("/health")
def health():

    return {
        "status": "healthy",
        "project": "Travel Intelligence MLOps",
        "version": "1.0.0"
    }


# ==========================================================
# Flight Price Prediction
# ==========================================================

@router.post(
    "/predict",
    response_model=FlightPredictionResponse
)
def predict_flight_price(request: FlightPredictionRequest):

    custom_data = CustomData(

        gender=request.gender,
        age=request.age,
        age_group=request.age_group,
        company_frequency=request.company_frequency,
        company=request.company,

        from_city=request.from_city,
        to_city=request.to_city,
        flight_type=request.flight_type,

        time=request.time,
        distance=request.distance,

        travel_year=request.travel_year,
        travel_month=request.travel_month,
        travel_day=request.travel_day,
        travel_weekday=request.travel_weekday,
        is_weekend=request.is_weekend

    )

    input_df = custom_data.get_dataframe()

    prediction = predictor.predict(input_df)

    return FlightPredictionResponse(
        predicted_price=float(prediction[0])
    )


# ==========================================================
# Hotel Price Prediction
# ==========================================================

@router.post(
    "/predict/hotel",
    response_model=HotelPredictionResponse
)
def predict_hotel_price(request: HotelPredictionRequest):

    input_data = {

        "name": request.name,
        "place": request.place,
        "stay_weekday": request.stay_weekday,
        "days": request.days,
        "stay_year": request.stay_year,
        "stay_month": request.stay_month,
        "stay_day": request.stay_day

    }

    prediction = hotel_predictor.predict(input_data)

    return HotelPredictionResponse(
        predicted_total_cost=float(prediction)
    )
