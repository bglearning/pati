from io import BytesIO

import json

import base64
import numpy as np
from PIL import Image

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def pati():
    if 'img' in request.form.keys():
        s = request.form['img']
        im = Image.open(BytesIO(base64.b64decode(s)))
        a = np.array(im)
        print(a.shape)
    return render_template('index.html', prediction='')


if __name__ == '__main__':
    app.run(debug=True)
