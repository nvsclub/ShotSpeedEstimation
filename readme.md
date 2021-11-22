# Supplementary material from A Survey of Advanced Computer Vision Techniques for Sports

If you want the videos to work with, please contact me directly. This repository is not able to host them.

- 00X notebooks -> video preprocessing
- 01X notebooks -> data extraction with computer vision models
- 02X notebooks -> prediction pipeline
- 08X & 09X notebooks -> extras

- data
    - tab -> contains tabular data
        - joined -> data resulting from joining the two models results
        - json -> data from the CenterNet object detection framework
        - npz -> data from the ROMP 3d pose estimation
    - video (WARNING: if you do not use this directory structure, you'll have to change the scripts to correct the directories)
        - crop -> videos cropped with notebook 003
        - cut -> videos cut with notebook 002
        - raw -> input videos