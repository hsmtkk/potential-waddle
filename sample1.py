import ib_insync as ib

broker = ib.IB()
broker.connect("127.0.0.1", 7497, clientId=1)

vix = ib.Index("VIX", "CBOE")
print(broker.qualifyContracts(vix))
print(broker.reqSecDefOptParams(vix.symbol, "", vix.secType, vix.conId))
