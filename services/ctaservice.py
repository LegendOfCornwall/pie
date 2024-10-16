from typing import List
import requests
import xml.etree.ElementTree as ET
import datetime
from models.trainarrival import TrainArrival

#test comment

def getTrainArrivals() -> List[TrainArrival]:
    baseCtaUrl = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx/"
    ctaKeyParam = "key=38baeaf33f1745baaa96c6fdd45b0820"
    mapIdParam = "mapid=40530"

    fullCtaUrl = baseCtaUrl + "?" + ctaKeyParam + "&" + mapIdParam

    ctareq = requests.get(fullCtaUrl)
    print(ctareq.content)
    root = ET.fromstring(ctareq.content)

    train_arrivals: List[TrainArrival] = []
    for eta in root.findall('eta'):
        # Extract details for each train
        station_name = eta.find('staNm').text
        service_direction = eta.find('stpDe').text
        train_run_number = eta.find('rn').text
        route = eta.find('rt').text
        destination = eta.find('destNm').text
        arrival_time = eta.find('arrT').text

        train_arrivals.append(TrainArrival(
            station_name = station_name,
            service_direction = service_direction,
            train_run_number = train_run_number,
            route = route,
            destination = destination,
            arrival_time = formatArrival(arrival_time)
        ))

    return train_arrivals

def formatArrival(arrivalStr: str) -> datetime.timedelta:
    # Define the date format used in the string
    date_format = "%Y%m%d %H:%M:%S"
    
    # Convert the string to a datetime object
    datetime_arrival = datetime.datetime.strptime(arrivalStr, date_format)
    
    # Get the current time
    now = datetime.datetime.now()
    
    # Calculate the time difference
    time_diff = datetime_arrival - now

    minutes_diff = divmod(time_diff.total_seconds(), 60)[0]  # divmod gives (minutes, seconds)

    
    return minutes_diff