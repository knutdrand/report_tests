# Markdown Example
from report_tests.function_info import get_function_info

template = """\
# {Title}
{Documentation}

```python
{code}
```
"""
image_template = """![Output]({image_path}) """


def get_function_markdown(function):
    info = get_function_info(function)
    return template.format(Title=info.title,
                           Documentation=info.description,
                           code=info.code)
