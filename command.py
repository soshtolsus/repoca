class Command:
	def __init__(self, number_of_arguments, number_of_returns, func):
		self.number_of_arguments = number_of_arguments
		self.number_of_returns = number_of_returns
		self.func = func

	def __call__(self, stack):
		result = self.func(stack, *[stack.pop().value for _ in range(self.number_of_arguments)])

		if self.number_of_returns > 0:
			stack.push(result)