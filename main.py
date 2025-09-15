import json
import os
from kiteconnect import KiteConnect, KiteTicker
from strategy import SimpleStrategy
from utils import safe_place_order

with open("config.json") as f:
    config = json.load(f)

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

strategy = SimpleStrategy()

def on_ticks(ws, ticks):
    for tick in ticks:
        decision = strategy.on_tick(tick)
        if decision:
            safe_place_order(kite, decision, config)

def on_connect(ws, response):
    tokens = config.get("instruments", [])
    ws.subscribe(tokens)

kws = KiteTicker(api_key, access_token)
kws.on_ticks = on_ticks
kws.on_connect = on_connect

if __name__ == "__main__":
    print("Starting Zerodha NIFTY bot...")
    kws.connect(threaded=True)
