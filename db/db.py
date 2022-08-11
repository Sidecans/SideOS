import pickle
class db():
  def __init__(self, obj, name):
    self.file = name + ".sideDB"
    with open(self.file, 'wb') as f:
      pickle.dump(obj, f)
    
