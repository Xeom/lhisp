#!/usr/bin/python

# AST node.
class HNode:

    types = []

    def getnode(text):
        for i in types:
            if i.match(text) == True:
                return i.fromtext(types)

    def fromtext(text):
        raise NotImplementedError()

    def match(text):
        raise NotImplementedError()

class HList(HNode):

    def fromtext(text):
        text = text.strip()[1:-1]
        children = []
        while len(text):
            atom, size = (text)
            children += atom
            text = text[size:].strip()

        return HList(children)

    def match(text):
        pass
