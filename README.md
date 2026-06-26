# Cartoonify AI — Image Cartoonification Web App

A Flask web application that transforms any photo into cartoon-style artwork using **OpenCV image processing**. Upload an image, click a button, and instantly get a cartoon version — no deep learning model required.

---

## Features

- **Cartoon Effect** — Converts real photos into cartoon-style images using pure OpenCV techniques
- **Edge Detection** — Adaptive thresholding highlights sharp edges like a hand-drawn outline
- **Color Smoothing** — Bilateral filtering flattens color regions while preserving edges
- **Instant Preview** — Processed cartoon image displayed immediately in the browser
- **Clean UI** — Glassmorphism-style interface built with Bootstrap 5 and custom CSS
- **Gradient Theme** — Purple-to-blue gradient design with a modern card layout

---

## How It Works (Cartoonification Pipeline)

| Step | Technique | Purpose |
|------|-----------|---------|
| 1 | Grayscale conversion | Prepare image for edge detection |
| 2 | Median blur (`5×5`) | Remove noise before edge detection |
| 3 | Adaptive threshold | Detect and sharpen edges (cartoon outline) |
| 4 | Bilateral filter (`d=9, σ=250`) | Smooth colors while keeping edges crisp |
| 5 | Bitwise AND | Combine color layer with edge mask → cartoon |

---

## Project Structure

```
cartoonify-app/
├── app.py              # Flask app — upload handling & cartoonify logic
├── templates/
│   └── index.html      # Upload form + preview UI (Bootstrap 5)
├── static/
│   └── style.css       # Custom glassmorphism styles
├── uploads/            # Temp storage for uploaded images (auto-created)
└── outputs/            # Cartoon output images (auto-created)
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Image Processing | OpenCV (cv2) |
| File Handling | Werkzeug |
| Frontend | HTML, Bootstrap 5, CSS |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/abhi66686668/abhi66686668-Cartoon-image-creater1.git
cd cartoonify-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install flask opencv-python werkzeug
```

### 4. Run the app

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Usage

1. Open the app in your browser
2. Click the upload box and select any image (`.jpg`, `.png`, `.webp`, etc.)
3. Click **Cartoonify Image**
4. The cartoon version appears instantly in the preview panel on the right

---

## Requirements

```
flask
opencv-python
werkzeug
```

---

## Contributors

- [abhi66686668](https://github.com/abhi66686668)

---

## License

This project is open-source and available under the [MIT License](LICENSE).
