import pandas as pd









if __name__ == "__main__":
    Olympics_2010 = "2010_Winter_Olympics.csv"
    olympics_df = pd.read_csv(Olympics_2010)
    print(olympics_df.head)
    print("----------------------------------------------")
    print(olympics_df.describe(include="all"))
    # temp = olympics_df.iloc[:, 4]
    # print(temp)
    # print(temp.describe())
    # temp2 = olympics_df.iloc[0:8, 4]
    # print(temp)
    # print("----------------------------------------------")
    # print(temp2.describe())
    # print("----------------------------------------------")
