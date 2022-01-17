from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse
from . import forms, algorithm
# Create your views here.
def index(request):
	plain_text = ''
	cipher_text = ''
	if request.method == 'POST':
		if 'encrypt' in request.POST:
			plain_text, cipher_text = encrypt(request)

		if 'decrypt' in request.POST:
			plain_text, cipher_text = decrypt(request)

	return render(request, 'index.html', forms.createForm(plain_text, cipher_text))

def encrypt(request):
	plain_text = forms.EncryptionForm(request.POST)
	if plain_text.is_valid():
		plain_text = plain_text.cleaned_data['plain_text']

		cipher_text = algorithm.simple_encrypt(plain_text)

		return plain_text, cipher_text
		

def decrypt(request):
	cipher_text = forms.DecryptionForm(request.POST)
	if cipher_text.is_valid():
		cipher_text = cipher_text.cleaned_data['cipher_text']

		plain_text = algorithm.simple_decrypt(cipher_text)

		return plain_text, cipher_text


