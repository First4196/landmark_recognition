#!/usr/bin/python

# Note to Kagglers: This script will not run directly in Kaggle kernels. You
# need to download it and run it on your local machine.

# Downloads images from the Google Landmarks dataset using multiple threads.
# Images that already exist will not be downloaded again, so the script can
# resume a partially completed download. All images will be save in the same format as source

######### Only use this if LD don't work properly ##########

import sys, os, multiprocessing, csv
from PIL import Image
from io import BytesIO
from urllib.request import urlretrieve

########## EDIT CONFIG HERE ##########
CSV = 'ltrain.csv'
outputFolder = 'E:/train'
########## EDIT CONFIG HERE ##########

def ParseData(data_file):
  csvfile = open(data_file, 'r')
  csvreader = csv.reader(csvfile)
  key_url_list = [line[:2] for line in csvreader]
  return key_url_list[1:]  # Chop off header


def DownloadImage(key_url):
    (key, url) = key_url
    print('downloading: ' + str(key))
    out_dir = outputFolder
    filename = os.path.join(out_dir, '%s.jpg' % key)

    if os.path.exists(filename):
        print('Image %s already exists. Skipping download.' % filename)
        return
    try:
        urlretrieve(url, filename)
    except:
        print('Warning: Could not download image %s from %s' % (key, url))
        return
    print('done: ' + str(key))

def Run():
    data_file = CSV
    out_dir = outputFolder

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    key_url_list = ParseData(data_file)
    pool = multiprocessing.Pool(processes=50)
    pool.map(DownloadImage, key_url_list)

if __name__ == '__main__':
    Run()
