import streamlit as st

st.set_page_config(
    page_title="COVID Self Test Reporting",
    layout="wide",
    page_icon="☠️"
)

# -- SETUP ---------------------------------------------------------------------

st.write(
    """
    # Streamlit App by Adrian Tan
    ---
    Below are the listed of projects, consolidated within this Streamlit App, that have been developed to serve as a portfolio for interested visitors.
    """
)

with st.expander("COVID-19 Self Test App"):

    st.markdown(
        """
        ### DESCRIPTION
        The motivation for this project stems from the need to perform COVID-19 self test reporting to team members that will be visiting the office weekly.
        
        This app tracks weekly self tests by each individual and visualises the different statuses of individuals on a chart along with the reported days that they will be visiting the office on.
        
        > Note! For visitors, do know that streamlit temporarily freezes applications that are not frequently visited after a given time. For these instances, simply start-up the app in the same link provided

        ### POTENTIAL IMPROVEMENTS
        > Logic to amend entry rows within the Gsheet for users that resubmits their current week's results and/or visit days
        """
    )

with st.expander("Plotly Crypto App"):

    st.markdown(
        """
        ### DESCRIPTION

        This app was deployed on Heroku as a cloud hosting platform to showcase an interactive dashboard that was developed using Python.
        The application scrapes the [Coin Market Cap](https://coinmarketcap.com/) website for crpyto coin prices with changes of prices in 3 different timeframes (last 1 hour, 24 hours, and 7 days).
        The application was developed using plotly for data visualisation with dash components to enable users to make changes to the graph objects.

        ### IMPROVEMENTS
        - Variety of coins that were scraped, to be included as a multi-select filter to provide users with the ability to filter out specific coins to be viewed/compared.
        - To implement a 'Refresh' button feature instead of re-scraping upon every action (this would simplify the interaction and unnecessity to submit requests).
        """
    )
