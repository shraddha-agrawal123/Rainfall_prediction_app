from flask import Flask, request, jsonify
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the model and scaler
with open('model.pkl', 'rb') as model_file:
    model_svc, scaler = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json(force=True)
    
    # Extract features from JSON
    features = [
        data['pressure'], 
        data['temperature'], 
        data['dewpoint'], 
        data['humidity'], 
        data['cloud'], 
        data['sunshine'], 
        data['winddirection'], 
        data['windspeed']
    ]
    
    # Convert features to numpy array and scale
    features_array = np.array([features])
    scaled_features = scaler.transform(features_array)
    
    # Predict probability of rainfall
    probability = model_svc.predict_proba(scaled_features)[0][1]
    
    # Return probability as JSON
    return jsonify({'rainfall_probability': probability})

if __name__ == '__main__':
    app.run(debug=True)
