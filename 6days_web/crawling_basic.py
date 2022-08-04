#다음 웹 크롤링
import requests
import pandas as pd
def daumex(pagesize=10,page=1):
    url= f'https://finance.daum.net/api/exchanges/FRX.KRWUSD/days?symbolCode=FRX.KRWUSD&terms=days&page={page}&perPage={pagesize}'
    response = requests(url)
    data = response.json()
    return pd.DataFrame(data)
usd = daumex(10,1)
print(usd.head())

