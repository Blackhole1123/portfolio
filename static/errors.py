from distutils.log import error
from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash, g, session, abort

errors = Blueprint(
    "errors",
    __name__,
    template_folder="./templates",
    static_folder="./static",
)

@errors.errorhandler('404')
def not_found(error):
    return '<h1>Error 404: Page not found</h1>', 404

@errors.errorhandler('500')
def internal_server_error(error):
    return '<h1>Error 500: Internal server error</h1>', 500

@errors.errorhandler('403')
def forbidden(error):
    return '<h1>Error 403: Forbidden</h1>', 403

@errors.errorhandler('401')
def unauthorized(error):
    return '<h1>Error 401: Unauthorized</h1>', 401

@errors.errorhandler('400')
def bad_request(error):
    return '<h1>Error 400: Bad request</h1>', 400

@errors.errorhandler('408')
def request_timeout(error):
    return '<h1>Error 408: Request timeout</h1>', 408

@errors.errorhandler('502')
def bad_gateway(error):
    return '<h1>Error 502: Bad gateway</h1>', 502

@errors.errorhandler('503')
def service_unavailable(error):
    return '<h1>Error 503: Service unavailable</h1>', 503

@errors.errorhandler('504')
def gateway_timeout(error):
    return '<h1>Error 504: Gateway timeout</h1>', 504