import shutil, os
from ultralytics import YOLO
from google.colab import files
from IPython.display import display, Image

model = YOLO('best.pt')

# Clear previous results
shutil.rmtree('/content/runs/detect/test_results', ignore_errors=True)

# Upload new image
uploaded = files.upload()
img_name = list(uploaded.keys())[0]

# Run detection
model.predict(
    source=img_name,
    conf=0.5,
    save=True,
    project='/content/runs/detect',
    name='test_results',
)

# Show result
result_img = os.listdir('/content/runs/detect/test_results')[0]
display(Image(filename=f'/content/runs/detect/test_results/{result_img}'))
