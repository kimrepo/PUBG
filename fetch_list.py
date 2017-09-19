#-*- coding: utf-8 -*-
import json
import urllib3
from operator import itemgetter

memberList = []
with open('list.json') as data_file:
    data = json.load(data_file)

    http = urllib3.PoolManager()
    for member in data:
        url = 'http://bzone.me/profile/pc/?username=' + member['nickname'] + '&match=all&season=2017-pre4'
        with http.request('GET', url, preload_content=False) as r:
            data = r.read()
            score = data.split('<li class="score-points">')[1].split('</p>')[0].split('<p class="b-text">')[1].strip()
            score_number = float(score[:len(score)-6])
            
            info = {
                'name': member['name'],
                'nickname': member['nickname'],
                'score': score_number
            }
            memberList.append(info)

last = 9999
lastName = {
    5: '핵유저',
    4: '신',
    3: '초월체',
    2: '신인류',
    1: '인간',
    0: '동키'
}
memberList.sort(key=itemgetter('score'), reverse=True)
for member in memberList:
    score_int = int(member['score'])
    if score_int <> last:
        print('\n## ' + lastName[score_int])
        last = score_int

    print(member['name'] + ' : ' + member['nickname'] + ' (' + str(member['score']) + ')')
