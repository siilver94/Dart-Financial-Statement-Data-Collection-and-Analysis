import requests
import pandas
from io import BytesIO

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

url_2021 = "https://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20210817001883&dcm_no=8182806&lang=ko"
url_2020 = "https://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20200814002203&dcm_no=7447766&lang=ko"

for period,url in zip(["2021","2020"], [url_2021, url_2020]):
    resp = requests.get(url, headers=headers)
    table = BytesIO(resp.content)   
    pocket = ["연결 재무상태표", "연결 손익계산서", "연결 포괄손익계산서"]

    for sheet in pocket:
        data = pandas.read_excel(table, sheet_name=sheet, skiprows=5)
        data.to_csv(period+sheet+".csv", encoding="euc-kr")
