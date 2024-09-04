from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245756',
        'name': 'Tarissa Mutia Andini',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)