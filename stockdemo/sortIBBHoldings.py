import csv
with open('data/IBB_holdings.csv', 'r') as f:
    readerCSV = csv.DictReader(f)
    print(readerCSV)
    #exit()

    for i, line in enumerate(readerCSV):
        if i >10:
            print(line)


#print(reader.head(3))
