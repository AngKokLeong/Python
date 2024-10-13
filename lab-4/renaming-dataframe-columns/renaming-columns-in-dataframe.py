import pandas

mydf: pandas.DataFrame = pandas.read_csv("../dataset/publictransport.csv", header=0)

print("*** Original Dataset ***")
print("")
print(mydf[:5])


print("")

print("*** Dataset after naming column names ***")
print("")

mydf.rename(columns={"year": "Year", "type_of_public_transport": "Transport Type", "average_ridership" : "Average Ridership"}, inplace=True)

print(mydf)

