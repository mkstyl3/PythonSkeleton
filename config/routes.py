# Add imports
from controllers.user_controller import UserController

# Add routes
routes = [
    {'method': 'get', 'path': '/user', 'resource': 'UserController:get'},
    {'method': 'post', 'path': '/save/user', 'resource': 'UserController:set'},
]