from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash, g, session, abort

#no url prefix
errors = Blueprint('errors', __name__, template_folder='./templates', static_folder='./static')

@errors.app_errorhandler(404)
def error_404(error):
    message="Error 404: Page not found"
    return render_template('error.html', message=message), 404

@errors.app_errorhandler(500)
def error_500(error):
    message="Error 500: Internal server error"
    return render_template('error.html', message=message), 500

@errors.app_errorhandler(403)
def error_403(error):
    message="Error 403: Forbidden"
    return render_template('error.html', message=message), 403

@errors.app_errorhandler(400)
def error_400(error):
    message="Error 400: Bad request"
    return render_template('error.html', message=message), 400

@errors.app_errorhandler(401)
def error_401(error):
    message="Error 401: Unauthorized"
    return render_template('error.html', message=message), 401

@errors.app_errorhandler(405)
def error_405(error):
    message="Error 405: Method not allowed"
    return render_template('error.html', message=message), 405

@errors.app_errorhandler(502)
def error_502(error):
    message="Error 502: Bad gateway"
    return render_template('error.html', message=message), 502

@errors.app_errorhandler(503)
def error_503(error):
    message="Error 503: Service unavailable"
    return render_template('error.html', message=message), 503

@errors.app_errorhandler(504)
def error_504(error):
    message="Error 504: Gateway timeout"
    return render_template('error.html', message=message), 504