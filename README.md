# LSTM-for-stock-price-volatility-detection
Volatility plays crucial roles in financial markets, such as in derivative pricing, portfolio risk management, and hedging strategies. Therefore, accurate prediction of volatility is critical.

We will be utilizing a comprehensive data set comprising bitcoin price fluctuations across various timeframes. This data will be divided into distinct buckets and inputted into a Recurrent Neural Network (RNN)


## Performance:
<p align="center">
  <img src="https://github.com/6amir6hosein6/LSTM-for-stock-price-volatility-detection/blob/main/result/001-performance.png">
</p>

<p align="center">
  <img src="https://github.com/6amir6hosein6/LSTM-for-stock-price-volatility-detection/blob/main/result/000-performance.png" width="50%">
</p>

## Example:

<p align="center">
  <img src="https://github.com/6amir6hosein6/LSTM-for-stock-price-volatility-detection/blob/main/result/000-Bitcoin-example.png" width="45%">
  &nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://github.com/6amir6hosein6/LSTM-for-stock-price-volatility-detection/blob/main/result/001-Bitcoin-example.png" width="45%">
</p>

## Functions:

### Evaluation : 
After the learning process is over, you can see the success rate of the trained model using this file


### Model Training : 
Here the model is defined and it is used to train the data


### Data Generator : 
In this file, after bucketing, the normalized data is ready to go to the model and start the learning process


### PreProcessor : 
In this file, the normalization operation on the read data is called


### Data Loader : 
In this file, the given raw data is prepared for further processing


