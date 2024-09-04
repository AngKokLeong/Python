
import pandas

national_flower_dict: dict = {
    "Indonesia": "Melati Putih",
    "Malaysia": "Hibiscus rosa-sinensis",
    "Phillippines": "Sampaguita",
    "Singapore": "Vanda Miss Joaquim"
}

print(pandas.Series(national_flower_dict.values(), national_flower_dict.keys()))