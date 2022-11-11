from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/for")
def hello():
    return render_template('index.j2', title = 'Hello jinja!')

@app.route("/")
def test():
    return render_template('SoCowNet.j2', title = 'SO COWNET')

if __name__ == '__main__':
    app.run()