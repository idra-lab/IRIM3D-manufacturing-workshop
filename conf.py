import os
import sys

newpath = os.path.abspath(os.path.join(__file__, '../..'))
print(newpath)
sys.path.insert(0, newpath)

project = "Industry 5.0: Workplace Transformation with Next Generation Smart Robots"
copyright = 'IDRA - 2025'
author = 'Matteo Dalle Vedove'
html_title = "Industry 5.0: Workplace Transformation with Next Generation Smart Robots"
# release = 'v0.0'

extensions = [
    "myst_parser",
]

source_suffix = ['.rst', '.md']

pygments_style = 'sphinx'

html_theme = 'furo'
autosummary_generate = True

html_static_path = ['_static', 'images/']
html_css_files = [
    'css/style.css',
]

exclude_patterns = [".venv/**"]

# def setup(app):
#     app.add_css_file("css/style.css")

from docutils import nodes
from docutils.parsers.rst import Directive, directives

class person_node(nodes.General, nodes.Element):
    pass

class PersonDirective(Directive):
    has_content = True
    required_arguments = 0  
    optional_arguments = 0
    option_spec = {
        'name': directives.unchanged,
        'affiliation': directives.unchanged,
        'photo': directives.unchanged,
    }

    def run(self):
        name = self.options.get('name', '')
        affiliation = self.options.get('affiliation', '')
        photo = self.options.get('photo', '')
        description = '\n'.join(self.content)

        # Build raw HTML
        html = f"""
<div class="person-card">
    <img src="{photo}" alt="{name} Photo" class="person-photo">
    <div class="person-info">
        <div class="person-name">{name}</div>
        <div class="person-affiliation">{affiliation}</div>
        <div class="person-description">
            {description}
        </div>
    </div>
</div>
"""
        return [nodes.raw('', html, format='html')]

def setup(app):
    app.add_directive("person", PersonDirective)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
