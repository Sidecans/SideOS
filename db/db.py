import pickle
class db():
  def __init__(self, obj, name):
    self.file = name + ".sidebot"
    with open(self.file, 'wb') as f:
      pickle.dump(obj, f)
    
