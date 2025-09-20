import csv
with open (r"C:\Users\HP\OneDrive\Pictures\Desktop\python_college\csv\basic.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)