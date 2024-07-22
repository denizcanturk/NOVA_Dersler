import pandas as pd
from sqlalchemy import create_engine
from binance.client import Client
from binance import BinanceSocketManager

#Nesneleri ayağa kaldırıyor
client = Client()
bsm= BinanceSocketManager(client)

#python-binance dokümanstasyonunda yazanın birebir aynısı
socket = bsm.kline_socket("BTCUSDT")
await socket.__aenter__()
msg = await socket.recv()
print(msg)
await socket.__aexit__(None, None, None)

#Alınana mesajdaki tarih bilgisini formatlı halde getiren fonksiyon
def datatransfo(msg):
    df = pd.DataFrame({"Time": msg["E"], "Price":msg["k"]["c"]}, index=[0])
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit="ms")
    return df

#Bu da kanıtı
print(datatransfo(msg))

#Sql Lite veri tabanında yeni bir VT oluşturuyor - Aldığı verileri depolamak için
engine = create_engine("sqllite:///BTCUSDTstream.db")

#Zaman bilgisini referans olarak kullanacak o nedenle değişken oluşturuyor
current_event = pd.Series(pd.to_datetime(0))


#Dokümantasyonunda yazıldığı üzere binance den bilgi alıyor, 
# aldığı bilginin güncelliğini current_event de sakladığı zaman bilgisinin karşılaştırması ile yapıyor
# ve bu bilgiyi veri tabanına ekliyor...
# Bu ayrıca çalışması gereken bir dosya... 
# Yani çalıştırıp bırakmalısın ki: gelen bilgiyi güncel olarak diğer tarafran işleyebilesin...

while True:
    await socket.__aenter__()
    msg = await socket.recv()
    await socket.__aexit__(None, None, None)
    df = datatransfo(msg)
    if df.Time.value > current_event.values:
        current_event = df.Time
        df.to_sql("BTCUSDT", engine, if_exists="append", index= False)


