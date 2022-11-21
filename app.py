from flask import Flask, render_template, url_for
from datetime import date, timedelta
import random

app = Flask(__name__)

@app.route("/")
def main():
    today = date.today()
    defaultStart = today - timedelta(29)
    dayLabel = list(range(1, (today - defaultStart).days + 1))
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1),]
    return render_template('main.j2', today=today, defaultStart=defaultStart, dayLabel=dayLabel, randomlist=randomlist)

@app.route("/2")
def mine():
    return render_template('cctv.j2')

if __name__ == '__main__':
    app.run()