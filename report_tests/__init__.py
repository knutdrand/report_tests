"""Top-level package for Report Tests."""

__author__ = """Knut Rand"""
__email__ = 'knutdrand@gmail.com'
__version__ = '0.0.1'

from .template import get_function_markdown as get_markdown

DO_SHOW = False


def disable_show():
    global DO_SHOW
    DO_SHOW = False


def enable_show():
    global DO_SHOW
    DO_SHOW = True


def show(fig):
    if DO_SHOW:
        fig.show()
    return fig
