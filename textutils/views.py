#views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Conditions are here for different buttons
    if removepunc == "on":
        # analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'remove punctuations', 'analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed+char
        params = {'purpose': 'Extra space Remove', 'analyzed_text': analyzed}
        djtext = analyzed

    # The below given if acts as an else function
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please select atleast one operation")

    return render(request, 'analyze.html', params)
