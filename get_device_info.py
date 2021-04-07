import requests
from requests.auth import HTTPBasicAuth
from get_token import get_auth_token
from print_device_info import print_device_list
from print_device_info import serial_list


def get_dev_info():
    global serial_list 
    token = get_auth_token()

    #Device End point
    url = 'https://sandboxdnac.cisco.com/api/v1/network-device'

    #header info (x-auth-token | content type : application/json)
    hdr = {'x-auth-token': token , 'content-type':'application/json'}

    #query 
    #querystring = {"macAddress":"00:c8:8b:80:bb:00","managementIpAddress":"10.10.22.74"}

    # GET request
    req_get = requests.request('GET', url , headers = hdr) #params = querystring

    #device list
    device_list = req_get.json()
    x = print_device_list(device_list)
    #print(x)
    return x
    #return serial_list


