import time
from flask import Flask, render_template
import os
from multiprocessing import Process, Value
import random

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
ALL_PHOTO = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_20210129_193309.jpg')

@app.route('/')
@app.route('/index')
def show_index():
#    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_20210129_193309.jpg')
    full_filename = get_random_jpg()
    return render_template("index.html", user_image = full_filename)



def record_loop(loop_on):
   while True:
      if loop_on.value == True:
          print("full_filename: ", full_filename)
      time.sleep(1)


def find_jpg():
    path_main = "/home/ALL/github/python/album/static/Nastya_young_Album_1"
    path_web = "static/Nastya_young_Album_1"
    for root, _, files in os.walk(path_main):
            for fname in files:
                filename = os.path.join(path_web, fname)
                ALL_PHOTO.append(filename)
 #               print(f'filename: {filename}')
  #              time.sleep(1)


def get_random_jpg():
    random_photo = random.randrange(0, len(ALL_PHOTO))
#    for x in ALL_PHOTO:
 #       print("path: ", x, " count: ", len(ALL_PHOTO), " rand: ", random_photo)
    #print("photo: ", ALL_PHOTO[random_photo])
 #   return render_template("index.html", user_image = full_filename)
    return ALL_PHOTO[random_photo]


if __name__ == "__main__":
    find_jpg()
 #   recording_on = Value('b', True)
  #  p = Process(target=find_jpg)
   # p.start()
    app.run(host='0.0.0.0', port=10052, debug=True)
    #p.join()




