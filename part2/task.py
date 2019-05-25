import argparse
from antlr4 import *
from task_1Lexer import task_1Lexer
from task_1Listener import task_1Listener
from task_1Parser import task_1Parser
from antlr4.tree.Trees import Trees

def get_token_type(token):
    if token.type == task_1Lexer.COMMAND:
        return "COMMAND"
    elif token.type == task_1Lexer.REG:
        return "REG"
    elif token.type == task_1Lexer.IMMEDIATE:
        return "IMMEDIATE"
    elif token.type == task_1Lexer.MEMORY:
        return "MEMORY"
    else:
        return "ERROR UNKNOWN TOKEN"

def main():

    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)
    lexer = task_1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = task_1Parser(token_stream)

    token = lexer.nextToken()
    output = ""
    while not token.type == Token.EOF:
        if not(token.type == task_1Lexer.SEPARATOR or token.type == task_1Lexer.NEWLINE or token.type == task_1Lexer.SPACE):
            output += get_token_type(token) + ' ' + token.text + '\n'
        token = lexer.nextToken()

    result = open("task_result.txt", "w")
    result.write(output)
    result.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()

    print(args.file)

    main()
