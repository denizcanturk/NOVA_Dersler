import pandas as pd
from sqlalchemy import create_engine

#Veri tabanı bağlantısını oluşturuyor yine...
engine = create_engine("sqllite:///BTCUSDTstream.db")

#Pandas ı kullanarak veri tabanından veri çekiyor...
importedDf = pd.read_sql("BTCUSDT",engine)

#Burası da alınan bilgilerin grafik üzerinde gösterilmesini sağlıyor... 
importedDf.set_index("Time").plot()