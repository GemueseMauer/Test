# Instruction of Data preparation and Training for trtpose
***Author: Qingrong Guo***
***Date: 2021.12.09***
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
More information about installation of **docker** Engine on Ubuntu > https://docs.docker.com/engine/install/ubuntu/
### 2. open coco-annotator
```
# open in the Terminal
cd /home/jetson/QingrongGUO/DataPreparation/coco-annotator
sudo docker-compose up
```

The next step is to open a Browser and go to the localhost:5000.
The login homepage looks like the shown picture.
The default Username and password are **probility** and **jetson**. ![Login Page Of COCO-Annotator](https://github.com/GemueseMauer/test/blob/main/pic/Login_COCO-Annotator.png)
### 3. create new dataset folder in coco-annotator
+ After logining in the page, you can see the green button **Create**. ![Homepage](https://github.com/GemueseMauer/test/blob/main/pic/Create_Dataset.png) Clicking this green button, you are going to initial the settings for the new folder (new dataset) (see picture). ![Create a Dataset](https://github.com/GemueseMauer/test/blob/main/pic/CreateADataset.png)
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
        sudo chmod 777 Your_Dataset_Name
        ```
    - Place all the images you want to annotate into the folder (eg. into folder **Test**)
    - Refresh the localhost page by clicking the **refresh button of the browser** or **grey button "Refresh"** near the **green button "Create"**
### 4. annotate the images
+ since all the preparation before annotation has been done, it is time to use coco-annotator to do the annotation work.
    - Click the dataset you created in the localhost in the browser (eg. **Test**). Then you will go to the similar interface where you can find the basic functions of the coco-annotator and all the images you placed in the local folder (s. picture below) 
    ![Dataset Test Starting Page](https://github.com/GemueseMauer/test/blob/main/pic/annotation%20example1.png)
    - Click one image and begin to annotate. The annotation details you could search by yourself or look into the 
    ***AnweisungZurAnnotationGabelstapler.pdf***
    > https://wwww.google.com It is recommened to click "save" each time one sinlge image has been annotated. By the way, more than one objects and one categories can also be annotated More tools including **Bounding box** and **Keypoints** can be used in the same time. (s. picture below) 
    ![Annotate one image](https://github.com/GemueseMauer/test/blob/main/pic/annotate_image.png)
    - If all the images are annotated, go back to the **Homepage** where you started with the coco-annotator after login, and click the **grey button "Export COCO"** on the left side of the page. It only needs clicking **"Export" button** after you see the Export window (eg. "Export Test")
    - Download the json annotation file in **"Exports"** in the same page by clicking the **green button "Download"** (s. picture below) 
    ![Export and download](https://github.com/GemueseMauer/test/blob/main/pic/Export.png)
After use of the ***coco-annotator*** click the button ***ctrl + C*** in the same Terminal to end the service. The json annotation file and the images are to be used for training. Before training a model the data needs to be preprocessed.
