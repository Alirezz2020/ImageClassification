from django.views.generic import FormView
from django.http import JsonResponse
from .forms import ImageUploadForm
from PIL import Image
import numpy as np

# Import Keras functions.
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2, preprocess_input, decode_predictions
)

class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = ImageUploadForm
    success_url = '.'  # Refresh the page after POST

    # Lazy load the model only once.
    model = None

    def form_valid(self, form):
        image_file = form.cleaned_data['image']
        result = self.classify_image(image_file)
        # If the request is AJAX, return a JSON response.
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'result': result})
        # Otherwise, render the template with the result.
        return self.render_to_response(self.get_context_data(form=form, result=result))

    def classify_image(self, uploaded_image):
        # Load the model if it hasn’t been loaded yet.
        if HomeView.model is None:
            HomeView.model = MobileNetV2(weights='imagenet')

        # Open the image, ensure it has 3 channels, and resize it to 224x224.
        img = Image.open(uploaded_image)
        img = img.convert('RGB')
        img = img.resize((224, 224))

        # Convert image to numpy array and preprocess.
        x = np.array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # Make a prediction.
        preds = HomeView.model.predict(x)
        decoded = decode_predictions(preds, top=1)[0][0]  # (class, label, probability)
        label, confidence = decoded[1], decoded[2]
        return f"{label} ({confidence*100:.2f}% confidence)"
