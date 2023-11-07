# 🧑🏻‍⚕️ Wound AI Assistant

The Wound AI Assistant is the Module of GoldenHour Application which find Where the wound that I occured is and How can I treat these wound by myself or by anyone who has the GoldenHour Application.


## 🩸 Wound Location Detection

The Wound Location Detection is based on Mediapipe Model and Pos2Seg Models which set the posing structures on bodies and estimate the range of detected bodies. This feature is a key-feature of our models.


## 🩹 Wound Segmentation

The Wound Segmentation Model based on YOLOv8 which is the greatest one layer detection model nowadays. The Datasets I used to train custom model is below. The amounts of these datasets are 50,000 images to train.

[The Wound Datasets](https://github.com/uwm-bigdata/wound-segmentation)
<br>
[The Segmentation]
<br>


## Getting Started
### Prerequisites
- Python 3.6+
- mediapipe 0.8.3.1+
- opencv-python 4.5.1.48+
- numpy 1.19.3+

### Installation

1. Clone the repository:
```css
git clone https://github.com/jwyeeh-dev/CPR-detection.git
```

2. Install the required packages:
```css
pip install -r requirements.txt
```


### ⚙️ Usage on Python

1. If you want to use by basic usage, then you write this commands and try it!

```bash
$ cd wound_detection
$ python main.py 
```

2. If you want to use by your custom usages, then you add the arguments which you want to choose. The arguments of this module is below.

```python
parser = add_arguments(
  
)
```


### References
1. MediaPipe Pose: https://google.github.io/mediapipe/solutions/pose
2. Pose2Seg : https://arxiv.org/abs/1803.10683

