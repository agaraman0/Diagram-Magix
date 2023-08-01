import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, render_template, send_from_directory


from constants import ErrorResponse
from helper import get_diagram_recipe, format_response, build_diagram

app = Flask(
    __name__,
    static_url_path='',
    static_folder='frontend/build',
    template_folder='frontend/build'
)

# set up the file handler
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
# set the log level in the handler
handler.setLevel(logging.DEBUG)

# set up the formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handler to the logger
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)  # set level to DEBUG


@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return ErrorResponse.text, ErrorResponse.status_code


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return ErrorResponse.text, ErrorResponse.status_code


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return ErrorResponse.text, ErrorResponse.status_code


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/call_prompt', methods=['GET', 'POST'])
def call_prompt():
    data = request.get_json()
    user_input = data.get('input')
    response = get_diagram_recipe(descroption=user_input)
    response = format_response(response)
    app.logger.info("formatted response {}".format(response))
    if "200" in response.get("metadata", ""):
        framework = response.get('framework')
        recipe = response.get('diagram_code')
        diagram = build_diagram(framework=framework, recipe=recipe)
        app.logger.info("here is your diagram response {}".format(diagram))
        return diagram.text, diagram.status_code
    return ErrorResponse.text, ErrorResponse.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))
