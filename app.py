from flask import Flask, render_template, url_for
from datetime import date, timedelta
import datetime

app = Flask(__name__)

@app.route("/")
def main():
    today = date.today()
    earlyMonth = date(today.year, today.month, 1)
    dayLabel = list(range(1, (today - earlyMonth).days + 2))
    now = datetime.datetime.now()
    return render_template('main.j2', today=today, earlyMonth=earlyMonth, dayLabel=dayLabel, now=now)

if __name__ == '__main__':
    app.run()