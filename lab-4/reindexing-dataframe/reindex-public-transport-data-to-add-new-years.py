import pandas

mydf: pandas.DataFrame = pandas.read_csv("../dataset/publictransportjourney.csv", header=0)
mydf.set_index("year", inplace=True)

print("*** Original dataset ***")
print("")
print(mydf)


mynewindex: list[int] = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

reindex_mydf: pandas.DataFrame = mydf.reindex(index=mynewindex)
print("")
print("*** Dataset after reindexing ***")
print("")

print(reindex_mydf)
