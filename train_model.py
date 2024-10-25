import pickle
from sklearn.ensemble import RandomForestRegressor  # or your actual model
from sklearn.model_selection import train_test_split
import numpy as np

# Example: Generate some random data (Replace this with actual data)
X = np.random.rand(100, 10)  # Example input features
y = np.random.rand(100)      # Example target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForestRegressor model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved to model.pkl")
