from flask import Flask, render_template, request
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Train and save model
X = np.array([[2, 1, 1, 1990], [3, 2, 2, 2000], [4, 3, 2, 2010]])
y = np.array([300000, 400000, 500000])

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
print("Model loaded successfully!")

@app.route('/')
def index():
    return render_template('index.html', data=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        floors = float(request.form['floors'])
        yr_built = float(request.form['yr_built'])

        input_data = np.array([[bedrooms, bathrooms, floors, yr_built]])

        prediction = model.predict(input_data)
        predicted_price = round(prediction[0], 2)

        return render_template('index.html', data=f"${predicted_price}")

    except Exception as e:
        print(f"Prediction error: {e}")
        return render_template('index.html', data="Error occurred during prediction.")

if __name__ == '__main__':
    app.run(debug=True)

