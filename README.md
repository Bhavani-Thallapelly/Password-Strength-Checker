# 🔒 Machine Learning Password Strength Checker

## Overview

This project is a **Machine Learning-based Password Strength Checker** that predicts whether a password is **Weak**, **Medium**, or **Strong** using a **Random Forest Classifier**. It provides a simple and interactive web interface where users can enter a password and instantly view its predicted strength.

---

## Dashboard Screenshot

![Dashboard](static/images/dashboard.png)

---

## Features

* Machine Learning-based password strength prediction
* Random Forest Classifier
* Predicts Weak, Medium, or Strong passwords
* Interactive web interface
* Show/Hide password option
* Password strength meter
* User-friendly design

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Scikit-learn
* Pandas
* NumPy
* Joblib

---

## Project Structure

```text
Password-Strength-Checker/
│
├── app.py
├── train.py
├── dataset_generator.py
├── password_dataset.csv
├── model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│       └── dashboard.png
│
└── README.md
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Bhavani-Thallapelly/Password-Strength-Checker.git
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in your browser

```text
http://127.0.0.1:5000
```

---

## Future Enhancements

* Password entropy calculation
* Password breach detection
* Strong password generator
* Real-time password suggestions

---

## Author

**Bhavani Thallapelly**

Machine Learning & Cybersecurity Enthusiast
