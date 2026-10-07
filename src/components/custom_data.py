import pandas as pd


class CustomData:

    def __init__(
        self,
        gender,
        age,
        age_group,
        company_frequency,
        company,
        from_city,
        to_city,
        flight_type,
        time,
        distance,
        travel_year,
        travel_month,
        travel_day,
        travel_weekday,
        is_weekend
    ):

        self.gender = gender
        self.age = age
        self.age_group = age_group
        self.company_frequency = company_frequency
        self.company = company
        self.from_city = from_city
        self.to_city = to_city
        self.flight_type = flight_type
        self.time = time
        self.distance = distance
        self.travel_year = travel_year
        self.travel_month = travel_month
        self.travel_day = travel_day
        self.travel_weekday = travel_weekday
        self.is_weekend = is_weekend

    def get_dataframe(self):

        return pd.DataFrame({

            "gender": [self.gender],
            "age": [self.age],
            "age_group": [self.age_group],
            "company_frequency": [self.company_frequency],
            "company": [self.company],
            "from": [self.from_city],
            "to": [self.to_city],
            "flightType": [self.flight_type],
            "time": [self.time],
            "distance": [self.distance],
            "travel_year": [self.travel_year],
            "travel_month": [self.travel_month],
            "travel_day": [self.travel_day],
            "travel_weekday": [self.travel_weekday],
            "is_weekend": [self.is_weekend]

        })
