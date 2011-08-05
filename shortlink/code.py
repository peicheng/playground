import web
import random
import string
import redis

render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/(.*)', 'redirect',
)

app = web.application(urls, globals())

r= redis.Redis(host='localhost', port=6379, db=0)

class index:
    def GET(self):
        return render.index(None, None)
    
    def POST(self):
        i = web.input()
        url = i.url
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
        return render.index(url=None, shortcode=shortcode)

application = app.wsgifunc()

if __name__ == "__main__":
    app.run()
