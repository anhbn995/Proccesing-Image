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
    for folder in name_folders:
        if os.path.isdir(os.path.join(root_path,folder)):
            # print(folder)
            continue
        else:
            os.makedirs(os.path.join(root_path,folder))
# root_path = "F:"
# folder = ["lol","xoa","tao"]
# make_multiple_folder(root_path,folder)

# di chuyển file sang thư mục theo định dạng file
def move_file_and_rename(path_source, name_folders, str_move):
    # tạo folder de chuyen cai da
    make_multiple_folder (path_source, name_folders)

    #bat dau di chuyen file va sua ten no theo dinh dang cua coco
    for file in glob.glob(path_source + "\*.tif"):
        if str_move in file:
            new_name_file = file.replace("_" + str_move,"")
            print(str_move)
            print(os.path.join(path_source, str_move, new_name_file))
            # copyfile(os.path.join(path_source,file), os.path.join(path_source,str_move,new_name_file))
        else:
            continue

path_source = r"F:\Xoa\Xoatiep"
# path_destination = "F:\Xoatiep", path_destination

# move_file_and_rename(path_source, path_destination)
name_folders = ["label","image","base"]
move_file_and_rename(path_source, name_folders, "label")


