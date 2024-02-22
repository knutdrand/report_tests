from report_tests.function_info import get_function_info
from tests.fixtures import example_function, example_function2, example_function3, example_function4

import pytest

@pytest.mark.parametrize("func", [example_function, example_function2, example_function3, example_function4])
def test_get_function_info(func):
    info = get_function_info(func)
    assert info.title==func.__name__# "example_function"
    assert info.description.strip()=="This is an example function."
    assert info.code=="return 1\n"
