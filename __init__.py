import requests
import json
from aqt import mw
from aqt.utils import qconnect, showInfo
from aqt.qt import *
from bs4 import BeautifulSoup

config = mw.addonManager.getConfig(__name__)

CARD_SELECTION = config["card_selection"]
DECK_TARGET = "deck:" + config["deck_target"]
KEY_FIELD = config["key_field"]
IMAGE_FIELD = config["image_field"]

def get_image_url(query):
    MAX_ITERATIONS = 5
    for i in range(MAX_ITERATIONS):
        response = requests.get(
            "https://www.bing.com/images/search",
            params={
                "q": query,
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")
        image_element = soup.find("img", class_="mimg")

        if image_element:
            link_element = image_element.find_parent("a")
            link_address = link_element["m"]
            dictionary = json.loads(link_address)
            turl = dictionary["turl"]
            try:
                response = requests.get(turl, timeout=5)
            except Exception as e:
                continue
            return turl

    return None

def generateImages():
    ctr = 0
    ids = mw.col.find_notes(DECK_TARGET)
    for id in ids:
        note = mw.col.get_note(id)
        if CARD_SELECTION == "override" or not note[IMAGE_FIELD]:
            note[IMAGE_FIELD] = f'<img src="{get_image_url(note[KEY_FIELD])}" width="600">'
            ctr = ctr + 1
        mw.col.update_note(note)
    showInfo("Notes changed: %d" % ctr)
        
action = QAction("Generate Images ", mw)
qconnect(action.triggered, generateImages)
mw.form.menuTools.addAction(action)