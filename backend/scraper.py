"""

To get access to API run - pip install pcpartpicker

"""

from re import L
from pcpartpicker import API
import pandas as pd
from csv import reader
api = API()

cpu_data = api.retrieve("cpu")
memory_data = api.retrieve("memory")
power_supply_data = api.retrieve("power-supply")
gpu_data = api.retrieve("video-card")
case_data = api.retrieve("case")
cpu_cooler_data = api.retrieve("cpu-cooler")
monitor_data = api.retrieve("monitor")
internal_hard_drive_data = api.retrieve("internal-hard-drive")



def parse_cpu():
    with open('c:/code/codered2023/backend/info_csv/cpu.csv') as obj:
        csv_reader = reader(obj)

        info = []

        for row in csv_reader:
            line = row[1].split(",")
            line2 = []
            #print(line)
            for i in line:
                line2.append(i.split("=")[1])

            info.append({"name": line2[0][1:-1]+" " +line2[1][1:-1], "cores": int(line2[2]),
             "price": (line2[4][line2[4].find(":")+1:-4]) })

            #print(line2)
        #print(info)

def parse_gpu():
    data = list(gpu_data['video-card'])
    newList = []
    for i in range(len(data)):
        temp = str(data[i])
        newList.append(temp)

    for i in range(len(newList)):
        newList[i] = newList[i][newList[i].find('(') + 1:newList[i].rindex(')')]
        newList[i] = list(newList[i].split(','))
        for x in range(len(newList[i])):
            newList[i][x] = newList[i][x][newList[i][x].find('=') + 2:-1]
        #print(newList[i])

    newDict = []
    for i in range(len(newList)):
        if 'on' not in newList[i] and float(newList[i][8][newList[i][8].find(':') + 2:-4]) != 0.0:
            brand = newList[i][0] + " " + newList[i][1] + " " + newList[i][2]
            price = float(newList[i][8][newList[i][8].find(':') + 2:-4])
            clockSpeed = float(newList[i][4][newList[i][4].find('=') + 1:])
            memory = float(newList[i][3][newList[i][3].find('=') + 1:])
            newDict.append({"name": brand, "price": price, "clockSpeed": clockSpeed, "memory": memory})
    return newDict

def parse_cpu_cooler():
    data = list(cpu_cooler_data['cpu-cooler'])
    newList = []
    for i in range(len(data)):
        temp = str(data[i])
        newList.append(temp)
        #print(temp)

    for i in range(len(newList)):
        newList[i] = newList[i][newList[i].find('(') + 1:newList[i].rindex(')')]
        newList[i] = list(newList[i].split(','))
        for x in range(len(newList[i])):
            newList[i][x] = newList[i][x][newList[i][x].find('=') + 2:-1]
        #print(newList[i])

    newDict = []
    for i in range(len(newList)):
        if 'on' not in newList[i] and '0.0' != newList[i][-1]:
            brand = newList[i][0] + " " + newList[i][1]
            price = float(newList[i][-1][newList[i][-1].find(':') + 2:-4])
            newDict.append({"name": brand, "price": price})

    return newDict

def parse_case_data():
    data = list(case_data['case'])
    newList = []
    for i in range(len(data)):
        temp = str(data[i])
        newList.append(temp)
        #print(temp)

    for i in range(len(newList)):
        newList[i] = newList[i][newList[i].find('(') + 1:newList[i].rindex(')')]
        newList[i] = list(newList[i].split(','))
        for x in range(len(newList[i])):
            newList[i][x] = newList[i][x][newList[i][x].find('=') + 2:-1]
        #print(newList[i])

    newDict = []
    for i in range(len(newList)):
            brand = newList[i][0] + " " + newList[i][1]
            price = float(newList[i][-1][newList[i][-1].find(':') + 2:-4])
            form_factor = newList[i][2]
            if price != 0.0:
                newDict.append({"name": brand, "price": price, "form_factor": form_factor})

    return newDict

def parse_memory_data():
    data = list(memory_data['memory'])
    newList = []
    for i in range(len(data)):
        temp = str(data[i])
        newList.append(temp)
        print(temp)

    for i in range(len(newList)):
        newList[i] = newList[i][newList[i].find('(') + 1:newList[i].rindex(')')]
        newList[i] = list(newList[i].split(','))
        for x in range(len(newList[i])):
            newList[i][x] = newList[i][x][newList[i][x].find('=') + 2:-1]
        print(newList[i])

    newDict = []
    for i in range(len(newList)):
        if 'on' not in newList[i] and '0.0' != newList[i][-1]:
            brand = newList[i][0] + " " + newList[i][1]
            price = float(newList[i][-1][newList[i][-1].find(':') + 2:-4])
            speed = newList[i][3][newList[i][3].find('=') + 1:]
            memory = newList[i][2]
            if memory == "DDR4" and price != 0.0:
                newDict.append({"name": brand, "price": price, "speed": speed, "memory": memory})

    return newDict

print(parse_memory_data())