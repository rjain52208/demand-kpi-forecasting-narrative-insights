from fastapi import FastAPI
from typing import List
from schemas import TimeSeriesPoint, ForecastResponse
from forecaster import generate_forecast
from kpi_analyzer import analyze_kpi_changes
from narrator import generate_narrative

app = FastAPI(
    title="Demand & KPI Forecasting API",
    description="Forecasts future KPI values and generates narrative insights.",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/forecast_and_explain", response_model=ForecastResponse)
def forecast_and_explain(data: List[TimeSeriesPoint]):
    """
    Simulated flow:
    1. Forecast KPI values
    2. Analyze trends (growth, drop, seasonality)
    3. Generate narrative insights
    """
    forecast = generate_forecast(data)
    analysis = analyze_kpi_changes(data, forecast)
    narrative = generate_narrative(analysis)

    return ForecastResponse(
        forecast=forecast,
        insights=narrative,
        trend_label=analysis.get("trend", "stable")
    )
