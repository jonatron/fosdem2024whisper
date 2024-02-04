import os
import time

import requests
from files import files


os.makedirs("videos", exist_ok=True)

for url_dict in files:
    url = url_dict["href"]
    print(url)
    path = url.split("fosdem.org")[1]
    filename = url.split("/")[-1]
    local_filename = f'videos/{filename}'
    if os.path.exists(local_filename):
        print("exists - skip")
        continue

    resp = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(resp.content)

    time.sleep(0.5)
