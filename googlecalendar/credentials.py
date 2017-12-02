##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from __future__ import print_function
import os

from oauth2client import client
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from pyprelude.file_system import make_path

# If modifying these scopes, delete your previously saved credentials
# at ~/.google-calendar/credentials/calendar-python-quickstart.json
_SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
_CLIENT_SECRET_FILE = 'client_secret.json'
_APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def get_credentials(config, args):
    credential_dir = make_path(config.dir, "credentials")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)

    credential_path = make_path(credential_dir, "calendar-python-quickstart.json")
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        client_secret_path = make_path(config.dir, _CLIENT_SECRET_FILE)
        flow = client.flow_from_clientsecrets(client_secret_path, _SCOPES)
        flow.user_agent = _APPLICATION_NAME
        credentials = run_flow(flow, store, args)
        print("Storing credentials to {}".format(credential_path))
    return credentials
