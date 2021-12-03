# Instruction of Data preparation and Training for trtpose
***Author: Qingrong Guo***
***Date: 2021.12.03***
***Device: Laptop of the Institute***
---

## Part 1 -- Data preparation
### Annotation Tool
As for the annotation tool used in keypoints-annotation, the usage of **coco-annotator** will be shown as followings. By the way, the **coco-annotator** doesn't work on the jetson devices. So if you want to install **coco-annotator** on a new device, it should be a not-jetson device.
### 1. download the coco-annotator (ignore when you have already this tool)
```
git clone https://github.com/jsbroks/coco-annotator.git
```
Go to the link below to see more details:
> https://github.com/jsbroks/coco-annotator
Before running **coco-annotator**, make sure that you have **docker** in your device.
More information about **docker** > https://docs.docker.com/engine/install/ubuntu/
### 2. open coco-annotator
```
# open in the Terminal
cd /home/jetson/QingrongGUO/DataPreparation/coco-annotator
sudo docker-compose up
```
The next step is to open a Browser and go to the localhost.
> localhost:5000/
The login homepage looks like the shown picture.
The default Username and password are **probility** and **jetson**.
![Login Page Of COCO-Annotator](https://github.com/GemueseMauer/test/blob/main/pic/Login_COCO-Annotator.png)
### 3. create new dataset folder in coco-annotator
+ After logining in the page, you can see the green button **Create**. Clicking this green button, you are going to set up the information for the new folder (new dataset)(see picture). ![Create a Dataset](https://github.com/GemueseMauer/test/blob/main/pic/CreateADataset.png)
    - You can type anything you want in the block **Dataset Name**. This Dataset Name will be the name of the new folder to be created.
    - Click the block of **Default Categories** to add a category. If you use the laptop of insitute, there is already an available category, namely **forklift** in blue. Click the button **forklift** in blue, this available category will be added automatically in the block. As for adding new categories, you can find **Categories** on the top of the same page. After clicking **Categories** you can create your own new categories.
    - The **Folder Directory** shows the path of the new dataset and can't be edited.
    - Click the button **Create Dataset** and a folder which has a same name as **Dataset Name** will be created. As example, a folder named **Test** has been created. The localhost page and the local folder look like the pictures shown below.
    localhost page:
    ![localhost page Test](https://github.com/GemueseMauer/test/blob/main/pic/Test_Dataset_cocoannotator.png)
    local folder:
    ![local folder Test](https://github.com/GemueseMauer/test/blob/main/pic/Test_Folder_cocoannotator.png)
    - Normally the created local folder is locked and needs to be unlocked. To unlock the folder, run followins codes in the terminal. And then check whether the folder is unlock.
    ```
    sudo chmod 777 Test
    ```
    - Place all the images you want to annotate into the folder (eg. into folder **Test**)
    - Refresh the localhost page by clicking the **refresh button of the browser** or **grey button "Refresh"** near the **green button "Create"**
### 4. annotate the images
+ since all the preparation before annotation has been done, it is time to use coco-annotator to do the annotation work.
    - Click the dataset you created in the localhost in the browser (eg. **Test**). Then you will go to the similar interface where you can find the basic functions of the coco-annotator and all the images you placed in the local folder (s. picture below) 
    ![Dataset Test Starting Page](https://github.com/GemueseMauer/test/blob/main/pic/annotation%20example1.png)
    - Click one image and begin to annotate. The annotation details you could search by yourself. It is recommened to click "save" each time one sinlge image has been annotated. By the way, more than one objects and one categories can also be annotated. More tools including **Bounding box** and **Keypoints** can be used in the same time. (s. picture below) 
    ![Annotate one image](https://github.com/GemueseMauer/test/blob/main/pic/annotate_image.png)
    - If all the images are annotated, go back to the **Dataset Test Starting Page** in the 1. Step and click the **grey button "Export COCO"** on the left side of the page. It only needs clicking **"Export" button** after you see the Export window (eg. "Export Test")
    - Download the json annotation file in **"Exports"** in the same page by clicking the **green button "Download"** (s. picture below) 
    ![Export and download](https://github.com/GemueseMauer/test/blob/main/pic/Export.png)
After use of the ***coco-annotator*** click the button ***ctrl + C*** in the same Terminal to end the service. The json annotation file and the images are to be used for training. Before training the data needs to be preprocessed.

### Data preprocessing
![Photo Name]("Photo Path")

'''
Codes
'''

```
Codes
```
> https://docs.nvidia.com/isaac/isaac/packages/skeleton_pose_estimation/doc/2Dskeleton_pose_estimation.html

Sheet1|Sheet2|Sheet3
:-----|:-----:|-----:
AlignL|AlignCT|AlignR

* This is an unordered list
* This is an unordered list
+ This is an unordered list
  - This is an unordered list
  - This is an unordered list

1. This is an ordered list
2. This is an ordered list
  2.1. This is an ordered list
  2.2. This is an ordered list
  2.3. This is an ordered list
3. This is an ordered list

## Part 2 -- Training

```
{'checkpoints': {'interval': 3},
 'color_jitter': {'brightness': 0.05,
                  'contrast': 0.05,
                  'hue': 0.01,
                  'saturation': 0.05},
 'epochs': 250,
 'lr_schedule': {'0': 0.001, '150': 1e-05, '75': 0.0001},
 'model': {'kwargs': {'cmap_channels': 12,
                      'num_upsample': 3,
                      'paf_channels': 32,
                      'upsample_channels': 256},
           'name': 'resnet18_baseline_att'},
 'optimizer': {'kwargs': {'lr': 0.001}, 'name': 'Adam'},
 'stdev_schedule': {'0': 0.025},
 'test_dataset': {'annotations_file': '/home/jetson/datapreparation/forklift_data_041121/val.json',
                  'category_name': 'forklift',
                  'image_shape': [224, 224],
                  'images_dir': '/home/jetson/datapreparation/forklift_data_041121/val/forklift',
                  'is_bmp': False,
                  'random_angle': [-0.0, 0.0],
                  'random_scale': [1.0, 1.0],
                  'random_translate': [-0.0, 0.0],
                  'stdev': 0.025,
                  'target_shape': [56, 56]},
 'test_loader': {'batch_size': 8,
                 'num_workers': 8,
                 'pin_memory': True,
                 'shuffle': True},
 'train_dataset': {'annotations_file': '/home/jetson/datapreparation/forklift_data_041121/train.json',
                   'category_name': 'forklift',
                   'image_shape': [224, 224],
                   'images_dir': '/home/jetson/datapreparation/forklift_data_041121/train/forklift',
                   'is_bmp': False,
                   'random_angle': [-0.2, 0.2],
                   'random_scale': [0.5, 2.0],
                   'random_translate': [-0.2, 0.2],
                   'stdev': 0.025,
                   'target_shape': [56, 56]},
 'train_loader': {'batch_size': 8,
                  'num_workers': 8,
                  'pin_memory': True,
                  'shuffle': True}}
```
