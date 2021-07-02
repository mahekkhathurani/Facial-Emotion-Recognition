# Facial-Emotion-Recognition using CNN
## Introduction

This project aims to classify the emotion on a person's face into one of **seven categories**, using deep convolutional neural networks. The model is trained on the **FER-2013** dataset which was published on International Conference on Machine Learning (ICML). This dataset consists of 35887 grayscale, 48x48 sized face images with **seven emotions** - angry, disgusted, fearful, happy, neutral, sad and surprised.

## Dependencies

* Python 3, [OpenCV](https://opencv.org/), [Tensorflow](https://www.tensorflow.org/)

## Basic Usage

The repository is currently compatible with `tensorflow-2.0` and makes use of the Keras API using the `tensorflow.keras` library.

* To train the model, use:  

```bash
cd src
python emotions.py --mode train
```

* To run the model, use:  

```bash
cd src
python emotions.py --mode display
```

* The folder structure is of the form:  
  src:
  * data (folder)
  * emojis (folder)
  * resized.png (background image)
  * `dataset_prepare.py` (file)
  * `emotions.py` (file)
  * `haarcascade_frontalface_default.xml` (file)
  * `model.h5` (file)
  * `test.py` (GUI file)

* This implementation by default detects emotions on all faces in the webcam feed. With a simple 4-layer CNN, the test accuracy reached 63.2% in 50 epochs.

## Accuracy plot:

![image](https://user-images.githubusercontent.com/72668413/124304063-d6bdec80-db80-11eb-8904-22b723c2674f.png)


## Data Preparation

The original FER2013 dataset in Kaggle is available as a single csv file. This csv file consists of pixel coordinates of all images. We have converted it into a dataset of images in the PNG format for training/testing. The training and testing folders contain 7 subfolders of 7 emotions each. The training set consists of 28,709 examples. The public test set used for the leaderboard consists of 3,589 examples.

## Algorithm

* First, the **haar cascade** method is used to detect faces in each frame of the webcam feed.

* The region of image containing the face is resized to **48x48** and is passed as input to the CNN.

* The network outputs a list of **softmax scores** for the seven classes of emotions.

* The emotion with maximum score is displayed on the screen.

## Output
The following are the features of the final application:
1) Real-time emotion recognition.
2) A graph showing the percentage of prediction of the different emotions shown by the user.
3) An emoji of the predicted emotion 

GUI:

![image](https://user-images.githubusercontent.com/72668413/124303666-54352d00-db80-11eb-9eba-5cc93894296e.png)

Surprised Face:

![image](https://user-images.githubusercontent.com/72668413/124303754-6fa03800-db80-11eb-826e-2564c6a16a7c.png)

Similarly, the remaining 6 emotions are also detected.

##  Technologies Used
* Front-end: Tkinter

* Face Detection: Haar Cascades, OpenCV

* Emotion Recognition: Tensorflow, Keras, CNN
