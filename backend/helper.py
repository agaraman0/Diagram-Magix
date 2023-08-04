import os
import requests
from flask import current_app, make_response, jsonify

from prompt import prompt_template, chat, svg_prompt_template

DIAGRAM_API_URL = os.environ.get('DIAGRAM_API')
EXTERNAL_API_URL = os.environ.get('EXTERNAL_DIAGRAM_API')
SVG_EXTENSION = 'svg'

MAX_RETRY = 4

DIAGRAM_API_HEADERS = {
    'Content-Type': 'text/plain'
}

FRAMEWORK_COLLECTION = ['plantuml', 'mermaid', 'blockdiag', 'bytefield', 'seqdiag', 'actdiag', 'nwdiag', 'packetdiag',
                        'rackdiag', 'c4plantuml', 'd2', 'dbml', 'ditaa', 'excalidraw', 'graphviz', 'nomnoml', 'pikchr',
                        'plantuml', 'structurizr', 'svgbob', 'vega', 'vegalite', 'wavedrom', 'wireviz']


def get_diagram_recipe(description="mindmap for happy life"):
    pif = prompt_template.format_messages(description=description)
    res = chat(pif)
    current_app.logger.info("LLM response {} for description {}".format(res.json(), description))
    qus = res.content
    return qus


def get_svg(description="happy life path"):
    template = svg_prompt_template.format_messages(description=description)
    response = chat(template)
    current_app.logger.info("LLM svg response {} for description {}".format(response.json(), description))
    llm_response = response.content
    return llm_response


def format_response(api_response, key_value_delimeter, pair_delimeter):
    """
    """
    try:
        api_response = api_response.strip('`') if api_response.startswith('`') or api_response.endswith('`') else api_response
        api_response = api_response.strip('\n') if api_response.startswith('\n') or api_response.endswith('\n') else api_response
        api_response = api_response.strip(pair_delimeter) if api_response.startswith(pair_delimeter) or api_response.endswith(pair_delimeter) else api_response
        formatted_response = api_response.split(pair_delimeter)
        response = {}
        for pair in formatted_response:
            key, value = pair.split(key_value_delimeter)
            key = key.strip('\n')
            key = key.strip('`')
            value = value.strip('\n')
            value = value.strip('`')
            response[key] = value

        current_app.logger.info("formatted and processed response {}".format(response))

        return response
    except Exception as err:
        current_app.logger.info("While processing Response for LLM error occur {}".format(err))
        return {}


def try_building_diagram(api_url, recipe):
    try:
        response = requests.request('POST', api_url, headers=DIAGRAM_API_HEADERS, data=recipe, timeout=7)
        return response if response.status_code == 200 else None
    except Exception as err:
        current_app.logger.info("Exception occur {}".format(err))
        return None


def build_diagram(framework, recipe, extension=SVG_EXTENSION):
    current_app.logger.info("building diagram for {} with recipe {}".format(framework, recipe))

    if framework not in FRAMEWORK_COLLECTION:
        return None

    recipe = process_code_recipe(recipe, framework)
    current_app.logger.info("here is processed code recipe {}".format(recipe))
    for curr in range(MAX_RETRY):
        api_url = DIAGRAM_API_URL if curr % 2 else EXTERNAL_API_URL
        api_url += framework + '/' + SVG_EXTENSION
        response = try_building_diagram(api_url, recipe)
        current_app.logger.info("current request count {} and response {}".format(curr, response))
        if response:
            return response

    return None


def process_code_recipe(code_recipe, framework):
    """
    """
    if code_recipe.startswith(framework):
        code_recipe = code_recipe.strip(framework)

    current_app.logger.info("processed recipe for {} with final recipe {}".format(framework, code_recipe))
    return code_recipe
