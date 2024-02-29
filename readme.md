'''
Homework 5 - leveraging a simple calculator approach, I developed an app with commmands and then converted the architecture into plugins.
'''

##1. Set up command branch, which covers REPL (read, eval, print, loop) by adding four basis calculator commands: add, subtract, multiply, and divide.

##2. Set up a menu command, which involved dynamically passing the list of command names to a new MenuCommand so it can display available commands.

##3. Achieved near 100% in testing files
'''
### Name                                Stmts   Miss  Cover
-------------------------------------------------------
# app/__init__.py                        28      0   100%
# app/commands/__init__.py               16      1    94%
# app/commands/add/__init__.py           16      0   100%
# app/commands/divide/__init__.py        21      2    90%
# app/commands/exit/__init__.py           5      0   100%
# app/commands/greet/__init__.py          4      0   100%
# app/commands/menu/__init__.py           8      0   100%
# app/commands/multiply/__init__.py      16      0   100%
# app/commands/subtract/__init__.py      16      0   100%
# tests/__init__.py                       0      0   100%
# tests/test_app.py                      16      0   100%
# tests/test_commands.py                109      0   100%
-------------------------------------------------------
# TOTAL                                 255      3    99%
'''
##4. Developed Plugin Architecture via plugins branch



