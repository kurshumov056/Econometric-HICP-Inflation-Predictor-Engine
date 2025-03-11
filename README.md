# Econometric-HICP-Inflation-Predictor-Engine  
Econometric Machine Learning Model for HICP Inflation Prediction with automated ECB & Eurostat API data pulling  

---

## 🏦📊 HICP Inflation Prediction Using ECB (European Central Bank) & Eurostat API Data 🔥📈  
An advanced macroeconomic forecasting model leveraging direct indicators to predict Euro Area inflation.  
Using real-time macroeconomic data, energy prices, and machine learning to enhance inflation nowcasting.  

---

## **[Status]** 🚀 In Development with new functional additions (Ready for User Deployment) | 📅 Econometric Forecasts - utilizing any historic range of ECB & Eurostat API data  

---

## 🔍 **Project Overview**  
This project builds a **HICP (Harmonized Index of Consumer Prices) inflation prediction model** for the Euro Area (U2) by integrating:

✅ **An automated system for ECB (European Central Bank) & Eurostat Data recognition:**  
   - Automated recognition of available datasets within ECB or ESTAT (depending on user input)  
   - Automated recognition of available Dimensions within each ECB or Eurostat dataset  
   - Automated recognition of available code list values (with characteristics & descriptions) that could be inputted as API query requests for data pulls  

✅ **An automated API Data Loader function for ECB & Eurostat API**  
   - A helper function which automatically pulls ESTAT (Eurostat) & ECB (European Central Bank) macroeconomic data via API  
   - Provides data pull status request updates  
   - Compatible for any **Data Date Range and Granularity** (Daily - Weekly - Monthly - Annual - Quarterly)  

✅ **Predictor function for macroeconomic Direct Indicators & Components** (70%-30% Direct Indicator vs Component datasets) 🏦 **(ECB & Eurostat data)**  
   - **Econometric Dataset Sources**:  
     - **SI** (Balance Sheet Items)  
     - **ESA** (European System of Accounts)  
     - **EXR** (Exchange Rates)  
     - **ICP** (Harmonized Index of Consumer Prices - HICP)  
     - **IRS** (Interest Rates Statistics)  
     - **LCI** (Labour Cost Index)  
     - **MIR** (Monetary and Financial Institutions Interest Rates)  

✅ **Energy & Commodity Prices** ⚡💰 *(Electricity, gas, raw materials)*  
✅ **Machine Learning (XGBoost)** 🤖 to forecast monthly inflation trends  

---

## 🔗 **Key Features:**  
📡 **Automated ECB/Eurostat API Extraction** – Fetches structured economic datasets programmatically  
📊 **Feature Engineering (Lag Features)** – Captures past trends & economic cycles  
⚙️ **ML Model (XGBoost)** – Predicts inflation using **44 economic indicators**  
🕒 **Nowcasting Approach** – Provides short-term inflation forecasts  

---

## 📂 **Data Sources**  
| Dataset         | Description                                        | Time Granularity  |  
|----------------|----------------------------------------------------|-------------------|  
| **ECB SDW**    | Monetary policy, labor market, GDP components     | Monthly / Quarterly |  
| **Eurostat**   | Consumer & producer prices, wages, employment     | Monthly            |  
| **EEX Energy Prices** | Electricity, gas, freight market prices  | Daily / Monthly    |  

💾 Data is stored in structured **CSV files** & extracted via API query pulls.  

---

## 🏗️ **Implementation & Workflow**  

### 🔹 **1️⃣ Data Extraction & Preprocessing**  
📡 **Automated API Requests** – Fetches ECB & Eurostat datasets using the SDMX API  
🛠️ **Data Cleaning** – Handles missing values, merges datasets, and aligns time-series data  
📌 **Feature Engineering** – Creates **lagged indicators (1 to 12 months)** to improve trend detection  

---

### 🔹 **2️⃣ Model Training & Prediction**  
🚀 **Algorithm** – XGBoost Regressor  
🔢 **Training Data:** *2017 – 2021*  
   - Many datasets relevant to HICP inflation **start to have data gaps before 2017**, making them incompatible for future harmonization and integration.  

📈 **Test Data:** *2022 – March 2023*  
   - Recommended to start **HICP inflation prediction** with a smaller **date range granularity** (Monthly-Quarterly).  

🎯 **Goal:** Predict **HICP inflation** based on **direct macroeconomic indicators**  
📌 **Note:**  
   - **Direct Indicators vs Component Index Datasets**:  
     **Direct indicator datasets** provide **raw, standalone economic measures** such as **actual market prices of goods and services** (e.g., food, gas, electricity) **without being aggregated** into an index.  
     **Direct component datasets**, on the other hand, represent **categorized sub-indices** of inflation (e.g., HICP subcategories for food or energy), which are already aggregated into the **overall inflation measure**.  
     - Direct indicators help econometric models estimate price movements before aggregation.  
     - Direct components analyze inflationary pressures within an index-based model like HICP decomposition.  

---

### 🔹 **3️⃣ Model Evaluation & Visualization**  
✅ **Performance Metric:** Mean Absolute Error (MAE)  
📊 **Visualization:** Compare **actual vs. predicted inflation** over time  
📡 **Feature Importance:** Analyze which indicators impact inflation the most  

---

## 🏗️ **Repository Structure**  

