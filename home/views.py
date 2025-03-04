from django.views.generic import FormView
from django.http import JsonResponse
from .forms import ImageUploadForm
import random

class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = ImageUploadForm
    success_url = '.'  # Refresh the page after POST

    def form_valid(self, form):
        image = form.cleaned_data['image']
        result = self.classify_image(image)
        # If the request is AJAX, return a JSON response.
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'result': result})
        # Otherwise, render the template with the result.
        return self.render_to_response(self.get_context_data(form=form, result=result))

    def classify_image(self, image):
        # Dummy classification logic. Replace this with your actual image classification code.
        labels = ['cat', 'dog', 'bird', 'other']
        return random.choice(labels)
