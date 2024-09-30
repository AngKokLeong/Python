import pandas
import numpy

df: pandas.DataFrame = pandas.read_csv("../dataset/graduate-employment-survey-ntu-nus-sit-smu-sutd.csv", header=0, nrows=290)

print("Shape of df in its original form = " + str(df.shape))

df.drop(columns=["school", "employment_rate_overall", "employment_rate_permanent", "basic_monthly_mean", "basic_monthly_median", "gross_mthly_25_percentile","gross_mthly_75_percentile"], inplace=True)

print("Shape of df after dropping unwanted columns = " + str(df.shape))

#df["university"].drop(labels=["Nanyang Technological University", "Singapore Institute of Technology", "Singapore University of Technology and Design"], inplace=True)

university_to_remove: pandas.DataFrame = df.query('university in ["Nanyang Technological University", "Singapore Institute of Technology", "Singapore University of Technology and Design"]')

df.drop(index=university_to_remove.index, inplace=True)

print("Shape of df after dropping unwanted rows (university) = " + str(df.shape))


year_data_to_remove: pandas.DataFrame = df.query("year in [2013, 2014]")

df.drop(index=year_data_to_remove.index, inplace=True)

print("Shape of df after dropping unwanted rows (year) " + str(df.shape))


df["gross_monthly_median"] = df["gross_monthly_median"].apply(lambda x: numpy.NaN if x == 'na' else x)
df["gross_monthly_median"] = df["gross_monthly_median"].apply(lambda x: int(x) if type(x) == str else x)

df["gross_monthly_mean"] = df["gross_monthly_mean"].apply(lambda x: numpy.NaN if x == 'na' else x)
df["gross_monthly_mean"] = df["gross_monthly_mean"].apply(lambda x: int(x) if type(x) == str else x)

df["LessThan4k"] = df["gross_monthly_median"].apply(lambda x: True if x != numpy.NaN and x >= 4000 else False)

gross_monthly_median_less_than_4k: pandas.DataFrame = df.query('LessThan4k == True')

df.drop(index=gross_monthly_median_less_than_4k.index, inplace=True)

#final_dataframe: pandas.DataFrame = df[["LessThan4k", "degree", "gross_monthly_mean", "gross_monthly_median"]]

