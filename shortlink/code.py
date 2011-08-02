import web

render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/shorten', 'shorten',
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return render.index()

class shorten:
    def POST(self):
        i = web.input()
        return i.url

if __name__ == "__main__":
    app.run()
