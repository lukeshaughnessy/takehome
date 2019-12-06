#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json

import redis
from flask import Flask, request
from typing import Text, Optional, Dict, Any

app = Flask(__name__)


def get_current_user() -> Optional[Dict[Text, Any]]:
    """Retrieve the current user from intermediate storage."""

    red = redis.StrictRedis(host="redis", port=6379, db=1)
    encoded_user = red.get("user")
    if encoded_user:
        return json.loads(encoded_user)
    else:
        return None


def store_user(user: Dict[Text, Any]) -> None:
    """Store a users details to our intermediate storage."""

    red = redis.StrictRedis(host="redis", port=6379, db=1)
    red.set("user", json.dumps(user))


@app.route('/', methods=["GET"])
def greet():
    """Send a welcoming message to the user."""

    user = get_current_user()
    if user is not None:
        return "Hello, {}!".format(user.get("name"))
    else:
        return "Hello, unknown stranger!"


@app.route('/', methods=["POST"])
def save_name():
    """Change a users details, most importantly his name."""

    user = request.json
    store_user(user)
    return "I'll try to remember your name, {}!".format(user.get("name"))
