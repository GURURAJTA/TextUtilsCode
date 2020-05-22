# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''For Entertainment youtube video''',
             '''For Interaction Facebook''',
             '''For Insight   Ted Talk''',
             '''For Internship   Intenship''',
             ]
    return HttpResponse(sites)


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    purpose = []
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose.append('Removed Punctuations')
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if fullcaps == "on":
        analyzed = djtext.upper()
        purpose.append("Made the text capital")
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for ind, char in enumerate(djtext):
            if not (djtext[ind] == " " and djtext[ind + 1] == " "):
                analyzed = analyzed + char
        purpose.append("Removed extra spaces")
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        purpose.append("Removed all of the new line characters")
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    elif newlineremover != 'on' and extraspaceremover != 'on' and fullcaps != 'on' and removepunc != 'on':
        return HttpResponse(djtext)

    else:
        return HttpResponse("Error please check your credentials and try again")
    return render(request, 'analyze.html', params)
