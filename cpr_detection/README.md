# 🧑🏻‍⚕️ CPR AI Assistant

 Currently, % of the world's population says CPR is available for training. Due to this lack of education rate, if you find a real cardiac arrest patient, they may miss a four-minute golden hour until a rescue worker arrives.

 At this time, real-time voice guidelines for effective pressure location, frequency, depth, and speed were presented to inexperienced cardiopulmonary resuscitation patients so that first aid can be performed in more situations.

## Technical Documentation

GoldenHour's CPR AI Assistant uses the Pose Detection Model provided by Mediapipe to implement the functionality.
Mediapipe is a lightweighted Pose Detection Model developed by Google Blazepose model that captures 33 human joint points with Feature Landmarks to shape the entire body.

<div align="center"> <img width="728" alt="landmarks example" src="https://user-images.githubusercontent.com/99489807/228809979-b8427253-17e6-4b4c-ab24-39db7b7d25d1.png"> </div>

And We determined that this model fits into the our solution which means that it is useful to implement the on-device model interface. The BlazePose model is not only lightweighted model, but also very high correctness to detect landmark features. And this is the reference of that reason to decide to use.

<div align="center"> <img width="500" alt="Blazepose model structure" src="https://user-images.githubusercontent.com/99489807/228817430-9649f5cd-c853-4aea-a498-a8b9ad5113eb.png"> </div>

<div align="center"> <img width="500" alt="model accuracy" src="https://user-images.githubusercontent.com/99489807/228817783-da324aba-f623-40f9-be4e-50213fa58950.png"> </div>

## 🩻 CPR Pressing Point Detection

As stipulated by the Korea Cardiopulmonary Resuscitation Association, it is to guide the lower half of the breastbone as accurately as possible to ensure effective pressure is applied to cardiac arrest patients with cardiac arrest. We find the press point numerically by chest bone position and the scale of the body.

<div align="center"> <img width="300" alt="chest calculate image" src="https://user-images.githubusercontent.com/99489807/228807718-73d0fb4c-caa5-4660-8364-012a36e0877d.png"> </div>


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

### Usage
1. Run main file to start the application.

    A. If you want to run cpr pose assistant, Run **cpr_main.py** to start the application:
    ```css
    python cpr_main.py
    ```

    B. If you want to run pressing point finder, Run **chest_point_main.py** to start the application:
    ```css
    python chest_point_main.py
    ```

2. The application will automatically access your camera and start detecting CPR performance. If you want to use a different camera, modify the parameter of cv2.VideoCapture() in **cpr_main.py** and **chest_point_main.py**.

3. To exit the application, press Esc key.

### References
1. MediaPipe Pose: https://google.github.io/mediapipe/solutions/pose
2. "Cardiopulmonary resuscitation (CPR)" by American Heart Association: https://www.heart.org/en/health-topics/cardiac-arrest/cpr-and-aeds/cardiopulmonary-resuscitation-cpr