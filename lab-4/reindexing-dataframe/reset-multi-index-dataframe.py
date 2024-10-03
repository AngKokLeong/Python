import pandas


mydf: pandas.DataFrame = pandas.read_csv("../dataset/publictransport.csv", header=0)

mydf.set_index(["year", "type_of_public_transport"], inplace=True)

print("*** Dataset with index year and type of public transport ***")
print("")

print(mydf[:10])

print("")

print("*** Dataset with its index reset ***")
print("")

mydf.reset_index(inplace=True)

print(mydf[:10])

