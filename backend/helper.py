import os
import requests
from flask import current_app, make_response, jsonify

from prompt import prompt_template, chat
from constants import Framework, ResponseKeys, ErrorResponse

DIAGRAM_API_URL = os.environ.get('DIAGRAM_API')
EXTERNAL_API_URL = os.environ.get('EXTERNAL_DIAGRAM_API')
SVG_EXTENSION = 'svg'

MAX_RETRY = 10

DIAGRAM_API_HEADERS = {
    'Content-Type': 'text/plain'
}

FRAMEWORK_COLLECTION = ['plantuml', 'mermaid', 'blockdiag', 'bytefield', 'seqdiag', 'actdiag', 'nwdiag', 'packetdiag',
                        'rackdiag', 'c4plantuml', 'd2', 'dbml', 'ditaa', 'excalidraw', 'graphviz', 'nomnoml', 'pikchr',
                        'plantuml', 'structurizr', 'svgbob', 'vega', 'vegalite', 'wavedrom', 'wireviz']


def get_diagram_recipe(descroption="mindmap for happy life"):
    pif = prompt_template.format_messages(description=descroption)
    res = chat(pif)
    current_app.logger.info("LLM response {} for description {}".format(res.json(), descroption))
    with open("questions2.txt", "w") as file:
        file.write(res.content)
    qus = res.content
    return qus


def format_response(api_response):
    """
    """
    try:
        formatted_response = api_response.split('$$')
        response = {}
        for pair in formatted_response:
            key, value = pair.split('%^&')
            key = key.strip('\n')
            key = key.strip('`')
            value = value.strip('\n')
            value = value.strip('`')
            response[key] = value

        return response
    except Exception as err:
        current_app.logger.info("While processing Response for LLM error occur {}".format(err))
        return {'framework': '', 'diagram_code': '', 'metadata': '400'}


def build_diagram(framework, recipe, extension=SVG_EXTENSION):
    """
    """
    current_app.logger.info("building diagram for {} with recipe {}".format(framework, recipe))
    if framework in FRAMEWORK_COLLECTION:
        for curr in range(MAX_RETRY):
            try:
                if curr % 2:
                    api_url = DIAGRAM_API_URL
                else:
                    api_url = EXTERNAL_API_URL
                api_url = api_url + framework + '/' + SVG_EXTENSION
                recipe = process_code_recipe(recipe, framework)
                response = requests.request('POST', api_url, headers=DIAGRAM_API_HEADERS, data=recipe)

                if response.status_code == 200:
                    return response
            except:
                pass

        return ErrorResponse.text, ErrorResponse.status_code

    return ErrorResponse.text, ErrorResponse.status_code


def process_code_recipe(code_recipe, framework):
    """
    """
    if code_recipe.startswith(framework):
        code_recipe = code_recipe.strip(framework)

    current_app.logger.info("processed recipe for {} with final recipe {}".format(framework, code_recipe))
    return code_recipe
