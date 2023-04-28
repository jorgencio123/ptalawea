from flask import Flask
import math
import time

app = Flask(__name__)

@app.route('/add/<float:tiempo_vuelta>')
def add_number(tiempo_vuelta):
    fin_vuelta = time.time()

    # Calcula el tiempo que tardó la pelota en dar una vuelta completa
    # tiempo_vuelta = fin_vuelta - inicio_vuelta

    # Imprime el tiempo de la vuelta en segundos
    # print("La pelota tardó {} segundos en dar una vuelta completa.".format(tiempo_vuelta))

    angulo = 2*math.pi
    tiempo = 0.6
    w = angulo/tiempo_vuelta
    aceleracion = w/tiempo_vuelta

    print(w)
    print(aceleracion)
    velocidad_angular = w
    aceleracion_angular = aceleracion

    algunawea = 0.3 * velocidad_angular ** 2 * math.cos(0.785398) - 9.8 * math.sin(0.785398)
    print(algunawea)
    import sympy as sp
    x = sp.symbols('x')
    f = algunawea
    integral1 = sp.integrate(f, x)
    integral2 = sp.integrate(integral1, x)
    print(integral2)
    integral2 = str(integral2)
    integral2 = integral2[:4]
    integral2 = float(integral2)
    print(integral2)

    otrawea = 0 + velocidad_angular*integral2 + 0.5*aceleracion_angular*integral2**2
    x = otrawea
    mod = math.fmod(x, 2*math.pi)
    deg = mod * 180 / math.pi
    if deg >= 0 and deg <= 90:
        return {"result": "la pelota termina arriba"}
    if deg >= 91 and deg <= 269:
        return {"result": "la pelota termina abajo"}
    if deg > 270:
        return {"result": "la pelota termina arriba"}

@app.route('/result/<int:result>')
def get_result(result):
    return {"result": result}

if __name__ == '__main__':
    app.run(debug=True)
