from abc import ABC
class Printable(ABC):
#  @abstractmethod
 def print_info(self):
  pass
class Savable(ABC):
#  @abstractmethod
 def save(self):
  pass
class Document(Printable, Savable):
 def __init__(self, content):
  self.content = content
 def print_info(self):
  print(f"Content: {self.content}")
 def save(self):
  print("Document saved successfully.")
  
d=Document("sachin")
d.save()
print(d.content)
