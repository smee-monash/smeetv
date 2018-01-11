# collect_imgs.py
#
# Usage:
# Script will search 'start_path' directory for files containing strings listed in the 
# 'file_search_key' input. It will search a certain no. of folder levels deeper based on 
# the input value of 'levels_deep' which defaults to 100.

from os import walk
import re
numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def make_img_list(file_list, search_key):
    if search_key == []:
        return file_list
    img_list = []
    for key in search_key:
        for filename in file_list:
            if filename.find(key) != -1:
                img_list.append(filename)
    return img_list


def search_dir(folder_name):
    file_list = []
    dir_list = []
    for (dirpath, dirnames, filenames) in walk(folder_name):
        file_list.extend(filenames)
        dir_list.extend(dirnames)
        break
    return (file_list, dir_list)


def collect_imgs(start_path, file_search_key=[], levels_deep=100):
    std_imgs = []
    file_list, dir_list = search_dir(start_path)
    std_imgs = make_img_list(file_list, file_search_key)
    if start_path != '.':
        std_imgs = ([start_path + img_file for img_file in std_imgs])
    if levels_deep != 0:
        if len(dir_list) != 0:
            if start_path == '.':
                start_path = ''
            for directory in dir_list:
                std_imgs += collect_imgs((start_path + directory + '/'), file_search_key, (levels_deep - 1))
    std_imgs = sorted(std_imgs, key=numericalSort)
    return std_imgs

if __name__ == "__main__":
    start_path = '.'
    file_search_key = ['.jpg', '.png']
    adv_imgs = collect_imgs(start_path, file_search_key,0)
    std_imgs = collect_imgs('smeetv/', file_search_key)
    asdf = collect_imgs('.')
    print adv_imgs
    print std_imgs

