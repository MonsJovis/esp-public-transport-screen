from lib.display import init_display, write_error_to_display, write_fetching_sign_to_display, write_start_msg_to_display, write_to_display
from lib.led import led_blink_success
from lib.led import led_blink_error
from lib.init_wifi import init_wifi
from lib.get_data import get_data
from machine import WDT

wdt = WDT(timeout=60 * 1000)

def initialize():
    print('Initializing display ...')
    init_display()
    write_start_msg_to_display('Initializing Wi-Fi ...')

    print('Initializing Wi-Fi ...')
    if not init_wifi():
        print('Wi-Fi connection failed')
        write_error_to_display('Wi-Fi connection failed')
        led_blink_error(10)
        return

    print('Wi-Fi connection successful')

    write_start_msg_to_display('Fetching data ...')

def start_main_loop():
    global wdt

    while True:
        wdt.feed()

        print('Fetching data ...')
        write_fetching_sign_to_display()

        data = None
        try:
            data = get_data()
        except Exception as e:
            print(e)

        if data is None:
            print('Error fetching data')
            write_error_to_display('Error fetching data')
            led_blink_error(5)
            continue

        print('Writing to display ...')
        write_to_display(data['data'], data['localeTimestamp'])
        led_blink_success(30)

def main():
    initialize()
    start_main_loop()

main()
