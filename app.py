import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Life Expectancy Prediction", layout="wide")
st.title("🌍 Life Expectancy Prediction using Linear Regression")

# Load dataset
uploaded_file = st.file_uploader("Upload your CSV dataset", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using sample dataset")
    df = pd.read_csv("life_expectancy.csv")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Select numeric features for model
numeric_cols = df.select_dtypes(include=['float64','int64']).columns.tolist()
if 'Life_Expectancy' not in numeric_cols:
    st.error("Dataset must have 'Life_Expectancy' column as target.")
else:
    X = df[numeric_cols].drop('Life_Expectancy', axis=1)
    y = df['Life_Expectancy']

    st.subheader("🔍 Correlation Heatmap")
    fig1, ax1 = plt.subplots(figsize=(8,6))
    numeric_df = df.select_dtypes(include=['number'])

    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax1)
    st.pyplot(fig1)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    st.subheader("📈 Model Performance")
    st.write(f"**R² Score:** {r2_score(y_test, y_pred):.3f}")
    st.write(f"**Mean Squared Error:** {mean_squared_error(y_test, y_pred):.3f}")

    # Predict new data
    st.subheader("🔮 Predict Life Expectancy for a New Sample")
    input_data = {}
    for col in X.columns:
        min_val, max_val = float(X[col].min()), float(X[col].max())
        default = float(X[col].mean())
        input_data[col] = st.number_input(col, min_val, max_val, default)

    if st.button("Predict"):
        sample = [list(input_data.values())]
        pred = model.predict(sample)[0]
        st.success(f"🌟 Predicted Life Expectancy: **{pred:.2f} years**")
