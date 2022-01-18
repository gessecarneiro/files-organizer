from json.tool import main
from ntpath import join
import os

audios_ext = ['.mp3', '.wmv']
videos_ext = ['.mp4', '.mov', '.avi', '.rmvb']
pictures_ext = ['.jpg', '.png', '.jpeg']
documents_ext = ['.txt', '.pdf', '.docx', '.log']

def get_extension(name):
    index = name.rfind('.')
    return name[index:]

def organize (dir):

    AUDIO_DIR = os.path,join(dir, "audios")
    PICTURES_DIR = os.path,join(dir, "images")
    DOCS_DIR = os.path,join(dir, "documents")
    OTHERS_DIR = os.path,join(dir, "others")
    VIDEOS_DIR = os.path,join(dir, "videos")

    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
    if not os.path.isdir(PICTURES_DIR):
        os.mkdir(PICTURES_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(OTHERS_DIR):
        os.mkdir(OTHERS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)

    name_files = os.listdir(dir)
    new_folder = ''
    for file in name_files:
        extension = str.lower( get_extension(file))
        print(file, extension)
        if extension in audios_ext:
            new_folder = AUDIO_DIR
        elif extension in videos_ext:
            new_folder = VIDEOS_DIR
        elif extension in documents_ext:
            new_folder = DOCS_DIR
        elif extension in pictures_ext:
            new_folder = PICTURES_DIR
        else:
            new_folder = OTHERS_DIR

        older_path = os.path.join(dir, file)
        new_path = os.path.join(new_folder)
        os.rename(os.path.join(dir, file), os.path.join(new_folder))
        print("Moved: ", older_path, "->", new_path)

if __name__ == '__main__':
    organize('downloads')