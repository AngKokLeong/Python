
import pandas

national_flower_dict: dict = {
    "Indonesia": "Melati Putih",
    "Malaysia": "Hibiscus rosa-sinensis",
    "Phillippines": "Sampaguita",
    "Singapore": "Vanda Miss Joaquim"
}


national_flower_pandas_series = pandas.Series(national_flower_dict.values(), national_flower_dict.keys())

print(national_flower_pandas_series)
print(type(national_flower_pandas_series))