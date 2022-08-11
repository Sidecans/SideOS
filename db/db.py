import pickle
class db():
  def __init__(self, name):
    self.file = str(name) + ".sideDB"
  def dump(self, obj)
    with open(self.file, 'wb') as f:
      pickle.dump(obj, f)
  def load(self):
    with open(self.file, 'rb') as f:
      pickle.load(f)
      
