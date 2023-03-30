# 🧑🏻‍⚕️ CPR AI Assistant

 Currently, % of the world's population says CPR is available for training. Due to this lack of education rate, if you find a real cardiac arrest patient, they may miss a four-minute golden hour until a rescue worker arrives.

 At this time, real-time voice guidelines for effective pressure location, frequency, depth, and speed were presented to inexperienced cardiopulmonary resuscitation patients so that first aid can be performed in more situations.

## Technical Documentation

GoldenHour's CPR AI Assistant uses the Pose Detection Model provided by Mediapipe to implement the functionality.
Mediapipe is a lightweighted Pose Detection Model developed by Google Blazepose model that captures 33 human joint points with Feature Landmarks to shape the entire body.

<div align="center"> <img width="728" alt="landmarks example" src="https://user-images.githubusercontent.com/99489807/228809979-b8427253-17e6-4b4c-ab24-39db7b7d25d1.png">
</div>

## 🩻 CPR Pressing Point Detection

As stipulated by the Korea Cardiopulmonary Resuscitation Association, it is to guide the lower half of the breastbone as accurately as possible to ensure effective pressure is applied to cardiac arrest patients with cardiac arrest. We find the press point numerically by chest bone position and the scale of the body.

<div align="center"> <img width="300" alt="chest calculate image" src="https://user-images.githubusercontent.com/99489807/228807718-73d0fb4c-caa5-4660-8364-012a36e0877d.png">
</div>


### Test Python Example
```python
!git clone https://github.com/jwyeeh-dev/GoldenHour_DL/cpr_detection # clone repository

!python cpr_chest_detection.py --cam 0 #if you want to use the webcam
```


## 🤲🏻 CPR Pose Recognition

### 1. The Pressing Time



### 2. The Pressing Deep



### 3. The Arm Angle


### Test Python Example
```python
!git clone https://github.com/jwyeeh-dev/GoldenHour_DL/cpr_detection # clone repository

!python cpr_pose_correction.py --cam 0 #if you want to use the webcam
```