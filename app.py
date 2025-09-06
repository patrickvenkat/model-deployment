from flask import Flask, render_template, request # type: ignore
import pickle

app = Flask(__name__)
cv = pickle.load(open("models/cv.pkl", "rb"))
clf = pickle.load(open("models/clf.pkl", "rb"))

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    email = request.form.get('email-content')
    tokenized_email = cv.transform([email]) # X 
    prediction = clf.predict(tokenized_email)
    prediction = 1 if prediction == 1 else -1
    
    return render_template("index.html", prediction=prediction, email=email)

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)