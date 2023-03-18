import os

with open("A.txt", encoding="utf-8") as archivo:
    for i in archivo:
        print(i)
        N = i.rstrip(i[-2])
        N2 = N[:-1]
        os.mkdir(N2)
        os.chdir(N2)
        os.mkdir("1.Evidencias_de_aprendizaje")
        os.mkdir("2.Sanciones_e_indidciplina")
        os.mkdir("3.Plan_concertado")
        os.mkdir("4.Material_de_estudio")
        os.mkdir("5.Planes_de_mejoramiento")
        os.chdir("E:\Programacion\Python\Yo")
