import requests

headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '104',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'HstCfa2448634=1629384576355; HstCmu2448634=1629384576355; c_ref_2448634=https%3A%2F%2Fwww.google.com.hk%2F; _ga=GA1.2.933223999.1629384576; _gid=GA1.2.654645615.1629384576; HstCnv2448634=2; __dtsu=51A0162939103261975914A9D55381D8; hasCookies=True; IPInfo=IP=101%2E228%2E2%2E193&CC=TW; ASPSESSIONIDSGBSQSCQ=DLMJFJBDDBJOHPCGDFCFNGKD; HstCns2448634=3; _gat=1; HstCla2448634=1629393781783; HstPn2448634=5; HstPt2448634=10',
    'Host': 'www.jpmarumaru.com',
    'Origin': 'https://www.jpmarumaru.com',
    'Referer': 'https://www.jpmarumaru.com/tw/toolKanjiFurigana.asp',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


s_voice = requests.session()
s_voice.auth = ('<your-key>','')

fOld = open('D:/Download/新日本语能力考试N4N5/新日本语能力考试N5文字词汇 练习篇.txt', 'r', encoding='utf-8')
fNew = open('D:/Download/新日本语能力考试N4N5/new.txt', 'w', encoding='utf-8')

textOld = fOld.readline().rstrip()
while textOld != '':

    d={'Text':textOld}
    res = requests.post(url='https://www.jpmarumaru.com/tw/api/json_KanjiFurigana.asp',data=d,headers=headers)
    textNew = res.text
    print(textNew)

    d_voice = {
        'text':textOld,
        'speaker':'hikari',
        'format':'mp3'
    }
    res_voice = s_voice.post(url='https://api.voicetext.jp/v1/tts',data=d_voice,stream=True)
    with open(f'd:/{textOld}.mp3', 'wb') as fd:
        for chunk in res_voice.iter_content(chunk_size=128):
            fd.write(chunk)

    fNew.write(f'{textOld} {textNew} [sound:{textOld}.mp3]\n')

    textOld = fOld.readline().rstrip()

fNew.close()
fOld.close()
