### --- ORDER BOOK CLASS --- ###
import threading
from AtomicInt import AtomicInt

class OrderNode:
    """
    Here is the node for the order book that will hold all the necessary information for the order.
    """
    def __init__(self, orderType, quantity, ticker, price):
        self.orderType = orderType
        self.quantity = AtomicInt(quantity)
        self.ticker = ticker
        self.price = price
        self.next = None

class OrderBook:
    def __init__(self):
        """
        There is a buy and sell order linked list to help with the order book and with matching.
        """
        self.buyOrders = None
        self.sellOrders = None
        self.lock = threading.Lock()

    def addOrder(self, orderType, quantity, ticker, price):
        """
        The function will add an order depending on the order type. Based on the order type, it will
        add the node in the correct order.
        """
        orderNew = OrderNode(orderType, quantity, ticker, price)
        print(f"Adding {orderType} order for {quantity} shares of {ticker} at price {price}")

        with self.lock:
            if orderType == "BUY":
                prev, curr = None, self.buyOrders
                while curr and curr.price >= orderNew.price:  # since it is a buy order, it will go through the linked list until it finds the price that is greater than or equal to the order price.
                    prev, curr = curr, curr.next
                orderNew.next = curr # adds the order
                if prev is None:
                    self.buyOrders = orderNew
                else:
                    prev.next = orderNew
            else:
                prev, curr = None, self.sellOrders
                while curr and curr.price <= orderNew.price:  # since it is a sell order, it will go through the linked list until it finds the price that is less than or equal to the order price. 
                    prev, curr = curr, curr.next
                orderNew.next = curr # adds the order
                if prev is None:
                    self.sellOrders = orderNew
                else:
                    prev.next = orderNew

        

    def matchOrders(self):
        """
        The function will help match the orders based on the price and also quantity. It will have different
        oeprations based on the trade amount as well.
        """
        while self.buyOrders and self.sellOrders and self.buyOrders.price >= self.sellOrders.price:
            with self.lock:
                buyAmount = self.buyOrders.quantity.get()
                sellAmount = self.sellOrders.quantity.get()
                
                if buyAmount <= sellAmount:
                    tradeAmount = buyAmount
                    if tradeAmount > 0:
                        print(f"Traded {tradeAmount} shares of {self.buyOrders.ticker} at {self.sellOrders.price}")
                        self.buyOrders.quantity.set(0)
                        self.sellOrders.quantity.set(sellAmount - buyAmount)
                        # Move to next buy order
                        self.buyOrders = self.buyOrders.next
                else:
                    tradeAmount = sellAmount
                    if tradeAmount > 0:
                        print(f"Traded {tradeAmount} shares of {self.buyOrders.ticker} at {self.sellOrders.price}")
                        self.buyOrders.quantity.set(buyAmount - sellAmount)
                        self.sellOrders.quantity.set(0)
                        # Move to next sell order
                        self.sellOrders = self.sellOrders.next
