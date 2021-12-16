from operator import itemgetter
 
class  PL:
    """Язык программирования"""
    def __init__(self, id, name_PL, year, SR_id):
        self.id = id
        self.name_PL = name_PL # имя
        self.year = year # год создания
        self.SR_id = SR_id # среда разработки
 
class SR:
    """Средство разработки"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class PLSR:
    """
    связь многие ко многим
    """
    def __init__(self, SR_id, PL_id):
        self.SR_id = SR_id
        self.PL_id = PL_id
 
# Компьютеры
SRs = [
    SR(1, 'Консоль'),
    SR(2, 'Среда Visual Studio'),
    SR(3, 'Среда Visual Code'),
    SR(4, 'Блокнот'),
    SR(5, 'Среда Xcode'),
]
 
# Жесткие диски
PLs = [
    PL(1, 'Python', 1991, 3),
    PL(2, 'C#', 2000, 2),
    PL(3, 'C++', 1983, 2),
    PL(4, 'Assembler', 1949, 1),
    PL(5, 'Html', 1993, 4),
    PL(6, 'Swift', 2014, 5),
]
 
PLs_SRs = [
    PLSR(1,1),
    PLSR(1,2),
    PLSR(2,4),
    PLSR(2,6),
    PLSR(3,3),
    PLSR(3,5),
    PLSR(4,6),
    PLSR(4,1),
    PLSR(5,2),
    PLSR(5,4),
    PLSR(6,1),
    PLSR(6,3),
    

]
 
 
    # Соединение данных один-ко-многим 
one_to_many = [(p.name_PL, p.year, s.name) 
        for s in SRs 
        for p in PLs 
        if p.SR_id==s.id]
    
    # Соединение данных многие-ко-многим
many_to_many_temp = [(s.name, sp.PL_id, sp.SR_id) 
        for s in SRs 
        for sp in PLs_SRs 
        if s.id==sp.SR_id]
    
many_to_many = [(p.name_PL, p.year, SR_name) 
        for SR_name, SR_id, PL_id in many_to_many_temp
        for p in PLs if p.id==PL_id]
 
def T1():   
    E1 = []
    for name_PL, year, name in one_to_many:
            if 'Среда' in name: # Ищем средство разработки с ключевым словом "Среда"
                E1.append((name, name_PL))
    return E1 

def T2():    
    # находим средний год выпуска языков
    E2_unsorted = []
    # Перебираем все компьютеры
    for  s in  SRs:
        # Список языков компьютера
        PLSS = list(filter(lambda i: i[2]==s.name, one_to_many))       
        if len(PLSS) > 0:
            Y = [year for _,year,_ in PLSS]
            avg_sum = sum(Y)/len(Y)
            E2_unsorted.append((s.name, avg_sum))
    E2 = sorted(E2_unsorted, key=itemgetter(1))
    return E2        
 
def T3():
    # находим языки программирования, начинающиеся с "С" и выводим их среды
    E3 = []
    for name_PL, year, name in many_to_many:
        if name_PL.find("C") == 0:
            E3.append((name_PL, name))
    return E3 

