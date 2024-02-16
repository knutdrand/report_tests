import os

from report_tests.template import get_function_markdown, get_html
from .fixtures import example_function


def test_get_function_markdown():
    md = get_function_markdown(example_function)
    open('example.md', 'w').write(md)
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

def test_to_html():
    html = get_html(example_function)
    print(html)
    with open('example.html', 'w') as f:
        # print cwd
        print(os.getcwd())
        f.write(html)

