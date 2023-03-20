README

BEFORE RUNNING THE PROGRAM

In order to ensure seamless and easy running of the code and by extension the Graphical User Interface (GUI)
please ensure that below files are in the same folder or directory
1. pythonGUI file
2. Module files named 'Stopandsearch_module.py' and  'Covid_module.py'
2. covid source document named 'specimenDate_ageDemographic-unstacked'
3. GUI logos (Image) named TUlogoblack, NHS, clevelandpolice

Install the following libraries using PIP if not installed:
1. matplotlib
2. pandas
3. request
4. JSON
5. PIL
6. tkinter

RUNNING THE PROGRAM

1. open the python file named 'GUI_complete' using jupyter notebook. Run the cell to launch the application landing page
2. select the respective analysis to run by selecting the appropraite button.

The Covid data analysis is dependent on the source CSV document named 'specimenDate_ageDemographic-unstacked' 

The Cleveland Police Stop and Search data analysis is dependent on the data.police.uk API and hence can take a little 
time to get the information during unit testing.

The Graphical User Interface (GUI) runs based on the two module files named:
'Stopandsearch_module.py' and  'Covid_module.py'
Please ensure both modules are in the same directory as the GUI file.
Images shown in the GUI is also dependent on the GUI logos being in the same directory


File exported from the GUI are saved in the same directory


CHARTS

COVID ANALYSIS
- Daily Infection Chart - Scatter plot showing daily infection change in LTLA Hartlepool and Stockton
- Weekly Infection Chart - bar chart showing weekly infection total in LTLA Hartlepool and Stockton
- Monthly Infection Chart - line chart showing monthly infection spread in LTLA Hartlepool and Stockton
- Comparing infection charts - two-line chart comparing monthly infection spread in LTLA Hartlepool and Stockton

STOP AND SEARCH ANALYSIS
Lockdown Months are April, May, and June
- Outcome chart - horizontal bar chart of the outcome spread of stop and search carried out by the Cleveland police in Lockdown months
- Gender chart - pie chart of the gender distribution of stop and search arrests carried out by the Cleveland police in Lockdown months
- Age Count Chart -  bar chart of the age distribution of stop and search arrests carried out by the Cleveland police in Lockdown months
- Objects searched charts - horizontal bar chart of the stop and search carried out by the Cleveland police based on objects searched in same Lockdown months of 2022
- age comparison chart - two-line chart comparing age group distribution of stop and search arrests carried out by the Cleveland police in 2020 and same Lockdown months of 2022
