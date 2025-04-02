"""
Album on Flask engine
"""
import os
import re
import random
from flask import Flask, render_template

FOLDER = os.path.join('static', 'photo')
PATH_MAIN = os.path.join(os.path.dirname(__file__), 'static', 'photo')
ALL_PHOTO = []
full_photo_name = None

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER

@app.route('/')
@app.route('/index')
@app.route('/album')
def show_index():
    """
    Show index
    """
    full_photo_name = get_random_jpg()
    return render_template("index.html", user_image = full_photo_name)


def find_jpg():
    """
    Find jpg
    """
    print("Search PATH_MAIN: ", PATH_MAIN)
    for root, _, files in os.walk(PATH_MAIN):
        for fname in files:
            # print("fname: ", fname)
            if re.search("favicon.png", fname):
                pass
            else:
                full_photo_name = os.path.join(FOLDER, fname)
                ALL_PHOTO.append(full_photo_name)
                # print(f'full_photo_name: {full_photo_name}')


def get_random_jpg():
    """
    Get random jpg
    """
    if len(ALL_PHOTO) == 0:
        full_photo_name = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.png')
        random_photo = 0
        ALL_PHOTO.append(full_photo_name)
    else:
        random_photo = random.randrange(0, len(ALL_PHOTO))

    print("Count All_PHOTO: ", len(ALL_PHOTO))

    return ALL_PHOTO[random_photo]


if __name__ == "__main__":
    find_jpg()
    app.run(host='0.0.0.0', port=8443, debug=True)
