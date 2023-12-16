import xml.etree.ElementTree as ET
import pandas as pd
import sqlite3

tree = ET.parse('file.xml')
root = tree.getroot()

first_names = []
last_names = []
contact_nos = []  
emails = []       
cities = []
states = []
zips = []

for employee in root.iter('Employee'):
    first_names.append(employee.find('FirstName').text)
    last_names.append(employee.find('LastName').text)
    contact_nos.append(employee.find('ContactNo').text)
    emails.append(employee.find('Email').text)
    cities.append(employee.find('Address/City').text)
    states.append(employee.find('Address/State').text)
    zips.append(employee.find('Address/Zip').text)

data = pd.DataFrame({
    'FirstName': first_names,
    'LastName': last_names,
    'ContactNo': contact_nos,
    'Email': emails,
    'City': cities,
    'State': states,
    'Zip': zips
})

print(data)

conn = sqlite3.connect(':memory:')
data.to_sql('data',conn,index = False, if_exists='replace')


query = "SELECT * FROM data WHERE State = 'California' "
print(f"\n\n{query}\n\n")
result = pd.read_sql_query(query, conn)
print(result)