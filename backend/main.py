# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock and the time range
start = '2012-01-01'
end = '2022-12-21'
stock = 'GOOG'

# Download stock data from Yahoo Finance
data = yf.download(stock, start, end)

# Reset index to have date as a column
data.reset_index(inplace=True)

# Display the data
print(data)

# Calculate the 100-day moving average
ma_100_days = data['Close'].rolling(100).mean()

# Plot the 100-day moving average against the stock closing price
plt.figure(figsize=(8,6))
plt.plot(ma_100_days, 'r')
plt.plot(data['Close'], 'g')
plt.show()

# Calculate the 200-day moving average
ma_200_days = data['Close'].rolling(200).mean()

# Plot the 100-day, 200-day moving averages and the stock closing price
plt.figure(figsize=(8,6))
plt.plot(ma_100_days, 'r')
plt.plot(ma_200_days, 'b')
plt.plot(data['Close'], 'g')
plt.show()

# Drop any missing values
data.dropna(inplace=True)

# Split the data into training and testing sets
data_train = pd.DataFrame(data['Close'][0:int(len(data) * 0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])

print(f"Training Data Size: {data_train.shape[0]}")
print(f"Testing Data Size: {data_test.shape[0]}")

# Scale the data for LSTM model
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
data_train_scale = scaler.fit_transform(data_train)

# Create training sequences
x = []
y = []

for i in range(100, data_train_scale.shape[0]):
    x.append(data_train_scale[i-100:i])
    y.append(data_train_scale[i, 0])

x, y = np.array(x), np.array(y)

# Build the LSTM model
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential

model = Sequential()
model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(x.shape[1], 1)))
model.add(Dropout(0.2))

model.add(LSTM(units=60, activation='relu', return_sequences=True))
model.add(Dropout(0.3))

model.add(LSTM(units=80, activation='relu', return_sequences=True))
model.add(Dropout(0.4))

model.add(LSTM(units=120, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x, y, epochs=50, batch_size=32, verbose=1)

# Print model summary
model.summary()

# Prepare the testing data
pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
data_test_scale = scaler.fit_transform(data_test)

x_test = []
y_test = []

for i in range(100, data_test_scale.shape[0]):
    x_test.append(data_test_scale[i-100:i])
    y_test.append(data_test_scale[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)

# Make predictions
y_predict = model.predict(x_test)

# Rescale the predictions back to the original range
scale = 1 / scaler.scale_
y_predict = y_predict * scale
y_test = y_test * scale

# Plot the predicted and actual stock prices
plt.figure(figsize=(10,8))
plt.plot(y_predict, 'r', label='Predicted Price')
plt.plot(y_test, 'g', label='Original Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

# Save the model
model.save('Stock_Predictions_Model.keras')
