


skip = True
cid = 3
with open('/home/fizo/Documents/SIMP/StockDatasets/BNL.csv') as file:
    
    for line in file:
        line = line[0:-1]
        if(skip):
            skip = False
            continue
        line = line.split(',')
        # line[0] = line[0]
        # line[1] = float(line[1])
        # line[2] = float(line[2])
        # line[3] = float(line[3])
        # line[4] = float(line[4])
        # line[5] = int(line[5])
        # line[6] = float(line[6])

        print(f"({cid}, '{line[0]}', {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}, {line[6]}),")
