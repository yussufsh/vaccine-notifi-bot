import logging
import sys
from datetime import datetime, timedelta
import requests
from requests import RequestException

# search for age limit less than:
AGE_LIMIT = 45
DOSE=1

#PANAJI
#lat=15.4909
#long=73.8278
#VASCO
lat=15.3982
long=73.8113

centersURL = "https://cdn-api.co-vin.in/api/v2/appointment/centers/public/findByLatLong?lat={0}&long={1}"
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter?center_id={0}&date={1}"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
log = logging.getLogger()
log.addHandler(logging.FileHandler("debug.log"))
log.setLevel(logging.INFO)


def print_availability(data, debug_flag):
    center=data["centers"]
    for session in center['sessions']:
        ACKey = "available_capacity_dose{0}".format(DOSE)
        if session['min_age_limit'] < AGE_LIMIT:
            if debug_flag:
                print(
                    f" {center['name']}, {center['district_name']} , {session['date']}, slots available: {session[ACKey]}")
            if not debug_flag and session[ACKey] != 0:
                print(
                    f" {center['name']}, {center['district_name']} , {session['date']}, slots available: {session[ACKey]}")

def check_availability(centers, debug_flag):
    dates = []
    today = datetime.now().strftime("%d-%m-%Y")
    next_monday = (datetime.now() + timedelta(days=-datetime.now().weekday(), weeks=1)).strftime("%d-%m-%Y")
    dates.append(today)
    dates.append(next_monday)
    log.info("checking availability across centers")
    for center in centers:
        for date in dates:
            try:
                response = requests.get(URL.format(center, date), headers={"user-agent": USER_AGENT})
                response.raise_for_status()
                if response.text == '{}':
                    continue
                # else:
                #     print(response.json())
                print_availability(data=response.json(), debug_flag=debug_flag)
            except RequestException as ex:
                log.error("Error calling API. Mostly due to rate limiting")
                log.exception(ex)
                if response.status_code > 299:
                    print("Alert: IP blocked")
                if debug_flag:
                    print("Failed to fetch. Response was: %s", ex.response.text)


def fetchCenters():
    centerIds = []
    centerNames = []
    log.info("Fetching all centers for given lat=%s long=%s", lat, long)
    response = requests.get(centersURL.format(lat, long), headers={"user-agent": USER_AGENT})
    response.raise_for_status()
    data=response.json()
    for center in data['centers']:
        centerIds.append(center["center_id"])
        centerNames.append(center["name"])
    return centerIds, centerNames

if __name__ == "__main__":
    debug = False
    if len(sys.argv) > 1:
        debug = sys.argv[1]
    centerIds, centerNames = fetchCenters()
    if debug:
        log.info("Found {0} centers near your location".format(len(centerIds)))
    log.info(centerNames)
    check_availability(centers=centerIds, debug_flag=debug)
