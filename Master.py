from A import Aritmética
from T import Trigonométrica
from C import Convertidora
class Principal:
    laarit=Aritmética()
    latrigo = Trigonométrica()
    laconver = Convertidora()
    a1 = "Aritmética"
    t1 = "Trigonométrica"
    c1 = "Convertidora"
    a11 = "sumar"
    a12 = "restar"
    a13 = "multiplicar"
    a14 = "dividir"
    t11 = "seno"
    t12 = "coseno"
    t13 = "tangente"
    c11 = "kilogramos a libras"
    c12 = "metros a pies"
    c13 = "centigrados a farenheit"
    s = input("Escriba Aritmética, Trigonométrica o Convertidora según la operación que desee realizar")
    if (a1 == s):
        s1 = input("Escriba sumar, restar, multiplicar o dividir según la operación aritmética que desee realizar")
        if (a11 == s1):
            laarit.operando1 = float(input("digite el primer valor"))
            laarit.operando2 = float(input("digite el segundo valor"))
            print("el resultado es " + str(laarit.sumar()))

        if (a12==s1):
            laarit.operando1 = float(input("digite el primer valor"))
            laarit.operando2 = float(input("digite el segundo valor"))
            print("el resultado es " + str(laarit.restar()))

        if (a13==s1):
            laarit.operando1 = float(input("digite el primer valor"))
            laarit.operando2 = float(input("digite el segundo valor"))
            print("el resultado es ")
            print(laarit.multiplicar())
        if (a14==s1):
            laarit.operando1 = float(input("digite el primer valor"))
            laarit.operando2 = float(input("digite el segundo valor"))
            print("el resultado es ")
            print(laarit.dividir())
    if(t1==s):
        s2 = input("Escriba seno, coseno o tangente según la operación trigonométrica que desee realizar")
        if(t11==s2):
            latrigo.ángulo = float(input("Escriba el valor en grados del cual requiere hallar el seno(el ángulo se convierte automáticamente a radianes)"))
            print("el valor del seno de este ángulo es: ")
            print(latrigo.seno())
        if (t12 == s2):
            latrigo.ángulo = float(input(
                "Escriba el valor en grados del cual requiere hallar el coseno(el ángulo se convierte automáticamente a radianes)"))
            print("el valor del seno de este ángulo es: ")
            print(latrigo.coseno())
        if (t13 == s2):
            latrigo.ángulo = float(input(
                "Escriba el valor en grados del cual requiere hallar el tangente(el ángulo se convierte automáticamente a radianes)"))
            print("el valor del seno de este ángulo es: ")
            print(latrigo.tangente())
    if(c1==s):
        s3=input("Escriba la conversión que desee: kilogramos a libras , metros a pies, centigrados a farenheit")
        if(c11==s3):
            laconver.número = float(input("Escriba la cantidad "))
            print(str(laconver.número) + " Kg " + "= " + str(laconver.kgToLb()) + " lb")
        if(c12==s3):
            laconver.número = float(input("Escriba la cantidad "))
            print(str(laconver.número) + " m " + "= " + str(laconver.mToFt()) + " ft")
        if(c13==s3):
            laconver.número = float(input("Escriba la cantidad "))
            print(str(laconver.número)+" C° "+"= "+str(laconver.CToF())+" F°")