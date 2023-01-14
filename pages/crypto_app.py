import streamlit as st
from library.crypto import scraper

import plotly.graph_objects as go
import numpy as np


st.set_page_config(
    page_title="Crypto Price App",
    layout="wide",
    page_icon="☠️"
)

st.write(
    """
    # Crypto Prices App
    ---
    *All prices were scraped from the following source: [Coin Market Cap](https://coinmarketcap.com/)*
    """
)

# -- Setup ---------------------------------------------------------------------

with st.sidebar:
    sorting = st.selectbox("Sorting", ["Volume (24h)", "Supply", "Market Cap", "Price", "1h%", "24h%", "7d%"], 0)
    coins = st.slider("Number of Coins", 0, 100, 50)


# -- Body setup ----------------------------------------------------------------

cols = ["Name", "Symbol", "Price", "1h%", "24h%", "7d%", "Market Cap", "Volume (24h)", "Supply"]

df = scraper.load_data()[cols].sort_values(by=[sorting], ascending=False)[:coins]
df.index = np.arange(1, len(df) + 1)

# for price, color against avg

df["color"] = np.where(
    df[sorting] >= np.where(sorting == "price", df[sorting].mean(), 0),
    "green",
    "red"
)

# horizontal bar chart
# issue: points were reversed instead of using yaxis={"categoryorder": "total ascending"}
# this is because the sorting somehow includes unfiltered yticks when using 24h% or 7d%

st.plotly_chart(
    go.Figure(
        go.Bar(
            x=df[sorting][::-1],
            y=df["Symbol"][::-1],
            marker_color=df["color"][::-1],
            customdata=df[["Price", "1h%", "24h%", "7d%", "Market Cap", "Volume (24h)", "Supply"]][::-1],
            hovertemplate="<br>".join([
                "<extra>",
                "<b>price</b>: %{customdata[0]:,.2f}",
                "<b>1h%</b>: %{customdata[1]:,.0%}",
                "<b>24h%</b>: %{customdata[2]:,.0%}",
                "<b>7d%</b>: %{customdata[3]:,.0%}",
                "<b>Market Cap</b>: %{customdata[4]:,.0f}",
                "<b>Volume (24h)</b>: %{customdata[5]:,.0f}",
                "<b>Circulating Supply</b>: %{customdata[6]:,.0f}",
                "</extra>"
            ]),
            orientation="h"
        ),
        layout=go.Layout(
            title="Bar Plot of % Price Changes",
            font_family="Helvetica",
            xaxis={"tickformat": ",.0f" if sorting in ("Price", "Market Cap", "Volume (24h)", "Supply") else ",.0%"},
            width=500, height=1000,
            hovermode="y unified"
        )
    ),
    use_container_width=True
)

# table chart

st.plotly_chart(
    go.Figure(
        go.Table(
            columnwidth=[150, 400],
            header=dict(
                values=["#"] + [f"<b>{c.upper().replace('_', ' ')}</b>" for c in df.columns[:-1]],
                font=dict(size=15, color="black"), align="left",
                fill_color="paleturquoise", line_color="darkslategray",
                height=40
            ),
            cells=dict(
                values=[df.index.tolist()] + [df[k].tolist() for k in df.columns[:-1]],
                font=dict(size=13, color="black"), align="right",
                fill_color="lavender", line_color="darkslategray",
                format=["", "", "", ",.2f", ",.0%", ",.0%", ",.0%", ",.0f", ",.0f", ",.0f"],
                height=25
            )
        ),
        layout=go.Layout(
            title="Table of Crypto Data",
            font_family="Helvetica",
            height=1000,
            width=1000
        )
    ),
    use_container_width=True
)
