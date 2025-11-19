"""
forecaster.py
Simulates a forecasting model (ARIMA/Prophet-style) for KPI or demand data.
"""

from typing import List
from schemas import TimeSeriesPoint, ForecastPoint


def generate_forecast(data: List[TimeSeriesPoint]) -> List[ForecastPoint]:
    """
    Placeholder forecasting logic.
    A real implementation would use ARIMA, Prophet, or XGBoost.

    Here we simply:
    - Take the last value
    - Add small incremental growth
    - Predict next 7 days
    """

    if not data:
        return []

    last_value = data[-1].value

    forecast = []
    for i in range(1, 8):
        predicted = last_value * (1 + (i * 0.01))  # 1% daily growth
        forecast.append(ForecastPoint(day=f"Day+{i}", predicted_value=predicted))

    return forecast
