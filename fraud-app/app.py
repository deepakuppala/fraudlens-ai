import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Fraudlens.ai", layout="wide")

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return pickle.load(open("model.pkl", "rb"))

# ---------------- LOGIN ----------------
def login():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #141E30, #243B55);
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
            <h1 style='color:white;'>🔐 Fraudlens.ai</h1>
            <p style='color:#ddd; font-size:18px;'>
            AI-powered fraud detection system<br><br>
            Detect suspicious transactions instantly<br>
            Secure your financial data using Machine Learning
            </p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="
                padding:30px;
                border-radius:15px;
                background:rgba(255,255,255,0.1);
                backdrop-filter:blur(10px);
                box-shadow:0 8px 32px rgba(0,0,0,0.3);
            ">
        """, unsafe_allow_html=True)

        st.markdown("<h2 style='color:white; text-align:center;'>Login</h2>", unsafe_allow_html=True)

        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if st.button("🚀 Login"):
            if username == "admin" and password == "1234":
                st.session_state["logged_in"] = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- MAIN APP ----------------
def main_app():
    model = load_model()

    st.sidebar.title("🔐 Fraudlens.ai")
    st.sidebar.success("Fraud Detection System")

    menu = st.sidebar.radio("Navigation", ["🏠 Home", "🧪 Demo", "📂 Upload", "🚪 Logout"])

    # -------- HOME --------
    if menu == "🏠 Home":
        st.title("💳 AI Fraud Detection Dashboard")
        st.markdown("### Detect fraudulent transactions instantly using Machine Learning")
        st.info("Use Demo mode or Upload your dataset to analyze fraud.")

    # -------- DEMO --------
    elif menu == "🧪 Demo":
        st.title("🧪 Demo Prediction (Balanced Sample)")

        data = pd.read_csv("creditcard.csv")

        # Balanced sample (avoid 0% fraud)
        fraud_data = data[data["Class"] == 1]
        legit_data = data[data["Class"] == 0]

        sample = pd.concat([
            fraud_data.sample(10),
            legit_data.sample(40)
        ]).sample(frac=1)

        X_sample = sample.drop("Class", axis=1)

        st.dataframe(X_sample)

        if st.button("🔍 Detect Fraud"):
            pred = model.predict(X_sample)
            X_sample["Prediction"] = ["Fraud" if x == 1 else "Legit" for x in pred]

            st.subheader("🚨 Results")
            st.dataframe(X_sample)

            fraud = (X_sample["Prediction"] == "Fraud").sum()
            legit = (X_sample["Prediction"] == "Legit").sum()
            total = len(X_sample)

            c1, c2, c3 = st.columns(3)
            c1.metric("Total", total)
            c2.metric("Legit", legit)
            c3.metric("Fraud", fraud)

            rate = (fraud / total) * 100
            if rate > 5:
                st.error(f"🚨 High Fraud Rate: {rate:.2f}%")
            else:
                st.warning(f"⚠️ Fraud Rate: {rate:.2f}%")

            st.subheader("📊 Distribution")
            st.bar_chart(X_sample["Prediction"].value_counts())

            st.subheader("🥧 Pie Chart")
            fig, ax = plt.subplots()
            X_sample["Prediction"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
            st.pyplot(fig)

    # -------- UPLOAD --------
    elif menu == "📂 Upload":
        st.title("📂 Upload CSV")

        file = st.file_uploader("Upload CSV", type=["csv"])

        if file:
            data = pd.read_csv(file)
            st.dataframe(data.head())

            if st.button("🔍 Detect Fraud"):
                try:
                    # 🔥 Load expected structure
                    original = pd.read_csv("creditcard.csv")
                    expected_cols = original.drop("Class", axis=1).columns

                    df = data.copy()

                    # 🔥 Remove Class if present
                    if "Class" in df.columns:
                        df = df.drop("Class", axis=1)

                    # 🔥 Convert all to numeric
                    df = df.apply(pd.to_numeric, errors='coerce')

                    # 🔥 Match column order
                    df = df[expected_cols]

                    # 🔥 Fill missing
                    df = df.fillna(0)

                    # Predict
                    pred = model.predict(df)
                    df["Prediction"] = ["Fraud" if x == 1 else "Legit" for x in pred]

                    st.subheader("🚨 Results")
                    st.dataframe(df)

                    fraud = (df["Prediction"] == "Fraud").sum()
                    legit = (df["Prediction"] == "Legit").sum()
                    total = len(df)

                    c1, c2, c3 = st.columns(3)
                    c1.metric("Total", total)
                    c2.metric("Legit", legit)
                    c3.metric("Fraud", fraud)

                    rate = (fraud / total) * 100
                    if rate > 5:
                        st.error(f"🚨 High Fraud Rate: {rate:.2f}%")
                    else:
                        st.warning(f"⚠️ Fraud Rate: {rate:.2f}%")

                    st.subheader("📊 Distribution")
                    st.bar_chart(df["Prediction"].value_counts())

                    st.subheader("🥧 Pie Chart")
                    fig, ax = plt.subplots()
                    df["Prediction"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
                    st.pyplot(fig)

                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

    # -------- LOGOUT --------
    elif menu == "🚪 Logout":
        st.session_state["logged_in"] = False
        st.rerun()

# ---------------- FLOW ----------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    main_app()
else:
    login()