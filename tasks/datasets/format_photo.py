import os
import json
import shutil

file = open("Gabelstapler.json", "r")

data_json = json.load(file)

file_val = open("val_GS.json", "r")
file_train = open("train_GS.json", "r")

data_val = json.load(file_val)
data_train = json.load(file_train)

#IsExistsVal = os.path.exists("/home/pantrack/DataG/val_gs")
#IsExistsTrain = os.path.exists("/home/pantrack/DataG/train_gs")
#if not IsExistsVal:
#    os.makedirs("/home/pantrack/DataG/val_gs")
#else:
#    print("Folder val_gs exists")
#if not IsExistsTrain:
#    os.makedirs("/home/pantrack/DataG/train_gs")
#else:
#    print("Folder train_gs exists")

#print(len(data_val["annotations"]))
#print(len(data_train["annotations"]))
folder_val = "/home/pantrack/DataG/train/val_gs"
folder_train = "/home/pantrack/DataG/train/train_gs"

gs = os.walk(r"/home/pantrack/DataG/coco-annotator/datasets/Gabelstapler")
for path, dirs, files in gs:
    for file in files:
        for i in range(len(data_json["annotations"])):
            if i%8 == 0:
                if file in data_val["images"]["%i" % i]["path"]:
                    shutil.copy(os.path.join(path, file), folder_val)
            else:
                if file in data_train["images"]["%i" % i]["path"]:
                    shutil.copy(os.path.join(path, file), folder_train)

#for path, dirs, files in file_val:
#    print("number of val-photos:", len(files))
#for path, dirs, files in file_train:
#    print("number of train-photos:", len(files))


