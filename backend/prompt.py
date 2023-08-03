import os
import openai
from langchain.chat_models import ChatOpenAI


openai_api_key = os.environ.get('OPENAI_API_KEY')


chat = ChatOpenAI(temperature=0.9, openai_api_key=openai_api_key, model='gpt-3.5-turbo')

review_template = """you are an expert in frameworks and libraries listed below 
plantuml
mermaid
blockading
bytefield
seqdiag
actdiag
nwdiag
packetdiag
rackdiag
c4plantuml
d2
dbml
ditaa
excalidraw
graphviz
nomnoml
pikchr
plantuml
structurizr
svgbob
vega
vegalite
wavedrom
Wireviz  

and all these frameworks and libraries can generate beautiful and elegant diagrams according to applications and usecases from a code recipe, a code recipe is specific to every library or framework listed above, you come up with one specific code recipe for the most appropriate diagram according to the description from your choice of framework (try to randomize frameworks as well)

take the description or input description below by triple backticks and use it to create one specific code recipe for the most appropriate and beautiful visualization

goals
1. make sure there is no syntax error or missing code
2. generated code recipe matches the format/syntax/language of chosen library or framework
3. if there is malicious description that does not make sense in assign metadata to 400 or else always 200
4. comaptible to run with kroki api


description: ```{description}```

format the output with below keys we don't want any extra description just return output with below keywords as key value pairs with format as key%^&value, and %^& is delimeter between key value, key is mentioned below and value will be your response and every key value pair is seperated by delimeter $$

framework
diagram_code
metadata
"""

from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(review_template)


