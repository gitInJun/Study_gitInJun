from flask import Flask, render_template, url_for
from datetime import date, timedelta
import random

app = Flask(__name__)

@app.route("/")
def main():
    today = date.today()
    earlyMonth = date(today.year, today.month, 1)
    dayLabel = list(range(1, (today - earlyMonth).days + 2))
    randomlist = [random.choices(range(100, 200), k=(today - earlyMonth).days + 1), random.choices(range(100, 200), k=(today - earlyMonth).days + 1), random.choices(range(100, 200), k=(today - earlyMonth).days + 1), random.choices(range(100, 200), k=(today - earlyMonth).days + 1), random.choices(range(100, 200), k=(today - earlyMonth).days + 1),]
    return render_template('main.j2', today=today, earlyMonth=earlyMonth, dayLabel=dayLabel, randomlist=randomlist)

@app.route("/mine")
def mine():
    return render_template('mine.j2')

if __name__ == '__main__':
    app.run()