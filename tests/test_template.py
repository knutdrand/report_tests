import os

from report_tests.template import get_function_markdown, get_html
from .fixtures import example_function, plotting_function


def test_get_function_markdown():
    md = get_function_markdown(example_function)
    open('example.md', 'w').write(md)
    truth = """\
## example_function
This is an example function.

```python
return 1

```
"""
    print(truth)
    print(md)
    assert md == truth


def test_get_function_markdown_plotting():
    md = get_function_markdown(plotting_function)
    open('plotting_function.md', 'w').write(md)
    assert md.strip().endswith("""![Output](plotting_function.png)""")


def test_to_html():
    html = get_html(example_function)
    print(html)
    with open('example.html', 'w') as f:
        # print cwd
        print(os.getcwd())
        f.write(html)

def test_plot_html():
    html = get_html(plotting_function)
    with open('plotting_function.html', 'w') as f:
        f.write(html)
