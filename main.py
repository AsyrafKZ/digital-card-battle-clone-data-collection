from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import json
import re
import os


def example_func():
    result = ""
    # output json
    # write file
    with open("states.json", "w") as f:
        json.dump(
            result, f, indent=2
        )  # json.dump - write JSON file to local directory from Python object in Python file

    write_json_string = json.dumps(
        None, indent=2
    )  # json.dumps - write Python object to JSON string within Python file

    # read the output json to check the result
    # read file
    with open("states.json") as f:
        data = json.load(
            f
        )  # json.load - read JSON file from local directory into Python Object in Python file
    read_json_result = json.loads(
        None
    )  # json.loads - read JSON string format file into Python Object within Python file

    # html_url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation='
    # html_text = requests.get(html_url).text
    # soup = BeautifulSoup(html_text, 'lxml')
    # job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
    # print(job)

    # read target webpage
    with open("home.html", "r") as html_file:
        content = html_file.read()

        # Create BeautifulSoup object
        soup = BeautifulSoup(content, "lxml")

        # get the first target tag
        first_tag = soup.find("div")
        # print(f'first_tag {first_tag}')

        # get all target tags
        all_tags = soup.find_all("div", class_="top1")
        print(f"all tags {all_tags}")

        for tag in all_tags:
            print(tag.find("div", class_="div2").text)


def scrape_page():
    cards = None
    with open("cards.json") as f:
        cards = json.load(f)
    option_cards = cards["option_cards"]

    for option in option_cards:
        img_url = option["img_src"]
        img_data = requests.get(img_url).content
        # filename follows cards' number
        number = option["number"]
        fileName = "./images/options/" + number + ".png"
        # make new directory
        dirname = os.path.dirname(fileName)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        # save file to local directory
        with open(fileName, "wb") as f:
            f.write(img_data)

    # cards["monster_cards"] = monster_cards

    # write effect cards Python list dict to JSON file

    # url = (
    #     "https://digimon.neoseeker.com/wiki/Option_cards_in_Digimon_Digital_Card_Battle"
    # )
    # req = Request(
    #     url,
    #     headers={
    #         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    #     },
    # )
    # webpage = urlopen(req).open()
    # soup = BeautifulSoup(webpage, "lxml")
    # print(soup)

    # get the html string
    # page_url = (
    #     "https://digimon.neoseeker.com/wiki/Option_cards_in_Digimon_Digital_Card_Battle"
    # )
    # html_string = requests.get(page_url).text
    # soup = BeautifulSoup(html_string, "lxml")
    # print(soup)

    # read cards json file
    # cards = None
    # with open("cards.json") as f:
    #     cards = json.load(f)
    # effect_cards = cards["effect_cards"]

    # get all image source links
    # image_tags = soup.find_all("img")
    # print(f"image tags count:{len(image_tags)}")
    # img = image_tags[0]
    # print(img["src"])

    # # # loop through all img_urls
    # for i, img in enumerate(image_div):
    #     img = image_div.find('img')
    #     print(img['src'])
    #     # effect_cards[i]["img_src"] = img["src"]
    # # # write effect cards Python list dict to JSON file
    # with open("effectCards.json", "w") as f:
    #     json.dump(effect_cards, f, indent=2)


def addMonsterImageUrls():
    # get the html string
    page_url = "https://digimon.fandom.com/wiki/Digimon_Digital_Card_Battle/Cards"
    html_string = requests.get(page_url).text
    soup = BeautifulSoup(html_string, "lxml")

    # read cards json file
    cards = None
    with open("cards.json") as f:
        cards = json.load(f)
    monster_cards = cards["monster_cards"]
    effect_cards = cards["effect_cards"]

    # get all image source links
    image_urls = soup.find_all("img", class_="pi-image-thumbnail")
    # # loop through all numbers
    numbers = soup.find_all("b")
    for i, img in enumerate(image_urls):
        monster_cards[i]["img_src"] = img["src"]
    # # write monster cards Python list dict to JSON file
    with open("monsterCards.json", "w") as f:
        json.dump(monster_cards, f, indent=2)


def updateMonsterCardJson():
    # read cards json file
    cards = None
    with open("cards.json") as f:
        cards = json.load(f)
    with open("monsterCards.json") as f:
        monster_cards = json.load(f)

    cards["monster_cards"] = monster_cards
    # write cards master JSON file
    with open("cards.json", "w") as f:
        json.dump(cards, f, indent=2)
    # # write monster cards Python list dict to JSON file
    with open("monsterCards.json", "w") as f:
        json.dump(monster_cards, f, indent=2)
    # # write effect cards Python list dict to JSON file
    # with open("effectCards.json", "w") as f:
    #     json.dump(effect_cards, f, indent=2)


def getUniqueEffects():
    cards = None
    with open("cards.json") as f:
        cards = json.load(f)
    monster_cards = cards["monster_cards"]
    effect_cards = cards["effect_cards"]

    effect_master = []

    for card in monster_cards:
        if card["x_effect"] != "None":
            effects = card["x_effect"].split(". ")
            for effect in effects:
                effect_master.append(effect.rstrip(".").lower())
        if card["support"] != "None":
            effects = card["support"].split(". ")
            for effect in effects:
                effect_master.append(effect.rstrip(".").lower())
    for card in effect_cards:
        if card["effect"] != "None":
            effects = card["effect"].split(". ")
            for effect in effects:
                effect_master.append(effect.rstrip(".").lower())
    temp = set(effect_master)
    effect_master = list(temp)
    effect_master.sort()
    temp2 = ""
    for effect in effect_master:
        temp2 = temp2 + effect + "\n"

    with open("effectList4.txt", "w") as f:
        f.write(temp2)


def addEffectImageUrls():
    with open("effect_cards_neoseeker.txt") as f:
        effects_cards_string = json.load(f)
    base_img_url = "https://cdn.staticneo.com/w/digimon/"

    cards = None
    with open("cards.json") as f:
        cards = json.load(f)
    effect_cards = cards["effect_cards"]
    # parse the wiki strings to list
    img_url_list = re.findall(r"image=\S+\n", effects_cards_string)
    for i, img_url in enumerate(img_url_list):
        url = img_url[len("image=") :].capitalize()
        url = base_img_url + url
        effect_cards[i]["img_src"] = url

    cards["effect_cards"] = effect_cards

    # write effect cards Python list dict to JSON file
    with open("effectCards.json", "w") as f:
        json.dump(effect_cards, f, indent=2)
    with open("cards.json", "w") as f:
        json.dump(cards, f, indent=2)


if __name__ == "__main__":
    scrape_page()
