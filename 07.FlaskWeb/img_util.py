import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

def center_img(img):
    h, w, _ = np.array(img).shape
    if h > w:
        width, height = w, w
    else : 
        width, height = h, h   
    diff = abs(h-w) // 2
    if w > h:
        final_img = np.array(img)[:,diff:diff+h]
    else:
        final_img = np.array(img)[diff:diff+w, :]
    return Image.fromarray(final_img)

def change_profile(app, filename):
    img = Image.open(filename)
    new_fname = os.path.join(app.static_folder, 'data/profile.png')
    center_img(img).save(new_fname, format='png')