from pcpartpicker import API
from csv import reader
from web import models

api = API()

cpu_data = api.retrieve("cpu")
memory_data = api.retrieve("memory")
power_supply_data = api.retrieve("power-supply")
gpu_data = api.retrieve("video-card")
case_data = api.retrieve("case")
cpu_cooler_data = api.retrieve("cpu-cooler")
monitor_data = api.retrieve("monitor")
internal_hard_drive_data = api.retrieve("internal-hard-drive")
mobo_data = api.retrieve("motherboard")

def parse_powerSupply():
    data = list(power_supply_data['power-supply'])
    newList = []
    for i in range(len(data)):
        temp = str(data[i])
        newList.append(temp)
        #print(temp)
    wattage = []
    for i in range(len(newList)):
        newList[i] = list(newList[i].split(','))
        for x in range(len(newList[i])):
            if (newList[i][x][newList[i][x].find("wattage=")+8].isnumeric()):
                wattage.append(newList[i][x][newList[i][x].find("wattage=")+8:newList[i][x].find("ge=")+11])
            newList[i][x] = newList[i][x][newList[i][x].find('=') + 2:-1]

    newDict = []

    for i in range (len(newList)):
        price = float(newList[i][7][newList[i][7].find(" "):-5])
        if (price == 0):
            continue
        name = newList[i][0] + " " + newList[i][1]
        line = {'name':name, 'watts':wattage[i], 'effiency':newList[i][3], "price":price}
        newDict.append(line)
    return newDict

def add_to_database_powerSupply():
    info = parse_powerSupply()
    for i in info:
        model = models.PowerSupply()
        model.price = i.get('price')
        model.watts = i.get('watts')
        model.effiency = i.get('effiency')
        model.name = i.get('name')
        model.save()

    add_to_database_powerSupply()

def parse_memory_data():
    data = list(memory_data['memory'])
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
            #speed = newList[i][3][newList[i][3].find('=') + 1:]
            memory = brand[brand.find('GB') - 3:brand.find('GB')].strip()
            if price != 0.0 and ("16" == memory or "32" == memory or "8" == memory):
                newDict.append({"name": brand, "price": price, "memory": int(memory)})

    return newDict

def parse_mobo_data():
    data = list(mobo_data['motherboard'])
    newList = []
    print(data)
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
        if "0.0" != newList[i][-1]:
            brand = newList[i][0] + " " + newList[i][1]
            price = float(newList[i][-1][newList[i][-1].find(':') + 2:-4])
            #speed = newList[i][3][newList[i][3].find('=') + 1:]
            size = newList[i][3][newList[i][3].find('=') + 1:]
            if price != 0.0:
                newDict.append({"name": brand, "price": price, "size": size})

    return newDict


def add_to_database_mobo():
    info = parse_mobo_data()
    for i in info:
        model = models.Motherboard()
        model.price = i.get('price')
        model.name = i.get('name')
        model.size = i.get('size')
        model.save()


def parse_internal_hard_drive_data():
    data = list(internal_hard_drive_data['internal-hard-drive'])
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
            ssd = "SSD" in newList[i]
            brand = newList[i][0] + " " + newList[i][1]
            price = float(newList[i][-1][newList[i][-1].find(':') + 2:-4])
            capacity = float(newList[i][2][newList[i][2].find('=') + 1:])
            if price != 0.0:
                newDict.append({"ssd": ssd, "name": brand, "price": price, "capacity": capacity})

    return newDict

def add_to_database_hdd():
    data = parse_internal_hard_drive_data()

    for i in data:
        model = models.Storage()
        model.ssd = i.get('ssd')
        model.price = i.get('price')
        model.name = i.get('name')
        model.capacity = i.get('capacity')
        model.save()


def parse_cpu():
    with open('c:/code/codered2023/backend/info_csv/cpu.csv') as obj:
        csv_reader = reader(obj)

        info = []
        
        for row in csv_reader:
            line = row[1].split(",")
            line2 = []
            price = float(line[8][line[8].find(":")+2:-6])
            clock = line[3][line[3].find("s=")+2:-1]
            print(clock)
            cpuClockSpeed = int(clock)
            for i in line:
                line2.append(i.split("=")[1])

            info.append({"name": line2[0][1:-1]+" " +line2[1][1:-1], "cores": int(line2[2]),
             "price": price, "clockSpeed": cpuClockSpeed })

    return info

def add_to_database_cpu():
    info = parse_cpu()
    for i in info:
        model = models.CPU()
        model.name = i.get("name")
        model.coreCount = i.get("cores")
        model.price = i.get("price")
        model.clockSpeed = i.get("clockSpeed")
        model.save()



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

def add_to_database_gpu():
    data = parse_gpu()
    for i in data:
        model = models.GPU()
        model.price = i.get('price')
        model.name = i.get('name')
        model.coreClock = i.get('clockSpeed')
        model.memory = i.get('memory')
        model.save()
        

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

def add_to_database_cpuCooler():
    info = parse_cpu_cooler()
    for i in info:
        if i.get('price') == 0:
            continue
        model = models.CPUCooler()
        model.name = i.get('name')
        model.price = i.get('price')
        model.save()

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
        color = newList[i][3]
        if price != 0.0:
            newDict.append({"name": brand, "price": price, "form_factor": form_factor, "color":color})

    #print(newDict)
    return newDict

def add_to_database_case():
     info = parse_case_data()
     for i in info:
        print(i)
        model = models.Case()
        model.name = i.get('name')
        model.size = i.get('form_factor')
        model.price = i.get('price')
        model.color = i.get('color')
        model.save()

def parse_memory_data():
    data = list(memory_data['memory'])
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
            #speed = newList[i][3][newList[i][3].find('=') + 1:]
            memory = brand[brand.find('GB') - 3:brand.find('GB')].strip()
            if price != 0.0 and ("16" == memory or "32" == memory or "8" == memory):
                newDict.append({"name": brand, "price": price, "memory": int(memory)})

    return newDict

def add_to_database_memory():
    data = parse_memory_data()
    for i in data:
        model = models.Memory()
        model.price = i.get('price')
        model.gigs = i.get('memory')
        model.name = i.get('name')
        model.save()

