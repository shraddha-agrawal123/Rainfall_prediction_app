import numpy as np
from sklearn.metrics import mean_squared_error

# Example data
y_test = np.array([3.5, 2.1, 4.2])
y_pred = np.array([3.6, 2.0, 4.3])

# Calculate MSE
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
