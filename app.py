from flask import Flask, render_template, request, jsonify
import datetime
import util
import pandas as pd
app = Flask(__name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


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
    labels = data.formatted_index
    values = data.asset_data['close'].values
    #labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    #values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template("chart.html",
                           symbol="MSFT",
                           values=values,
                           labels=labels)


@app.route("/symbol/<string:symbol>", methods=["POST"])
def get_asset_data(symbol):
    errors = []
    try:
        args = request.args
        if "start" in args:
            start = pd.to_datetime(args['start'], format="%Y-%m-%d")
        else:
            raise InvalidUsage("Start date not defined")
        if "stop" in args:
            stop = pd.to_datetime(args["stop"], format="%Y-%m-%d")
        else:
            raise InvalidUsage("Stop date not defined")
        data = util.Asset("MSFT", start=start, stop=stop)

        # dictionary to return as json
        r = {"symbol": symbol,
             "data": data.asset_data['close'].values.tolist(),
             "labels":  data.formatted_index.tolist()}

        return jsonify(r), 200
    except Exception as e:
        errors.append(str(e))
        return jsonify(errors), 400





if __name__ == '__main__':
    app.run(debug=True)