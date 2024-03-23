import json
from random import randint, choice, sample
from datetime import datetime, timedelta
import pycountry


def datetime_to_timestamp(dt):
    return int(dt.timestamp() * 1000)
# Helper function to generate random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Helper function to generate random list of unique countries
def random_countries():
    all_countries = list(pycountry.countries)
    num_countries = randint(1, len(all_countries))
    return [country.alpha_2 for country in sample(all_countries, num_countries)]

# Generate current date and date in April
now = datetime.now()
april_date = datetime(now.year, 4, 1)


# Generate 1000 documents
documents = []
for i in range(1000):
    start_date = random_date(datetime(2023, 1, 1), now)
    end_date = random_date(april_date, datetime(now.year + 1, 1, 1))
    age_start = randint(1, 100)
    age_end = randint(age_start, 100)
    genders = [["M"], ["F"], ["M", "F"]]
    countries = random_countries()
    platforms = [["ios"], ["android"], ["web"], ["ios", "android"], ["ios", "web"], ["android", "web"], ["ios", "android", "web"]]

    document = {
        "title": f"active {i}",
        "startAt": {"$date": start_date.strftime("%Y-%m-%dT%H:%M:%SZ")},
        "endAt": {"$date": end_date.strftime("%Y-%m-%dT%H:%M:%SZ")},
        "conditions": {
            "ageStart": age_start,
            "ageEnd": age_end,
            "genders": choice(genders),
            "countries": countries,
            "platforms": choice(platforms)
        }
    }
    documents.append(document)

# Save documents to JSON file
with open("documents.json", "w") as file:
    json.dump(documents, file, indent=2)

print("JSON file created successfully.")


may_date = datetime(now.year, 5, 1)
july_date = datetime(now.year, 7, 1)
documents = []
for i in range(5000):
    start_date = random_date(may_date, datetime(now.year, 6, 1))
    end_date = random_date(july_date, datetime(now.year + 1, 1, 1))
    age_start = randint(1, 100)
    age_end = randint(age_start, 100)
    genders = [["M"], ["F"], ["M", "F"]]
    countries = random_countries()
    platforms = [["ios"], ["android"], ["web"], ["ios", "android"], ["ios", "web"], ["android", "web"], ["ios", "android", "web"]]

    document = {
        "title" : f"not active {i}",
        "startAt": {"$date": start_date.strftime("%Y-%m-%dT%H:%M:%SZ")},
        "endAt": {"$date": end_date.strftime("%Y-%m-%dT%H:%M:%SZ")},
        "conditions": {
            "ageStart": age_start,
            "ageEnd": age_end,
            "genders": choice(genders),
            "countries": countries,
            "platforms": choice(platforms)
        }
    }
    documents.append(document)

# Save documents to JSON file
with open("documents_after.json", "w") as file:
    json.dump(documents, file, indent=2)

