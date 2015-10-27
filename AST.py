#!/usr/bin/python

# AST node.
class HNode:

    types = []

    def fromtext(text):
        for t in HNode.types:
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
HNode.types.append(HList)

class HSymbol(HNode):

    def __init__(self, symbol):
        self.symbol = symbol

    def fromtext(text):
        t = text.split()[0].split(str=")")[0]
        if not t in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            raise SyntaxError()
        return len(t), HSymbol(t)
HNode.types.append(HSymbol)

class HNumber(HNode):

    def __init__(self, value):
        self.value = value

    def fromtext(text):
        ilen = len(text)
        text.lstrip()
        b = text.split()[0].split(str=")")[0]
        if not b[0] in "0123456789":
            raise SyntaxError()
        return ilen - len(text) + len(b), int(b)
HNode.types.append(HNumber)

class HString(HNode):

    def __init__(self, value):
        self.value = value

    def fromtext(text):
        ilen = len(text)
        text.lstrip()

        if text[0] != '"':
            raise SyntaxError()

        text = text[1:]
        res = None

        for i in range(len(text)):
            if text[i] == '"':
                res = i
                break

        if res == None:
            raise SyntaxError()

        return 2 + i, HString(text[0:i])
HNode.types.append(HString)
