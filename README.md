# house-price-prediction-
# House-price-prediction-using-flask
This project demonstrates the predictive capabilities of a model trained on house price data using Linear Regression. The model is deployed using a Flask API, providing an interface to predict house prices based on input features.


# House Price Prediction Web App

## Purpose or Description
This is a simple web application that predicts house prices based on user inputs (bedrooms, bathrooms, floors, and year built). The app uses a pre-trained linear regression model to make predictions.

## Technologies Used
- Python
- Flask
- NumPy
- HTML
- CSS


## How to Install/Run the Project
1. Clone or download this repository.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv

## Installation

You'll need to install the required libraries to run this web app on your local machine. These are listed in the requirements.txt file. The project was developed using Python 3.8.0 and Flask 2.0.1.<br><br> Install the necessary packages by running the following command in your terminal:<br><br>

```
pip install flask
pip install numpy
pip install scikit-learn
pip install flask numpy scikit-learn
pip freeze > requirements.txt
pip install -r requirement.txt
python -m pip install --upgrade pip

```
<br>
<br>

## Getting Started

After installing the required packages, you can start the application by executing the following command in your terminal:<br><br>
```
python app.py
```
<br>
<br>

##Activate the virtual environment:

On Windows:
bash
venv\Scripts\activate

On macOS/Linux
bash
source venv/bin/activate
Install the required dependencies:

bash
pip install flask numpy scikit-learn
Run the Flask app:

bash
python app.py
Open your web browser and go to:

cpp
http://127.0.0.1:5000/
Any Dependencies or Setup Requirements
Python 3.x

Flask

NumPy

scikit-learn

HTML/CSS files (in the templates and static folders)

Make sure model.pkl is present in the project directory (it will be created automatically when the app runs for the first time).

Usage Examples (Optional)
Open the web app in your browser.

Enter the number of bedrooms, bathrooms, floors, and the year of build.

Click Predict to see the predicted house price.

## Preview
<img src='(https://github.com/nikitapatil0406/house-price-prediction-/blob/main/price%20prediction.png)'></img>
<br>
<br>
<img src='https:C:\Users\shree\Downloads\House-price-prediction-using-flask-main\House-price-prediction-using-flask-main\static\images'></img>
<br>
<br>

⚠️ Notes
The model is trained on dummy data:

python
Copy
Edit
X = np.array([
    [2, 1, 1, 1990],
    [3, 2, 2, 2000],
    [4, 3, 2, 2010]
])
y = np.array([300000, 400000, 500000])
For real-world use, replace this with your own housing dataset.

Usage Examples (Optional)
Open the web app in your browser.

Enter the number of bedrooms, bathrooms, floors, and the year of build.

Click Predict to see the predicted house price.

## copy right by 2025
developed by Nikita Patil

<br>
<br>

### Thank you
