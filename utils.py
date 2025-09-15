def safe_place_order(kite, decision, config):
    dry_run = config.get("dry_run", True)
    side = decision["side"]
    symbol = decision["symbol"]
    qty = decision["qty"]
    if dry_run:
        print(f"[DRY RUN] {side} {qty} of {symbol}")
        return
    try:
        kite.place_order(
            variety=kite.VARIETY_REGULAR,
            exchange=kite.EXCHANGE_NFO,
            tradingsymbol=symbol,
            transaction_type=kite.TRANSACTION_TYPE_BUY if side == "BUY" else kite.TRANSACTION_TYPE_SELL,
            quantity=qty,
            product=kite.PRODUCT_MIS,
            order_type=kite.ORDER_TYPE_MARKET
        )
        print(f"Order placed: {side} {qty} {symbol}")
    except Exception as e:
        print("Order failed:", e)
