import pandas as pd
import json
import requests


def lockdown_months():
    forces_request = requests.get('https://data.police.uk/api/forces')
    forces = forces_request.json()
    df_forces = pd.json_normalize(forces)
    df_forces
    # retrieve cleveland data for 3 lockdown months(april, may, june) 
    cleveland_forces_april20 = requests.get('https://data.police.uk/api/stops-force?force=cleveland&date=2020-04')
    cleveland_april20 = cleveland_forces_april20.json()
    df_cleveland_april20 = pd.json_normalize(cleveland_april20)
    df_cleveland_april20
    cleveland_forces_may20 = requests.get('https://data.police.uk/api/stops-force?force=cleveland&date=2020-05')
    cleveland_may20 = cleveland_forces_may20.json()
    df_cleveland_may20 = pd.json_normalize(cleveland_may20)
    df_cleveland_may20
    cleveland_forces_june20 = requests.get('https://data.police.uk/api/stops-force?force=cleveland&date=2020-06')
    cleveland_june20 = cleveland_forces_june20.json()
    df_cleveland_june20 = pd.json_normalize(cleveland_june20)
    df_cleveland_june20
    # concat the three lockdown months
    lockdown2020_df = pd.concat([df_cleveland_april20, df_cleveland_may20, df_cleveland_june20], ignore_index=True)
    lockdown2020_df
    # remove unwanted columns
    lockdown2020_df_mod = lockdown2020_df.drop(lockdown2020_df.columns[[3, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 
                                                                        18, 19, 20]], axis = 1, inplace = False)
    return lockdown2020_df_mod
    # wanted columns - 1,2,4,12,14


def same_months():
    forces_request = requests.get('https://data.police.uk/api/forces')
    forces = forces_request.json()
    df_forces = pd.json_normalize(forces)
    df_forces
    # retrieve cleveland data for 3 lockdown months(april, may, june) of 2022
    cleveland_forces_april22 = requests.get('https://data.police.uk/api/stops-force?force=cleveland&date=2022-04')
    cleveland_april22 = cleveland_forces_april22.json()
    df_cleveland_april22 = pd.json_normalize(cleveland_april22)
    df_cleveland_april22
    cleveland_forces_may22 = requests.get('https://data.police.uk/api/stops-force?force=cleveland&date=2022-05')
    cleveland_may22 = cleveland_forces_may22.json()
    df_cleveland_may22 = pd.json_normalize(cleveland_may22)
    df_cleveland_may22
    cleveland_forces_june22 = requests.get('https://data.police.uk/api/stops-force?force=cleveland&date=2022-06')
    cleveland_june22 = cleveland_forces_june22.json()
    df_cleveland_june22 = pd.json_normalize(cleveland_june22)
    df_cleveland_june22
    # concat the three lockdown months
    lockdown2022_df = pd.concat([df_cleveland_april22, df_cleveland_may22, df_cleveland_june22], ignore_index=True)
    lockdown2022_df
    #remove unwanted columns
    lockdown2022_df_mod = lockdown2022_df.drop(lockdown2022_df.columns[[3, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 
                                                                        18, 19, 20]], axis = 1, inplace = False)
    return lockdown2022_df_mod
    # wanted columns - 1,2,4,11,13
    
