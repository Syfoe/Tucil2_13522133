import matplotlib.pyplot as plt
import numpy as np
import time

def quadratic_bezier_dnc(p0, p1, p2, iterasi):
    midLeft = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    midRight = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    midCenter = ((midLeft[0] + midRight[0]) / 2, (midLeft[1] + midRight[1]) / 2)
    if(iterasi == 1):
        return[p0, midCenter, p2]
    else:
        leftDNC = quadratic_bezier_dnc(p0, midLeft, midCenter, iterasi - 1)
        rightDNC = quadratic_bezier_dnc(midCenter, midRight, p2, iterasi - 1)

        return leftDNC + rightDNC[1:]
    
def main():
    # input koordinat p0, p1, p2
    p0x, p0y = map(float, input("Masukkan koordinat p0x dan p0y. Terpisahkan oleh spasi: ").split())
    p1x, p1y = map(float, input("Masukkan koordinat p1x dan p1y. Terpisahkan oleh spasi: ").split())
    p2x, p2y = map(float, input("Masukkan koordinat p2x dan p2y. Terpisahkan oleh spasi: ").split())
    jumlah_iterasi = int(input("Masukkan banyaknya iterasi: "))

    start_time = time.time()

    p0 = (p0x, p0y)
    p1 = (p1x, p1y)
    p2 = (p2x, p2y)

    BezierCurve = quadratic_bezier_dnc(p0, p1, p2, jumlah_iterasi)

    plt.figure(figsize=(12, 8))
    BezierCurve = np.array(BezierCurve)
    plt.plot(BezierCurve[:, 0], BezierCurve[:, 1], label="Bezier Curve with DnC", color = "blue")
    plt.scatter([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], color = "red", label = "control points")
    plt.title("Quadratic Bezier Curve DnC ({} iterations)".format(jumlah_iterasi))
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.savefig('Bezier with DnC.png')

    end_time = time.time()
    program_time = (end_time - start_time)

    print("waktu jalan program: {:.3f} detik".format(program_time))

if __name__ == "__main__":
    main()