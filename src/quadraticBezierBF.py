import matplotlib.pyplot as plt
import numpy as np
import time

def quadratic_bezier_bf(p0, p1, p2, t):
    qx = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    qy = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return qx, qy

def main():
    # input koordinat p0, p1, p2
    p0x, p0y = map(float, input("Masukkan koordinat p0x dan p0y. Terpisahkan oleh spasi: ").split())
    p1x, p1y = map(float, input("Masukkan koordinat p1x dan p1y. Terpisahkan oleh spasi: ").split())
    p2x, p2y = map(float, input("Masukkan koordinat p2x dan p2y. Terpisahkan oleh spasi: ").split())
    jumlah_iterasi = int(input("Masukkan banyaknya iterasi: "))

    start_time = time.time()

    jumlah_titik = 2**jumlah_iterasi + 1

    p0 = (p0x, p0y)
    p1 = (p1x, p1y)
    p2 = (p2x, p2y)

    values = np.linspace(0, 1, jumlah_titik)
    BezierCurve = np.array([quadratic_bezier_bf(p0, p1, p2, v) for v in values])

    plt.figure(figsize=(12, 8))
    BezierCurve = np.array(BezierCurve)
    plt.plot(BezierCurve[:, 0], BezierCurve[:, 1], label="Bezier Curve with BF", color = "blue")
    plt.scatter([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], color = "red", label = "control points")
    plt.title("Quadratic Bezier Curve BF ({} iterations)".format(jumlah_iterasi))
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.savefig('Bezier with BF.png')

    end_time = time.time()
    program_time = (end_time - start_time)

    print("waktu jalan program: {:.3f} detik".format(program_time))

if __name__ == "__main__":
    main()