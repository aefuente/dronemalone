# Capstone II Final Porject Team 14
The aim of this project is to bring facial tracking technology to drones. 
This will be accomplished by the development of a computer vision algorithm 
for facial detection that will interface with and control the drone. The 
drone’s camera will communicate with a Haar cascade object detection model to 
gather information about the presence and location of a human face and make 
decisions about how the drone should be maneuvered to locate and track the 
face. The development of the technology in this project will have benefits for 
surveillance, tracking, and the film industry.

## Contents
1. [Environment Setup](#environment-setup)
2. [Demo](#demo)

## Environment setup

- Clone the repository
```
git clone git@github.com:aefuente/dronemalone.git capstone && cd capstone
export capstone=$PWD
```
- Setup python environment  
This project uses conda package manager. For details on how to install conda
visit https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html 

```
conda create -n capstone python=3.10
conda activate capstone
pip install -r requirements.txt
```

## Demo
- [Setup](#environment-setup) your environment
- Run `src/main.py`
```
cd $capstone
python3 ./src/main.py
```
