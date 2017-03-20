import random

def jogar_dado():
    return random.randint(1,6)

def zerar_passo():
    if 1 == random.randint(1,1000):
        return True
    return False

def executa_passo(floor, step):
    if -1 == step and 0 == step:
        return floor
    return (floor + step)

epoch     = 100
seed      = 123456
rounds    = 500
roundList = []

for i in range(rounds):
    floor = 0
    steps = []

    for j in range(epoch):
        if zerar_passo():
            steps.append(0)
            continue

        dado = jogar_dado()

        if dado in [1,2]:
            step  = -1
            floor = executa_passo(floor, -1)            
        elif dado in [3,4,5]:
            step  = 1
            floor = executa_passo(floor, 1)
        else:
            dado  = jogar_dado()
            step  = dado
            floor = executa_passo(floor, dado)
        if floor < 0:
            floor = 0
        
        
        steps.append(floor)

    roundList.append(steps)

print("Lista de JOGADAS => ", roundList)
