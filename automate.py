import json
import csv
import pandas as pd

#newtitle,oldtitle = set(),set()
#newfile=json.load(open("items.json"))
#oldfile = json.load(open("old.json"))
#
#for i in newfile:
#    newtitle.add(i["title"])
#for i in oldfile:
#    oldtitle.add(i["title"])
#
#with open("items.csv","w") as newcsvfile, open("old.csv","w") as oldcsvfile:
#    l=set()
#    for i in newfile:
#        l=l.union(i.keys())
#    fieldnames=list(l)
#    writer = csv.DictWriter(newcsvfile, fieldnames=fieldnames)
#    writer.writeheader()
#    for i in newfile:
#        writer.writerow(i)
#    writer = csv.DictWriter(oldcsvfile, fieldnames=fieldnames)
#    writer.writeheader()
#    for i in oldfile:
#        writer.writerow(i)
new_df= pd.read_csv("items.csv")
old_df= pd.read_csv("old.csv")
removed = old_df[old_df["title"].isin(set(old_df["title"]) - set(new_df["title"]))]
increased = new_df[new_df["title"].isin(set(new_df["title"]) - set(old_df["title"]))]
removed.to_csv("removed.csv",index=False)
increased.to_csv("newly_added.csv",index=False)
