# Instruction of Data preparation and Training for trtpose
***Author: Qingrong Guo***

***Date: 2021.12.03***
---

## Part 1 -- Data preparation
![Photo Name]("Photo Path")

'''
Codes
'''

```
Codes
```

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
  2.1 This is an ordered list
  2.2 This is an ordered list
  2.3 This is an ordered list
3. This is an ordered list

## Part 2 -- Training

'''
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
'''
