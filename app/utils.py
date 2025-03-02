def enforce_policies(prediction):
    """
    Enforces company policies on the prediction.
    Example: Ensure the prediction is within a specified range.
    """
    # Example policy: Min value = 100, Max value = 1000
    min_value = 100
    max_value = 1000

    if prediction < min_value:
        return min_value
    elif prediction > max_value:
        return max_value
    else:
        return prediction

def plot_stock_data(symbol):
    """
    Fetches and plots stock data for the given symbol.
    """
    import requests
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    # Fetch stock data
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=YOUR_API_KEY"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        time_series = data.get("Time Series (Daily)", {})
        dates = list(time_series.keys())[:30]  # Last 30 days
        prices = [float(time_series[date]["4. close"]) for date in dates]
        return dates, prices
    else:
        raise Exception("Failed to fetch stock data")