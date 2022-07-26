# Project_Ecommerce

##############################   INSTALAÇÕES TERMINAL   #######################

python3.10 -m venv venv
. venv/bin/activate
venv/bin/python3.10 -m pip install --upgrade pip
pip install django
pip install django-crispy-forms (v1.14.0)
pip install django-debug-toolbar (v3.5.0) #
pip install pillow # para redimencionar as imagens (v9.2.0)

python -m pip install -U autopep8

django-admin startproject eloja .
python manage.py startapp produto
python manage.py startapp pedido
python manage.py startapp perfil
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp
python manage.py runserver


##############################     EXTENSÕES USADAS     #######################

Django - Baptiste Darthenay
Dracula Official
IntelliJ Idea Keybindings (atalhos pycharm)
Material Icon Theme
*TODO Tree



##############################     ALTERAÇÕES JSON     ########################

    #Pelo Pylinting#
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--errors-only",
    ]


######################     ALTERAÇÕES DO SETTINGS DO ELOJA     ###################

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'
-------------------------------------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'templates/static')
STATICFILES_DIRS = [
    os.path.join('static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-info',
    constants.ERROR: 'alert-danger',
    constants.INFO: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.WARNING: 'alert-warning',
}


# Tempo de duração das sessões: (seg, min, hr, d)
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

# Salvar requisição:
SESSION_SAVE_EVERY_REQUEST = False




######################     INSTALAÇÃO DEBUG_TOOLBAR     ###################

https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
https://docs.djangoproject.com/en/4.0/howto/static-files/
 
 """+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    alterado para:
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)   """



------------------------------------------------------------------------------
######################     Importação no models.py     ###################

Importações feitas para alterar o tamanho das imagens que são inseridas e ficarem
padrão


import os
from PIL import Image


# REDIMENCIONANDO AS IMAGENS

    @staticmethod
    def resize_image(img, new_width=800):

        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            print('retornando, tamanho original menor ou igual que nova largura')
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50,
        )
        # print(img_full_path)
        # print(img.name)  # nome da imagem

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome
------------------------------------------------------------------------------
1rd PARTE

INSTALTION AND CONFIGURATION OF DJANGO AND OTHER COMPONENTS


------------------------------------------------------------------------------


2rd PARTE 

Created and added the files views.py e urls.py in the folders 'Produto',
 'Perfil' and 'Pedido'. The test results in no fails.

------------------------------------------------------------------------------

3rd

Addicioned of index.html (base.html), Tamplates


------------------------------------------------------------------------------

4rd 

Created uteis folder;
Fixed price formation;


5rd

Added: 
    Product Details;
    Product Variations;

6rd

Added:
    'Add Cart' 
    #Criar a função de Adicionar ao Carrinho seria ideal com JavaScript