"""
kpi_analyzer.py
Analyzes trends and patterns in KPI data.
"""

from typing import List
from schemas import TimeSeriesPoint


def analyze_kpi_changes(
    history: List[TimeSeriesPoint],
    forecast: List[object]
) -> dict:
    """
    Simplified KPI analysis:
    - Compare last value with previous value
    - Determine trend label: upward / downward / stable
    """

    if len(history) < 2:
        return {"trend": "stable", "change_percent": 0}

    prev = history[-2].value
    last = history[-1].value

    if last > prev:
        trend = "upward"
    elif last < prev:
        trend = "downward"
    else:
        trend = "stable"

    percent_change = ((last - prev) / prev) * 100 if prev != 0 else 0

    return {
        "trend": trend,
        "change_percent": round(percent_change, 2),
    }
