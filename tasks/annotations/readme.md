# Instruction of Data preparation and Training for trtpose
***Author: Qingrong Guo***
***Date: 2021.12.03***
---

## Part 1 -- Data preparation
### Annotation Tool
As for the annotation tool used in keypoints-annotation, the usage of *coco-annotator* will be shown as followings.
#### run *coco-annotator*
```
# open in the *Terminal*
cd /home/jetson/QingrongGUO/Data preparation/coco-annotator
sudo docker-compose up
```
The next step is to open a Browser and go to the localhost.
> localhost:5000/

The login homepage looks like the shown picture.
The default Username and password are ***probility*** and ***jetson***.
![Login_COCO-Annotator]("/home/jetson/Pictures/Login_COCO-Annotator.png")

"add folder" in the website and "add pictures" in the local folder

Then you can annotate the objects in images in the form you want like bounding box or keypoints.
When the annotation has been done, then the annotation file in json format can be exported and saved.

The json annotation file and the images are to be used for training. Before training the data needs to be preprocessed.

After use of the ***coco-annotator*** then run the codes below in the same Terminal or click the button ***ctrl + C*** to end the service.
```
sudo docker-compose down
```

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
