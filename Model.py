import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("test.csv")

# split the dataset into input features and target variable
X = df[["open", "high", "low", "volume"]].values
y = df["close"].values

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create an instance of the Linear Regression model
lr = LinearRegression()

# fit the model to the training data
lr.fit(X_train, y_train)

# predict the target variable for the specific date
X_pred = pd.DataFrame(
    {
        "open": [17.04999924],
        "high": [17.17000008],
        "low": [15.80000019],
        "volume": [29954300],
    }
)
y_pred = lr.predict(X_pred)[0]

# calculate the confidence interval
y_pred_std = np.std(y_pred)
y_pred_interval = (y_pred - 1.96 * y_pred_std, y_pred + 1.96 * y_pred_std)

# display the predicted price and confidence interval
print(f'Predicted Price: ${y_pred:.2f}')
print(f"Confidence Interval: (${y_pred_interval[0]:.2f} - ${y_pred_interval[1]:.2f})")


# predict the target variable using the trained model
y_pred = lr.predict(X_test)
print(y_pred)
