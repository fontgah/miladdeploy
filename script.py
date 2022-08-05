import re, requests, time
from urllib import parse
username = ''
password = ''
import os
cwd = os.getcwd()
dirext = cwd+r'\''.split("'")[0]
def bytes_2_human_readable(number_of_bytes):
    step_to_greater_unit = 1024.

    number_of_bytes = float(number_of_bytes)
    unit = 'bytes'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'KB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'MB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'GB'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)

    return str(number_of_bytes) + ' ' + unit
def leech(link):
    l = link.split('//')[1]
    l2 = 'https://test.com'+l
    r = requests.post(l2, data={'username': username, 'password': password, 'submit': 'Submit+Query'})
    r2 = requests.get('https://test.com',
                      headers={
                           'Accept': 'text/html,application/xhtml+xml,application/xml;'
                                     'q=0.9,image/avif,image/webp,*/*;q=0.8',
                           'Cookie': r.headers['Set-Cookie'].split(';')[0],
                           'Sec-Fetch-Dest': 'document',
                           'Sec-Fetch-Mode': 'navigate',
                           'Sec-Fetch-Site': 'none',
                           'Sec-Fetch-User': '?1',
                           'Upgrade-Insecure-Requests': '1'
                       }, allow_redirects=True)
    time.sleep(1)
    r3 = requests.post('test.com',
                       headers={
                           'Accept': 'text/html,application/xhtml+xml,application/xml;'
                                     'q=0.9,image/avif,image/webp,*/*;q=0.8',
                           'Cookie': r.headers['Set-Cookie'].split(';')[0],
                           'Sec-Fetch-Dest': 'document',
                           'Sec-Fetch-Mode': 'navigate',
                           'Sec-Fetch-Site': 'none',
                           'Sec-Fetch-User': '?1',
                           'Upgrade-Insecure-Requests': '1'

                       },
                       data={'link': link, 'premium_acc': 'on'})

    try:
        name = re.findall("type='hidden' name='filename' value='(.*?)'", r3.text, re.MULTILINE)[0]
        l = re.findall("name='link' value='(.*?)'", r3.text, re.MULTILINE)[0]
        host = re.findall("name='host' value='(.*?)'", r3.text, re.MULTILINE)[0]
        referer = re.findall("name='referer' value='(.*?)'", r3.text, re.MULTILINE)[0]
        path = re.findall("name='path' value='(.*?)'", r3.text, re.MULTILINE)[0]
        try:
            port = re.findall("name='port' value='(.*?)'", r3.text, re.MULTILINE)[0]
        except:
            pass
        try:
            cookie = re.findall("name='cookie' value='(.*?)'", r3.text, re.MULTILINE)[0]
        except:
            pass
        try:
            d = {'link': l, 'cookie': cookie, 'referer': referer, 'host': host, 'filename': name, 'path': path,
                 'port': port}
        except:
            try:
                d = {'link': l, 'cookie': cookie, 'referer': referer, 'host': host, 'filename': name, 'path': path}
            except:
                try:
                    d = {'link': l, 'referer': referer, 'host': host, 'filename': name, 'path': path, 'port': port}
                except:
                    d = {'link': l, 'referer': referer, 'host': host, 'filename': name, 'path': path}
        r4 = requests.post('test.com',
                           headers={
                           'Accept': 'text/html,application/xhtml+xml,application/xml;'
                                     'q=0.9,image/avif,image/webp,*/*;q=0.8',
                           'Cookie': r.headers['Set-Cookie'].split(';')[0],
                           'Sec-Fetch-Dest': 'document',
                           'Sec-Fetch-Mode': 'navigate',
                           'Sec-Fetch-Site': 'none',
                           'Sec-Fetch-User': '?1',
                           'Upgrade-Insecure-Requests': '1'

                       }, data=d)

        try:
            filename = parse.unquote(name).replace('.html', '')
            if '.' not in filename:
                filename = re.findall('">(.*?)<', r4.text, re.M)
                filename = filename[::-1][0]
            #f2 = re.findall('''lass='htmlerror'><b>Download: <a href="(.*?)"''', r4.text, re.MULTILINE)[0]
            f2 = re.findall('" download="(.*?)">', r4.text, re.M)
            f2 = f2[0].split('/files/')[0] + '/files/' + filename
            size = requests.head(f2)
            return {'name': filename, 'link': f2, 'size': bytes_2_human_readable(size.headers['Content-Length'])}
        except:
            r4 = requests.post('test.com',
                               headers={
                           'Accept': 'text/html,application/xhtml+xml,application/xml;'
                                     'q=0.9,image/avif,image/webp,*/*;q=0.8',
                           'Cookie': r.headers['Set-Cookie'].split(';')[0],
                           'Sec-Fetch-Dest': 'document',
                           'Sec-Fetch-Mode': 'navigate',
                           'Sec-Fetch-Site': 'none',
                           'Sec-Fetch-User': '?1',
                           'Upgrade-Insecure-Requests': '1'

                       }, data=d)
            f2 = re.findall('''lass='htmlerror'><b>Download: <a href="(.*?)"''', r4.text, re.MULTILINE)[0]
            size = requests.head(f2)
            return {'name': parse.unquote(name), 'link': f2[0], 'size': bytes_2_human_readable(size.headers['Content-Length'])}
    except Exception as f:
        return 'Link Is Deleted'
def leech3(link):
    l = link.split('//')[1]
    l2 = 'https://test.com='+l
    r = requests.post(l2, data={'username': username, 'password': password, 'submit': 'Submit+Query'})
    #print(r.text)

    r2 = requests.get('https://test.com=' + link,
                      headers={'Cookie': r.headers['Set-Cookie'].split(';')[0]
                       }, allow_redirects=True)
    try:
        link = re.findall('" download="(.*?)"', r2.text, re.M)[0]
        filename = link.split('/')[::-1][0]
        size = requests.head(link)
        return {'name': parse.unquote(filename), 'link': link,
                'size': bytes_2_human_readable(size.headers['Content-Length'])}
    except:
        return 'Link Is Deleted'

def leech2(link):
    l = link.split('//')[1]
    l2 = 'https://test.com='+l
    r = requests.post(l2, data={'username': username, 'password': password, 'submit': 'Submit+Query'})
    #print(r.text)

    r2 = requests.get('https://test.com?dl=' + link,
                      headers={'Cookie': r.headers['Set-Cookie'].split(';')[0]
                       }, allow_redirects=True)
    try:
        link = re.findall('" download="(.*?)"', r2.text, re.M)[0]
        filename = link.split('/')[::-1][0]
        size = requests.head(link)
        return {'name': parse.unquote(filename), 'link': link,
                'size': bytes_2_human_readable(size.headers['Content-Length'])}
    except:
        return 'Link Is Deleted'
def shutter(link):
    r = requests.post('https://shuttersaver.xyz/', data={'url': link})
    f = re.findall("\n(.*?)' ", r.text, re.MULTILINE)
    r2 = requests.get(f[0])
    f2 = re.findall('http-equiv="refresh" content="10; url=(.*?)"', r2.text, re.MULTILINE)
    r3 = requests.get(f2[0], allow_redirects=False)
    return r3.headers['Location']
def pic(link):
    if 'https://www.shutterstock.com/' in link:
        return shutter(link=link)
    else:
        r = requests.post('https://iglo.co.in/photo.php', data={'url': link})
        try:
            f = re.findall("a href='(.*?)' class='btn btn-success", r.text, re.MULTILINE)
            r2 = requests.get(f[0])
            f2 = re.findall('http-equiv="refresh" content="10; url=(.*?)"', r2.text, re.MULTILINE)
            return {'link': f2[0], 'type': 'link'}
        except:
            import base64, random
            imgstring = re.findall("href='data: image/png;base64,(.*?)'", r.text, re.MULTILINE)
            imgdata = base64.b64decode(imgstring[0])
            a = str(random.randrange(100000000, 1000000000000))
            filename = a + '.png'  # I assume you have a way of picking unique filenames
            with open(dirext+'/html/'+filename, 'wb') as f:
                f.write(imgdata)
            return {'type': 'link',
                    'link': 'http://20.56.254.19:8080/'+filename}

def googledrive(link):
    try:
        if 'open?id=' in link:
            l = link.split('open?id=')[1]
        if '/file/d' in link:
            l = link.split('/file/d/')[1]
            l = l.split('/')[0]
        t = 'https://www.googleapis.com/drive/v3/files/' + l + \
            '?alt=media&key=AIzaSyCoiW1ot9kh3b3x1B_KxGAj6UEs4jItVbI'
        r = requests.head(t)
        size = r.headers['Content-Length']
        ty = r.headers['Content-Type']
        return {'status': 'ok', 'size': bytes_2_human_readable(size), 'type': ty}
    except Exception as f:
        print(f)
        return {'status': 'error', 'error': str(f)}

def leecher(link):
    a = leech3(link)
    if a != 'Link Is Deleted' and a['link'] != 'h' and '.' in a['name']:
        return a
    b = leech2(link)
    if b != 'Link Is Deleted' and b['link'] != 'h' and '.' in b['name']:
        return b
    c = leech(link)
    if c != 'Link Is Deleted' and c['link'] != 'h' and '.' in c['name']:
        return c
    return 'Link Is Deleted'


