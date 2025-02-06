from lib.parse_datetime import parse_datetime
from lib.utils import two_digits
from st7735 import TFT
from st7735 import sysfont
from machine import SPI, Pin

DISPLAY_WIDTH = 160
DISPLAY_HEIGHT = 128

TEXT_LEFT_OFFSET = 14
LAST_ROW_TOP_OFFSET = 120

FONT = sysfont.sysfont

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,17,18, ScreenSize=(160, 128))

def init_display():
    tft.rotate = 1
    tft.initr()
    tft.rgb(True)
    tft.fill(TFT.BLACK)  # Clear the screen

def write_start_msg_to_display(msg = "Booting"):
    tft.text((TEXT_LEFT_OFFSET, 30), "Starting ...", TFT.WHITE, FONT, 2, nowrap=True)

    tft.fillrect((0, 62), (DISPLAY_WIDTH, 62 + 20), TFT.BLACK)
    tft.text((TEXT_LEFT_OFFSET, 62), msg, TFT.WHITE, FONT, 1, nowrap=True)

def write_error_to_display(msg="Unknown reason"):
    tft.fill(TFT.BLACK)  # Clear the screen
    tft.text((TEXT_LEFT_OFFSET, 30), "Error", TFT.WHITE, FONT, 3, nowrap=True)
    tft.text((TEXT_LEFT_OFFSET, 62), msg, TFT.WHITE, FONT, 1, nowrap=True)

def write_fetching_sign_to_display():
    tft.text((DISPLAY_WIDTH - 20, LAST_ROW_TOP_OFFSET), "...", TFT.WHITE, FONT, 1, nowrap=True)

def write_to_display(data, timestamp):
    global tft

    tft.fill(TFT.BLACK)  # Clear the screen

    font_height = 10
    font_width = FONT["Width"]
    line_index = 0
    top_offset = 8
    left_offset = 4

    lines = [line for stop in data for line in stop['lines']]
    lines = sorted(lines, key=lambda line: (line['name'] not in ['49', '47A', '52', 'U4'], line['name'] != '49', line['name'] != '47A', line['name'] != '52', line['name'] != 'U4', line['name']))

    for line in lines:
        pos_height = top_offset + line_index * (font_height + 16)
        line_name = line['name']
        departures = line['departures']

        if line_name == 'U4':
            departures = [departure for departure in departures if departure['countdown'] >= 6]

        text = '", '.join([f"{departure['countdown']}" for departure in departures[:4]])
        if (len(text) > 0):
            text += '"'

        tft.text((left_offset, pos_height), line_name, TFT.WHITE, FONT, 2, nowrap=True)
        tft.text((left_offset + 6 * font_width + 10, pos_height + 5), text, TFT.WHITE, FONT, 1, nowrap=True)

        line_index += 1

    datetime_tuple = parse_datetime(timestamp)
    hours = two_digits(datetime_tuple[3])
    minutes = two_digits(datetime_tuple[4])

    tft.text((0, LAST_ROW_TOP_OFFSET), "Last updated: " + "{}:{}".format(hours, minutes), TFT.WHITE, FONT, 1, nowrap=True)
