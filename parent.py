local_val = "bla bla bla"
def square(x):
  return x*x

class User:
  def __init__(self, name):
    self.name = name
  def say_hello(self):
    return "hello"


if __name__ == "__main__":
  print("the file is being executed directly")
else:
  print("the file is being executed because it is imported by another file. The file is called:", __name__)