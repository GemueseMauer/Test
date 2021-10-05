# Differences between the experiments
### resnet18_baseline_att_224x224_A.json
images_dir: datasets/train_gs or datasets/val_gs
annotation_file: annotations/train_GS.json or annotations/val_GS.json

If you are training the model with resnet18_baseline_att_224x224_A.json, you need to adjust another coco.py in the folder "/.local/lib/python3.6/site-packages/trt_pose-0.0.1-py3.6-linux-x86_64.egg/trt_pose". This adjusted coco.py is also posted and showed in Forklift_Detection/tasks/experiments/.

### resnet18_baseline_att_224x224_A_eval.json 
Besides the log file where the train and test loss are documented, there is also an evaluation function for human pose in coco.py. I will upload the new coco.py and train.py with this evaluation function for forklift pose.

### resnet18_baseline_att_224x224_B.json
batch_size: 64

### resnet18_baseline_att_224x224_C.json
batch_size: 8

### resnet18_baseline_att_224x224_D.json
batch_size: 1
