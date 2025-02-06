import network
from utime import sleep
from lib.secrets import get_wifi_secrets

WIFI_CONNECTION_ATTEMPTS = 10
WIFI_CONNECTION_RETRY_WAIT_SEC = 1

def init_wifi():
    # Get Wi-Fi credentials
    secrets = get_wifi_secrets()

    wlan = network.WLAN(network.STA_IF)

    # Try to connect to the network (max 10 attempts)
    for _ in range(WIFI_CONNECTION_ATTEMPTS):
        # Activate the network interface
        wlan.active(True)

        # Connect to your network
        try:
            wlan.connect(secrets[0], secrets[1])
        except Exception as e:
            print('Error while connecting to Wi-Fi')
            print(e)

        if wlan.isconnected():
            return True

        print("Not connected to Wi-Fi yet. Trying again in {} second ...'".format(WIFI_CONNECTION_RETRY_WAIT_SEC))
        sleep(WIFI_CONNECTION_RETRY_WAIT_SEC)

    return False