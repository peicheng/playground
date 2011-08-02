import web

render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/shorten', 'shorten',
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return render.index(None)

class shorten:
    def POST(self):
        i = web.input()
        return render.index(url=i.url)

if __name__ == "__main__":
    app.run()
