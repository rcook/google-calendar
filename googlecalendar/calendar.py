##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from __future__ import print_function
import apiclient.discovery
import datetime
import httplib2

def run_demo(credentials):
    http = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build(
        "calendar",
        "v3",
        http=http)

    # "Z" indicates UTC time
    now = datetime.datetime.utcnow().isoformat() + "Z"

    result_count = 10
    print("Getting the upcoming {} events".format(result_count))

    result_list = service.events().list(
        calendarId="primary",
        timeMin=now,
        maxResults=result_count,
        singleEvents=True,
        orderBy="startTime").execute()
    events = result_list.get("items", [])

    if events:
        for event in events:
            start = event["start"].get(
                "dateTime",
                event["start"].get("date"))
            print("{}: {}".format(start, event["summary"]))
    else:
        print("No upcoming events found.")
