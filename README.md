# Forklift_Detection

### Step 1 - Install dependency
1. Install OpenCV. Refer [this link](https://automaticaddison.com/how-to-install-opencv-4-5-on-nvidia-jetson-nano/) to install opencv in jetson nano 

2. Install PyTorch and Torchvision.  To do this on NVIDIA Jetson, we recommend following [this guide](https://forums.developer.nvidia.com/t/72048)

3. Install [torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt)

    ```python
    git clone https://github.com/NVIDIA-AI-IOT/torch2trt
    cd torch2trt
    sudo python3 setup.py install --plugins

4. Install other miscellaneous packages

    ```python
    sudo pip3 install tqdm cython pycocotools
    sudo apt-get install python3-matplotlib
    
### Step 2 - Install trt_pose

```python
git clone https://github.com/Probility/Forklift_Detection.git
cd trt_pose
sudo python3 setup.py install    
```

### Step 3 - Forklift
variable : 
1. model file name : see **readme.txt** in folder `tasks/`, download and put it in the `tasks/` folder
2. topology file name - default: forklift.json
3. camera : "csi" or 0 for csi camera or usb camera

live-video detection
```
cd tasks/fork_lift
python3 detect.py <<model file name>> forklift.json <<camera>> 
```
My environment:
GeForce RTX 2060

python == 3.9.7
torch == 1.9.1
torchvision == 0.10.1
torchaudio == 0.9.0
Cuda == 11.1.74

### Step 4 - Train
```
cd tasks/
python3 -m trt_pose.train experiments/resnet18_baseline_att_224x224_A.json
```
After the training a model will be created. The name of the model would be like **epoch_498.pth**
Then it is necessary to transform epoch_498.pth to **epoch_498_trt.pth** using **torch2trt.py** in the `tasks/` folder.
Attention: the names, which depends on your train settings, of **MODEL_WEIGHTS** and **OPTIMIZED_MODEL** should also be changed in torch2trt.py.
```
cd tasks/
python3 torch2trt.py
```

