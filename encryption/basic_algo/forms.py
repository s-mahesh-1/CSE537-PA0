from django import forms

attrs = {'cols': 100, 'rows': 15}

class EncryptionForm(forms.Form):
	plain_text = forms.CharField(label = 'Plain Text', widget = forms.Textarea(attrs = attrs))

	# def clean_plain_text(self):
	# 	return self.cleaned_data['plain_text'].lower()


class DecryptionForm(forms.Form):

	cipher_text = forms.CharField(label = 'Cipher Text', widget = forms.Textarea(attrs = attrs))

	# def clean_cipher_text(self):
	# 	return self.cleaned_data['cipher_text'].lower()

def createForm(plain_text = '', cipher_text = ''):
	forms = {
		'encryption_form': EncryptionForm(initial = {'plain_text': plain_text}),
		'decryption_form': DecryptionForm(initial = {'cipher_text': cipher_text})
	}
	return forms