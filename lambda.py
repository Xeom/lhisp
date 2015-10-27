import scope
import AST

def lamb:
	def __init__(currScope, node):
		self.proto = currScope.copy()

		assert node.children[0] == "lambda"

		if len(node.children) < 2:
			raise SyntaxError("Lamda has no arguments")

		argsNode = node.children[1]

		if not isinstance(AST.HList, argsNode):
			raise SyntaxError("Lambda arguments not in list format")

		self.args = []
		for arg in argsNode.children:
			if not isinstance(AST.HName, arg):
				raise SyntaxError("Lambda arguments not a name")

			args.append(arg.text)

		self.lines = node.children[2:]

	def call(args):
		scope = scope.scope(self.proto)

		for name, value in zip(self.args):
			scope.set(name, value)

		for line in self.lines:
			Eval(line)
