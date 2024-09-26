import matplotlib.pyplot
import pandas
import matplotlib

df_rainfall: pandas.DataFrame = pandas.read_csv("../dataset/rainfall-monthly-total.csv").set_index("month")

df_rainfall_in_1982: pandas.DataFrame = df_rainfall.loc[df_rainfall.index.str.startswith("1982")]

matplotlib.pyplot.rcParams["figure.figsize"] = (14, 7)
matplotlib.pyplot.plot(df_rainfall_in_1982, label="total_rainfall")
matplotlib.pyplot.legend(loc='upper right')
matplotlib.pyplot.xlabel("month")

matplotlib.pyplot.savefig("rainfall in 1982.jpg")


