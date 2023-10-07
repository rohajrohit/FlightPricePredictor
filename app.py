import streamlit as st
import pickle
import pandas as pd
import numpy as np
from datetime import datetime


def helper(query):
    Route1 = 0
    Route2 = 0
    Route3 = 0
    Route4 = 0
    Route5 = 0
    source = query[0]
    destination = query[1]
    stoppage = query[2]
    airline = query[3]
    arrival_date = query[4]
    arrival_time = query[5]
    departure_date = query[6]
    departure_time = query[7]

    Journey_day = arrival_date.day
    Journey_month = arrival_date.month
    Journey_year = 2019

    Dep_Timehours = departure_time.hour
    Dep_Timeminutes = departure_time.minute

    Arrival_Timehours = arrival_time.hour
    Arrival_Timeminutes = arrival_time.minute

    Total_Stops = stoppage

    Duration_hours = abs(Arrival_Timehours - Dep_Timehours)
    Duration_minute = abs(Arrival_Timeminutes - Dep_Timeminutes)

    if (airline == 'Jet Airways'):
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'IndiGo'):

        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Multiple carriers'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0


    elif (airline == 'Vistara'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0


    elif (airline == 'GoAir'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0


    elif (airline == 'Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0


    elif (airline == 'Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0


    elif (airline == 'Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1
    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    if (source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    elif (source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0

    elif (source == 'Mumbai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0

    elif (source == 'Chennai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1

    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    if (destination == 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0


    elif (destination == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (destination == 'New_Delhi'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (destination == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0

    elif (destination == 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    prediction = forest.predict([[
        Total_Stops,
        Journey_day,
        Route1,
        Route2,
        Route3,
        Route4,
        Route5,
        Journey_month,
        Journey_year,
        Dep_Timehours,
        Dep_Timeminutes,
        Arrival_Timehours,
        Arrival_Timeminutes,
        Duration_hours,
        Duration_minute,
        Air_India,
        GoAir,
        IndiGo,
        Jet_Airways,
        Jet_Airways_Business,
        Multiple_carriers,
        Multiple_carriers_Premium_economy,
        SpiceJet,
        Trujet,
        Vistara,
        Vistara_Premium_economy,
        s_Chennai,
        s_Delhi,
        s_Kolkata,
        s_Mumbai,
        d_Cochin,
        d_Delhi,
        d_Hyderabad,
        d_Kolkata,
        d_New_Delhi
    ]])
    return prediction


forest = pickle.load(open('rf_random.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.markdown("# Flight Cost Predictor")

#st.title("Flight Cost Predictor")

# Create a sidebar for user input
#st.sidebar.header("User Input")

# Source and Destination in one row
col1, col2 = st.columns(2)
with col1:
    source = st.selectbox('Source', df['Source'].unique())

with col2:
    destination = st.selectbox('Destination', df['Destination'].unique())

# Total Stops and Airline in one row
col3, col4 = st.columns(2)
with col3:
    dict = {'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4}
    stoppage = st.selectbox('No.of Stoppage', [0, 1, 2, 3, 4])

with col4:
    airline = st.selectbox('Airline Company', df['Airline'].unique())

# Arrival and Departure Date in one row
col5, col6 = st.columns(2)
with col5:
    departure_date = st.date_input("Departure Date", datetime.today())

with col6:
    arrival_date = st.date_input("Arrival Date", datetime.today())

# Arrival and Departure Time in one row
col7, col8 = st.columns(2)
with col7:
    departure_time = st.time_input("Departure Time", datetime.now().time())

with col8:
    arrival_time = st.time_input("Arrival Time", datetime.now().time())


#st.sidebar.button("Predict Flight Cost")


if st.button('Predict Price'):
    query = np.array(
        [source, destination, stoppage, airline, arrival_date, arrival_time, departure_date, departure_time])
    flight_price = helper(query)[0]  # Assuming the price is a single value in a list
    formatted_price = f"Rs. {int(flight_price):,}"  # Format the price as "Rs. 11,747"

    st.markdown(f"<p style='font-size: 40px;'>Flight Price is: {formatted_price}</p>", unsafe_allow_html=True)
