from django.conf import settings
from django.shortcuts import render

def demo_recaptcha(request):
    return render(request, 'demo_recaptcha.html', {
        "key": settings.RE_CAPTCHA_SITE_KEY
    })