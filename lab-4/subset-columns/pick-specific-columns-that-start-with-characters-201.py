import pandas

mydf: pandas.DataFrame = pandas.read_excel("../dataset/singstats_maritalstatus.xlsx").set_index("Variables")


year_starts_with_201_column_name_list: list[str] = []

for element in mydf.columns:
    if element.startswith("201") == True:
        year_starts_with_201_column_name_list.append(element)


df_2010_and_after: pandas.DataFrame = mydf[year_starts_with_201_column_name_list]

print(df_2010_and_after)