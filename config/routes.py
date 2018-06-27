# Add imports
from controllers.user_controller import UserController

# Add routes
routes = [
    {'method': 'get', 'path': '/user/get', 'resource': 'UserController:get'},
    {'method': ['post', 'put'], 'path': '/user/set', 'resource': 'UserController:set'},
]