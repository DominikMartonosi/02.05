class Allat:
        def __init__(self,allat,suly):
            self.allat = allat
            self.suly = suly
    
allatfaj=[]
for _ in range(3):
    allatka=input('Add meg egy állatfaj nevét! ')
    sulya=int(input('Hány kilogramm a tömege egy példánynak? '))
    allatfajok= Allat(allatka,sulya)
    allatfaj.append(allatfajok)
for a in allatfaj:
    print('A(z)',a.allat,'tömege',a.suly,'kg')
    