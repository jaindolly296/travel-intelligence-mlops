from pydantic import BaseModel


class FlightPredictionRequest(BaseModel):

    gender: str
    age: int
    age_group: str
    company_frequency: int
    company: str
    from_city: str
    to_city: str
    flight_type: str
    time: int
    distance: int
    travel_year: int
    travel_month: int
    travel_day: int
    travel_weekday: str
    is_weekend: int




class FlightPredictionResponse(BaseModel):

    predicted_price: float


class HotelPredictionRequest(BaseModel):

    name: str
    place: str
    stay_weekday: str
    days: int
    stay_year: int
    stay_month: int
    stay_day: int


class HotelPredictionResponse(BaseModel):

    predicted_total_cost: float
