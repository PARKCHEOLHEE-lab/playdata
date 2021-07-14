import pandas as pd

sb = pd.read_excel("Starbucks.xlsx")

sb.columns = ["매장명", "주소", "전화번호", "매장타입", "위도", "경도"]
print(sb.columns)

gu = []
for i in sb["주소"]:
    gu.append(i.split()[1])

sb["시군구명"] = gu

sb.to_excel("Starbucks/df_starbucks_final.xlsx", index=False)