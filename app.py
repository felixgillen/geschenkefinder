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
    if req.get("result").get("action") != "present.query":
        return {}

    result = req.get("result")
    parameters = result.get("parameters")
    age = parameters.get("age")
    gender = parameters.get("gender")
    occasion = parameters.get("occasion")


    speech = "Wie wäre es hiermit: https://www.amazon.de/dp/B01IFHL5J4/"

    facebook_message =  {
        "message": {
            "text":"hello, world!"
          }
        "buttons":[
            {
                "type":"postback",
                "title":"Bookmark Item",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
            }
        ]
    }


    return {
        "speech": speech,
        "displayText": speech,        
        "data": {"facebook": facebook_message },
        "source": "coupies-bot"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
