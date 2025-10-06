# 💼 Employee Salary Prediction

A web app built with Streamlit that uses machine learning on the Adult Income dataset to predict whether an employee’s annual salary is above or below 50K.

---

## 📝 Features

- Interactive web app built with Streamlit  
- Predicts salary class (`>50K` or `<=50K`) based on employee details  
- Uses only the most relevant employee features for prediction  

---

## 🛠️ How to Run Locally

1. **Clone the repository:**
    ```
    git clone https://github.com/BasutkarSony/Employee-Salary-Prediction.git
    cd employee-salary-prediction
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```
    streamlit run app.py
    ```

---

## ⚙️ Model Details

- **Dataset:** [Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult)  
- **Features Used:** Age, Workclass, Education, Occupation, Gender, Hours per week, and more  
- **Model Selection:** Tested Logistic Regression, Random Forest, SVM, KNN, and Gradient Boosting. The best model (Gradient Boosting with accuracy around 85.7%) was saved as `best_model.pkl`.  
- **Preprocessing:** Handled missing values, encoded categorical variables, removed outliers, and dropped redundant features to improve model accuracy.  

---

## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sony-employee-salary-prediction.streamlit.app/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

**Enjoy predicting salaries!😊**
