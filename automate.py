import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser(description="Your are suppose to use it \n >>> python automate.py new.csv old.csv")
    parser.add_argument("new", type=str,help="Specify the new csv file")
    parser.add_argument("old", type=str,help="Specify old csv file")
    args = parser.parse_args()
    new_df= pd.read_csv(args.new)
    old_df= pd.read_csv(args.old)
    assert new_df.shape[1] ==old_df.shape[1] ,"The Two Csv files have different number of columns. Please check"
    removed = old_df[old_df["title"].isin(set(old_df["title"]) - set(new_df["title"]))]
    increased = new_df[new_df["title"].isin(set(new_df["title"]) - set(old_df["title"]))]
    removed.to_csv("removed.csv",index=False)
    increased.to_csv("newly_added.csv",index=False)

if __name__ =="__main__":
    main()
