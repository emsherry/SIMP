# Stock Price Prediction using LSTM
This code uses Long Short-Term Memory (LSTM) neural networks to predict stock prices. The program loads historical stock data, trains a model on it, and then uses the trained model to predict future stock prices.

## Model
The program uses a sequential LSTM model with 3 LSTM layers, each with 50 units, and a dense output layer with 1 unit. Dropout layers are added after each LSTM layer to prevent overfitting. The model is compiled with the Adam optimizer and the mean squared error loss function.

## Data
The program loads data from a CSV file. The file should have a column named 'Close' with the closing prices for the stock.

The data is preprocessed using the MinMaxScaler from Scikit-Learn, which scales the data to a range between 0 and 1. The program then creates training data by using a sliding window approach, where it takes a sequence of 60 stock prices as input and the next stock price as output.

## Training
The program trains the model on the prepared training data for 25 epochs with a batch size of 32.

## Testing
The program then uses the trained model to predict future stock prices. It first loads the last 60 days of historical data, and then makes predictions for the next 5 days.

The program plots the actual stock prices and the predicted stock prices for the test data.
