"""
narrator.py
Produces simple narrative insights for KPI forecasting results.
"""

def generate_narrative(analysis: dict) -> list:
    """
    Converts KPI analysis results into plain English insights.

    Example:
    - "KPI is trending upward with a 12% increase since last period."
    - "KPI is stable with minimal change."
    """

    trend = analysis.get("trend", "stable")
    change = analysis.get("change_percent", 0)

    insights = []

    if trend == "upward":
        insights.append(
            f"KPI is trending upward with a {change}% increase from the previous period."
        )
    elif trend == "downward":
        insights.append(
            f"KPI has decreased by {change}% compared to the previous period."
        )
    else:
        insights.append("KPI is stable with minimal changes compared to earlier periods.")

    insights.append(
        "Forecast for the next period shows continued behavior based on recent trends."
    )

    return insights
