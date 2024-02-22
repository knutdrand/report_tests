# Markdown Example
from report_tests.function_info import get_function_info
import markdown

from report_tests.function_output import get_function_output

template = """\
## {Title}
{Documentation}

```python
{code}
```
"""
image_template = """![Output]({image_path}) """


def get_function_markdown(function):
    info = get_function_info(function)
    if info.description is None:
        info.description = ""
    output = get_function_output(function)
    if output is not None:
        image_text = image_template.format(image_path=output)
        image_text = f'\n{image_text}\n'
    else:
        image_text = ""
    return template.format(Title=info.title,
                           Documentation=info.description,
                           code=info.code) + image_text + "\n"


def get_html(function):
    md = get_function_markdown(function)
    return markdown.markdown(md)
