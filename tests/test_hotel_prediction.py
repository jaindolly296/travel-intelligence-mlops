from src.pipeline.hotel_prediction_pipeline import HotelPredictionPipeline


pipeline = HotelPredictionPipeline()

sample = {

    "name": "Hotel Paradise",

    "place": "Goa",

    "travelCode": 1001,

    "userCode": 25,

    "days": 3,

    "total": 15000,

    "stay_year": 2024,

    "stay_month": 8,

    "stay_day": 15,

    "stay_weekday": "Thursday"

}

prediction = pipeline.predict(sample)

print(f"Predicted Hotel Price: {prediction:.2f}")
