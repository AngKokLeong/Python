import pandas

df_m: pandas.DataFrame = pandas.read_csv("../dataset/merge_students-male.csv", header=0)
df_f: pandas.DataFrame = pandas.read_csv("../dataset/merge_students-female.csv", header=0)
df_test: pandas.DataFrame = pandas.read_csv("../dataset/merge_testscores.csv", header=0)

total_student: int = df_m.shape[0] + df_f.shape[0]
print("Total students: " + str(total_student))

print("")

print("Test scores in descending order")

print("")


df_student: pandas.DataFrame = pandas.concat([df_m, df_f])
df_student.set_index("studentid", inplace=True)

df_merged: pandas.DataFrame = pandas.merge(df_student, df_test, on=["studentid"], how='inner')
df_merged.set_index("studentid", inplace=True)

df_merged.sort_values("test score", ascending=False, inplace=True)

print(df_merged[:20])