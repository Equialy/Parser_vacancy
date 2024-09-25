import csv

def save_csv_file(jobs):
    with open('vacancies.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'company', 'location','link'])
        for v in jobs:
            writer.writerow(list(v.values()))
    return