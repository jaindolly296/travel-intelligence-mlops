from src.pipeline.prediction_pipeline import PredictPipeline
from src.components.custom_data import CustomData


def main():

    data = CustomData(
        gender="male",
        age=30,
        age_group="Adult",
        company_frequency=120,
        company="4You",
        from_city="Brasilia (DF)",
        to_city="Rio de Janeiro (RJ)",
        flight_type="economic",
        time=180,
        distance=2200,
        travel_year=2026,
        travel_month=8,
        travel_day=15,
        travel_weekday="Friday",
        is_weekend=0
    )

    df = data.get_dataframe()

    print("=" * 60)
    print("INPUT DATA")
    print("=" * 60)
    print(df)

    predictor = PredictPipeline()

    prediction = predictor.predict(df)

    print("=" * 60)
    print(f"Predicted Flight Price: {prediction[0]:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()
