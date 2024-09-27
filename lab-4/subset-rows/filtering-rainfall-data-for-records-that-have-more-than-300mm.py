import pandas
import matplotlib.pyplot

df_rainfall: pandas.DataFrame = pandas.read_csv("../dataset/rainfall-monthly-total.csv").set_index("month")

df_rainfall_with_top_twelve_records_of_more_than_300mm_rainfall = df_rainfall[df_rainfall["total_rainfall"] > 300].sort_values("total_rainfall").iloc[-12:]


matplotlib.pyplot.rcParams["figure.figsize"] = (14, 7)
matplotlib.pyplot.plot(df_rainfall_with_top_twelve_records_of_more_than_300mm_rainfall, label="total_rainfall")
matplotlib.pyplot.legend(loc='upper right')
matplotlib.pyplot.xlabel("month")

matplotlib.pyplot.savefig("rainfall that have more than 300mm.jpg")