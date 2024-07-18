# soybean_phenotype_platform

## 1. Outdoor counting model 

### 1.1 Dataset
Outdoor soybean images can be downloaded here [P2PNet-Soy](https://github.com/UTokyo-FieldPhenomics-Lab/P2PNet-Soy?tab=readme-ov-file).    
Some other images used in this study that not taken by us can be downloaded here [YOLO-Pod](https://drive.google.com/drive/folders/1-Ouj8fFG_owOnJtDDGBQ29_gDyCUdu93).    

The soybean images and detection-annotation files in our paper can be downloaded here [Normal dataset](https://drive.google.com/file/d/1pe8Yg5W6oVnYMZ3dHseLVEUQxmblPWai/view?usp=drive_link), [Domain adaptation dataset](https://drive.google.com/file/d/1PmQALeJxR7hxE7UHhgGxQfSc0xXBSHec/view?usp=drive_link).    

You may need to place the images from other studies into the downloaded dataset's right image folder (corresponding to the annotation files in the training and evaluation sets).    
Corresponding annotation files can be find in this repository (yolo_soybean/datasets).      

### 1.2 Training and inference
Use YOLOv8_for_soybean.ipynb, YOLOv8_SAM.ipynb, YOLOv8_DA_for_soybean.ipynb at /yolo_soybean/ultralytics/ to train and inference the YOLOv8, YOLOv8-SAM, YOLOv8-DA, respectively.     

Pretrained checkpoints can be downloaded here [Dropbox](https://www.dropbox.com/scl/fo/ygb9mj1mdsn4cq1pfk0hf/AAwF2KBuQbnID3n1bqDD0Os?rlkey=ulj4zy49uawqn3iv2jp1ti7va&st=x886gxqh&dl=0).    
Specifically, high-quality segment-anything model can be downloaded from [Github HQ-SAM](https://github.com/SysCV/sam-hq). 

## 2. Indoor counting model 

### 2.1 Dataset
The real soybean images and instance segmentation annotations can be downloaded here [Google Drive](https://drive.google.com/file/d/1YOhUsZsPdHPEJT0AGEmSayO4n_Lhhfsh/view?usp=drive_link).    
You can use Simulation/main.py to generate more data for training.

### 2.2 Checkpoints
The Mask-RCNN checkpoints can be downloaded here [Dropbox]().    
The Swin-Transformer checkpoints can be  downloaded here [Dropbox](https://www.dropbox.com/scl/fi/7l7p008hymq8lj3w7x0tp/SwinTrans_soybean_podnum.pth?rlkey=4ni2slgtl95m47l77lxkphxky&st=asei33ui&dl=0).

