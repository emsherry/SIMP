import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# load data
company = "SHEZ"

data = pd.read_csv("../StockDatasets/SHEZ.csv", index_col="Date", parse_dates=True)
print(data.head())

# Prepare data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1, 1))

prediction_days = 60

X_train = []
Y_train = []

for i in range(prediction_days, len(scaled_data)):
    X_train.append(scaled_data[i - prediction_days : i, 0])
    Y_train.append(scaled_data[i, 0])

X_train = np.array(X_train)
Y_train = np.array(Y_train)


X_train, Y_train = np.array(X_train), np.array(Y_train)
# X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

X_train = np.reshape(X_train, (X_train.shape[0], 60, 1))
Y_train = np.reshape(Y_train, (Y_train.shape[0], 1))

# Building the model
model = Sequential()

print(X_train.shape)

model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))  # Prediction of the next closing value

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X_train, Y_train, epochs=50, batch_size=32)

###TEST###
test_data = pd.read_csv("../StockDatasets/SHEZ.csv", index_col="Date", parse_dates=True)
actual_prices = test_data["Close"].values

total_Data = pd.concat((data["Close"], test_data["Close"]), axis=0)

model_inputs = total_Data[len(total_Data) - len(test_data) - prediction_days :].values
model_inputs = model_inputs.reshape(-1, 1)
model_inputs = scaler.transform(model_inputs)

# Make Predictions on test data

X_test = []

for x in range(prediction_days, len(model_inputs)):
    X_test.append(model_inputs[x - prediction_days : x, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

predicted_prices = model.predict(X_test)
predicted_prices = scaler.inverse_transform(predicted_prices)


# Plotting the prediction
plt.plot(actual_prices, color="blue", label=f"actual {company} price")
plt.plot(
    predicted_prices,
    color="green",
    label=f"predicted {company} price",
)
plt.title(f"{company} share price")
plt.xlabel("time")
plt.ylabel("price")
plt.legend()
plt.show()

# Predicting the next 5 days
last_5_days = total_Data[-prediction_days:].values.reshape(-1, 1)
last_5_days_scaled = scaler.transform(last_5_days)

X_test = []
X_test.append(last_5_days_scaled[-prediction_days:, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

predicted_prices = []
for i in range(5):
    predicted_price = model.predict(X_test)
    predicted_prices.append(predicted_price)
    predicted_price = predicted_price.reshape(1, 1, 1)
    X_test = np.concatenate((X_test[:, 1:, :], predicted_price), axis=1)

predicted_prices = np.array(predicted_prices).reshape(-1, 1)
predicted_prices = scaler.inverse_transform(predicted_prices)

print("Predicted Prices for the next 5 days: ")
print(predicted_prices)
