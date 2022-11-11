from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def test():
    return render_template('main.j2')

if __name__ == '__main__':
    app.run()