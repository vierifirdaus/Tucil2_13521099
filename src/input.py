point=[]

def inp() :
    derajatcnt=int(input("Masukkan banyak derajat : "))
    n=int(input("Masukkan banyak titik : "))

    for i in range(n) :
        print(f"Masukkan titik ke-{i+1}")
        temptitik=input()
        datatitik=temptitik.split(" ")
        datatitik=[float(i) for i in datatitik]
        point.append(datatitik)

    print(point)
def main() :
    inp()

main()
