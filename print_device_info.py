serial_list = []
def print_device_list(device_json):
    global serial_list
    serial_list = []
    serial_list.append(("Host Name", "Mgmt IP", "Serial","PlatformId", "SW Version", "Role", "Uptime"))
    #print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
         # format("hostname", "mgmt IP", "serial","platformId", "SW Version", "role", "Uptime"))
    for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            #print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                 # format(device['hostname'],
                        # device['managementIpAddress'],
                         #serialNumber,
                         #platformId,
                        # device['softwareVersion'],
                         #device['role'],
                         #uptime,
                        #))
            serial_list.append((device['hostname'], device['managementIpAddress'], serialNumber,platformId, device['softwareVersion'],device['role'],uptime))
            
            #serial_list.append(serialNumber)  
    return serial_list

    #print (serial_list)
