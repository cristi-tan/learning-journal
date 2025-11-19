#Append to a file
with open("note.txt", "a") as f:
    f.write("\nThis is a new line.")

#Read the file
with open("note.txt", "r") as f:
    content = f.read()
    print(content)

#CSV file
import csv

with open("clients.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["John", 30])
    writer.writerow(["Maria", 25])
    writer.writerow(["Alex", 33])

#Read the file
with open("clients.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#Products CSV file
import csv

with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product name", "Price"])
    writer.writerow(["Laptop", 3000])
    writer.writerow(["Phone", 1500])
    writer.writerow(["Mouse", 50])

#Read the csv file
with open("products.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"{row[0]}  -> {row[1]} USD")
