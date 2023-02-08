import cherrypy

class Test(object):
    @cherrypy.expose
    def test(self):
        html_body = \
        """
        <h3>this is test</h3>
        """
        return html_body

# if __name__ == '__main__':
#     cherrypy.quickstart(Test().test())