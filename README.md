# 🚕 FareCast — NYC Cab Fare Predictor

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-ff4b4b?logo=streamlit&logoColor=white)](https://farecast-by-sei.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> *No more fare surprises! Get an instant fare estimate for your NYC cab ride. 🗽*

---

## 🔮 About

**FareCast** is a Streamlit web app that predicts NYC taxi fares in real time using a Machine Learning model served via a FastAPI REST API deployed on Google Cloud Run.

Enter your pickup and dropoff coordinates, choose your date and number of passengers — and let FareCast do the math!

---

## 🚀 Features

- 🗺️ Interactive map with pickup and dropoff markers (pydeck)
- 📡 Real-time fare prediction via REST API
- 🎬 Animated GIF while waiting for the prediction
- 🎵 Soundtrack for the ride
- 🧭 Sidebar with trip input controls

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Frontend | Streamlit |
| Map | pydeck |
| API client | requests |
| ML Model | TensorFlow / Keras |
| API server | FastAPI + Uvicorn |
| Deployment | Google Cloud Run |
| Containerization | Docker |

---

## 📦 Installation

```bash
git clone https://github.com/Seiiferu/taxifare-website
cd taxifare-website
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

```
taxifare-website/
├── app.py                  # Streamlit app
├── man_waiting_car.json    # Lottie animation
├── F1.mp3                  # Soundtrack
├── requirements.txt
└── README.md
```

---

## 🌐 API

The fare prediction is powered by a FastAPI backend:

```
GET /predict?pickup_datetime=...&pickup_longitude=...&pickup_latitude=...&dropoff_longitude=...&dropoff_latitude=...&passenger_count=...
```

Returns:
```json
{ "fare": 12.50 }
```

---

## 📝 License

MIT
