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

        if result_data["RESULT"]["CODE"] == "INFO-000":
            return result_data["row"]

    except:
        pass

s_api = open_api(url, "SdeTlSccoSigW")
columns = ["SIG_CD", "SIG_KOR_NM", "LAT", "LNG"]

df_seoul = pd.DataFrame(s_api, columns=columns)
print(df_seoul.head())