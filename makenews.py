import os


with open('scrapy.txt', "r") as f:
    
    for line in f:
        ln = line.split(';')

        if(len(ln) != 3):
            continue
        elif ln[0] == "0.0":
            continue
        else:
            print(f"(1, '{ln[0]}', '{ln[1]}', {ln[2]}),")