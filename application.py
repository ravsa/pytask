from jinja2config import JinjaConfig
from redisworks import Root
from scrapy import FetchData
import cherrypy
import os


root = Root(host='0.0.0.0', port=6379, db=0)


class Application(object):

    @cherrypy.expose
    def index(self):
        template = JinjaConfig.JINJA_ENVIRONMENT.get_template('index.html')
        return template.render(data=root.data)


cherrypy.config.update({
    'environment': 'production',
    'log.screen': True,
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 8080,
})

conf = {
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(JinjaConfig.BASE_DIR, 'static'),
        'tools.staticdir.content_types': {'html': 'application/octet-stream'}
    }
}

if __name__ == "__main__":
    fetch_data = FetchData()
    fetch_data.start()
    cherrypy.quickstart(Application(), '/', config=conf)
