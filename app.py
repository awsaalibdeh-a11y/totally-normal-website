import os
import random

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Common questions. The answers are wrong on purpose.
QUESTIONS = [
    ("Is this website real?", "Mostly. About 40 percent."),
    ("Why is everything flashing?", "It is not flashing. You are blinking wrong."),
    ("How do I leave?", "You do not. You have always been here."),
    ("What does this website do?", "It exists. Some days that is enough."),
    ("Where are the buttons?", "Everywhere. Especially the one that is running away from you."),
    ("Who made this?", "Me, Aws. All of it. On purpose, which makes it worse."),
    ("Is it safe?", "It has never hurt anyone, except your eyes."),
    ("Can I get a refund?", "You paid nothing, so we are giving you nothing back. Very fair."),
    ("Why is the font like that?", "We asked a committee of pigeons."),
    ("What is the meaning of life?", "42. Or a sandwich. We are still arguing."),
    ("How many clicks until something happens?", "Between 1 and 9000. Good luck."),
    ("Why does the cursor have a tail?", "It escaped from a cat."),
]

FACTS = [
    "A group of flamingos is called a flamboyance, and none of them paid for this website.",
    "Bananas are slightly radioactive, like this page's design choices.",
    "Octopuses have three hearts and zero opinions about fonts.",
    "The shortest war in history lasted 38 minutes. Your visit here is already longer.",
    "Honey never spoils. This website already has.",
    "A day on Venus is longer than its year. Time is fake. Click something.",
    "Cows have best friends and get stressed when separated. Be nice to your cows.",
    "There are more possible chess games than atoms in the universe. We still lost.",
    "Wombat poop is cube-shaped. You are welcome.",
    "Sharks are older than trees. Trees are not bothered.",
]

NAMES = ["Sir Bonkers", "Captain Soup", "Dave (the real one)", "Lord Spoon", "Princess Toast", "Gary", "The Unnamed Goose", "Professor Noodle"]
EXCUSES = [
    "The server is on a tea break.", "A pigeon sat on the wifi.", "Mercury is in a weird mood.",
    "Someone typed 'sudo please'.", "The internet is full, try again after emptying it.", "We lost it. It was right here a second ago.",
]


@app.get("/")
def home():
    return render_template("index.html", questions=QUESTIONS)


BALL = ["Maybe. Ask a duck.", "Absolutely not, probably.", "The ball is thinking. Come back in 3 years.", "Yes, but also no.", "Outlook cloudy with a chance of soup.", "Ask again but louder.", "Definitely. Or the opposite.", "The ball has no comment."]
POTATO = ["Hello. I am a potato. This is all I know.", "Have you tried being a potato?", "I have eyes but I cannot see. Relatable.", "Mash me. I dare you.", "I was going to say something wise but I forgot.", "Roots are important. So is gravy.", "I have been underground a lot. It is fine.", "Fries are my cousins. We do not talk about it."]
HORO = ["Today you will find something. Probably your keys. Possibly a sandwich.", "A stranger will wave at you. Wave back, it is polite.", "Mercury is in retrograde, which is a lot of words for nothing.", "You will click a button today. Bold of me to predict that.", "Great fortune awaits, but only if you drink some water.", "Someone is thinking of you. It might be a pigeon.", "Avoid decisions involving glitter."]


def _pick(items):
    return jsonify(text=random.choice(items))


@app.get("/api/8ball")
def ball():
    return _pick(BALL)


@app.get("/api/potato")
def potato():
    return _pick(POTATO)


@app.get("/api/horoscope")
def horoscope():
    return _pick(HORO)


@app.get("/api/random")
def random_thing():
    return jsonify(fact=random.choice(FACTS), name=random.choice(NAMES), excuse=random.choice(EXCUSES),
                   number=random.randint(-9999, 9999), hue=random.randint(0, 360))


@app.get("/health")
def health():
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5155)))
