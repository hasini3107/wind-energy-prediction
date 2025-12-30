# 🌬️ Wind Energy Prediction

This project predicts **wind energy (power output)** using machine learning based on wind turbine data such as wind speed, wind direction, and theoretical power curve values.

The project includes a **Polynomial Regression model** and an interactive **Streamlit web application** for real-time prediction.

---

## 📌 Features

- Predicts wind energy output (kW)
- Uses Polynomial Regression for better non-linear fitting
- Interactive Streamlit web interface
- Background image and sound effects
- Easy-to-use sliders and inputs

---

## 📊 Dataset

The dataset contains the following columns:

- **Date/Time**
- **Wind Speed (m/s)**
- **Wind Direction (°)**
- **Theoretical Power Curve (kWh)**
- **LV ActivePower (kW)** → Target variable

File used: `T1.csv`

---

## 🧠 Machine Learning Model

- **Algorithm:** Polynomial Regression  
- **Why Polynomial Regression?**  
  Wind energy does not increase linearly with wind speed. Polynomial regression captures the non-linear relationship between wind speed and power output.

Saved files:
- `polynomial_regression_model.pkl`
- `poly_features.pkl`
- `scaler.pkl`

---

## 🖥️ Web Application (Streamlit)

The Streamlit app allows users to input:
- Wind Speed
- Wind Direction
- Theoretical Power Curve

And predicts:
- **Wind Energy Output (kW)**

Main file:
- `app.py`

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/hasini3107/wind-energy-prediction.git
cd wind-energy-prediction
## 🔗 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hasini%20Unnamatla-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/hasini-unnamatla-365995334/)
