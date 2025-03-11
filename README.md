# Econometric-HICP-Inflation-Predictor-Engine
Econometric Machine Learning Model for HICP Inflation Prediction with automated ECB &amp; Eurostat API data pulling


🏦📊 HICP Inflation Prediction Using ECB (European Central Bank) & Eurostat API Data 🔥📈
An advanced macroeconomic forecasting model leveraging direct indicators to predict Euro Area inflation.
Using real-time macroeconomic data, energy prices, and machine learning to enhance inflation nowcasting.

[Status] 🚀 In Development with new functional additions (Ready for User Deployment) | 📅 Econometric Forecasts - utilizing any historic range of ECB & Eurostat API data

🔍 Project Overview
This project builds a HICP (Harmonized Index of Consumer Prices) inflation prediction model for the Euro Area (U2) by integrating:
✅ An automated system for ECB (European central Bank) & Eurostat Data recognition:
      - Automated recognition of available datasets within ECB or ESTAT (depending on user input)
      - Automated recognition of available Dimensions within each ECB or Estat dataset 
      - Automated recognition of available code list values (with characteristics & descriptions) that could be inputed as API query requests for data pulls 
✅ An automated API Data Loader function for ECB & Eurostat API  
      - A helper function which automatically pulls ESTAT (Eurostat) & ECB (European Central Bank) macroeconomic data via API 
      - Provides data pull status request update
      - Compatible for any Data Date Range and Data Graunalirity (Daily - Weekly - Monthly - Annual - Quarterly) 
✅ Predictor function for macroeconomic Direct Indicators & Components (70%-30% Direct Indicator vs Component datasets) 🏦 (ECB & Eurostat data)
      - Econometric Dataset Sources : 
            - SI (Balance Sheet Items)
            - ESA (European System of Accounts) 
            - EXR (Exchange Rates) 
            - ICP (Harmonized Index of Consumer Prices - HICP) 
            - IRS (Interest Rates Statistics) 
            - LCI (Labour Cost Index)  
            - MIR (Monetary and Financial Institutions Interest Rates).
✅ Energy & commodity prices ⚡💰 (Electricity, gas, raw materials)
✅ Machine Learning (XGBoost) 🤖 to forecast monthly inflation trends

🔗 Key Features:

📡 Automated ECB/Eurostat API Extraction – Fetches structured economic datasets programmatically
📊 Feature Engineering (Lag Features) – Captures past trends & economic cycles
⚙️ ML Model (XGBoost) – Predicts inflation using 44 economic indicators
🕒 Nowcasting Approach – Provides short-term inflation forecasts
📂 Data Sources
🚀 Function Compatible Datasets: European Central Bank (ECB) & Eurostat
⚡ Energy & Commodity Data: Electricity & gas prices (EEX)

Dataset	Description	Time Granularity
ECB SDW	Monetary policy, labor market, GDP components	Monthly / Quarterly
Eurostat	Consumer & producer prices, wages, employment	Monthly
EEX Energy Prices	Electricity, gas, freight market prices	Daily / Monthly
💾 Data is stored in structured CSV files & extracted via APIs query pulls.

🏗️ Implementation & Workflow
🔹 1️⃣ Data Extraction & Preprocessing
📡 Automated API Requests: Fetches ECB & Eurostat datasets using the SDMX API
🛠️ Data Cleaning: Handling missing values, merging datasets, and aligning time-series data
📌 Feature Engineering: Creating lagged indicators (1 to 12 months) to improve trend detection

🔹 2️⃣ Model Training & Prediction
🚀 Algorithm: XGBoost Regressor
🔢 Advised Training Data: 2017 – 2021 
      - Many datasets relevent to HICP inflation start to have datagaps prior to 2017, making them incompatible for future harmonization and integration
📈 Test Data: 2022 – March 2023
      - Reccomended to start out HICP inflation prediction for a smaller data date range granularity (Monthly-Quarterly) 
🎯 Goal: Predict HICP inflation based on direct macroeconomic indicators
      - Note: **Understand Direct Indicators vs Component Idx Datasets** Direct indicator datasets provide raw, standalone economic measures such as actual market prices of goods and services (e.g., food, gas, electricity) without being aggregated into an index, whereas direct component datasets represent categorized sub-indices of inflation, such as HICP subcategories for food or energy, which are already aggregated into the overall inflation measure. In inflation forecasting, direct indicator datasets are often used in econometric models to estimate price movements independently before aggregation, allowing for a more granular and potentially leading assessment of inflation trends, whereas direct component datasets are used within index-based models like HICP decomposition to analyze how specific categories contribute to overall inflation, helping in understanding underlying inflationary pressures rather than predicting inflation from external variables.

🔹 3️⃣ Model Evaluation & Visualization
✅ Performance Metric: Mean Absolute Error (MAE)
📊 Visualization: Compare actual vs. predicted inflation over time
📡 Feature Importance: Analyze which indicators impact inflation the most

 
🏗️ Repository Structure
📦 HICP-Inflation-Predictor-Engine
│── 📂 data/               # Processed datasets & feature-engineered files
│── 📂 notebooks/          # Jupyter notebooks for data analysis & modeling
│── 📂 scripts/            # Python scripts for API extraction & ML pipeline
│── 📂 models/             # Trained models & hyperparameter tuning results
│── 📄 README.md           # Project documentation
│── 📄 requirements.txt    # Dependencies list
🚀 How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Run Data Extraction
python scripts/data_loader.py
3️⃣ Train the Model & Predict Inflation
python scripts/train_model.py
4️⃣ Visualize Predictions
 
python scripts/visualize_results.py
🔮 Future Enhancements
🔹 Integrate Deep Learning Models (LSTM, Transformers) for sequence modeling
🔹 Use alternative inflation metrics (Core HICP, Trimmed Mean CPI)
🔹 Expand energy price dataset (OIL, GAS, ELECTRICITY from multiple sources)

🏆 Acknowledgments
💡 Data Providers: ECB, Eurostat, EEX Energy Markets
💡 Machine Learning Framework: XGBoost
💡 Visualization: Matplotlib, Seaborn
