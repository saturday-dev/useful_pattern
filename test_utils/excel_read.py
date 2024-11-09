import xlwings as xw
import pandas as pd
import os

# 주의점. xlwings 는 Windows 에서만 사용가능하다.
filePath = '/mnt/d/cloud/nextcloud/hobbies/01.금융투자_주식_코인/카드사용금액/2023년/4월/이용대금명세서(신용카드)_신한카드.xls'
sheetName = '이용대금명세서(신용카드)_신한카드'

book = xw.Book(filePath)
sheet = book.sheets[sheetName]

df = sheet.used_range.options(pd.DataFrame, index = False).value

print(df.head())

print()