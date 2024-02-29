from app.commands import CommandHandler
from app.commands.greet import GreetCommand
from app.commands.exit import ExitCommand
from app.commands.add import addCommand
# from app.commands.subtract import subtractCommand
# from app.commands.multiply import multiplyCommand
# from app.commands.divide import divideCommand
# from app.commands.menu import MenuCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("add", addCommand())
        # self.command_handler.register_command("divide", divideCommand())
        # self.command_handler.register_command("multiply", multiplyCommand())
        # self.command_handler.register_command("subtract", subtractCommand())
        # self.command_handler.register_command("menu", MenuCommand)

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip()
            parts = user_input.split(maxsplit=1)
            command_name = parts[0] if parts else ''
            args = parts[1].split() if len(parts) > 1 else []
            
            # Execute the command with any argument that were provided
            if command_name:
                self.command_handler.execute_command(command_name, *args)
