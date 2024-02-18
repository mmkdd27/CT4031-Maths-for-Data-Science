import pandas as pd

part1 = pd.read_csv("clean1.csv")
part2 = pd.read_csv("clean2.csv")

combined_csv = pd.concat([part1, part2])

combined_csv.drop(["Unnamed: 0"], inplace=True, axis=1)

combined_csv.to_csv("combined.csv")
