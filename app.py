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

    speech = "Wie kann ich dir helfen"

    print("Response:")

    slack_message = {
        "text": "Wie kann ich dir helfen",
        "attachments": [
            {
				"text": "zum Beispiel so",
            	"color": "#3AA3E3",
            	"actions": [
                	{
                    "name": "Rezepte",
                    "text": "Zeige mir Rezepte",
                    "type": "button",
                    "value": "rezept"
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
