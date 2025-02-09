from django.shortcuts import render
from django.http import JsonResponse
import random
import string

# Generate random captcha
def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def captcha_view(request):
    captcha = generate_captcha()
    request.session['captcha'] = captcha
    return render(request, 'captcha.html', {'captcha': captcha})

def validate_captcha(request):
    user_input = request.GET.get('captcha_input', '')
    stored_captcha = request.session.get('captcha', '')
    
    attempts = request.session.get('attempts', 0)
    if user_input == stored_captcha:
        request.session['attempts'] = 0
        return JsonResponse({'status': 'success', 'message': 'Captcha matched!'})
    
    attempts += 1
    request.session['attempts'] = attempts
    if attempts >= 3:
        return JsonResponse({'status': 'error', 'message': 'Too many failed attempts. Input disabled!', 'disable': True})
    
    return JsonResponse({'status': 'error', 'message': 'Captcha mismatch. Try again!'})