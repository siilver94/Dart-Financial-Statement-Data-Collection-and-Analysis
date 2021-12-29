import requests
import pandas
from io import BytesIO

url= "https://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20210817001883&dcm_no=8182806&lang=ko"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

resp = requests.get(url,headers = headers)

# url로 열기
table = BytesIO(resp.content)

pocket = ["연결 재무상태표", "연결 손익계산서", "연결 포괄손익계산서"]

for sheet in pocket:
    data = pandas.read_excel(table, sheet_name=sheet,skiprows=5)
    data.to_csv(sheet+".csv", encoding="euc-kr")
