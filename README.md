# ⏱️️ 2023 Solution Challenge : Golden Hour ⏱️

## What is Golden Hour ?
Many types of natural disasters are now five times more common in the world than they were 50 years ago. Each year, an increasing number of people are injured or killed by natural disasters.

One of the reasons for the high number of casualties is the "lack of information for proper first aid and safety guides".

To solve this problem, we created Golden Hour, an app that provides safety guides and first aid instructions.
> ### The Meaning of Golden Hour
> The first hour after the occurrence of a traumatic injury, considered the most critical for successful emergency treatment.

## Feature
### Safety Guides
- It provides a slide webtoon format using images and text to show how to respond to emergencies we may encounter, such as CPR and airway obstruction. 
- It provides CPR compression points using MLKit Pose Detection to assist in effective CPR.
- It provides hemostasis points based on TFlite Object Detection to assist in hemostasis in case of bleeding.

### Disaster Behavior Tips
- Based on the disaster message, the slide webtoon format using images and text to provide actions that correspond to the current disaster situation.
- Users can carefully check their pre-set emergency contacts and relief supplies through the checklist.

### Emergency Report
- It provides a button to call the police, fire, or civil authorities to make a quick report.
- It provides the current user's location so that it can be utilized in reporting.
- The question/answer format allows users to quickly and easily fill out the necessary information to submit an emergency text report.

### Safety Map
- It provides the location of safety amenities based on the user's current location utilizing Google Maps. 
- Safety amenities provided include hospitals/emergency rooms, pharmacies, AEDs, fire extinguishers, shelters, and transitional housing.

## Demo Video

<a href="유튜브 링크"><img width="755" src="https://user-images.githubusercontent.com/68090939/228529082-1306ec5d-6bff-4296-b5ba-8a3cc807b88c.png"/></a>


## Team Member
<table algin="center">
   <tr>
      <td colspan="2" align="center"><strong>Android</strong></td>
      <td colspan="1" align="center"><strong>Back-End</strong></td>
      <td colspan="1" align="center"><strong>ML</strong></td>
   </tr>
  <tr>
     <td align="center">
        <a href="https://github.com/100SongH"><img src="https://avatars.githubusercontent.com/u/88391162?v=4" width="150px" alt="백송희"/><br /><sub><b>백송희</b></sub></a>
     </td>
    <td align="center">
    <a href="https://github.com/leeeha"><img src="https://avatars.githubusercontent.com/u/68090939?v=4" width="150px;" alt="이하은"/><br /><sub><b>이하은</b></sub></a><br />
    </td>
     <td align="center">
        <a href="https://github.com/yuseogi0218"><img src="https://avatars.githubusercontent.com/u/64399505?v=4" width="150px" alt="이유석"/><br /><sub><b>이유석</b></sub></a>
     </td>
     <td align="center">
        <a href="https://github.com/jwyeeh-dev"><img src="https://avatars.githubusercontent.com/u/99489807?v=4" width="150px" alt="황재영"/><br /><sub><b>황재영</b></sub></a>
  <tr>
</table> 


## Project Structure
<img width="755" alt="golden-hour structure" src="https://user-images.githubusercontent.com/64399505/228250494-3c6ecca2-e35f-4a83-99c9-5ad0ba452dc3.png">


## Detailed implementations using Google Technologies

### DL
- To provide the specific DL technology to the Android Application, we used several model and services from Google Technologies.

- To train, provide the object detection and recognition model about the bleeding wounds of the patient, We used Google Tensorflow libraries, especially TFLite as a mobile library to deploy the model to the Android application.

- To make lightweight the wounds detection and recognition model to put in Android App, We also amke the custom model based on MobileNet_V2 from Tensorflow Hub by Google. 

- To detect the precise body landmarks of the patient, we used the mediapipe pose detector from the ML Kit. Mediapipe pose detector is inspired by the lightweighted BlazeFace model as a proxy for a person detector.

- If you want to see more information, please see the Additional DL Documentation below.

## Repositories
<table algin="center">
   <tr>
      <td align="center"><a href="https://github.com/orgs/gdsc-seoultech/projects/3"><strong>Project</strong></a></td>
      <td align="center"><a href="https://github.com/gdsc-seoultech/GoldenHour_Android"><strong>Android</strong></a></td>
      <td align="center"><a href="https://github.com/gdsc-seoultech/GoldenHour_Backend"><strong>Back-End</strong></a></td>
      <td align="center"><a href="https://github.com/jwyeeh-dev/GoldenHour_DL"><strong>DL</strong></a></td>
   </tr>
</table> 

## 🤖 Additional DL Documentation 

> This DL projects are not included in the Android Application.

The original plan was to build own custom models, but due to time constraints, we used ML kit.
This repository is the DL operations which I build own custom operations and we will add on our Application soon. So if you want to see our application, please go Android repository.

## How to test in Python

- **[CPR AI Assistant](https://github.com/jwyeeh-dev/GoldenHour_DL/blob/main/cpr_detection/)** 
- **[Wound AI Assistant](https://github.com/jwyeeh-dev/GoldenHour_DL/blob/main/wound_detection/)** 