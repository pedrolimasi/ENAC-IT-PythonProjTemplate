from my_project.foo import bar


def test_bar():
    # Test the return type
    assert isinstance(bar(), str)
