from PIL import Image
import os, glob

DIMENSIONS = (960, 1280)
FILETYPES = ['*.jpg']


def get_pictures_from_directory(subject_path, filetypes):
    lst = []
    for extension in filetypes:
        lst.extend(glob.glob(subject_path + "/" + extension))
    return lst


def get_folders_in_curr_directory(directory):
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]


def load_and_resize_image(img_path, size_tuple):
    img = Image.open(img_path)
    img = img.resize(size_tuple)
    return (img)


def save_image(img, img_path):
    img.save(img_path)


def resize_pictures(pictures, DIMENSIONS):
    for picture in pictures:
        img = load_and_resize_image(picture, DIMENSIONS)
        save_image(img, picture)


def run_recursive_resize(base_path, DIMENSIONS, FILETYPES):
    directories = get_folders_in_curr_directory(base_path)
    pictures = get_pictures_from_directory(base_path, FILETYPES)
    resize_pictures(pictures, DIMENSIONS)
    for directory in directories:
        next_path = base_path + '/' + directory
        run_recursive_resize(next_path, DIMENSIONS, FILETYPES)


#run_recursive_resize('.', DIMENSIONS, FILETYPES)
run_recursive_resize('/home/dagmara/Projects/pytorch-yolo-v3-custom/imgs', DIMENSIONS, FILETYPES)

