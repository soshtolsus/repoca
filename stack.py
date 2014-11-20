class Stack:
	def __init__(self):
		self._head = None

	def __iter__(self):
		yield from iter(self._items)

	def pop(self):
		if self._head is None:
			return None
		else:
			to_return, self._head = self._head, self._head.prev
			return to_return

	def push(self, value):
		if self._head is None:
			self._head = Item(value, None)
		else:
			self._head = Item(value, self._head)

	def peek(self):
		return self._head

	def walk(self):
		current = self._head
		while current is not None:
			yield current.value
			current = current.prev

class Item:
	def __init__(self, value, prev):
		self.prev = prev
		self.value = value

	def __str__(self):
		return str(self.value)
