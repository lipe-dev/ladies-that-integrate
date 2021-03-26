import json

import requests


def request_jobs(app, key):
    print("Requesting Jobs")
    r = requests.get(f"https://api.airtable.com/v0/{app}/Vagas",
                     params={"filterByFormula": "AND(Status='Backlog',Imagem!=TRUE())"},
                     headers={"Authorization": f"Bearer {key}"})

    return r.json().get('records')


def update_jobs(app, key, all_jobs):
    print("Updating Jobs on Air Table")
    request_url = f"https://api.airtable.com/v0/{app}/Vagas"

    records = []
    batch_count = 0

    for index, cur_job in enumerate(all_jobs):
        records.append({
            "id": cur_job.get("id"),
            "fields": {
                "Imagem": True
            }
        })

        if len(records) == 10 or cur_job == all_jobs[-1]:
            update_data = {
                "typecast": True,
                "records": records
            }

            batch_count += 1

            r = requests.patch(
                request_url,
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json"
                },
                data=json.dumps(update_data))

            s = "s" if len(records) > 1 else ""

            if r.ok:
                print(f"Air Table batch {batch_count} ({len(records)} job{s}) updated successfully!")
            else:
                print("**************************************************")
                print("* COULD NOT UPDATE AIR TABLE, DO THAT MANUYALLY! *")
                print("**************************************************")

            records = []
