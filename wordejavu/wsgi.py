import web
from web.contrib.template import render_mako

render = render_mako(directories=['templates'],
                     input_encoding='utf-8',
                     output_encoding='utf-8')

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self, name):
        return render.index(name=name)

if __name__ == '__main__':
    app.run()
