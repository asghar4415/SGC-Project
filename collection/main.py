import csv
import os
import random

def generate_random_data(file_number):
    return [
        f"{file_number:03d}",
        random.choice([" Sindh ", " Punjab ", " Balochistan ", " KPK "]),
        random.choice([" Grant ", " Merit ", " Need-Based "]),
        random.choice([" Biology ", " Physics "]),
        random.randint(8000, 15000),
        f" https://{random.choice(['sindh', 'punjab', 'balochistan', 'kpk'])}.gov.pk "
    ]

def create_csv_file(file_number):
    file_name = f"{file_number:03d}.csv"
    data = [generate_random_data(file_number)]

    with open(file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["ID ", " Province ", " Category ", "Field ", " Amount ", " Website "])
        csvwriter.writerows(data)

def main():
    # Create 50 CSV files
    for file_number in range(1, 51):
        create_csv_file(file_number)

if __name__ == "__main__":
    main()
