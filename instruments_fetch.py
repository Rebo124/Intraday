import json, os
from kiteconnect import KiteConnect

api_key = os.getenv("API_KEY")
access_token = os.getenv("ACCESS_TOKEN")
kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

instruments = kite.instruments("NFO")
nifty_opts = [i for i in instruments if i["name"] == "NIFTY"]
with open("nifty_instruments.json", "w") as f:
    json.dump(nifty_opts, f, indent=2)
print("Saved NIFTY options to nifty_instruments.json")
