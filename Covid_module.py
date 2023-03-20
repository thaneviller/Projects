import pandas as pd

# Covid Analysis
def covid():
    # read in data
    covid_df = pd.read_csv("specimenDate_ageDemographic-unstacked.csv")
    covid_df
    
    # remove unwanted columns from read dataframe
    covid_df_mod = covid_df.drop(covid_df.columns[[4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20,
                                                   21, 22, 23,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                                                   37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                                                   51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
                                                   65, 66, 67,68]], axis = 1, inplace = False)

    # create a column for total daily infection
    total_infected = (covid_df_mod["newCasesBySpecimenDate-0_59"] + covid_df_mod["newCasesBySpecimenDate-60+"] 
                      + covid_df_mod["newCasesBySpecimenDate-90+"] 
                      + covid_df_mod["newCasesBySpecimenDate-unassigned"])
    covid_df_mod["TotalDailyInfected"] = total_infected

    # group data by area name and get difference in total daily infected.
    covid_df_area = covid_df_mod.copy()
    covid_df_area["DailyNewCases"] = covid_df_mod.groupby("areaName").TotalDailyInfected.diff()
    covid_df_area
    
    # group data by area type
    grouped_df = covid_df_area.copy()
    grouped_df_area = grouped_df.groupby("areaType")

    # create dataframe for only lowtierlocalauthority(ltla)
    grouped_df_ltla = grouped_df.query('areaType in ["ltla"]')
    return grouped_df_ltla
