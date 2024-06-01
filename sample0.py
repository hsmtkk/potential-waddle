import ib_insync as ib

broker = ib.IB()
broker.connect("127.0.0.1", 7497, clientId=1)

contract = ib.Forex("EURUSD")
bars = broker.reqHistoricalData(
    contract,
    endDateTime="",
    durationStr="30 D",
    barSizeSetting="1 hour",
    whatToShow="MIDPOINT",
    useRTH=True,
)

df = ib.util.df(bars)
print(df)
