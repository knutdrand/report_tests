import inspect

from .template import get_function_markdown
import logging

logger = logging.getLogger(__name__)

template = """\
# {Title}
{Documentation}

{functions}
"""


def get_module_markdown(module):
    docstring = module.__doc__
    title = module.__name__.split('.')[-1]
    functions = ""
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            # check if is test
            if name.startswith('test_'):
                logger.info(f"Running function {name}")
                functions += get_function_markdown(obj)
    return template.format(Title=title, Documentation=docstring, functions=functions)
