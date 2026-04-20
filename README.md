
# fraudlens1
=======
# 🔐 Fraudlens.ai – AI Fraud Detection System

Fraudlens.ai is a machine learning-powered web application that detects fraudulent financial transactions using real-world data. It provides an interactive dashboard with analytics, visualizations, and real-time predictions.

---

## 🚀 Features

* 🔐 Secure Login System
* 🤖 Machine Learning-based Fraud Detection
* 📊 Interactive Dashboard (Metrics, Charts)
* 🧪 Demo Mode with Balanced Data
* 📂 Upload CSV for Custom Predictions
* 📈 Fraud Rate Analysis
* 🥧 Pie Chart & 📊 Bar Graph Visualization

---

## 🧠 Technology Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Machine Learning:** Scikit-learn (Random Forest)
* **Data Processing:** Pandas
* **Visualization:** Matplotlib

---

## 📂 Project Structure

```
fraud-app/
│── assets/
│   ├── login.png
│   ├── demo.png
│   ├── graph.png
│   ├── bar.png
│── app.py
│── train.py
│── model.pkl
│── creditcard.csv
│── requirements.txt
│── README.md
```

---

## 📊 Dataset

* Credit Card Fraud Detection Dataset (Kaggle)
* Highly imbalanced real-world transaction data

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/fraudlens-ai.git
cd fraudlens-ai
pip install -r requirements.txt
```

---

## 🧠 Train Model

```bash
python train.py
```

---

## ▶️ Run App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🔑 Login Credentials

```
Username: admin
Password: 1234
```

---

# 📸 Screenshots

## 🔐 Login Page

![Login](assets/login.png)

## 🧪 Demo Prediction

![Demo](assets/demo.png)

## 📊 Dashboard Graph

![Graph](assets/graph.png)

## 📈 Bar Chart

![Bar](assets/bar.png)

---

## 🎯 How It Works

1. Load trained ML model
2. Preprocess input data
3. Align dataset features
4. Predict fraud using Random Forest
5. Display results with analytics

---

## ⚠️ Note

* Fraud data is highly imbalanced (~0.2%)
* Demo mode uses balanced sampling for better visualization
* Uploaded CSV must match dataset structure

---

## 🚀 Future Improvements

* 🎯 Real-time API integration
* 📊 Confusion Matrix
* 🎨 Advanced UI
* ☁️ Deployment

---

## 👨‍💻 Author

**Deepak**
AIML Student | Aspiring Software Developer

---

## ⭐ Project Tagline

**Fraudlens.ai – See fraud before it happens**
