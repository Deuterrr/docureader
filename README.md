```                                                                     
████▄   ▄▄▄   ▄▄▄▄ ▄▄ ▄▄ ▄▄▄▄  ▄▄▄▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  
██  ██ ██▀██ ██▀▀▀ ██ ██ ██▄█▄ ██▄▄  ██▀██ ██▀██ ██▄▄  ██▄█▄ 
████▀  ▀███▀ ▀████ ▀███▀ ██ ██ ██▄▄▄ ██▀██ ████▀ ██▄▄▄ ██ ██

Document Reader, from Classification to Extraction.
```


# Project Overview

This project is an AI-based [describe function: e.g. *document understanding service*] built with **FastAPI**.
It uses a modular architecture separating **API**, **use cases**, and **services** (AI model inference, preprocessing, etc.).

<div>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.12+-ffd700?logo=python&logoColor=white" alt="Python" />
  </a>
  &nbsp;&nbsp;
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.ultralytics.com/">
    <img src="https://img.shields.io/badge/YOLO-v11-0b0c0f" alt="YOLOv11" />
  </a>
  &nbsp;&nbsp;
  <a href="https://docs.nestjs.com">
    <img src="https://img.shields.io/badge/Ultralytics-Official-3d8ff0" alt="Ultralytics" />
  </a>
</div>

<br>

# Folder Structure

```
├── 📁 src/
│   ├── 📁 core/
│   │   ├── 🐍 config.py
│   │   ├── 🐍 file_checker.py
│   │   ├── 🐍 image_loader.py
│   │   └── 🐍 response_builder.py
│   │
│   ├── 📁 infra/
│   │   ├── 📁 helpers/
│   │   ├── 📁 weights/
│   │   ├── 📁 services/
│   │   └── 📁 models/
│   │       └── 🐍 yolo_model.py
│   │       
│   ├── 📁 lib/
│   │   ├── 📁 app/
│   │   │   └── 📁 usecases/
│   │   │
│   │   ├── 📁 domain/
│   │   │   ├── 📁 entities/
│   │   │   └── 📁 interfaces/
│   │   │
│   │   └── 📁 inter/
│   │       ├── 📁 controllers/
│   │       └── 📁 routes/
│   │
│   └── 🐍 main.py
│
├── ⚙️ .env.example
├── ⚙️ .gitignore
├── 📝 README.md
└── 📄 requirements.txt
```

<br>

# Run Locally

## 1. Clone & Setup

```bash
git clone https://github.com/Deuterrr/docureader.git
cd docureader
```

## 2. Create Virtual Environment (recommended)
```bash
python -m venv .venv
```

On Linux/Mac

```bash
source .venv/bin/activate
```

On Windows

```bash
.venv\Scripts\activate
```

## 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Prepare Model Weights
Create a folder for model weights and place the YOLO .pt file inside it:

```bash
mkdir -p infra/weight
```

Move your model file into:
```bash
infra/weight/yolo.pt
```

Model available on https://drive.google.com/drive/folders/1iYJnvHnOmFYPUZtJtERr9as3okKeD0-v?usp=drive_link

## 5. Environment Variables
Copy .env.example to .env and fill in the required values.

Add the model path:
```ini
KTP_DETECT_MODEL=infra/weight/yolo.pt
```

## 6. Run in Development
```bash
uvicorn src.main:app --reload
```

<br>

# Endpoints

## 1. Classify KTP Document

**URL:** `/ktp/classify`<br>
**Method:** `POST`<br>
**Description:** Classifies the uploaded document to determine if it is a KTP and returns confidence level.

**Request:**

| Parameter | Type         | Description                               |
| --------- | ------------ | ----------------------------------------- |
| `file`    | `UploadFile` | The image file of the document (JPG/PNG). |

**Response:**

```json
{
    "code": "000",
    "message": "success",
    "data": {
        "doc_type": "ktp",
        "confidence": 0.969,
        "processing_time_ms": 118.41
    }
}
```

* `doc_type`: Detected document type.
* `confidence`: Confidence score (0–1) of classification.
* `processing_time_ms`: Time taken to process the request.
<br>

# Notes for Endpoint

* Only **1 image** per input.
* Only **JPG** and **PNG** image are supported.
* **Extract KTP Fields** only supports **RGB/BRG image** input.
