# Stock Alert Bot

This Python script monitors stock prices and sends notifications when certain thresholds are reached.

## Overview

The script fetches the latest stock prices for a predefined list of tickers and compares them to predefined upper and lower limits. It sends a desktop notification when a stock price crosses these limits.

## Features

- Monitors multiple stock tickers.
- Sends desktop notifications for buy and sell signals.
- Uses `yfinance` to fetch stock data.
- Uses `plyer` to send notifications.

## Requirements

- Python 3.x
- `yfinance` library
- `plyer` library

You can install the required libraries using pip:

```bash
pip install yfinance plyer
