'''

'''
import pytest
import sys, os
sys.path.insert(0,os.getcwd()+'/../dashboard')
sys.path.insert(0,os.getcwd()+'/../dashboard/utils')
import pickle
from PIL import Image, PngImagePlugin
from dashboard import update

def test_update_class():
    a = update.Update()
    a.save_as_pickle(parent_path=os.getcwd()+'/../dashboard/output/')

    with open (os.getcwd()+'/../dashboard/output/cache.pkl', 'rb') as f:
        d = pickle.load(f)

    img = Image.open(os.getcwd()+'/../dashboard/output/overview.png')

    assert isinstance(d, dict), 'Problems with cache!'
    assert isinstance(img, PngImagePlugin.PngImageFile), 'Error while reading the heatmap image!'
