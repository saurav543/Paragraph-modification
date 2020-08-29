from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'about.html')
def contactus(request):
    return render(request, 'contact.html')
def remove(request):
    text1 = request.POST.get('text', 'default')
    text2 = request.POST.get('rem', 'off')
    text3 = request.POST.get('upper', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    if(text2 == "on" or text3 == "on" or newlineremover == "on" or extraspaceremover == "on" or charactercounter == "on" ):
        if(text2 == "on"):
            punc = '''!#$%&"/'\()*+,-./:;?@[\]^_`{|}~'''
            analyze = ""
            for char in text1:
                if char not in punc:
                    analyze = analyze + char
            letter = {'purpose': 'Remove punctuation', 'analyze_text': analyze}
            text1=analyze
            # return render(request, 'analyze.html', param1)
        if(text3 == "on"):
              analyze = ""
              for char in text1:
                       analyze = analyze + char.upper()

              letter = {'purpose': 'uppercase', 'analyze_text': analyze}
              text1=analyze
              # return render(request, 'analyze.html', letter)
        if(newlineremover == "on"):
            analyze = ""
            for char in text1:
                if char!="\n" and char != '\r':
                    analyze = analyze + char

            letter = {'purpose': 'newlineremover', 'analyze_text': analyze}
            text1=analyze
            # return render(request, 'analyze.html', letter)
        if(extraspaceremover == "on"):
            analyze = ""
            for index,char in enumerate(text1):
                if not(text1[index] == " " and text1[index+1] == " "):

                    analyze = analyze + char

            letter = {'purpose': 'Extraspaceremover', 'analyze_text': analyze}
            text1=analyze
          # return render(request, 'analyze.html', letter)
        if (charactercounter == "on"):
            j =0
            i=0
            for i in enumerate(text1):
               j=j+1

            letter = {'purpose': 'Character Count', 'analyze_text': j}
            # return render(request, 'analyze.html', letter1)
            
        return render(request, 'analyze.html', letter)
    else:
        return HttpResponse("Error")
