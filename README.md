# Anti-Spoofing-Liveliness-Detector



## Overview

This project implements a computer vision system for Anti-Spoofing, specifically liveliness detection, using the YOLO (You Only Look Once) model. The system is designed to distinguish between real and fake faces in live webcam or images.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Data Collection](#data-collection)
- [Training](#training)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Kaustbh/Anti-Spoofing-Liveliness-Detector

```

2. Install dependencies:<br>
   <br>
   - Before Installing dependencies , create a virtual environmnet , to prevent conflicts between different projects that may have different versions of the same library.

```bash
pip install -r requirements.txt
```

## Usage

To use the Anti-Spoofing system, follow these steps:

1. Run the data collection script to gather real and fake face images using the webcam:

```bash
python data_collection.py
```

2. Split the collected data into training, testing, and validation sets:

```bash
python split_data.py
```

3. Train the YOLO model:

```bash
python train.py
```

4. Run the main script to perform face detection and liveliness detection:

```bash
python main.py
```

## Testing

The `testing` folder contains Python scripts and images for testing the face detection and YOLO model.

To run the tests:

```bash
python testing/facedetector.py
python testing/yolotest.py
```

## Data Collection

The `data_collection` folder contains scripts for collecting real and fake face images using the webcam. Run the `data_collection.py` script to initiate the data collection process.

## Training

The `training` folder contains scripts and resources for training the YOLO model. The model weights are stored in the `weights` folder. To train the model, use the `train.py` script.

```bash
python training/train.py
```

## Folder Structure

- `data_collection/`: Scripts for collecting real and fake face images using the webcam.
- `testing/`: Python scripts and images for testing the face detection and YOLO scripts.
- `training/`: Scripts and resources for training the YOLO model.
- `weights/`: Folder where trained model weights are stored.
- `main.py`: Main script for face detection and liveliness detection.
- `split_data.py`: Script to split collected data into training, testing, and validation sets.
- `requirements.txt`: List of dependencies.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request. Issues and feature requests are welcome as well!

## License

This project is licensed under the [MIT License](LICENSE).

