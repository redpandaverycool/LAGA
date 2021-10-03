#Import modules
import pandas as pd

#import excel-file
excel_file = pd.read_excel('C:/Programming/LaborProtokoll/2021P527432v1.xlsx')
print(excel_file)

# Create dictionary with concentrations
Analysenergebnisse_index = excel_file[excel_file.iloc[:,0] == "Analysenergebnisse"].index.values
startrow_names = int(Analysenergebnisse_index[0] + 1)

Probenbezeichnung_index = excel_file[excel_file.iloc[:,0] == "Probenbezeichnung"].index.values
startcolumn_values = excel_file.loc[[int(Probenbezeichnung_index[0])]]
print(startcolumn_values)
a = startcolumn_values.values.tolist()
flat_list_a = [item for sublist in a for item in sublist]
print(flat_list_a)
b = str(input("Probenbezeichnung eingeben (exakt):"))
print(b)
column_values = flat_list_a.index(b) # final column index with the desired values
print(column_values)

Liste_Stoffnamen = excel_file.iloc[startrow_names:,0].values.tolist() # Stoffnamen
Liste_Gehalte = excel_file.iloc[startrow_names:,column_values].values.tolist() # Gehalte (Werte)
Zip = zip(Liste_Stoffnamen, Liste_Gehalte)
Dictionary = dict(Zip)
print(Dictionary)

