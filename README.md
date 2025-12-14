# 🌍 Life Expectancy Prediction using Linear Regression

This project is a **Machine Learning web application** built with **Streamlit** that predicts **Life Expectancy** based on various socio-economic and health-related factors using **Linear Regression**.

The app allows users to:

* View and explore the dataset
* Understand feature relationships through visualizations
* Train a Linear Regression model
* Predict life expectancy for new input values

---

## 📌 Project Overview

Life expectancy is influenced by many factors such as mortality rates, BMI, GDP, schooling, alcohol consumption, and health conditions. This project uses **Linear Regression**, a supervised learning algorithm, to model the relationship between these factors and life expectancy.

---

## 🧠 Machine Learning Algorithm

* **Algorithm Used:** Linear Regression
* **Type:** Supervised Learning (Regression)
* **Target Variable:** `Life_Expectancy`
* **Evaluation Metrics:**

  * R² Score
  * Mean Squared Error (MSE)

---

## 📂 Dataset Details

**File:** `life_expectancy.csv`

### Sample Features:

* Adult_Mortality
* Infant_Deaths
* Alcohol
* Percentage_Expenditure
* BMI
* HIV_AIDS
* GDP
* Schooling

### Target Column:

* **Life_Expectancy** (in years)

You can upload your own dataset, but it **must contain numeric columns** and the target column named `Life_Expectancy`.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

---

## 📁 Project Structure

```
Life-Expectancy-Prediction/
│
├── app.py
├── life_expectancy.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/life-expectancy-prediction.git
cd life-expectancy-prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

---

## 🎯 How the App Works

1. Loads the dataset (default or user-uploaded)
2. Displays dataset preview
3. Shows correlation heatmap
4. Splits data into training and testing sets
5. Trains a Linear Regression model
6. Evaluates performance using R² and MSE
7. Predicts life expectancy based on user inputs

---

## 🔮 Sample Prediction

Users can input values for features like BMI, GDP, Schooling, etc., and the app predicts:

> **Predicted Life Expectancy (in years)**

---

## 🛑 Common Errors & Fixes (Important)

### ❌ Correlation Heatmap Error on Streamlit Cloud

If you see an error related to `df.corr()` or `ValueError`, it means your dataset contains **non-numeric columns**.

✅ **Fix used in this app:**
Only numeric columns are selected before plotting the heatmap:

```python
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
```

This makes the app **100% compatible with Streamlit Cloud**.

---

## ☁️ Deploy on Streamlit Cloud

1. Push all files to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select repository and `app.py`
5. Click **Deploy**

---

## 📸 Screenshots (Optional)

*Add screenshots of your Streamlit app here for better presentation.*

---

## 🙌 Author

**Guru Nagajothi**
Computer Science Engineering Student
Aspiring Machine Learning & Data Science Engineer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it on LinkedIn 🚀
