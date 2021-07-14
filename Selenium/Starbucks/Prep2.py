import pandas as pd

sgg = pd.read_excel("Starbucks/df_seoul_final.xlsx")
# print(sgg.head())

sb = pd.read_excel("Starbucks/df_starbucks_final.xlsx")
# print(sb.head())

sb_count = sb.pivot_table(index="시군구명", values="매장명", aggfunc="count")
sb_count.rename(columns={"매장명": "매장수"}, inplace=True)
sgg_count = pd.merge(sgg, sb_count, how="left", on="시군구명")

pop = pd.read_excel("Starbucks/df_pop_final.xlsx")
sgg_pop = pd.merge(sgg_count, pop, how="left", on="시군구명")

comp = pd.read_excel("Starbucks/df_comp_final.xlsx")
final_data = pd.merge(sgg_pop, comp, how="left", on="시군구명")
print(final_data.head())

final_data.to_excel("Starbucks/final_data.xlsx", index=False)