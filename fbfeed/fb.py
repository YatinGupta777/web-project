import urllib3
import facebook
import requests
import json
token = "EAAGXu9TWzxwBABZBQcbgFPF0ZCaWCI1QB0QvBu70ljBhM7g6acLd3PSKZB3ihjhQKDwiI8wiRTAY0CKb9NAwRlCEbY078k8roFywO744n8ZAazA21dHd95QzpBtMTVt8eE6jiYdZBt07YYNhEtT9MhNaHxb9t9Y4ZD"
graph = facebook.GraphAPI(access_token=token, version = 2.7)
pagesdata = requests.get("https://graph.facebook.com/me/accounts?access_token="+token)
page_id = "145561028808040"#DTU TIMES
posts_on_page = requests.get("https://graph.facebook.com/"+page_id+"/feed?access_token="+token)
posts_data = (posts_on_page.json())
fb_message = ""
#for posts in posts_data['data']:
#        for j in posts['message']:
#                print (j,end='')

fbpost = []
for i in range(5):
    fbpost.append(posts_data['data'][i]['message']);
    print (fbpost)

print(posts_data)
