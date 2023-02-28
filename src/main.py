import numpy as np
import matplotlib.pyplot as plt
import os
import time
import platform
import psutil

from ADT.point import Point
from ADT.listPoint import ListPoint

# Warna ANSI
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
magenta = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'


# Style ANSI
bold = '\033[1m'
underline = '\033[4m'
italic = '\033[3m'
reset = '\033[0m'

# Prosedur Membuat splashscreen


def splashScreen():
    os.system('cls')
    print(red)
    print('        ░█████╗░░██████╗   ░█████╗░░█████╗░██████╗░███████╗')
    print('        ██╔══██╗██╔════╝   ██╔══██╗██╔══██╗██╔══██╗██╔════╝')
    print('        ██║░░╚═╝╚█████╗░   ██║░░╚═╝██║░░██║██║░░██║█████╗░░', white)
    print('        ██║░░██╗░╚═══██╗   ██║░░██╗██║░░██║██║░░██║██╔══╝░░')
    print('        ╚█████╔╝██████╔╝   ╚█████╔╝╚█████╔╝██████╔╝███████╗')
    print('        ░╚════╝░╚═════╝░   ░╚════╝░░╚════╝░╚═════╝░╚══════╝')
    print('            ▀█▀ █░█ █▀▀ ▄▀█ █▀   █▄▀ █▀▀ █▀▀ █ █░░   ▀█')
    print('            ░█░ █▄█ █▄█ █▀█ ▄█   █░█ ██▄ █▄▄ █ █▄▄   █▄ ')
    print()
    print('Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer')
    print('----------------------------------------------------------------------')
    print(
        '|      ' + bold + 'Anggota' + reset + ' : • 13521028 - Muhammad Zulfiansyah Bayu Pratama      |')
    print('|                • 13521031 - Fahrian Afdholi                        |')
    print('|____________________________________________________________________|')
    print()


def checkInputN(warning):
    # Prosedur untuk mengecek inputan N (jumlah titik yang akan dibuat)
    splashScreen()
    if (warning != ""):
        print(red + "WARNING:", warning, "\n")

    N = input(green + "Jumlah titik  : " + yellow)
    if (N.isdigit() == False):
        warning = "Input harus berupa bilangan bulat positif dan lebih dari 1"
        return checkInputN(warning)
    elif (int(N) <= 1):
        warning = "Input harus berupa bilangan bulat positif dan lebih dari 1"
        return checkInputN(warning)
    else:
        N = int(N)
        return N


def printSystemInfo():
    print(cyan + bold + "\nInformasi sistem" + reset)
    print(blue + "Nama sistem operasi  :" + white, platform.system())
    print(blue + "Versi sistem operasi :" + white, platform.release())
    print(blue + "Processor            :" + white, platform.processor())
    print(blue + "Jumlah core          :" + white, psutil.cpu_count())
    print(blue + "Jumlah thread        :" +
          white, psutil.cpu_count(logical=False))
    print(blue + "RAM                  :" + white,
          psutil.virtual_memory().total / 1024 / 1024, "MB")


def checkInputD(warning, N):
    splashScreen()
    if (warning != ""):
        print(red + "WARNING:", warning, "\n")

    print(green + "Jumlah titik  :" + yellow, N)
    # Prosedur untuk mengecek inputan D (dimensi)
    D = input(green + "Dimensi ruang : " + yellow)
    if (D.isdigit() == False):
        warning = "Dimensi harus berupa bilangan bulat positif"
        return checkInputD(warning, N)
    elif (int(D) <= 0):
        warning = "Dimensi harus berupa bilangan bulat positif"
        return checkInputD(warning, N)
    else:
        D = int(D)
        return D


def visualitation(listPoint, pair, D, text):
    # Beri warna merah pada warna titik terdekat, sedangkan titik lainnya berwarna biru
    if (D == 2):
        # Plot 2D
        x = []
        y = []
        for i in range(N):
            x.append(listPoint.get(i).coordinates[0])
            y.append(listPoint.get(i).coordinates[1])

        plt.scatter(x, y, color='blue')
        plt.scatter([pair[0].coordinates[0], pair[1].coordinates[0]], [
                    pair[0].coordinates[1], pair[1].coordinates[1]], color='red')
        plt.title(text)
        plt.show()

    elif (D == 3):
        # Plot 3D
        x = []
        y = []
        z = []
        for i in range(N):
            # Jika titik bukan titik terdekat, maka beri warna biru
            if (listPoint.get(i) != pair[0] and listPoint.get(i) != pair[1]):
                x.append(listPoint.get(i).coordinates[0])
                y.append(listPoint.get(i).coordinates[1])
                z.append(listPoint.get(i).coordinates[2])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, color='blue')
        ax.scatter([pair[0].coordinates[0], pair[1].coordinates[0]], [
            pair[0].coordinates[1], pair[1].coordinates[1]], [pair[0].coordinates[2], pair[1].coordinates[2]], color='red')
        ax.set_title(text)
        plt.show()

    elif (D == 1):
        # Plot 1D
        x = []
        for i in range(N):
            x.append(listPoint.get(i).coordinates[0])

        plt.scatter(x, [0] * N, color='blue')
        plt.scatter([pair[0].coordinates[0], pair[1].coordinates[0]], [
                    0, 0], color='red')
        plt.title(text)
        plt.show()

    print(reset)


# Main Program
if __name__ == "__main__":
    # Input berapa banyak titik yang akan dibuat
    N = checkInputN("")

    # Input dimensi
    D = checkInputD("", N)

    # Membuat list of point
    listPoint = ListPoint()

    # Membuat titik-titik secara random
    print(green + "\nTitik-titik yang dibuat secara random: ")
    for i in range(N):
        coordinates = []
        for j in range(D):
            coordinates.append(np.random.randint(0, 100))
        listPoint.add(Point(coordinates))
        print(yellow + "Titik", i+1, ":" + white, listPoint.get(i))

    # Mencari pasangan titik terdekat
    timeStart = time.time()
    pair = listPoint.getClosestPointPairByDivideAndConquer()
    timeNow = time.time() - timeStart
    printSystemInfo()
    # Mencetak pasangan titik terdekat

    print(magenta + bold + "\nAlgoritma Divide and Conquer" + reset)
    print(blue + "Pasangan titik terdekat          :", white, end='')
    print("(" + str(pair[0]) + ", " + str(pair[1]) + ")")
    print(blue + "Jarak                            :" +
          white, pair[0].distance(pair[1]))
    print(blue + "Jumlah operasi perhitungan jarak :" + white, pair[2])
    print(blue + "Waktu eksekusi                   :" +
          white, timeNow, "detik\n")

    # Bandingkan dengan algoritma brute force
    print(magenta + bold + "Algoritma Brute Force" + reset)
    timeStart = time.time()
    pair2 = listPoint.getClosestPointPairByBruteForce()
    timeNow = time.time() - timeStart
    print(blue + "Pasangan titik terdekat          :", white, end='')
    print("(" + str(pair2[0]) + ", " + str(pair2[1]) + ")")
    print(blue + "Jarak                            :" +
          white, pair2[0].distance(pair2[1]))
    print(blue + "Jumlah operasi perhitungan jarak :" + white, pair2[2])
    print(blue + "Waktu eksekusi                   :" +
          white, timeNow, "detik\n")

    if (pair[0] == pair2[0] and pair[1] == pair2[1]):
        print(green + "Hasil sama!")
    elif (pair[0].distance(pair[1]) == pair2[0].distance(pair2[1])):
        print(yellow + "Hasil sama, namun urutan pasangan berbeda!")
    else:
        print(red + "Hasil berbeda!")

    # Membuat plot sesuai dengan dimensi
    visualitation(listPoint, pair, D, "Hasil Divide and Conquer")
    if (pair[0] != pair2[0] or pair[1] != pair2[1]):
        visualitation(listPoint, pair2, D, "Hasil Brute Force")
