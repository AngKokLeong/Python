import pandas
import numpy

pandas_dataframe_array = []


number_of_columns: int = 5
number_of_rows: int = 5

matrix: list[list] = []

for row_index in range(number_of_rows):
    # define the row and then column
    new_row: list = []
    for column_index in range(number_of_columns):
        random_number: int = numpy.random.default_rng().integers(100, 200, endpoint=True)
        new_row.append(random_number)
    
    matrix.append(new_row)


pandas_dataframe = pandas.DataFrame(matrix)

print(pandas_dataframe)