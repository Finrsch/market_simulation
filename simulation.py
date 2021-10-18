import pandas
import requests

import quandl #necessary ONLY if using quandl function below
quandl.ApiConfig.api_key="YOUR_TOKEN_HERE" #necessary ONLY if using the QUANDL function below

holding_list=list() #global variable. It holds the position. List element = [ticker, position_buy_value]
investment=int() #global variable, this is the amount needed to invest. Needs to be initiated with an actual VALUE!


#VARIOUS WAYS of getting the stock data, automatically. Alternatively nasdaq.com is a good source for personal use
def api_iex(stock):
    """
    -- requires IEX subscription from https://iexcloud.io/
    Function calls the IEX API and returns a pandas df of it. This function accesses the FULL available historical data
    """
    data=requests.get('https://cloud.iexapis.com/stable/stock/{}/chart/max?token=pk_{YOUR_TOKEN_HERE}'.format(stock.lower()))
    try:
        dataj=data.json()
    except:
        return 'Error in api_iex for {}.'.format(stock)
    data_list=list()
    for i in dataj:
        data_list.append([i['date'], i['open'], i['close'], i['low'], i['high'], i['volume']])
    df=pd.DataFrame(data_list, columns=['date', 'open', 'close', 'low', 'high', 'volume'])
    return df

def api_quandl(equity):
    """
    -- requires QUANDL subscription for SHARDAR data sets from https://www.quandl.com/
    Function calls QUANDL API for stocks
    -- this needs to install and import quandl library
    -- after importing quandl, you need to set your toke calue: quandl.ApiConfig.api_key="YOUR_TOKEN_HERE"
    """
    source=quandl.get_table('SHARADAR/SEP', ticker=equity)
    data=source[['date', 'close', 'open', 'low', 'high']]
    return data
  
#function that checks if enough liquidity in the stock, considering investment variable set above
def stock_liquidity(stock_data, investment):
    return value #yes/no

#each of the functions below are using the holding_list global variable to hold & track the position
def buying_condition():
    #if BUY condition met, then we append [stock.lower(), stock_value] to the holding_list
    #the buying is executed within the level of investment, the global variable
    return

def loss_cut():
    #check if today's LOW value is below stock_value*(1-loss_cut_level)
    #it also updates investment, the global valriable
    return

def sell_condition():
    #if SELL condition met, then we remove [stock.lower(), stock_value] from the holding_list
    #it also updates investment, the global variable
    return


def algo_market_simulation(stock):
    stock_data=api_iex(stock) #getting stock data, in padas format. Can be further processed as needed
    a=stock_liquidity(stock_data)
    if a=='no':
      return 'Not enough liquidity in the stock'
    """
    STARTING the loop, using the length of the pandas as the index to follow
    """
    position='' #initiating position as an empty string
    for i in range(len(stock_data)):
        if position:
            buying_condition()
        else:
            if loss_cut_level_condition:
                loss_cut()
            else:
                sell_condition()
        #assuming the list only holds one position
        if stock.lower() in holding_list[0]:
            position='yes'
        else:
            position=''
    return
