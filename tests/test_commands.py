import pytest
from app import App
from app.commands.exit import ExitCommand
from app.commands.greet import GreetCommand

def test_greet_command(capfd):
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_exit_command(capfd):
    command = ExitCommand()
    with pytest.raises(SystemExit) as e:  # Expect a SystemExit exception
        command.execute()
    assert str(e.value) == "Exiting...", "The exit message did not match expected output."

    """command.execute()
    out, err = capfd.readouterr()
    assert out == "Exit\n", "The GreetCommand should print 'Hello, World!'"""

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
    

    """'''My calculator test'''
import pytest
from app import add, subtract, multiply, divide

# pylint: disable=invalid-name

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (0, 0, 0),
    (-1, -1, -2),
    (100, 100, 200)
])
def test_addition(a, b, expected):
    '''Test addition with multiple inputs to ensure correctness'''
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 0),
    (0, 0, 0),
    (-1, -1, 0),
    (100, 50, 50)
])
def test_subtraction(a, b, expected):
    '''Test subtraction with various inputs'''
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (0, 0, 0),
    (-1, -1, 1),
    (10, 5, 50)
])
def test_multiply(a, b, expected):
    '''Test multiplication for correct results across different scenarios'''
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 1),
    (0, 1, 0),
    (-1, -1, 1),
    (10, 5, 2)
])
def test_divide(a, b, expected):
    '''Test division, including edge cases'''
    assert divide(a, b) == expected

def test_divide_by_zero():
    '''Ensure division by zero is handled, if applicable'''
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
"""