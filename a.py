import random

PAS = 1
MACKA = -1

data = [
    [3, 7, PAS],
    [17, 3, MACKA],
    [15, 5, MACKA],
    [3, 3, PAS],
    [15, 3, MACKA],
    [3, 5, PAS]
]

def model(w, x):

    y = w[0]*x[0]+w[1]*x[1]+w[2]
    if y<0:
        return MACKA
    if y>0:
        return PAS
    return 0

def loss(data, model, w):
    err = 0
    n = len(data)
    for i in range(n):
        x = data[i][:2]
        izracunato = model(w, x)
        ocekivano = data[i][2]
        err += abs(izracunato-ocekivano)
    return err

def fit(data, model, loss):
    # pronaci w tako da loss bude najmanji
    w_best = None
    loss_best = None
    for it in range(10000000):
        w = [
            10*random.random()-5, # w0
            10*random.random()-5, # w1
            10*random.random()-5  # w2
        ]
        err = loss(data, model, w)
        if err==0:
            return w, err
        if loss_best==None or loss_best>err:
            w_best = w
            loss_best = err
    return w_best, loss_best

w, err = fit(data, model, loss)

print(w, err)

p1 = [17, 5]
p2 = [3, 6.5]

print(f'Klasa za 1 je {model(w, p1)} PAS={PAS}  MACKA={MACKA}')
print(f'Klasa za 2 je {model(w, p2)}')