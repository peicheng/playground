import web
import random
import string

render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/shorten', 'shorten',
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return render.index(None, None)

class shorten:
    def POST(self):
        i = web.input()
        shortcode = ''.join(random.choice(string.letters + string.digits) for x in range(6))
        return render.index(url=i.url, shortcode=shortcode)

if __name__ == "__main__":
    app.run()
