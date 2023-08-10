import asyncio
import requests
import os
import csv
from datetime import datetime, timedelta
from schema.station_schema import StationSchema

BASE_URL = "http://environment.data.gov.uk/flood-monitoring"


def http_get(url):
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.json()
    except Exception:
        return {}


async def http_get_async(url):
    return await asyncio.to_thread(http_get, url)


def fetch_latest_readings() -> dict:
    url = f"{BASE_URL}/data/readings?latest&_view=full"
    return http_get(url)


def extract_station_id(latest_data) -> set:
    if not latest_data:
        return set()
    station_ids = set()
    items = latest_data.get("items")
    for item in items:
        measure = item.get("measure")
        if measure:
            station_reference = measure.get("stationReference")
            station_ids.add(station_reference)
    return station_ids


async def fetch_station_data_async(station_id) -> dict:
    url = f"{BASE_URL}/id/stations/{station_id}"
    response = await http_get_async(url)
    if response:
        items = response.get("items", {})
        station_schema = StationSchema()
        data = station_schema.dump(items)
        return data


async def fetch_all_stations_details(station_ids):
    tasks = [fetch_station_data_async(station_id) for station_id in station_ids]
    return await asyncio.gather(*tasks)


def write_to_csv(data, csv_name):
    header = list(StationSchema().dump({}).keys())
    data = [row for row in data if row]
    if not data:
        return
    with open(csv_name, "w") as f:
        writer = csv.DictWriter(f, header)
        writer.writeheader()
        writer.writerows(data)


async def main():
    latest_data = fetch_latest_readings()
    station_ids = extract_station_id(latest_data)
    data = await fetch_all_stations_details(station_ids)
    csv_name = "station_data.csv"
    previous_snapshot = (datetime.now() - timedelta(days=1)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    if os.path.exists(csv_name):
        os.rename(csv_name, f"station_data_bak_{previous_snapshot}.csv")
    write_to_csv(data, csv_name)


if __name__ == "__main__":
    asyncio.run(main())
