import falcon

from utils.router import Router

from utils.cors import middlewares


app = falcon.API(middleware=middlewares)

Router(app)

# def main():


# main()
