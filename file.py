import urllib.request
import zipfile
import csv
import redis
url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ220318_CSV.ZIP"
data = urllib.request.urlretrieve(url,"trial.zip")

with zipfile.ZipFile("trial.zip","r") as zip_ref:
    zip_ref.extractall()

conn = redis.Redis()

with open('EQ220318.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        
        name = row['SC_NAME']
        open_value = row['OPEN']
        conn.set('name', row['SC_NAME'])
        conn.set('open',row['OPEN'])
        conn.set('close',row['CLOSE'])
        conn.set('high',row['HIGH'])
        conn.set('low',row['LOW'])
        print("Name",conn.get('name'))
        print("Open Value",conn.get('open'))
        print("Close Value",conn.get('close'))
        print("High Value",conn.get('high'))
        print("Low Value",conn.get('low'))

        
        
            
        
