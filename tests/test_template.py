from report_tests.template import get_function_markdown
from .fixtures import example_function

def test_get_function_markdown():
    md = get_function_markdown(example_function)
    print(md)
    truth = """\
# example_function
This is an example function.

```python
def example_function():
    '''This is an example function.'''
    return 1

```
"""
    print(truth)
    assert md == truth
