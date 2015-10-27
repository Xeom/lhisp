#!/usr/bin/python

# AST node.
class HNode:

    types = []

    def fromtext(text):
        for t in types:
            try:
                return t.fromtext(text)
            except:
                pass
        raise SyntaxError()

class HList(HNode):

    def __init__(self, children):
        self.children = children

    def fromtext(text):

        ilen = len(text)

        children = []
        text.lstrip()

        if text[1] != '(':
            raise SyntaxError()

        text = text[1:]
        text.lstrip()

        try:
            while text[0] != ')':
                atom, size = HNode.fromtext(text)
                children += atom
                text = text[size:]
                text.lstrip()
        except:
            raise SyntaxError()

        text = text[1:]

        return ilen - len(text), HList(children)
