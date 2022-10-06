from PIL import Image
import numpy as np

obrazek = Image.open("inicjaly.bmp")
obrazek.show()
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)



dane_obrazka = np.asarray(obrazek)
print("---------------- informqcje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)
print("***************************************")
print(dane_obrazka)


dane_obrazka1 = dane_obrazka * 1
print(dane_obrazka1)
ob_d = Image.fromarray(dane_obrazka)
print("-------informacje o obrazie ob_d ------------")
print("tryb:", ob_d.mode)
print("format:", ob_d.format)
print("rozmiar:", ob_d.size)
ob_d.show()