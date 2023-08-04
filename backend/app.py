import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, render_template, send_from_directory


from constants import ErrorResponse, STANDARD_KEY_VALUE_DELIMETER, SVG_KEY_VALUE_DELIMETER, STANDARD_PAIR_DELIMETER, SVG_PAIR_DELIMETER
from helper import get_diagram_recipe, format_response, build_diagram, get_svg

app = Flask(
    __name__,
    static_url_path='',
    static_folder='frontend/build',
    template_folder='frontend/build'
)

# set up the file handler
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
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


def handle_diagram_prompt_response(response, user_input):
    response = format_response(response, STANDARD_KEY_VALUE_DELIMETER, STANDARD_PAIR_DELIMETER)
    if "200" not in response.get("metadata", ""):
        return None

    framework = response.get('framework')
    recipe = response.get('diagram_code')
    diagram = build_diagram(framework=framework, recipe=recipe)
    if diagram:
        return diagram.text, diagram.status_code
    return None


def handle_svg_prompt_response(response):
    svg_response = format_response(response, SVG_KEY_VALUE_DELIMETER, SVG_PAIR_DELIMETER)
    return svg_response.get("svg_response"), 200 if "200" in svg_response.get("metadata", "") else None


@app.route('/call_prompt', methods=['GET', 'POST'])
def call_prompt():
    data = request.get_json()
    user_input = data.get('input')
    response = get_diagram_recipe(description=user_input)

    diagram_response = handle_diagram_prompt_response(response, user_input)
    if diagram_response:
        return diagram_response

    svg_response = get_svg(description=user_input)
    svg_response_result = handle_svg_prompt_response(svg_response)
    if svg_response_result:
        return svg_response_result

    return ErrorResponse.text, ErrorResponse.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))
