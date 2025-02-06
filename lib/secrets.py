import ujson

secrets = None

def load_secrets():
    try:
      with open('secrets.json') as fp:
        return ujson.loads(fp.read())
    except (OSError, ValueError) as e:
      print(f"Error loading secrets: {e}")
      return {}

def get_wifi_secrets():
    global secrets

    if secrets is None:
        secrets = load_secrets()

    return secrets['wifi']['ssid'], secrets['wifi']['password']
