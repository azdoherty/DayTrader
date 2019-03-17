from flask import Flask, render_template
import datetime
import util
import pandas as pd
app = Flask(__name__)


@app.route("/")
def index():
    date = '{0:%Y-%m-%d %H:%M:%S}' .format(datetime.datetime.now())
    return render_template("index.html",
                           date=date)

@app.route("/chart")
def chart():
    start = pd.to_datetime("2018-01-02", format="%Y-%m-%d")
    stop = pd.to_datetime("2019-02-18", format="%Y-%m-%d")
    data = util.Asset("MSFT", start=start, stop=stop)
    return render_template("chart.html", symbol="MSFT", values=data.asset_data['close'].values)




if __name__ == '__main__':
    app.run(debug=True)