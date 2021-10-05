import json
import trt_pose.coco
import trt_pose.models
import torch
import torch2trt

with open('forklift.json', 'r') as f:
    forklift_pose = json.load(f)

topology = trt_pose.coco.coco_category_to_topology(forklift_pose)

num_parts = len(forklift_pose['keypoints'])
num_links = len(forklift_pose['skeleton'])

model = trt_pose.models.resnet18_baseline_att(num_parts, 2 * num_links).cuda().eval()

MODEL_WEIGHTS = 'resnet18_baseline_att_224x224_A_epoch_245.pth'

model.load_state_dict(torch.load(MODEL_WEIGHTS))

WIDTH = 224
HEIGHT = 224

data = torch.zeros((1, 3, HEIGHT, WIDTH)).cuda()

model_trt = torch2trt.torch2trt(model, [data], fp16_mode=True, max_workspace_size=1<<25)

OPTIMIZED_MODEL = 'resnet18_baseline_att_224x224_A_epoch_245_trt.pth'

torch.save(model_trt.state_dict(), OPTIMIZED_MODEL)

