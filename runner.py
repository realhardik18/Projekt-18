import os
from Google import Create_Service
import pandas as pd

API_NAME = 'youtube'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'creds.json'
SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload'

]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
print(service.videos())
# work from here
