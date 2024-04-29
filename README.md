

# Applied Computer Vision Project
This is a repository that contains Applied Computer Vision class's Project 

# Contributers
- Ahishakiye Eric
- Ishimwe Benjamin Mukapa
- Harerimana Kevin
- Kwizera Jean De Dieu
- Izera Pacific

This repository contains the necessary files for running a computer vision model using YOLOv5. Below is the structure of the project folder and descriptions of its contents.

## Folder Structure

- **requirements.txt** - This file lists all the Python libraries that need to be installed to run the project.
- **yolov5_best_weights.pt** - The pre-trained YOLOv5 weights optimized for our specific computer vision task.
- **Dehaze.py** - The main Python script that executes the model using the test images and the provided weights.
- **test_images/** - This folder contains the images used for testing the model.

## Important Notes

- Before running `Dehaze.py`, please ensure you have installed all the necessary libraries listed in `requirements.txt`. You can install these by running the following command in your terminal:
  ```
  pip install -r requirements.txt
  ```
- However, you need to install the Pysseract and change the Path to The exe file located at the top cell
  
- Place all test images inside the `test_images` folder. The script `Dehaze.py` is configured to read images from this directory.

## Running the Script

To execute the main script, use the following command:
```
python main_script.py
```

This will process the images in the `test_images` folder using the YOLOv5 model and output the results.

---

## Algorithms
- Single Image Haze Removal Using Dark Channel Prior, Kaiming He, Jian Sun, and Xiaoou Tang", in CVPR 2009
- Guided Image Filtering, Kaiming He, Jian Sun, and Xiaoou Tang", in ECCV 2010.


