#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Flask, request
from flask import render_template

from secret import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def index():
    birthday_str = request.args.get('birthday', default='1986-06-25', type=str)
    birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
    weeks_from_now = int((datetime.now() - birthday).days / 7)
    return render_template('index.html',
                           birthday=birthday_str,
                           used_weeks=weeks_from_now)


if __name__ == '__main__':
    app.run(debug=True)