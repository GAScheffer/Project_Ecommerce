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