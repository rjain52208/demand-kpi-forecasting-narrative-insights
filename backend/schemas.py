"""
schemas.py
Shared Pydantic models for time-series forecasting and responses.
"""

from pydantic import BaseModel


class TimeSeriesPoint(BaseModel):
    day: str
    value: float


class ForecastPoint(BaseModel):
    day: str
    predicted_value: float


class ForecastResponse(BaseModel):
    forecast: list
    insights: list
    trend_label: str
