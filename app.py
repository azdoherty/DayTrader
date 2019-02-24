from flask import Flask, render_template
import datetime
import util

app = Flask(__name__)


@app.route("/")
def index():
    date = '{0:%Y-%m-%d %H:%M:%S}' .format(datetime.datetime.now())
    return render_template("index.html",
                           date=date)

@app.route("/chart")
def chart():
    return render_template("chart.html")




if __name__ == '__main__':
    app.run(debug=True)