import dataclasses
import inspect


@dataclasses.dataclass
class FunctionInfo:
    title: str
    description: str
    code: str


def remove_title_anddocstring(code: str) -> str:
    lines = code.split("\n")
    if lines[0].startswith("def "):
        lines = lines[1:]
    if lines[0].strip().startswith('"""') or lines[0].strip().startswith("'''"):
        for i, line in enumerate(lines):
            if line.strip().endswith('"""') or line.strip().endswith("'''"):
                if i== 0 and len(line.strip()) == 3:
                    continue
                lines = lines[i+1:]
                break
        else:
            raise Exception('''Invalid docstring'''+str(lines))
    return "\n".join(lines)


def remove_init_tab(code):
    lines = code.split("\n")
    if lines[0].startswith("    "):
        lines = [line[4:] for line in lines]
    elif lines[0].startswith("\t"):
        lines = [line[1:] for line in lines]
    return "\n".join(lines)


def get_function_info(function):
    title = function.__name__
    description = function.__doc__
    if description is None:
        description = ""
    # remove indents from docstring
    description = inspect.cleandoc(description)
    # description = description
    code = inspect.getsource(function)
    code = remove_title_anddocstring(code)
    code = remove_init_tab(code)
    return FunctionInfo(title, description, code)
