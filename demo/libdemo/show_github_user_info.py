import requests

resp = requests.get("https://api.github.com/users/gvanrossum")

if resp.status_code != 200:    # success
    print('Sorry! Could not get details!')
    exit(1)

details = resp.json()
print(f"Name         : {details['name']}")
print(f"Company      : {details['company']}")
print(f"Location     : {details['location']}")
print(f"Public Repos : {details['public_repos']}")

