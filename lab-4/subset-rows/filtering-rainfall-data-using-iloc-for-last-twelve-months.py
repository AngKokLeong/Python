import pandas
import matplotlib.pyplot

df_rainfall:pandas.DataFrame = pandas.read_csv("../dataset/rainfall-monthly-total.csv").set_index("month")

df_rainfall_for_the_past_twelve_months: pandas.DataFrame = df_rainfall.iloc[-12:]

matplotlib.pyplot.rcParams["figure.figsize"] = (14, 7)
matplotlib.pyplot.plot(df_rainfall_for_the_past_twelve_months, label="total_rainfall")
matplotlib.pyplot.legend(loc='upper right')
matplotlib.pyplot.xlabel("month")

matplotlib.pyplot.savefig("rainfall in the past 12 months.jpg")