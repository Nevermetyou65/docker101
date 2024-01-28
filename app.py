from flask import Flask, render_template
import os
import random

app = Flask(__name__)
images = [
    "https://i.gifer.com/3tA6.gif",
    "https://i.gifer.com/Awch.gif",
    "https://i.gifer.com/WJRx.gif",
    "https://i.gifer.com/Jnt.gif",
    "https://i.gifer.com/8ExH.gif",
    "https://i.gifer.com/7m0v.gif",
    "https://i.gifer.com/S67E.gif",
    "https://i.gifer.com/Pvm.gif",
    "https://i.gifer.com/D85T.gif",
    "https://i.gifer.com/E3TW.gif",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
