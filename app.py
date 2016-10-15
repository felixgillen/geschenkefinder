#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    #if req.get("result").get("action") != "other.help":
    #    return {}
    result = req.get("result")
    parameters = result.get("parameters")
    # zone = parameters.get("shipping-zone")

    #cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':400, 'Africa':500}

    #speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."

    speech = "Der Test hat funktioniert."

    print("Response:")
    print(speech)

    slack_message = {
        "text": speech,
        "attachments": [
            {
                "title": "Beispieltitle",
                "title_link": "Beispieltitle",
                "color": "#36a64f",

                "fields": [
                    {
                        "title": "Condition",
                        "value": "Temp ",
                        "short": "false"
                    },
                    {
                        "title": "Wind",
                        "value": "Speed:",
                        "short": "true"
                    },
                    {
                        "title": "Atmosphere",
                        "value": "Humidity ",
                        "short": "true"
                    }
                ]
            }
        ]
    }


    return {
        "speech": speech,
        "displayText": speech,        
        "data": {"slack": slack_message },
        "source": "coupies-bot"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
