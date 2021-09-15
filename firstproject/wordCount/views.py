from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):
    sentence=request.GET['sentence']
    wordList=sentence.split()

    wordDict={}

    for word in wordList:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1

    return render(request, "result.html", {'fulltext':sentence, 'count':len(wordList), 'wordDict':wordDict.items})
# wordDict가 리스트형태니까, 그냥 써주면 에러나서 그 안의 값을 한번에 다 넘겨준다는 의미로 .items를 사용

