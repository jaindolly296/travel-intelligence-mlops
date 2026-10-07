from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="Travel Intelligence MLOps API",
    description="Flight Price Prediction API",
    version="1.0.0"
)


app.include_router(router)
