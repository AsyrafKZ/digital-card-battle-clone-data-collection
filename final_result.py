import json

# cards to be updated
with open("cards.json") as f:
    cards = json.load(f)
# effect speeds to be added
with open("result.json") as f:
    effect_speeds = json.load(f)

# monster cards to be updated
monster_cards = cards["monster_cards"]
# effect speeds to be added
effect_speeds_cards = effect_speeds["cards"]

for i, card in enumerate(effect_speeds_cards):
    number = str(card["number"]).zfill(3)
    monster_cards[i]["x_effect_speed"] = card["x_speed"]
    monster_cards[i]["support_speed"] = card["support_speed"]

cards["monster_cards"] = monster_cards

# write monster cards JSON file
with open("monsterCards.json", "w") as f:
    json.dump(monster_cards, f, indent=2)
# write cards master JSON file
with open("cards.json", "w") as f:
    json.dump(cards, f, indent=2)