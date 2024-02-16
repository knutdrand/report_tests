import dataclasses
import inspect


@dataclasses.dataclass
class FunctionInfo:
    title: str
    description: str
    code: str


def get_function_info(function):
    title = function.__name__
    description = function.__doc__
    code = inspect.getsource(function)
    return FunctionInfo(title, description, code)
