Here’s a clean and professional **README.md** for your project based on your code:

---

#  AI Wellness Assistant (Student Burnout Predictor)

## Description

The **AI Wellness Assistant** is a machine learning–based application designed to predict the risk of student burnout using lifestyle and behavioral metrics. It collects inputs such as study hours, sleep patterns, stress levels, and more, then analyzes them using a trained model to provide predictions along with actionable recommendations.

This tool aims to promote healthier routines and early intervention for students at risk.

---

##  Features

*  **Burnout Prediction** using a trained Random Forest model
*  **Interactive CLI Interface** for user input
*  **Personalized Recommendations** based on user data
*  **Prediction History Tracking** with timestamps
*  **History Management** (view and clear records)
*  **Feature Importance Insights** to understand key burnout factors
*  **Input Validation** for accurate data entry

---

##  Technologies Used

* **Python**
* **Pandas** – Data handling
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine Learning (Random Forest Classifier)
* **CSV** – Data storage and history tracking

---

##  Project Structure

```
project/
│── main.py                  # Main application file
│── data.csv                 # Dataset for training the model
│── prediction_history.csv   # Stores user predictions
│── README.md               # Project documentation
```

---

##  Installation

1. Clone the repository:

```bash
git clone <your-repo-link>
cd <project-folder>
```

2. Install required dependencies:

```bash
pip install pandas numpy scikit-learn
```

---

##  How to Run

Run the main Python file:

```bash
python main.py
```

---

##  Input

The program asks the user to enter:

* Name
* Age
* Study hours per day
* Sleep hours
* Screen time
* Stress level (1–10)
* Exercise hours
* Caffeine intake (cups)

---

##  Output

The system provides:

* Burnout Risk Status (High / Low)
* Probability of burnout
* AI-generated personalized recommendation
* Stored record in history file

---

##  Example

```
Enter student details:
Study hours: 6
Sleep hours: 5
Screen time: 8
Stress level: 9
Exercise hours: 0.2
Caffeine: 5

Output:
 STATUS: HIGH RISK OF BURNOUT
 PROBABILITY: 78.5%
 AI SUGGESTION:  High Stress: Try the 4-7-8 breathing method...
```

---

##  Model Details

* Model Used: **Random Forest Classifier**
* Number of Trees: 100
* Class Weight: Balanced (to handle imbalance in burnout cases)
* Threshold: **0.55** probability for classification
* Features Used:

  * Study hours
  * Sleep hours
  * Screen time
  * Stress level
  * Exercise hours
  * Caffeine intake

The model is trained dynamically using `data.csv`. If the dataset is missing, synthetic data is generated automatically. 

---

##  Conclusion

This project demonstrates how machine learning can be applied to real-life student wellness challenges. It not only predicts burnout risk but also provides actionable insights, making it a practical tool for awareness and prevention.

Future improvements could include:

* GUI/Web interface
* Larger and more realistic dataset
* Advanced models (e.g., XGBoost, Neural Networks)
* Visualization dashboards

---

##  Author

**Yash Kesarwani (25BHI10044)**

---
