import threading
import random
import time
import requests
from OrderBook import OrderBook
from Array import Array
## --- STOCK TRADING ENGINE --- ###


class StockTrading:
    def __init__(self):
        self.orderBookList = Array(1024)  
        for i in range(1024):
            self.orderBookList.set(i, OrderBook()) # creates an order book in each index of the array

        self.tickers = Array(size=1024) # tickers array which holds all the tickers
        self.loadTickers()

    def loadTickers(self):
        """
        This function loads the tickers from the API. The API endpoint provides the necesary information
        and using that information, can get the tickers from it.
        """
        try:
            url = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo" # API endpoint that we can use
            response = requests.get(url)
            if response.status_code == 200:
                counter = 0
                values = response.text.split('\n') # Splits the response
                for value in range(1024):
                    ticker = values[value].split(',')
                    self.tickers.set(counter, ticker[0]) # gets the ticker and then sets it to the array
                    counter += 1
                print(f"Loaded {counter} tickers")
        except Exception as e:
            print(f"Error loading tickers: {e}")

    def addOrder(self, orderType, quantity, ticker, price):
        """
        This function finds the index of the ticker based in the array and then uses 
        that index to add and match the orders.
        """
        index = -1
        for i in range(1024):
            if self.tickers.get(i) == ticker: # checks if the ticker is there and if it is, then sends the corresponding index to the variable
                index = i
                break
                
        if index != -1:
            book = self.orderBookList.get(index) # gets the specific order book and will add and match that order
            book.addOrder(orderType, quantity, ticker, price)
            book.matchOrders()
        else:
            print(f"Ticker {ticker} not found in stock list")

### --- SIMULATION FUNCTION --- ###
def simulation(tradingPlatform, orders):
    """
    The simulation which will generate random variables for the order and then add those random orders.
    """
    for _ in range(orders):
        orderType = random.choice(["BUY", "SELL"])
        index = random.randint(0, 1023)
        ticker = tradingPlatform.tickers.get(index)
        quantity = random.randint(1, 100)
        price = random.randint(500, 1000) if orderType == "BUY" else random.randint(1, 500)
        tradingPlatform.addOrder(orderType, quantity, ticker, price) # with all the random variables, will be able to add the orders
        time.sleep(0.1)

### --- MAIN EXECUTION --- ###
if __name__ == "__main__":
    """
    This is the main function where the engine will be initialized and then will simulate the orders.
    Threading is used here to help run the simulation.
    """
    engine = StockTrading()
    threads = []
    for _ in range(2): # used to run the number of threads for the simulation
        t = threading.Thread(target=simulation, args=(engine, 50)) 
        threads.append(t)
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    for i in range(1024):
        engine.orderBookList.get(i).matchOrders()
