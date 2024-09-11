import pandas
import numpy


nus_median_gross_pay_2013to2015 = {
    'BA': [3000, 3000, 3000],
    'BA (Honours)': [3200, 3520, 3800],
    'BA (Accountancy)': [2700, 2838, 2850],
    'BA (Accountancy)(Honours)': [2800, 2912, 3000],
    'BComp (Comm & Media)': [3050, 3088, 3500],
    'BComp (Comp Science)': [3425, 3500, 3700],
    'BComp (Info Sys)': [3005, 3500, 3550]
}

year_list: list[int] = [2013, 2014, 2015]

nus_median_gross_pay_dataframe: pandas.DataFrame = pandas.DataFrame(nus_median_gross_pay_2013to2015, index=year_list)

print(nus_median_gross_pay_dataframe[["BComp (Comm & Media)", "BComp (Comp Science)", "BComp (Info Sys)"]])


