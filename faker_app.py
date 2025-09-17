import csv
from faker import Faker

fake = Faker()

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "email", "job"])
    
    for i in range(10):
        writer.writerow([fake.name(), fake.email(), fake.job()])