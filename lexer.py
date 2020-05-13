import re


class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):

        tokens = []
        location = []
        source_code = self.source_code.split()
        source_index = 0

        while source_index < len(source_code):

            word = source_code[source_index]

            for i in range(0, len(word)):

                if re.match('[a-z]', word[i]) or re.match('[A-Z]', word[i]):
                    tokens.append(['IDENTIFIER', word[i]])
                    location.append(source_index)

                elif re.match('[0-9]', word[i]):
                    tokens.append(['Integer', word[i]])
                    location.append(source_index)

                elif word[i] == "!":
                    tokens.append(['NOT', word[i]])
                    location.append(source_index)

                elif word[i] == ",":
                    tokens.append(['Comma', word[i]])
                    location.append(source_index)

                elif word[i] == "(":
                    tokens.append(['LAPR', word[i]])
                    location.append(source_index)

                elif word[i] in ")":
                    tokens.append(['RPAR', word[i]])
                    location.append(source_index)

                elif word[i] == "<":
                    if word[i+1] == "=" and word[i+2] == ">":
                            tokens.append(['IFF', word[i]+word[i+1]+word[i+2]])
                            location.append(source_index)

                elif word[i] == "=" and word[i+1] == ">" and word[i-1] != "<":
                    tokens.append(['IMPLIES', word[i]+word[i+1]])
                    location.append(source_index)

                elif word[i] == "/" and word[i+1] == "\\":
                    tokens.append(['AND', word[i]+word[i+1]])
                    location.append(source_index)

                elif word[i] == "\\" and word[i+1] == "/":
                        tokens.append('OR')
                        location.append(source_index)
            i += 1

            source_index += 1

        print(tokens)
        print(location)

        return tokens
