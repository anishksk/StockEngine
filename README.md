# Stock Engine

## The Overview of the Project:
The project has 4 files:
  1. The first file is an Array file, which is a Linked List simulating an Array to use throughout the program.
  2. The second file is an Atomic Integer file which provides a thread-safe way to handle integers using a locking mechanism.
  3. The third file is an Order Book file which implements an order book for each ticker. It has a buy and sell Linked List, adds orders to the Linked Lists when appropriate, and matches orders when needed.
  4. The fourth file is the Stock Engine which manages order books for multiple tickers and processes buy and sell orders. The file is the main engine and simulates the trading sequences as well.

## Installation
In order to run the project, have to follow these steps:
  1. Clone the repository
  2. Install the necessary dependency: pip install requests (helps get the stock tickers)
  3. Run python StockEngine.py (the file has the simulation and will simulate the stock trading)
Once you run the file, the program should work.
