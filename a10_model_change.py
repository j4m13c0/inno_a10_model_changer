import io, json
from io import BytesIO
import requests
from urllib.parse import urlencode
from urllib import parse
import queue
from datetime import datetime, timedelta

timeout = 5

def check_if_miner(ip_address):
    try:
        r = requests.get('http://{}/'.format(ip_address), timeout=timeout)
        if r.status_code == 200:
            if '<title>DragonMint</title>' in r.text or \
                    '<title>AsicMiner</title>' in r.text:
                return True
                
    except Exception as e:
        return False

    return False

def change_miner_model(ip_address,username,password,model):

    if not check_if_miner(ip_address):
        print("\nThis is not a compatible Innosilicon Miner")
        exit()

    def _stream_data(data):
        print(data)
        # 
    response = requests.post(
    parse.urljoin("http://{}".format(ip_address), '/api/auth'),
    timeout=timeout,
    data={'username': username, 'password': password})
    response.raise_for_status()
    json = response.json()
    if 'jwt' not in json:
        print("Login Error")
        raise ValueError("Not authorized: didn't receive token, check username or password.")
    jwt = json['jwt']

    print("\nLogin to miner was successful.")

    data={'type': model, 'plat': "G19"}
    
    response = requests.post(
    parse.urljoin("http://{}".format(ip_address), '/api/setPlatform'),
    headers={'Authorization': 'Bearer ' + jwt},
    timeout=timeout,
    data=data)
    response.raise_for_status()
    try:
        if not response.json()['success']:
            print("\nThere was an error changing the model.")
    except Exception as e:
        print(e)
        print("\nThere was an error changing the model.")


if __name__ == '__main__':

    print("\nInnosilicon A10 Model Changer by @j4m13c\n")

    print("Please enter the username and password for the miner: (default is admin for both):")

    username = input("Username: ")
    password = input("Password: ")

    print("\nNow enter the full IP Address for example 192.168.1.100:")
    ip_address = input("IP Address: ")

    if(check_if_miner(ip_address=ip_address)):
        print("Dragon Miner Detected!\n")
    else:
        print("Miner was not detected on this IP. Please try again.")
        exit()

    valid_input = False
    change_model = False
    while not valid_input:
        model_or_ssh = input("Press 1 to change model, 2 to quit:")

        if model_or_ssh == '1':
            change_model = True
            valid_input = True
        elif model_or_ssh == '2':
            valid_input = True
            exit()
        else:
            print("\nInvalid input!")

    model_name = ""
    if(change_model):
        valid_input = False
        while not valid_input:
            print("\nChange model number of miner. (t2ti is used to unlock SSH initially)")
            print("1: A10")
            print("2: A10L")
            print("3: A10S")
            print("4: A10U")
            print("5: A10X")
            print("6: T2TI")
            selected_model = input("Please enter the number:")

            if selected_model == '1':
                valid_input = True
                model_name = "a10"
            elif selected_model == '2':
                valid_input = True
                model_name = "a10l"
            elif selected_model == '3':
                valid_input = True
                model_name = "a10s"
            elif selected_model == '4':
                valid_input = True
                model_name = "a10u"
            elif selected_model == '5':
                valid_input = True
                model_name = "a10x"
            elif selected_model == '6':
                valid_input = True
                model_name = "T2TI"

        print("Changing Model to %s"%model_name)
        change_miner_model(ip_address=ip_address,username=username,password=password,model=model_name)

