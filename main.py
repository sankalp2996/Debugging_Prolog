import lexer
import parser


def main():

    content = ""

    with open('test.lang', 'r') as file1:
        content = file1.read()

    lex = lexer.Lexer(content)
    tokens = lex.tokenize()

    #parse1 = parser.Parser(tokens)
    #objects = parse1.parse()


main()
