import numpy
import pandas


five_by_five_numpy_array = numpy.random.randint(100, 201, (5, 5))

dataframe_index: pandas.Index = ["Game 1", "Game 2", "Game 3", "Game 4", "Game 5"]
dataframe_column_header: list = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5"]

mydf: pandas.DataFrame = pandas.DataFrame(five_by_five_numpy_array, index=dataframe_index, columns=dataframe_column_header)


mydf.to_csv("../dataset/mydf.csv")
mydf.to_excel("../dataset/mydf.xlsx")