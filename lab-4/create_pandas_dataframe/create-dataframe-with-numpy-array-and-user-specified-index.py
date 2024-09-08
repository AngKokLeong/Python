import numpy
import pandas


number_of_columns: int = 5
number_of_rows:int = 5

column_name_list: list[str] = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5"]

index_list: list[str] = ["Game 1", "Game 2", "Game 3", "Game 4", "Game 5"]

dataframe: list[list[int]] = []



for row_index in range(number_of_rows):
    
    column_list: list[int] = []

    for column_index in range(number_of_columns):
    
        random_number: int = numpy.random.default_rng().integers(100, 200, endpoint=True)
        column_list.append(random_number)

    dataframe.append(column_list)



generated_dataframe: pandas.DataFrame = pandas.DataFrame(dataframe, index=index_list, columns=column_name_list)

print(generated_dataframe)