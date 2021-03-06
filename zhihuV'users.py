
import requests

headers = {
    'cookie': '_zap=00a8829f-c446-4bfe-9b95-81b6f08f5f36; d_c0="ADBvbENHjQ2PTlUPL2a6I2HJvXcCxAPdFvc=|1525599330"; capsion_ticket="2|1:0|10:1526219875|14:capsion_ticket|44:ZWM1YWY4ZDg4ZDBjNDQxMjk0OTEyY2YxNTVmZjFhOTU=|f5345badbf1721d879be31b6f88fe1bc77ba99c2e1cf9116fe4393351ec14dd3"; z_c0="2|1:0|10:1526219903|4:z_c0|92:Mi4xLU0xTkFBQUFBQUFBTUc5c1EwZU5EU1lBQUFCZ0FsVk5mNUxsV3dDMjRfUk1ETFBXcUdMQVNId0Vpei13NXZuLWZB|bd8b5b718c19c960f5271376c2c4ca49ede08813f83c6284344ec774799428fe"; q_c1=bc2de00cdd2643349f97f9879d3fe71b|1526219903000|1526219903000; _xsrf=f32972b1-47c3-4327-bbf2-7dccda67a319; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; anc_cap_id=37859397271a46e3af560a4d1e15b27e',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://www.zhihu.com/people/hidecloud/answers',
    'authority': 'www.zhihu.com',
    'x-udid': 'ADBvbENHjQ2PTlUPL2a6I2HJvXcCxAPdFvc=',
}

params = {
    'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,collapsed_by,suggest_edit,comment_count,can_comment,content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,question,excerpt,relationship.is_authorized,voting,is_author,is_thanked,is_nothelp;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': '0',
    'limit':'20',
    'sort_by':'created',
}

url = 'https://www.zhihu.com/api/v4/members/hidecloud/answers'
response = requests.get(url, headers=headers, params=params)

j = response.json()

answerlist = []
while j['paging']['is_end'] == False:
    for answer in j['data']:
        answerlist.append(answer['id'])
    params['offset'] = int(params['offset']) + 20
    response = requests.get(url, headers=headers, params=params) 
    j = response.json()
else:
    for answer in j['data']:
        answerlist.append(answer['id'])

answerlist

len(answerlist)

commentlist = []
for answer in answerlist:
    params = {
    'include': 'data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
    'order': 'normal',
    'limit': '20',
    'offset': '0',
    'status': 'open',}
    url = 'https://www.zhihu.com/api/v4/answers/' + str(answer) + '/comments'
    response = requests.get(url, headers=headers, params=params)
    p = response.json()
    while p['paging']['is_end'] == False:
        for comment in p['data']:
            print(comment['author']['member']['url_token'])
        params['offset'] = int(params['offset']) + 20
        response = requests.get(url, headers=headers, params=params)
        p = response.json()
    else:
        for comment in p['data']:
            print(comment['author']['member']['url_token'])
        params = {
    'include': 'data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
    'order': 'normal',
    'limit': '20',
    'offset': '0',
    'status': 'open',}

params = {
    'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': '0',
    'limit': '20',
    'sort_by': 'created',
}
url = 'https://www.zhihu.com/api/v4/members/hidecloud/articles'
response = requests.get(url, headers=headers, params=params)
q = response.json()

articlelist = []
while q['paging']['is_end'] == False:
    for article in q['data']:
        articlelist.append(article['id'])
    params['offset'] = int(params['offset']) + 20
    response = requests.get(url, headers=headers, params=params) 
    q = response.json()
else:
    for article in q['data']:
        articlelist.append(article['id'])

articlelist

len(artilcelist)

params = {
    'include': 'data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
    'order': 'normal',
    'limit': '20',
    'offset': '0',
    'status': 'open',
}

commentlist = []
for article in artilcelist:
    params = {
    'include': 'data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
    'order': 'normal',
    'limit': '20',
    'offset': '0',
    'status': 'open',
}
    url = 'https://www.zhihu.com/api/v4/articles/' + str(article) + '/comments'
    response = requests.get(url, headers=headers, params=params)
    u = response.json()
    while u['paging']['is_end'] == False:
        for comment in u['data']:
            commentlist.append(comment['author']['member']['url_token'])
        params['offset'] = int(params['offset']) + 20
        response = requests.get(url, headers=headers, params=params)
        u = response.json()
    else:
        for comment in u['data']:
            commentlist.append(comment['author']['member']['url_token'])
        
commentlist

len(commentlist)

params = {
    'offset': '0',
    'limit': '15',
    'includes': 'data[*].upvoted_followees,admin_closed_comment',
}
url = 'https://www.zhihu.com/api/v4/members/hidecloud/pins'
response = requests.get(url, headers=headers, params=params)
j = response.json()

pinlist = []
while j['paging']['is_end'] == False:
    for pin in j['data']:
        pinlist.append(pin['id'])
    params['offset'] = int(params['offset']) + 15
    response = requests.get(url, headers=headers, params=params) 
    j = response.json()
else:
    for pin in j['data']:
          pinlist.append(pin['id'])

pinlist

len(pinlist)

params = {
    'include': 'data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
    'order': 'normal',
    'limit': '20',
    'offset': '0',
    'status': 'open',
}

commentlist = []
for pin in pinlist:
    params = {
    'include': 'data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
    'order': 'normal',
    'limit': '20',
    'offset': '0',
    'status': 'open',
}
    url = 'https://www.zhihu.com/api/v4/pins/' + str(pin) + '/comments'
    response = requests.get(url, headers=headers, params=params)
    j = response.json()
    while j['paging']['is_end'] == False:
        for comment in j['data']:
            commentlist.append(comment['author']['member']['url_token'])
        params['offset'] = int(params['offset']) + 20
        response = requests.get(url, headers=headers, params=params)
        j = response.json()
    else:
        for comment in j['data']:
            commentlist.append(comment['author']['member']['url_token'])

commentlist

len(commentlist)

params = {
    'include': 'data[*].column.intro,followers,articles_count',
    'offset': '0',
    'limit': '20',
}

url = 'https://www.zhihu.com/api/v4/members/hidecloud/column-contributions'
response = requests.get(url, headers=headers, params=params)
j = response.json()

columnlist = []
while j['paging']['is_end'] == False:
    for column in j['data']:
        columnlist.append(column['column']['id'])
    params['offset'] = int(params['offset']) + 20
    response = requests.get(url, headers=headers, params=params) 
    j = response.json()
else:
    for column in j['data']:
          columnlist.append(column['column']['id'])

columnlist
 
articlelist = []
for column in columnlist:
    params = {
    'include': 'data[*].admin_closed_comment,comment_count,suggest_edit,is_title_image_full_screen,can_comment,upvoted_followees,can_open_tipjar,can_tip,voteup_count,voting,topics,review_info,author.is_following',
}  
    url = 'https://www.zhihu.com/api/v4/columns/' + str(column) + '/articles'
    response = requests.get(url, headers=headers, params=params)
    j = response.json()
    while  j['paging']['is_end'] == False:
        for article in j ['data']:
            articlelist.append(article['id'])
        params['offset'] = int(params['offset']) + 20
        response = requests.get(url, headers=headers, params=params) 
        j = response.json()
    else:
         for article in j ['data']:
            articlelist.append(article['id'])

articlelist

len(articlelist)

commentlist = []
for article in articlelist:
    params = {
    'include': 'data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
    'order': 'normal',
    'limit': '20',
    'offset': '0',
    'status': 'open',
}
    url = 'https://www.zhihu.com/api/v4/articles/' + str(article) + '/comments'
    response = requests.get(url, headers=headers, params=params)
    j = response.json()
    while  j['paging']['is_end'] == False:
        for comment in j ['data']:
            print(comment['author']['member']['url_token'])
        params['offset'] = int(params['offset']) + 20
        response = requests.get(url, headers=headers, params=params) 
        j = response.json()
    else:
         for comment in j ['data']:
            print(comment['author']['member']['url_token'])

params = {
    'include': 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics',
    'offset': '0',
    'limit': '20',
}

url = 'https://www.zhihu.com/api/v4/members/hidecloud/followers'
response = requests.get(url, headers=headers, params=params)
j = response.json()

followerlist = []
while j['paging']['is_end'] == False:
    for follower in j['data']:
        print(follower['url_token']) 
    params['offset'] = int(params['offset']) + 20
    response = requests.get(url, headers=headers, params=params) 
    j = response.json()
else:
    for follower in j['data']:
        print(follower['url_token'])

