import json
import trt_pose.coco 
import torch
from torch2trt import TRTModule
import trt_pose.models
import cv2
import torchvision.transforms as transforms
import PIL.Image
from trt_pose.draw_objects import DrawObjects
from trt_pose.parse_objects import ParseObjects
import argparse


def preprocess(image):
    global device
    device = torch.device('cuda')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = PIL.Image.fromarray(image)
    image = transforms.functional.to_tensor(image).to(device)
    image.sub_(mean[:, None, None]).div_(std[:, None, None])
    return image[None, ...]

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def read_camera(cam):
	if cam == "csi":
		return cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
	else :
		return cv2.VideoCapture(0)
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Insert model path, tolopogy path, and camera profile.")
	parser.add_argument('model_path', type=str)
	parser.add_argument('topology_path', type=str)
	parser.add_argument('camera', type=str)
	args = parser.parse_args()	
	OPTIMIZED_MODEL = args.model_path
	topology_file = args.topology_path
	cam = args.camera

	WIDTH = 224
	HEIGHT = 224
	# topology
	print("loading topology...")
	with open('forklift.json', 'r') as f:
		forklift = json.load(f)

	topology = trt_pose.coco.coco_category_to_topology(forklift)
	print("topology loaded...")
	
	# # Each model takes at least two parameters, cmap_channels and paf_channels corresponding to the number of heatmap channels and part affinity field channels. The number of part 	affinity field channels is 2x the number of links, because each link has a channel corresponding to the x #and y direction of the vector field for each link. 
	# num_parts = len(forklift['keypoints'])
	# num_links = len(forklift['skeleton'])

	# model = trt_pose.models.resnet18_baseline_att(num_parts, 2 * num_links).cuda().eval()

	###
	parse_objects = ParseObjects(topology)
	draw_objects = DrawObjects(topology)

	# # load the model weights
	# MODEL_WEIGHTS = 'resnet18_baseline_att_224x224_A_epoch_249.pth'
	# model.load_state_dict(torch.load(MODEL_WEIGHTS))

	# # use torch2trt to optimize the model
	# model_trt = torch2trt.torch2trt(model, [data], fp16_mode=True, max_workspace_size=1<<25)

	# # save the optimized model
	# OPTIMIZED_MODEL = 'resnet18_baseline_att_224x224_A_epoch_249_trt.pth'
	# torch.save(model_trt.state_dict(), OPTIMIZED_MODEL)

	# load model
	print("loading model...")
	model_trt = TRTModule()
	model_trt.load_state_dict(torch.load(OPTIMIZED_MODEL))
	print("model loaded...")


	mean = torch.Tensor([0.485, 0.456, 0.406]).cuda()
	std = torch.Tensor([0.229, 0.224, 0.225]).cuda()
	device = torch.device('cuda')
	
	# cap = read_camera(cam)
	cap = cv2.VideoCapture('Bc_YT_6K_416.avi')
	frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	if cap.isOpened():
		window_handle = cv2.namedWindow("Camera", cv2.WINDOW_AUTOSIZE)
		# Window
		while cv2.getWindowProperty("Camera", 0) >= 0:
		    t0 = time.time()
		    ret, frame = cap.read()
		    if ret:
		        # detection process
		        frame = cv2.resize(frame, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
		        data = preprocess(frame)
		        cmap, paf = model_trt(data)
		        cmap = cmap.detach().cpu()
		        paf = paf.detach().cpu()
		        counts, objects, peaks = parse_objects(cmap, paf)
		        draw_objects(frame, counts, objects, peaks)
		        frame = cv2.resize(frame, (1920, 1080))
		        t1 = time.time()
		        FPS = (1 / (t1 - t0))
		    cv2.putText(frame, 'FPS = %.2f' % FPS, (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 5)
		    cv2.imshow("Camera", frame)
		    cv2.moveWindow("Camera", 0, 0)
		    keyCode = cv2.waitKey(30)
		    if keyCode == ord('q'):
		    	break
		cap.release()
		cv2.destroyAllWindows()
	else:
		print("Unable to open camera")




