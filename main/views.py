from django.shortcuts import render


def index(request):
    turn_on_block = True
    text = 'Лаборатория Django-разработки от школы Thinknetica'

    return render(request, 'index.html', {'turn_on_block': turn_on_block, 'text':text})
