import webbrowser
urls =(
     '/', 'Myclass'
    '/about', 'secondClass'
)
class Myclass:
    def GET(self):
        return "<h1>Hello world</h1>"
class secondClass:
    def GET(self):
        return "<h1>This is a second route</h1>"
application=web.application(urls,globals()),wsgifunc()