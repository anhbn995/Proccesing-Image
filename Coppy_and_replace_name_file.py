import os, glob
from shutil import copyfile


# in ra ten các file dạng tif trong folder
def create_list_id(path):
    list_id = []
    os.chdir(path)
    for file in glob.glob("*.tif"):
        list_id.append(file)
        # print(file)
    # files = os.listdir(path)
        # print(file[:-4])

# tao nhieu folder# o day nhieu folder nen name_folders = [folder1, folder2, ...]
def make_multiple_folder(root_path, name_folders):
    os.chdir(root_path)
    for folder in name_folders:
        if os.path.isdir(folder):
            # print(folder)
            continue
        else:
            os.makedirs(folder)

# di chuyển file sang thư mục theo định dạng file
def move_file_and_rename(path_source, name_folders, str_move):
    os.chdir(path_source)
    # tạo folder de chuyen cai da
    make_multiple_folder (path_source, name_folders)

    #bat dau di chuyen file va sua ten no theo dinh dang cua coco
    for f in glob.glob("*.tif"):
        # print(file)
        if str_move in f:
            new_name_file = f.replace("_" + str_move,"")
            path_copy = os.path.join(path_source,str_move)
            copyfile(os.path.join(path_source,f), os.path.join(path_copy,new_name_file))
        else:
            continue

path_source = "/media/khoi/Data/ChangeDetection/Bangalore/Xonglaxoa"

name_folders = ["label","image","base"]
move_file_and_rename(path_source, name_folders, "image")


