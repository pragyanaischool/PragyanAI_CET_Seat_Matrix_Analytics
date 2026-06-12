# ui/components/metrics.py

import streamlit as st


def metric_card(
    title: str,
    value,
    delta=None
):

    st.metric(
        label=title,
        value=value,
        delta=delta
    )


def render_dashboard_metrics(
    colleges,
    seats,
    branches,
    districts
):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "🏫 Colleges",
            colleges
        )

    with c2:
        metric_card(
            "🎓 Seats",
            f"{seats:,}"
        )

    with c3:
        metric_card(
            "📚 Branches",
            branches
        )

    with c4:
        metric_card(
            "🗺 Districts",
            districts
        )
