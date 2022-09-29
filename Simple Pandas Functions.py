import pandas as pd
#pd.Series Function Defines the Data in Series
my_series=pd.Series(data = [ -100, 100, -300, 50, 100])
print(300 in my_series.values)
#example of Crypto List (Basically a String array)
crypto_list = ['BTC','XRP','LTC', 'ADA', 'ETH'] 
crypto_series = pd.Series(data = crypto_list)
print(crypto_series.dtype) #Prints the Type of the Data Frame

# A Simple Mess Around with Dictionary To Acknowledge the difference in Python and pandas Data Fram
stocks = {'Facebook': 3000, 
          'Apple'   : 400,
          'Nvidia'  : 2200}
print(stocks)
# A TableAu Format of the Two Arrays 
my_list = ['Facebook','Apple','Nvidia'] 
my_labels = ['stock #1', 'stock #2', 'stock #3']
my_series = pd.Series(data = my_list, index = my_labels)
print(my_series)
# Again Simple List
my_list = ['Facebook','Apple','Nvidia'] 
my_series = pd.Series(data = my_list) 
print(my_series)