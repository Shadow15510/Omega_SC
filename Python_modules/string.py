class String(str):
  def __init__(self, txt = ""):
    self.txt = txt
    
  def capitalize(self):
    return self.txt[0].upper() + self.txt[1:].lower()

  def center(self, width, fillchar = " "):
    result = (width - len(self.txt)) // 2 * fillchar + self.txt
    return result + (width - len(result)) * fillchar

  def expendtabs(self, tabsize = 8):
    return self.txt.replace("\t", tabsize * " ")

  def isalnum(self):
    if len(self.txt): return (0, 0) not in [(i.isalpha(), i.isdigit()) for i in self.txt]
    else: return False

  def ljust(self, width, fillchar = " "):
    return self.txt + (width - len(self.txt)) * fillchar

  def rjust(self, width, fillchar = " "):
    return (width - len(self.txt)) * fillchar + self.txt

  def partition(self, sep):
    position_sep = self.txt.find(sep)
    if position_sep + 1: return (self.txt[:position_sep], sep, self.txt[position_sep + len(sep):])
    else: return (self.txt, "", "")

  def rpartition(self, sep):
    position_sep = self.txt.rfind(sep)
    if position_sep + 1: return (self.txt[:position_sep], sep, self.txt[position_sep + len(sep):])
    else: return ("", "", self.txt)

  def swapcase(self):
     new_str = String()
     for i in self.txt: new_str += (i.upper(), i.lower())[i.isupper()]
     return new_str

  def title(self):
    new_str = String()
    for i in self.txt.split(" "): new_str += String(i).capitalize() + " "
    return new_str[:-1]
