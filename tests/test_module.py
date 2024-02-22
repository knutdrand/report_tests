from report_tests.template import get_function_markdown
from . import example_module
from report_tests.module import get_module_markdown


def test_module_md():
    md = get_module_markdown(example_module)
    assert md.startswith('# example_module\n\nExample text\n\n')
    func1txt = get_function_markdown(example_module.test_example)
    assert func1txt in md
    func2txt = get_function_markdown(example_module.test_example2)
    assert func2txt in md
    assert md.count('```python') == 2
    assert md.count('```') == 4
    with open('example_module.md', 'w') as f:
        f.write(md)
