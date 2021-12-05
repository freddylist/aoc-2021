import os
import requests
import json

with open("config.json") as f:
    config = json.load(f)

year = config["Year"]
cookies = config["Cookies"]

paths = {
    "inputs": config["Inputs"],
}

for path in paths.values():
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def file_name(day):
    return f"{day:>02}.txt"

def get(day):
    input_path = os.path.join(paths["inputs"], file_name(day))

    try:
        with open(input_path) as f:
            return f.read()
    except OSError:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        r = requests.get(url, cookies=cookies)

        r.raise_for_status()

        input = r.text.strip()

        with open(input_path, 'w') as f:
            f.write(input)

        return input