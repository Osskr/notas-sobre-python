
class Gato:
    
    def __init__(self,name,color,year):
        self.name = name
        self.color = color
        self.year = year
        
    def maullar():
        return 'miau'
    
    def nombre(self):
        return self.name
    
    

def contar_letras(s):
    d = {}
    for letra in s:
        d[letra] = d.get(letra,0) + 1
        
    return d

s = 'aaaassssdddddaaasss'

print(contar_letras(s))