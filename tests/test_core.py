import pytest

from starter import greet
from starter.cli import main


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_name():
    assert greet("  Ada ") == "Hello, Ada!"


def test_greet_empty_raises():
    with pytest.raises(ValueError):
        greet("   ")


def test_cli(capsys):
    assert main(["Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"
