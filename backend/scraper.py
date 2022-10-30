"""

To get access to API run - pip install pcpartpicker

"""

from re import L
from pcpartpicker import API
import pandas as pd
from csv import reader
api = API()

cpu_data = api.retrieve("cpu")

"""
memory_data = api.retrieve("memory")
power_supply_data = api.retrieve("power-supply")
video_card_data = api.retrieve("video-card")
case_data = api.retrieve("case")
cpu_cooler_data = api.retrieve("cpu-cooler")
monitor_data = api.retrieve("monitor")
internal_hard_drive_data = api.retrieve("internal-hard-drive")
external_hard_drive_data = api.retrieve("external-hard-drive")
all_data = api.retrieve_all()
"""

    
'''
df_memory = pd.DataFrame(memory_data)
df_power_supply = pd.DataFrame(power_supply_data)
df_video_card = pd.DataFrame(video_card_data)
df_case = pd.DataFrame(case_data)
df_cpu_cooler = pd.DataFrame(cpu_cooler_data)
df_monitor = pd.DataFrame(monitor_data)
df_internal_hard_drive = pd.DataFrame(internal_hard_drive_data)
df_external_hard_drive = pd.DataFrame(external_hard_drive_data)
df_cpu.to_csv('c:/code/codered2023/backend/info_csv/cpu.csv')
df_memory.to_csv('memory.csv')
df_power_supply.to_csv('power-supply.csv')
df_video_card.to_csv('video-card.csv')
df_case.to_csv('case.csv')
df_cpu_cooler.to_csv('cpu-cooler.csv')
df_monitor.to_csv('monitor.csv')
df_internal_hard_drive.to_csv('internal-hard-drive.csv')
df_external_hard_drive.to_csv('external-hard-drive.csv')
'''
'''
df_cpu = pd.DataFrame(cpu_data)
df_cpu.to_csv('c:/code/codered2023/backend/info_csv/cpu.csv')
'''
with open('c:/code/codered2023/backend/info_csv/cpu.csv') as obj:
    csv_reader = reader(obj)
    
    for row in csv_reader:
        print(row)

'''
print('')
print(df_memory)
print('')
print(df_power_supply)
print('')
print(df_video_card)
print('')
print(df_case)
print('')
print(df_cpu_cooler)
print('')
print(df_monitor)
print('')
'''

