"""
Album on Flask engine
"""
import os
import re
import random
from flask import Flask, render_template

FOLDER = os.path.join('static', 'photo')
ALL_PHOTO = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER
full_filename = None

@app.route('/')
@app.route('/index')
@app.route('/album')
def show_index():
    """
    Show index
    """
    full_filename = get_random_jpg()
    return render_template("index.html", user_image = full_filename)


def find_jpg():
    """
    Find jpg
    """
    path_main = "static/photo"
    for root, _, files in os.walk(path_main):
        for fname in files:
            if re.search("favicon.png", fname):
                pass
            else:
                filename = os.path.join(path_main, fname)
                ALL_PHOTO.append(filename)
                print(f'filename: {filename}')


def get_random_jpg():
    """
    Get random jpg
    """
    if len(ALL_PHOTO) == 0:
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.png')
        print("All_PHOTO: ", len(ALL_PHOTO))
        return full_filename
    else:
        random_photo = random.randrange(0, len(ALL_PHOTO))
        return ALL_PHOTO[random_photo]


if __name__ == "__main__":
    find_jpg()
    app.run(host='0.0.0.0', port=8443, debug=True)
