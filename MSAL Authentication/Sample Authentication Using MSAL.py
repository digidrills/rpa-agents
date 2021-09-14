# Some Important Points to keep in mind:
# All fields populated withing the angular brackets (<>) are meant to be populated with your own values of the items
# This code snippet uses the default caching method and caches the procured access token in memory as long as the RunTime lasts
# the "#%%" Comment makes individual cells that can be run individually if you will be using Visual Studio Code as your development environment

#%%
import json
import msal
import requests
from requests import Response
from pprint import pprint



#%%
# config = json.load(open("./parameters.json")) 
# While not necessary, it's usually easier to store the values of the variables such as client id etc in an external JSON file

cache = msal.SerializableTokenCache()

app = msal.ConfidentialClientApplication(
    <client_id>,
    authority=<authority>,
    client_credential=<secret>,
    # token_cache= Default cache is in memory only.
    # You can learn how to use SerializableTokenCache from
    # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache
)

#%%
result = None
# First, the code looks up a token from the cache.
# Because we're looking for a token for the current app, not for a user,
# use None for the account parameter.
result = app.acquire_token_silent(scopes= 'scopes')

if not result:
    print("No suitable token exists in cache. Let's get a new one from AAD.")
    result = app.acquire_token_by_username_password(
        scopes=<Scopes>,
        username=<Username>,
        password=<Password>,
    )
    if "access_token" in result:
        print("Success") #print result['access_token'] if you want to see the raw access_token



#%%
headers = {"Authorization": "Bearer " + result["access_token"]} # Adds the access token to the header for the GET request
drive_details = requests.get(
    f"https://graph.microsoft.com/v1.0/me/drive/root/children",
    headers=headers,
)  # Lists all the children items within the root directory of the user's OneDrive

pprint(drive_details.json()) #Prints Details of all files and folders within root directory