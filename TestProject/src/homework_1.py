import pandas as pd

print ("welcome to your first HW: FILTER BY. So yallaa...")

df = pd.DataFrame({"ID":[703,783,788,780,790],"NAME":["John","James","Marry","Gil","Roy"], "LEVEL":[5,5,4,5,4],"GRADE":[87,88,90,65,100]})

print (df)
print ("--------------")
print ("Your task: given the dataframe above print on screen all those that their grade is grater than 80")