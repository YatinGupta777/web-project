from django.shortcuts import render
from django.views.generic import TemplateView
import urllib3
import facebook
import requests
import json

# Create your views here.
class FbPostsView(TemplateView):

    template_name='fbfeed/fb.html'
    def get(self,request):
        token = "EAAGXu9TWzxwBABZBQcbgFPF0ZCaWCI1QB0QvBu70ljBhM7g6acLd3PSKZB3ihjhQKDwiI8wiRTAY0CKb9NAwRlCEbY078k8roFywO744n8ZAazA21dHd95QzpBtMTVt8eE6jiYdZBt07YYNhEtT9MhNaHxb9t9Y4ZD"
        graph = facebook.GraphAPI(access_token=token, version = 2.7)
    #    pagesdata = requests.get("https://graph.facebook.com/me/accounts?access_token="+token)
        page_id = "145561028808040"#DTU TIMES
        posts_on_page = requests.get("https://graph.facebook.com/"+page_id+"/feed?access_token="+token)
        posts_data = (posts_on_page.json())
        fbpost = []
        for i in range(5):
            fbpost.append(posts_data['data'][i]['message']);

        return render(request,'fbfeed/fb.html', {'post_message': fbpost})
