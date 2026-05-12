# improved-seat-detection
This AI project is the improved version of the previous one by improving the dataset and training process.
# AI-Based Smart Campus Seat Detection System

## Project Overview
YOLOv8m model trained to detect Available and Occupied seats on campus.

## Requirements
pip install ultralytics

## How to Train
python train.py

## How to Test
python test.py

## Dataset
- 609 original images + 400 additional multi-chair images
- 2 classes: Available, Occupied
- Annotated using CVAT

## Results
| Model | Precision | Recall | mAP@0.5 |
|-------|-----------|--------|---------|
| YOLOv8n (Baseline) | 0.95 | 0.808 | 0.971 |
| YOLOv8m (Improved) | 0.889 | 0.807 | 0.875 |

## Environment
- Python 3.12
- Ultralytics 8.4.48
- CUDA (Tesla T4 via Google Colab)
- Random seed: 0

- ## Model Weights
Download best.pt here: [Google Drive Link]( https://drive.google.com/file/d/1ilBgbwOOp6Wk-FoL6unr0DrcIotqDIOz/view?usp=drive_link )
