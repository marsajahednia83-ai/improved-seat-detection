# improved-seat-detection
This AI project is the improved version of the previous one by improving the dataset and training process.
# AI-Based Smart Campus Seat Detection System

## Project Overview
YOLOv8m model trained to detect Available and Occupied seats on campus.
This project is a direct continuation of Project 1: AI‑Based Smart Campus Detection System. In Project 1, we developed a YOLOv8n object detection model to classify and localise available and occupied seats in campus environments (libraries, food courts, study areas). Using a custom dataset of 600 manually annotated images, the baseline model achieved a mean average precision (mAP@0.5) of 97.1%, with high precision for occupied seats (0.98) but lower recall for occupied seats (0.808). Error analysis revealed that small personal items (bags, notebooks) and poor lighting conditions were the primary causes of missed detections.

The goal of Project 2 is to systematically improve the baseline model’s performance by applying at least two distinct improvement strategies, measuring their isolated effects, and documenting all findings in a formal research article format. Following the project guidelines, we selected and implemented two strategies:

Model / Architecture upgrade – replacing the YOLOv8n backbone with the larger YOLOv8m model to potentially improve feature extraction for small or partially occluded objects.

Dataset enhancement through improved splitting – moving from a person‑specific validation split (one group member’s images held out entirely) to a generalised 80/20 stratified split across all contributors, ensuring that the validation set better represents the full diversity of camera angles, lighting conditions, and chair types.

Additionally, we migrated training from a CPU (approx. 10 hours) to Google Colab with GPU acceleration, reducing training time to 20–40 minutes and enabling faster experimentation.

All experiments are benchmarked against the Project 1 baseline using precision, recall, mAP@0.5, and mAP@0.5:0.95. A final combined model integrates both improvements. The report follows a conference‑style structure, includes an ethical reflection using the FAT (fairness, accountability, transparency) framework, and updates the real‑world deployment analysis from Project 1. A mandatory viva session will be used to defend all methodological choices and results.

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
