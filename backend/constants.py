from enum import Enum

response = """<svg xmlns="http://www.w3.org/2000/svg" width="300" height="80" style="background-color:#f2f2f2;">
    <text x="50%" y="50%" font-family="'Lucida Handwriting', 'cursive'" font-size="20px" text-anchor="middle" alignment-baseline="middle" fill="#ff6347">Sorry, I Failed You 😔</text>
</svg>
"""

STANDARD_KEY_VALUE_DELIMETER = '%^&'
STANDARD_PAIR_DELIMETER = '$$'

SVG_KEY_VALUE_DELIMETER = "#&*"
SVG_PAIR_DELIMETER = "@#&"


class ErrorResponse:
    text = response
    status_code = 500


class Framework(Enum):
    MERMAID = "mermaid"
    PLANTUML = 'plantuml'
    C4PLANTUML = 'c4plantuml'
    BLOCKDIAG = 'blockdiag'
    BYTEFIELD = 'bytefield'
    SEQDIAG = 'seqdiag'
    ACTDIAG = 'actdiag'
    NWDIAG = 'nwdiag'
    PACKETDIAG = 'packetdiag'
    RACKDIAG = 'rackdiag'
    D2 = 'd2'
    DBML = 'dbml'
    DITAA = 'ditaa'
    EXCALIDRAW = 'excalidraw'
    GRAPHVIZ = 'graphviz'
    NOMNOML = 'nomnoml'
    PIKCHR = 'pikchr'
    STRUCTURIZR = 'structurizr'
    SVGBOB = 'svgbob'
    VEGA = 'vega'
    VEGALITE = 'vegalite'
    WAVEDROM = 'wavedrom'
    WIREVIZ = 'wireviz'


class ResponseKeys(Enum):
    DIAGRAM_CODE = 'diagram_code'