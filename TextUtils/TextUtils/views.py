# I have created this file - Abhie4557
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Home")
    # dict1 = {'name': 'Abhie', 'place': 'India'}
    # return render(request, 'index.html', dict1)
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')

    removepunc= request.GET.get('removepunc', 'off')
    fullcaps= request.GET.get('fullcaps', 'off')
    newlineremove= request.GET.get('newlineremove', 'off')
    spaceremove= request.GET.get('spaceremove', 'off')
    charcount= request.GET.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\\]^_{|}~`'''
        # print(removepunc)
        # print(djtext)
        analyzed = ""   #Creating empty string for analyzed text(removed punctuations)
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != '/n':
                analyzed = analyzed + char
        params = {'purpose': 'Removed New lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif spaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error !")

