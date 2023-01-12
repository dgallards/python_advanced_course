# Do not run code!!! copy and paste code into server.py and run through console!

import tornado.ioloop 
import tornado.web
import json



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/index.html")
    def post(self):
        searchterm = self.get_argument('searchterm')
        self.render("html/searchpage.html", searchterm=searchterm)
        
class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        vehiculos = ""
        with open("resources/vehiculos.json", "r") as f:
            vehiculos = json.dumps(json.load(f))
            self.write(vehiculos)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/vehiculos",ApiHandler),
        (r"/html/(.*)", tornado.web.StaticFileHandler, {"path": "html"}), # Nos hace la vida más sencilla 
        (r"/resources/(.*)", tornado.web.StaticFileHandler, {"path": "resources"}), # sirve los recursos
        
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started on port 8888")
    tornado.ioloop.IOLoop.current().start()