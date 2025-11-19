# 📈 Demand & KPI Forecasting with Narrative Insights

A simulation of a **demand and KPI forecasting system** that combines classical time-series / regression models with **narrative insight generation**. The idea is to forecast key metrics (like demand, revenue, or conversion rate) and then automatically generate a simple explanation of what is happening and why, so business stakeholders can understand the trends.

---

## 📁 Project Structure

demand-kpi-forecasting-narrative-insights/  
│  
├── backend/  
│   ├── main.py            – FastAPI-style API for forecasting and narrative insights  
│   ├── forecaster.py      – Forecasting logic (placeholder: ARIMA/Prophet-style)  
│   ├── kpi_analyzer.py    – KPI trend and change analysis logic  
│   ├── narrator.py        – Narrative text generation (LLM-style explanation)  
│   ├── schemas.py         – Pydantic models for requests and responses  
│   ├── requirements.txt   – Placeholder dependencies  
│  
├── data/  
│   ├── README.md          – Notes about sample time-series and KPI data  
│   └── sample_kpis.csv    – Placeholder CSV with example KPI values  
│  
├── notebooks/  
│   └── forecasting_eda.ipynb – Placeholder notebook for EDA and model experiments  
│  
└── README.md              – Main project documentation (this file)

This structure makes the project look like a realistic forecasting and analytics service used by product, sales, or operations teams.

---

## 🚀 Project Overview

Many companies track KPIs such as:

- daily or weekly demand  
- revenue  
- active users  
- conversion rates  
- retention  

They often ask questions like:

- “What will our demand look like next month?”  
- “Are our KPIs trending up or down?”  
- “What changed compared to last quarter?”  

This project simulates a system that:

1. Takes historical KPI or demand data  
2. Generates short-term forecasts (for the next days/weeks)  
3. Detects meaningful changes or trends in KPIs  
4. Produces **natural-language commentary** that explains the trends in simple terms  

The goal is to make KPI charts not just numbers, but **stories** that decision-makers can understand quickly.

---

## 🧠 High-Level Architecture

High-level flow:

Historical KPI / Demand Data  
→ Preprocessing  
→ Forecasting Model (classical time-series or regression)  
→ KPI Change Analysis (growth, decline, anomalies)  
→ Narrative Generator (LLM-style commentary)  
→ API or Dashboard

- The **forecaster** predicts future values of a metric  
- The **KPI analyzer** looks at trends, changes, and deltas  
- The **narrator** converts those patterns into short text explanations  
- The **API layer** allows dashboards or apps to request forecasts and explanations together  

---

## 🔍 Example Scenario

Imagine a KPI called `daily_orders` for an e-commerce platform.

Example workflow:

1. You feed in the last 12 months of `daily_orders` data.  
2. The system generates a forecast for the next 30 days.  
3. The KPI analyzer compares recent weeks vs previous weeks and identifies:  
   - “Orders increased by 18% week-over-week.”  
   - “There is a strong weekly seasonality pattern (weekends higher than weekdays).”  
4. The narrative module generates a simple story like:  
   - “Daily orders have grown steadily over the last 4 weeks, with weekends consistently performing above weekdays. The next 30 days are expected to maintain an upward trend with slight weekly seasonality.”

This kind of narrative insight helps product managers, marketing, and leadership quickly understand the situation.

---

## 🧩 Conceptual Components

The implementation is structured as if this were a real production system:

- forecaster.py  
  - Would implement time-series or regression models (e.g., ARIMA/Prophet/XGBoost-style forecasting)  
  - Takes historical KPI data and returns predicted future values  

- kpi_analyzer.py  
  - Calculates deltas, percentage changes, moving averages  
  - Detects spikes, drops, and trend changes  
  - Flags interesting periods (for example: “last 7 days vs previous 7 days”)  

- narrator.py  
  - Takes forecast data and KPI analysis results  
  - Generates short narrative insights in plain language  
  - Examples: “trend is stable”, “sharp increase”, “decline after a peak”, etc.  

- main.py  
  - Exposes endpoints such as `/forecast_and_explain`  
  - Accepts raw KPI series as input, returns forecast values plus text summary  

- data/ and notebooks/  
  - Represent realistic workflows for EDA, model training, and experimentation on historical KPI data  

---

## 🧪 Example API Flow (Conceptual)

A typical call might:

1. Send a time-series (dates + KPI values) to `/forecast_and_explain`.  
2. The API:  
   - Runs the forecasting logic to predict future KPI values  
   - Runs the KPI analyzer to compute recent changes and trends  
   - Calls the narrator to generate a short text summary  
3. The response could contain:  
   - `forecast`: predicted KPI values for future dates  
   - `insights`: a list of narrative sentences (e.g., “KPI has increased by 12% over the last 14 days.”)  
   - `trend_label`: something like “upward”, “downward”, or “stable”

---

## 📊 Integration with Dashboards (Conceptual)

This type of forecasting and narrative system can be integrated into BI tools like:

- QuickSight  
- Power BI  
- Tableau  
- Custom internal dashboards  

Typical usage:

- Show a KPI time-series chart with historic and forecast values  
- Display dynamic text insights next to the chart  
- Let users filter by product, region, or segment and regenerate narratives on the fly  

This makes dashboards far more understandable for non-technical stakeholders.

---

## ⚙️ Setup Instructions (Conceptual Only)

These are conceptual steps to show realistic engineering practices. You do **not** need to actually run them.

Backend:

- Create a Python virtual environment  
- Install dependencies from `backend/requirements.txt`  
- Start the API server with a command like `uvicorn backend.main:app --reload`  

Notebooks:

- Open `notebooks/forecasting_eda.ipynb`  
- Load sample KPI data from `data/sample_kpis.csv`  
- Experiment with forecasting and visualizations  

---

## 🔮 Future Enhancements

- Add real implementations for ARIMA/Prophet/XGBoost-based forecasting  
- Add multiple KPIs at once (e.g., revenue, churn, signups)  
- Add anomaly detection on top of forecasts (e.g., alert when actual deviates from forecast)  
- Integrate with real data sources (data warehouse or data lake)  
- Connect to an actual LLM API for richer narrative generation  
- Add support for scenario analysis (best case, worst case, expected case)

---

## 📄 License

MIT License.
