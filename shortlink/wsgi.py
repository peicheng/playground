import web
import random
import string
import redis
import urlparse

render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/(.*)', 'redirect',
)

app = web.application(urls, globals())

r= redis.Redis(host='d6d77854.dotcloud.com', port=8603, password="6Mb3Y1IzxFaqmjM0CB4k", db=0)
#r= redis.Redis(host='localhost', port=6379, db=0)

class index:
    def GET(self):
        return render.index(url=None, shortcode=None)
    
    def POST(self):
        i = web.input()
        url = i.url
        if urlparse.urlparse(url)[0] == '' and urlparse.urlparse(url)[1] == '':
            return render.index(url=None, shortcode=None, err="error")
        else:
            shortcode = r.get("shortcode:%s" % url)
            if shortcode == None:
                while True:
                    shortcode = ''.join(random.choice(string.letters + string.digits) for x in range(6))
                    if r.get("url:%s" % shortcode) == None:
                        r.set("url:%s" % shortcode, url)
                        break
                    r.set("shortcode:%s" % url, shortcode)
            return render.index(url=url, shortcode=shortcode)

class redirect:
    def GET(self, shortcode):
        url = r.get("url:%s" % shortcode)
        if url != None:
            raise web.seeother(url)

application = app.wsgifunc()

if __name__ == "__main__":
    app.run()
