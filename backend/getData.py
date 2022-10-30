import pandas as pd
import numpy as np
import requests




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





print(getCPU(400, 100))