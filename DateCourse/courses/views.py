from django.shortcuts import render
import json
import requests
import urllib.parse 

def index(request):
    data = {'池袋': 'ラーメン二郎池袋店'}
    ##立石のhottopepperのkey
    api_key="e1a59ffd311bed72"  

    ##池袋をURLエンコードに変換 
    ##(本当は"池袋"っていうワードもトップページのファイルから受け渡したい)
    word="池袋"
    utf_word=urllib.parse.quote(word)

    ##キーワードを池袋として,おすすめ順に検索
    api = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?"\
        "key={key}&large_area=Z011&keyword={keyword}&order=4&format=json"
    url=api.format(key=api_key,keyword=utf_word)


    response = requests.get(url)
    result_list = json.loads(response.text)["results"]["shop"]

    ##お勧め順上位10件の店名をリストansに格納
    ans = [d.get("name") for d in result_list]
    seat_json = json.dumps({'池袋':ans})

    return render(request, 'courses/Home2.html',{'data_json':seat_json})