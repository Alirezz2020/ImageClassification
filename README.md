
# Image Classifier Django Project

## Overview

Image Classifier is a Django web application that lets you classify images using a pre‑trained deep learning model (MobileNetV2). Users can register and log in either via local credentials or using their Google account. The website features a modern, responsive interface powered by Bootstrap 5, and follows RESTful principles with class‑based views.

## Features

- **Image Classification:** Uses TensorFlow/Keras MobileNetV2 with ImageNet weights to predict image labels along with confidence scores.
- **User Authentication:** Supports both local registration/login and Google OAuth2 login.
- **Modern UI:** Responsive design with a Bootstrap 5 navbar, clean templates, and AJAX support.
- **RESTful Endpoints:** AJAX requests return JSON responses for dynamic content updates.
- **Extensible Architecture:** Built to easily integrate new features and enhancements.

## Prerequisites

- Python 3.7+
- pip (package installer)
- Virtual environment tool (recommended)
- Required Python packages:
  - Django
  - Pillow
  - tensorflow
  - social-auth-app-django
## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Alirezz2020/ImageClassification.git
   cd ImageClassification
2. **Set Up a Virtual Environment:**
    ```sh
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
3. **Install Dependencies:**
   ```sh
    pip install -r requirements.txt

4. **Apply Migrations:**
    ```sh
    python manage.py migrate
5. **Create a Superuser:**
    ```sh
   python manage.py createsuperuser
6. **Run the Development Server:**
    ```sh
   python manage.py runserver
7. **Access the Application:**

    Visit http://127.0.0.1:8000/ in your browser to start exploring the platform.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to include tests and follow the project’s coding standards.

## License
This project is licensed under the MIT License.

## How It Works

### Image Classification
Upload: On the home page, users can upload an image using a simple form.

Processing: The backend:

Opens the image with Pillow and converts it to RGB.

Resizes the image to 224x224 pixels.

Preprocesses the image using Keras’s preprocess_input.

Prediction: The processed image is fed into MobileNetV2. The model predicts the most likely label along with its confidence score.

Response: The classification result is either rendered in the template or returned as JSON if the request is made via AJAX.

## User Authentication
Local Login/Registration: Users can create an account or log in using a standard username and password.

Google Login: Users can also sign in with their Google account. The navbar displays a “Login with Google” option when a user is not authenticated.

## RESTful & Modern Design
Class‑Based Views: All views are implemented using Django’s class‑based views for a clean and scalable codebase.

AJAX Support: The image classification endpoint supports AJAX, allowing seamless interaction without full page reloads.

Bootstrap 5: The base template uses Bootstrap 5 for a modern, responsive UI that works well on all devices.

## Extending the Project
This project is built to be flexible and scalable. Future enhancements might include:

Improved image preprocessing and error handling.

Additional social authentication providers (e.g., Facebook, GitHub).

A user dashboard to view past classifications.

Integration with a custom or more advanced image classification model.