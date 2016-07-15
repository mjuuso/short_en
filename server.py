import string
import random
import sys
from short_en import Shortener
from flask import Flask, redirect

app = Flask("short_en")
shortener = Shortener(sys.argv[1])


@app.route("/create/<path:url>")
def create(url):
    return shortener.create(url)


@app.route("/<key>")
def shorted(key):
    u = shortener.find(key)
    return redirect(u if u else sys.argv[2])


@app.route("/")
def redir_home():
    return redirect(sys.argv[2])


if __name__ == "__main__":
    app.run()
