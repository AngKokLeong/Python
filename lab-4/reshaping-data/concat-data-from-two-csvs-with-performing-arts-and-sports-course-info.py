import pandas


df_arts: pandas.DataFrame = pandas.read_csv("../dataset/pa-performing-arts-courses.csv", header=0)
df_sports: pandas.DataFrame = pandas.read_csv("../dataset/pa-sports-courses.csv", header=0)

print("***** With Performing Art Courses Data Only ******")
print("df_arts.shape: " + str(df_arts.shape))
print(df_arts[:2])
print(df_arts[-2:])



print("")

print("***** With Sports Courses Data only ******")
print("df_sports.shape: " + str(df_sports.shape))
print(df_sports[:2])
print(df_sports[-2:])


print("")

df_all: pandas.DataFrame = pandas.concat([df_arts, df_sports])

print("***** After concatenating the two DataFrame objects ******")

print("df_all.shape: " + str(df_all.shape))
print(df_all[:3])
print(df_all[-3:])
