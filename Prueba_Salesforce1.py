from salesforce_bulk import SalesforceBulk, CsvDictsAdapter
import json

with open('data.json', 'r') as myfile:
    data = json.loads(myfile.read())
    
username = data["user"]
password = data["password"]
instance = data["instance"]
security_token = data["token"]

try:
    bulk = SalesforceBulk(username=username, password=password, security_token=security_token)
    job = bulk.create_insert_job("Account", contentType='CSV')
    accounts = [dict(Name="Account%d" % idx) for idx in range(5,10)]
    csv_iter = CsvDictsAdapter(iter(accounts))
    batch = bulk.post_batch(job, csv_iter)
    bulk.wait_for_batch(job, batch)
    bulk.close_job(job)
    result = bulk.get_batch_results(batch,job)
    jsonString = json.dumps(result)
    print(jsonString)
except Exception as e:
    Exception(e)
