from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import numpy as np


def load_data(currency="USD"):

    # coinmarketcap page no longer has the currency option embedded within the html
    # its a toggleable option now

    page = requests.get("https://coinmarketcap.com/")
    soup = BeautifulSoup(page.content, "html.parser")

    data = soup.find('script', id='__NEXT_DATA__', type='application/json')

    coin_data = json.loads(data.contents[0])
    listings = json.loads(coin_data['props']['initialState'])['cryptocurrency']['listingLatest']['data']

    df = pd.DataFrame(
        np.array([n for n in listings[1:]], dtype=object),
        columns=listings[0]["keysArr"]+["Null"]
    )[[
        "slug",
        "symbol",
        f"quote.{currency}.price",
        f"quote.{currency}.percentChange1h",
        f"quote.{currency}.percentChange24h",
        f"quote.{currency}.percentChange7d",
        f"quote.{currency}.marketCap",
        f"quote.{currency}.volume24h",
        "selfReportedCirculatingSupply"
    ]].rename(columns={
        "slug": "Name",
        "symbol": "Symbol",
        f"quote.{currency}.price": "Price",
        f"quote.{currency}.percentChange1h": "1h%",
        f"quote.{currency}.percentChange24h": "24h%",
        f"quote.{currency}.percentChange7d": "7d%",
        f"quote.{currency}.marketCap": "Market Cap",
        f"quote.{currency}.volume24h": "Volume (24h)",
        "selfReportedCirculatingSupply": "Supply"
    })

    df.index = np.arange(1, len(df) + 1)

    return df


if __name__ == "__main__":
    print(load_data())
