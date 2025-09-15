class SimpleStrategy:
    def __init__(self):
        self.last_price = None

    def on_tick(self, tick):
        price = tick['last_price']
        if self.last_price is None:
            self.last_price = price
            return None
        # Example: if price jumps by >0.5%
        change = (price - self.last_price) / self.last_price * 100
        self.last_price = price
        if change > 0.5:
            return {"side": "BUY", "symbol": tick["instrument_token"], "qty": 50}
        elif change < -0.5:
            return {"side": "SELL", "symbol": tick["instrument_token"], "qty": 50}
        return None
