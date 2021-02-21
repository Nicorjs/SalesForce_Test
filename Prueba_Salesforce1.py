from simple_salesforce import Salesforce
import json

with open('data.json', 'r') as myfile:
    data = json.loads(myfile.read())
    
print(data)

