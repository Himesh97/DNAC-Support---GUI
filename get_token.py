import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP , USERNAME , PASSWORD

requests.packages.urllib3.disable_warnings() # disable warnings

def get_auth_token():

    # End Point URL
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'

    # Post Request - Making
    req_post = requests.post(url, auth=HTTPBasicAuth(USERNAME,PASSWORD), verify = False)

    # Retrive Token
    token = req_post.json()['Token']

    # Print Token
    #print("Token Recieved : {} ".format(token))

    return token


if __name__ == "__main__":
    get_auth_token()
