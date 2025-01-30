from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)
    

# o formulário de criação de conta vai criar um novo usuário
class Criarcontaform(UserCreationForm): 
    email = forms.EmailField()
    
    # Dentro dessa classe  tem que criar outra classe chamada meta para definir qual o modelo 
    # que gerencia o usuário: ( o modelo padrão do django ou o seu modelo próprio)
    # no nosso caso é o meu modelo proprio, então informo que o model da classe meta é igual a Usuario
    class Meta:
        model = Usuario
        # fields é uma tupla que vai dizer quais campos vão ser exibidos no formulário
        fields = ('username','email','password1','password2' ) # o nome padrão de coloque a sua senha é: password1 , o nome padrão de confirmação de senha é password2
    






