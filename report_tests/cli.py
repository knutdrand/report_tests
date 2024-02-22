"""Console script for report_tests."""
import os
import importlib
from .module import get_module_markdown
import importlib.util
import sys
from . import enable_show, disable_show
import typer
import logging

logger = logging.getLogger(__name__)

def load_module(module_filename: str):
    spec = importlib.util.spec_from_file_location("module.name", module_filename)
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
    return foo


def main_function(module_filename: str):
    '''
    This function should just be type hinted with common types,
    and it will run as a command line function
    Simple function

    >>> main()
    '''
    logging.basicConfig(level=logging.INFO)
    disable_show()
    # import the module
    logger.info(f"Creating report for {module_filename}")
    assert module_filename.endswith('.py')
    # import the module given in module_filename
    module = load_module(module_filename)
    markdown = get_module_markdown(module)
    md_filename = module_filename.replace('.py', '.md')
    with open(md_filename, 'w') as f:

        f.write(markdown)
    print(f"Report written to {md_filename}")
    # Create pdf with pandoc
    os.system(f'pandoc {md_filename} -o {md_filename.replace(".md", ".pdf")}')



def main():
    typer.run(main_function)


if __name__ == "__main__":
    main()
