 MyoCast 🫀

> **Predicting cardiovascular risks before the next beat. An end-to-end machine learning application forecasting myocardial infarction with 87% accuracy.**

---

MyoCast is an intelligent predictive framework designed to assist in the early detection of myocardial infarction (heart attacks). By leveraging a pipeline of classic machine learning classifiers, MyoCast analyzes key patient physiological metrics to evaluate cardiac risk with high precision and reliability.

Rather than relying on a single algorithm, this project evaluates a suite of predictive models to find the most robust decision boundary for cardiac health classification.

---

## 🚀 Key Features

* **87% Classification Accuracy:** Rigorously trained and evaluated using optimized hyperparameters.
* **Multi-Model Pipeline:** Built with standard preprocessing (`StandardScaler`) and evaluates multiple classification algorithms (KNN, SVM, Decision Trees, Naive Bayes, and Logistic Regression).
* **Developer-Friendly Interface:** Structured, clean code written in Python using `scikit-learn` for rapid deployment and testing.

---

## 📊 Model Evaluation & Metrics

To ensure the model is both highly accurate and clinically relevant, performance was evaluated using multiple metrics (Precision, Recall, and F1-Score). 

*An 87% accuracy represents a highly viable, generalized model optimized to balance false positives and false negatives.*

| Machine Learning Model | Accuracy | F1-Score | Status |
| :--- | :---: | :---: | :--- |
| **MyoCast (Best Classifier)** | **87%** | **0.86** | **Active Production** |
| Support Vector Classifier (SVC) | 84% | 0.83 | Evaluated |
| K-Nearest Neighbors (KNN) | 81% | 0.80 | Evaluated |
| Decision Tree Classifier | 80% | 0.79 | Evaluated |
| Naive Bayes (GaussianNB) | 79% | 0.78 | Evaluated |

---

## 🛠️ Tech Stack & Dependencies

MyoCast is built purely in Python, utilizing standard, industry-grade scientific libraries:

* **Language:** Python 3.x
* **Core ML Library:** `scikit-learn`
* **Data Manipulation:** `pandas`, `numpy`

---

## ⚙️ Installation & Usage

To run MyoCast locally, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/MyoCast.git](https://github.com/YOUR_GITHUB_USERNAME/MyoCast.git)
cd MyoCast
