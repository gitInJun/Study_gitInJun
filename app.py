from flask import Flask, render_template, url_for
import datetime as dt

app = Flask(__name__)

@app.route("/")
def mian():
    today=str(dt.datetime.today())[:10]
    return render_template('main.j2', today=today, a=1)

if __name__ == '__main__':
    app.run()