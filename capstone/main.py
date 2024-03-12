import influxdb_client, os, time
import random
import requests
import json
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


# Initialize Client
def init():
    token = "uCy_LubAvac9xP0DQa_Iaazt0-KmGcAgS232lA-1XIhimMh-x4cDH_MKqDmHpn5EWOz3U29-IrJxWRmNAY7M2A=="
    org = "mydesque"
    url = "http://localhost:8086"

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)



# def write():
#     bucket = "semfi"
#     write_api = client.write_api(write_options=SYNCHRONOUS)

#     mist_api_token = 'Dh845cWdrn3bn8au3ceZjaKZxn80ORnp7SYEzBYiKfhmBaERGliXcB6t89fXm3bCAY0USw0d5uz8cG8vvaHbssljtYanTIwB'
#     headers = {'Content-Type': 'application/json', 'Authorization': 'Token ' + mist_api_token}
#     url = 'https://api.gc2.mist.com/api/v1/sites/15c239c3-a50b-46e4-b9b6-4a818603753b/wlans'
#     # url = 'https://api.gc2.mist.com/api/v1/orgs/b84983ca-9e53-4f66-a2ea-cf6ca6489ff1/rftemplates'
#     response = requests.get(url, headers=headers)
#     data = json.loads(response.text)

#     for entry in data:
#         ssid = entry['ssid']
#         # bands = entry['bands']
#         modified_time = entry['modified_time']
#         client_limit_up = entry['client_limit_up']

#         # field_value = len(data)
#         # field_value2 = client_limit_up
#         # field_value3 = modified_time

#         # point = Point("measurement1").tag("SSID", ssid).field("field1", field_value)
#         # point2 = Point("measurement2").tag("client_limit_up", client_limit_up).field("field2", field_value2)
#         # point3 = Point("measurement3").tag("modified_time", modified_time).field("field3", field_value3)

#         point = Point("measurement")
#         # point = point.field("downlink_rates", downlink_rates)
#         # point = point.field("bands", bands)
#         point = point.field("modified_time", modified_time)
#         point = point.field("client_limit_up", client_limit_up)
#         # point = point.field("frequency_6", frequency_6)
#         write_api.write(bucket=bucket, org="mydesque", record=point)

#         # write_api.write(bucket=bucket, org="mydesque", record=point)
#         # write_api.write(bucket=bucket, org="mydesque", record=point2)
#         # write_api.write(bucket=bucket, org="mydesque", record=point3)

#     time.sleep(1)


def write():
    bucket = "resur"
    write_api = client.write_api(write_options=SYNCHRONOUS)

    mist_api_token = 'Dh845cWdrn3bn8au3ceZjaKZxn80ORnp7SYEzBYiKfhmBaERGliXcB6t89fXm3bCAY0USw0d5uz8cG8vvaHbssljtYanTIwB'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token ' + mist_api_token}
    # url = 'https://api.gc2.mist.com/api/v1/sites/15c239c3-a50b-46e4-b9b6-4a818603753b/wlans'
    url = 'https://api.gc2.mist.com/api/v1/sites/15c239c3-a50b-46e4-b9b6-4a818603753b/stats/devices'
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    for radio in data[0]['radio_stat']:
        channel = data[0]['radio_stat'][radio]['channel']
        bandwidth = data[0]['radio_stat'][radio]['bandwidth']
        power = data[0]['radio_stat'][radio]['power']
        util_all = data[0]['radio_stat'][radio]['util_all']
        num_clients = data[0]['radio_stat'][radio]['num_clients']
        
        point = Point("measurement1").tag("channel", channel).field("channels", channel)
        point2 = Point("measurement1").tag("bandwidth", bandwidth).field("bandwidth", bandwidth)
        point31 = Point("measurement1").tag("num_clients", num_clients).field("number_of_clients", num_clients)
        point4 = Point("measurement1").tag("power", power).field("power", power)

        # write_api.write(bucket=bucket, org="mydesque", record=point)
        # write_api.write(bucket=bucket, org="mydesque", record=point2)
        write_api.write(bucket=bucket, org="mydesque", record=point31)
        # write_api.write(bucket=bucket, org="mydesque", record=point4)

    time.sleep(1)

# Read data
def read():
    query_api = client.query_api()
    query = """from(bucket: "Semfio")
    |> range(start: -10m)
    |> filter(fn: (r) => r._measurement == "measurement1")"""
    tables = query_api.query(query, org="HumberWireless")

    for table in tables:
        for record in table.records:
            print(record)


# Aggregate
def aggregate():
    query_api = client.query_api()
    query = """from(bucket: "mide")
    |> range(start: -10m)
    |> filter(fn: (r) => r._measurement == "measurement1")"""
    tables = query_api.query(query, org="mydesque")

    for table in tables:
        for record in table.records:
            print(record)


if __name__ == "__main__":
    token = "uCy_LubAvac9xP0DQa_Iaazt0-KmGcAgS232lA-1XIhimMh-x4cDH_MKqDmHpn5EWOz3U29-IrJxWRmNAY7M2A=="
    org = "mydesque"
    url = "http://localhost:8086"
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    for x in range(100):
        write()
        # aggregate()
    print("done!")
