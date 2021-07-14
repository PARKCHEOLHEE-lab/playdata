import requests
import pandas as pd

# https://data.seoul.go.kr/

MY_KEY = "6f62554f5a636a6638365056535078"
url = f"http://openapi.seoul.go.kr:8088/{MY_KEY}/json/SdeTlSccoSigW/1/25"

def open_api(url, service):
    data_list = None
    try:
        result_dict = requests.get(url).json()
        result_data = result_dict[service]
        code = result_data["RESULT"]["CODE"]

        if code == "INFO-000":
            data_list = result_data["row"]

    except:
        pass

    return data_list

s_api = open_api(url, "SdeTlSccoSigW")

columns = ["SIG_CD", "SIG_KOR_NM", "LAT", "LNG"]

df_seoul_final = pd.DataFrame(data=s_api, columns=columns)
df_seoul_final.columns = ["시군구코드", "시군구명",  "위도", "경도"]


df_seoul_final.to_excel("Starbucks/df_seoul_final.xlsx", index=False)
print(df_seoul_final.head())

url2 = f"http://openapi.seoul.go.kr:8088/{MY_KEY}/json/octastatapi419/1/5/2018.1-4/합계"
s_pop = open_api(url2, "octastatapi419")
df_pop = pd.DataFrame(s_pop)

# 통계데이터 open api 서비스 종료....
# *.tsv file download


# -------------------------------------------------------------------------------- seoul populate data collceting ▼

df_pop = pd.read_csv("Starbucks/df_pop.tsv", delimiter="\t", header=2)
df_pop = df_pop[df_pop["자치구"] != "합계"]

df_pop_final = df_pop[["자치구", "계"]]
df_pop_final["계"] = df_pop_final["계"].str.replace(",", "").astype(int)
df_pop_final.columns = ["시군구명", "주민등록인구"]

df_pop_final.to_excel("Starbucks/df_pop_final.xlsx", index=False)


# -------------------------------------------------------------------------------- seoul company data collecting ▼

df_comp = pd.read_csv("Starbucks/df_comp.tsv", delimiter="\t", header=2)
df_comp = df_comp[df_comp["동"] == "소계"]

df_comp_final = df_comp[["자치구", "계", "사업체수"]].reset_index(drop=True)
df_comp_final.columns = ["시군구명", "종사자수", "사업체수"]

df_comp_final["종사자수"] = df_comp_final["종사자수"].str.replace(",", "").astype(int)
df_comp_final["사업체수"] = df_comp_final["사업체수"].str.replace(",", "").astype(int)

df_comp_final.to_excel("Starbucks/df_comp_final.xlsx", index=False)