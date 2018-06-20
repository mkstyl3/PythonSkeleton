from falcon_cors import CORS

# from falcon_require_https import RequireHTTPS
# from falcon_multipart.middleware import MultipartMiddleware

middlewares = []

cors = CORS(allow_all_origins=['*'], allow_methods_list=['POST', 'PUT', 'GET'],
            allow_headers_list=['Content-Type', 'Accept', 'Authorization'], max_age=300)
middlewares.append(cors.middleware)

# middlewares.append(RequireHTTPS())
# middlewares.append(MultipartMiddleware())

