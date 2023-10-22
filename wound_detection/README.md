# 🧑🏻‍⚕️ Wound AI Assistant

The Wound AI Assistant is the Module of GoldenHour Application which find Where the wound that I occured is and How can I treat these wound by myself or by anyone who has the GoldenHour Application.


## 🩸 Wound Location Detection

The Wound Location Detection is based on Mediapipe Model and Pos2Seg Models which set the posing structures on bodies and estimate the range of detected bodies. This feature is a key-feature of our models.


## 🩹 Wound Segmentation

The Wound Segmentation Model based on YOLOv8 which is the greatest one layer detection model nowadays. The Datasets I used to train custom model is below. The amounts of these datasets are 50,000 images to train.

[The Wound Datasets](https://github.com/uwm-bigdata/wound-segmentation)
<br>
[The Segmentation]


## ⚙️ How to Use on Python

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


