# Add reCAPTCHA to DRF

Adding Recaptcha is always good practice to avoid spambots such as creating dummy users that will fill the database with useless data. In DRF, some public API endpoints (register/login/reset password and etc.) need to be protected from such attacks.

## Getting Started

Works on **Python 3+** and **Django 3+**.

1. First, you need to get API credentials from the [Recaptcha admin](https://www.google.com/recaptcha/admin/create) to use them later to verify requests.

2. Replace placeholders with your credentials in `settings.py`

```python
RE_CAPTCHA_SITE_KEY = "YOUR_RE_CAPTCHA_SITE_KEY"
RE_CAPTCHA_SECRET_KEY = "YOUR_RE_CAPTCHA_SECRET_KEY"
```

3. Install dependencies:

```
python -m pip install -r requirements.txt
```

4. Start the server:

```
python manage.py migrate
python manage.py runserver
```

## Testing

Navigate to demo recapctha page and complete the recaptcha puzzle to get response token.

```
localhost:8000/demo-recaptcha/
```

Send multiple requests to user registration endpoint until you get `recaptcha_required` message.

```
localhost:8000/accounts/register/
```

Once message appeared, add response token to request data alongsode with user details:

```
recapctha: <response_token>
```

## More Details

https://www.thepylot.dev/recaptcha-django-rest-framework/
