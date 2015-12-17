from urllib.request import urlopen
import io

def get_robots_txt(url):
        if url.endswith('/'):
                path = url
        else:
                path = url + '/'
        try:
                
                req = urlopen(path + "robots.txt", data=None)
                data = io.TextIOWrapper(req, encoding='utf-8')
                return data.read()

        except Exception as e:
                return "Recalling robots_txt failed"




