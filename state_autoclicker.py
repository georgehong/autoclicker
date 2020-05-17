import pytesseract
from PIL import ImageGrab
import pyautogui
from pynput import mouse


def main():
    """This script serves as an auto-clicker for https://online.seterra.com/en/vgp/3002

    This script requires three mouse-clicks to frame.  First click is the upper left corner of the map.  Second
    click is the bottom right corner of the rectangle including %accuracy | time | state to click.  Third click
    is the bottom right corner of the map.  For less trivial uses, this script allows one to select two points and
    apply OCR to the region.  The border is the rectangle with sharp edges, not the rounded ones.

    For Dana :)

    :return: None
    """
    global x1, y1, x2, y2, x3, y3
    x1, y1, x2, y2, x3, y3 = 0, 0, 0, 0, 0, 0

    for f in [on_click, on_click2, on_click3]:
        with mouse.Listener(
                on_click=f) as listener:
            listener.join()

    print(x1, y1, x2, y2, x3, y3)

    w = x3 - x1
    l = y3 - y1

    # Saved as x, y coordinates
    map_size = (2180, 1700)
    rel_location = {
        "WA": (253, 254),
        "OR": (197, 407),
        "CA": (150, 780),
        "NV": (290, 670),
        "ID": (435, 475),
        "MT": (620, 344),
        "UT": (494, 738),
        "AZ": (440, 980),
        "WY": (666, 546),
        "CO": (715, 767),
        "NM": (674, 1000),
        "ND": (940, 346),
        "SD": (946, 503),
        "NE": (946, 652),
        "KS": (1000, 815),
        "OK": (1045, 972),
        "TX": (988, 1200),
        "MN": (1144, 415),
        "IA": (1187, 630),
        "MO": (1237, 822),
        "AR": (1240, 989),
        "LA": (1236, 1153),
        "WI": (1314, 482),
        "IL": (1354, 754),
        "MS": (1363, 1111),
        "MI": (1510, 546),
        "IN": (1476, 720),
        "KY": (1553, 833),
        "TN": (1488, 938),
        "AL": (1486, 1086),
        "OH": (1596, 690),
        "GA": (1638, 1098),
        "FL": (1760, 1344),
        "ME": (2045, 317),
        "NH": (1985, 446),
        "VT": (1935, 393),
        "MA": (1972, 503),
        "RI": (2011, 529),
        "CT": (1969, 543),
        "NJ": (1914, 663),
        "NY": (1866, 491),
        "PA": (1787, 622),
        "DE": (1900, 716),
        "MD": (1838, 696),
        "WV": (1685, 774),
        "VA": (1798, 800),
        "NC": (1800, 900),
        "SC": (1730, 1010),
        "HI": (726, 1535),
        "AK": (266, 1388),
        "Ml": (1510, 546),
    }
    print(len(rel_location))

    for _ in range(50):
        cap = ImageGrab.grab(bbox=trans_coords(x1, y1, x2, y2))
        # print(cap.size)
        tesstr = pytesseract.image_to_string(cap, lang='eng')
        print(tesstr)
        coords = rel_location[tesstr.strip()[-2:]]
        x_val = x1 + (w / 2180) * coords[0]
        y_val = y1 + (l / 1700) * coords[1]
        pyautogui.click(x=x_val, y=y_val)


def on_click(x, y, button, pressed):
    """This method records the upper-left corner of the bounding box"""
    global x1, y1
    x1 = x
    y1 = y
    if not pressed:
        # Stop listener
        return False


def on_click2(x, y, button, pressed):
    """ This method records the lower-right corner of the bounding box around the click instruction"""
    global x2, y2
    x2 = x
    y2 = y
    if not pressed:
        # Stop listener
        return False


def on_click3(x, y, button, pressed):
    """ This method records the lower-right corner of the bounding box"""
    global x3, y3
    x3 = x
    y3 = y
    if not pressed:
        # Stop listener
        return False


def trans_coords(xu, yu, xl, yl):
    """ Translates coordinates proportionally from grab resolution to resolution found by using PIL's ImageGrab
    :param xu: first horizontal coordinate of image in grab resolution
    :param yu: first vertical coordinate
    :param xl: second horizontal coordinate of image in grab resolution
    :param yl: second vertical coordinate
    :return: tuple of respective coordinates as ints in the resolution of PIL's ImageGrab
    """
    # PIL's resolution of screen / Mac's Grab resolution
    xscale = 3360 / 1680
    yscale = 2100 / 1050
    return int(xu * xscale), int(yu * yscale), int(xl * xscale), int(yl * yscale)


if __name__ == "__main__":
    main()





