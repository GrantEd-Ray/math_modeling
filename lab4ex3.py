import constants as con

def energy(a, b, c):
    Ek = (a * c ** 2) / 2
    Ep = a * con.g * b
    E = Ek + Ep
    return E

m = int(input())
h = int(input())
v = int(input())

print(energy(m, h, v))