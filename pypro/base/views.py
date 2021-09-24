from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse('<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8">'
                        '<meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" '
                        'content="width=device-width, initial-scale=1.0"><title>Módulo Django - DevPro</title>'
                        '</head><body>''Olá Django</body></html>', content_type='text/html')
