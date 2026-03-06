import streamlit as st
import requests
import pandas as pd
import pydeck as pdk
import time
import json

from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="🏙️ FareCast",
    page_icon="*",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://unsplash.com/photos/jZc5eTXnYLU/download?force=true");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

with open("man_waiting_car.json") as f:
    lottie = json.load(f)

if lottie:
    st_lottie(lottie, height=150)

st.title(":crystal_ball: :rainbow[ FareCast] :crystal_ball:")
st.caption("*Your NYC cab fare predictor*")

st.write_stream((c for word in "🗽 No more fare surprises! Enter your trip details and get an instant fare estimate for your NYC cab ride. 🚖" for c in (time.sleep(0.03) or word)))

# st.audio("lofi.mp3", autoplay=True)

with st.sidebar:
    st.header("🗽 Your Ride")
    st.caption("🛰️ Longitude, Latitude (⊙_⊙;)... if you don't know, Google is your bestie (*ノ▽ノ)")
    pickup_datetime = st.datetime_input("📆 Pickup a date:", value="now")
    pickup_longitude = st.number_input("📍 Pickup longitude:", value=-73.950655)
    pickup_latitude = st.number_input("📍 Pickup latitude:", value=40.783282)
    dropoff_longitude = st.number_input("🏁 Dropoff longitude:", value=-73.984365)
    dropoff_latitude = st.number_input("🏁 Dropoff latitude:", value=40.769802)
    passenger_count = st.number_input("👤 Passengers:", value=1)

df = pd.DataFrame({
    "lat": [pickup_latitude, dropoff_latitude],
    "lon": [pickup_longitude, dropoff_longitude],
    "color": [[18, 35, 158, 200], [232, 119, 34, 200]],
    "label": ["Here", "Destination"]
})

st.pydeck_chart(
    pdk.Deck(
        map_style="road",
        initial_view_state=pdk.ViewState(
            latitude=(pickup_latitude + dropoff_latitude) / 2,
            longitude=(pickup_longitude + dropoff_longitude) / 2,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "TextLayer",
                data=df,
                get_position="[lon, lat]",
                pickable=True,
                get_text="label",
                get_size=20,
                get_alignment_baseline="'bottom'",
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="color",
                get_radius = 300,
            ),
        ],
    )
)


# url = 'https://meterdrop-2207-679359889286.europe-west1.run.app/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


st.caption("🔊 *Warning: this app comes with a soundtrack, your ears have been warned* 🎵")

if st.button("🚕 Hail a Cab!"):
    st.audio("F1.mp3", autoplay=True)
    placeholder = st.empty()
    placeholder.image("https://media.giphy.com/media/0syAYHMyKZTijnnfkr/giphy.gif")
    time.sleep(5)
    response = requests.get('https://meterdrop-2207-679359889286.europe-west1.run.app/predict',
        params= {
            "pickup_datetime": pickup_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "pickup_longitude": pickup_longitude,
            "pickup_latitude": pickup_latitude,
            "dropoff_longitude": dropoff_longitude,
            "dropoff_latitude": dropoff_latitude,
            "passenger_count": passenger_count,
        }
)
    time.sleep(5)
    placeholder.empty()
    col1, col2 = st.columns(2)
    with col1:
        st.warning(f"🎯 Let's ride together! Your fare: **${response.json()['fare']:.2f}**")
    with col2:
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWw1ZHEzdGNmczZqOTgybHJiYmQwczhma2R0cGh2cnc3MnVlcXo3ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/m3cR00yyZoLAY/giphy.gif")
