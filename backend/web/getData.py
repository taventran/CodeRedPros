import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests
import random
import models
import views

print(models.UserData.lastUser())

def getWeights(use, budget):
    weights = ()

    cpu = 0
    cpu_cooler = 0
    gpu = 0
    ram = 0
    storage = 0
    mobo = 0
    case = 0
    psu = 0

    if use == "1":
        cpu = 0.2
        cpu_cooler = 0.1
        gpu = 0.2
        ram = 0.1
        storage = 0.1
        mobo = 0.1
        case = 0.1
        psu = 0.1
    elif use == "2":
        cpu = 0.2
        cpu_cooler = 0.05
        gpu = 0.2
        ram = 0.1
        storage = 0.2
        mobo = 0.1
        case = 0.1
        psu = 0.05
    elif use == "3":
        cpu = 0.2
        cpu_cooler = 0.05
        gpu = 0.2
        ram = 0.1
        storage = 0.2
        mobo = 0.1
        case = 0.1
        psu = 0.05
    elif use == "4":
        cpu = 0.25
        cpu_cooler = 0.05
        gpu = 0.25
        ram = 0.2
        storage = 0.1
        mobo = 0.05
        case = 0.05
        psu = 0.05
    elif use == "5":
        cpu = 0.2
        cpu_cooler = 0.1
        gpu = 0.25
        ram = 0.2
        storage = 0.1
        mobo = 0.05
        case = 0.05
        psu = 0.05

    weights = (cpu, cpu_cooler, gpu, ram, storage, mobo, case, psu) * budget
    return weights

def getCPU(budgetMax, budgetMin):
    api_url = "http://127.0.0.1:8000/api/CPU/"
    response = requests.get(api_url)
    df = pd.DataFrame(response.json())
    df = df.loc[(df['price'] <= budgetMax) & (df['price'] >= budgetMin)]
    df = df.sort_values(["coreCount", "clockSpeed"], ascending = False)
    return df[:10]

def getCPUCooler(budgetMax, budgetMin):
    api_url = "http://127.0.0.1:8000/api/CPUCooler/"
    response = requests.get(api_url)
    df = pd.DataFrame(response.json())
    df = df.loc[(df['price'] <= budgetMax) & (df['price'] >= budgetMin)]
    return df[:10]

def getGPU(budgetMax, budgetMin):
    api_url = "http://127.0.0.1:8000/api/GPU/"
    response = requests.get(api_url)
    df = pd.DataFrame(response.json())
    df = df.loc[(df['price'] <= budgetMax) & (df['price'] >= budgetMin)]
    df = df.sort_values(["memory", "coreClock"], ascending = False)
    return df[:10]

def getRAM(budgetMax, budgetMin):
    api_url = "http://127.0.0.1:8000/api/memory/"
    response = requests.get(api_url)
    df = pd.DataFrame(response.json())
    df = df.loc[(df['price'] <= budgetMax) & (df['price'] >= budgetMin)]
    df = df.sort_values(["memory", "gigs"], ascending = False)
    return df[:10]

def getStorage(budgetMax, budgetMin):
    api_url = "http://127.0.0.1:8000/api/storage/"
    response = requests.get(api_url)
    df = pd.DataFrame(response.json())
    df = df.loc[(df['price'] <= budgetMax) & (df['price'] >= budgetMin)]
    df = df.sort_values(["capacity"], ascending = False)
    return df[:10]

def getMobo(budgetMax, budgetMin, size):
    api_url = "http://127.0.0.1:8000/api/motherboard/"
    response = requests.get(api_url)
    df = pd.DataFrame(response.json())
    df = df.loc[(df['price'] <= budgetMax) & (df['price'] >= budgetMin)]
    df = df.loc[(df['size'] == size)]
    return df[:10]

def getCase(budgetMax, budgetMin, size, aesthetic):
    api_url = "http://127.0.0.1:8000/api/case/"
    response = requests.get(api_url)
    df = pd.DataFrame(response.json())
    df = df.loc[(df['price'] <= budgetMax) & (df['price'] >= budgetMin)]
    df = df.loc[(df['size'] == size)]
    return df[:10]

def getPSU(budgetMax, budgetMin):
    api_url = "http://127.0.0.1:8000/api/powersupply/"
    response = requests.get(api_url)
    df = pd.DataFrame(response.json())
    df = df.loc[(df['price'] <= budgetMax) & (df['price'] >= budgetMin)]
    return df[:10]


def CPUData():
    sns.set_theme(style="whitegrid", palette="muted")
    data_cpu = getCPU(400, 100)

    sns.swarmplot(data=data_cpu, x="coreCount", y="price")
    line = ""
    for i in range(10):
        line += str(random.randint(0, 9))

    plt.savefig(f'images/{line}.png')
    
    return f'images/{line}.png'

def CPUCoolerData():
    sns.set_theme(style="darkgrid", palette="muted")
    data_cpu_cooler = getCPUCooler(400, 100)

    sns.swarmplot(data=data_cpu_cooler, x="name", y="price")
    plt.xticks(
        rotation = 45,
        horizontalalignment = "right",
        fontweight = 'light',
        fontsize = 5
    )
    line = ""
    for i in range(10):
        line += str(random.randint(0, 9))

    plt.savefig(f'images/{line}.png')
    
    return f'images/{line}.png'

def GPUData():
    sns.set_theme(style="whitegrid", palette="muted")
    data_gpu = getGPU(200, 100)
    #print(getGPU(400, 100))
    sns.swarmplot(data=data_gpu, x="price", y="coreClock")
    plt.xticks(
        rotation = 45,
        horizontalalignment = "right",
        fontweight = 'light',
        fontsize = 5
    )

    line = ""
    for i in range(10):
        line += str(random.randint(0, 9))

    plt.savefig(f'images/{line}.png')
    
    return f'images/{line}.png'