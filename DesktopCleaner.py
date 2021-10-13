import os
from shutil import move
from time import sleep
from datetime import datetime


def moving_renamed_files(file, name, extension, path, folder):      # moving files with identical names
    original_name = path + '/' + file
    new_file = name + '1' + extension
    renamed = path + '/' + new_file
    os.rename(original_name, renamed)
    if os.path.isfile(folder + '/' + new_file):
        name, extension = os.path.splitext(new_file)
        moving_renamed_files(new_file, name, extension, path, folder)
    else:
        move(path + '/' + new_file, folder + '/' + new_file)


def moving_documents(file, name, extension, path, folder):          # basic function for moving files
    creation_date = datetime.fromtimestamp(os.path.getctime(path + '/' + file)).strftime('%Y %m').split()
    target_year_folder = folder + '/' + creation_date[0]
    target_month_folder = folder + '/' + creation_date[0] + '/' + creation_date[1]
    if not os.path.isdir(target_year_folder):
        os.mkdir(target_year_folder)
        os.mkdir(target_month_folder)
    else:
        if not os.path.isdir(target_month_folder):
            os.mkdir(target_month_folder)
    if os.path.isfile(target_month_folder + '/' + file):
        moving_renamed_files(file, name, extension, path, target_month_folder)
    else:
        move(path + '/' + file, target_month_folder + '/' + file)


def sorting_files():        # sorting files by their extensions
    path = r'C:\Users\UserName\Desktop'        # have to change to your path
    for file in os.listdir(path):
        name, ext = os.path.splitext(file)
        if ext in ('.jpg', '.gif', '.jfif', '.png'):
            folder = r'C:\Users\UserName\Pictures'         # have to change to your path
            moving_documents(file, name, ext, path, folder)

        elif ext in ('.avi', '.mp4'):
            folder = r'C:\Users\UserName\Videos'           # have to change to your path
            moving_documents(file, name, ext, path, folder)

        elif ext == '.mp3':
            folder = r'C:\Users\UserName\Music'            # have to change to your path
            moving_documents(file, name, ext, path, folder)

        elif ext in ('.txt', '.pdf', '.docx', '.doc', '.fb2', '.djvu'):
            folder = r'C:\Users\UserName\Desktop\Documents'            # have to change to your path
            moving_documents(file, name, ext, path, folder)

        elif ext == '.zip':
            folder = r'C:\Users\Admin\Desktop\Archives'           # have to change to your path
            moving_documents(file, name, ext, path, folder)


while 1:
    sorting_files()
    sleep(180)

