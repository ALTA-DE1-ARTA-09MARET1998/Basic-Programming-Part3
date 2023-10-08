import sys

# input
student_score = 80

# Process: Your Solution Code Here
nama_mhs=input("Masukkan nama mahasiswa: ")

if 80 <= student_score <= 100:
    print("Nilai",nama_mhs,"adalah A")

if 65 <= student_score <= 79:
    print("Nilai",nama_mhs,"adalah B+")

if 50 <= student_score <= 64:
    print("Nilai",nama_mhs,"adalah B")

if 35 <= student_score <= 49:
    print("Nilai",nama_mhs,"adalah C")

if 0 <= student_score <= 34:
    print("Nilai",nama_mhs,"adalah D. Maaf, anda tidak lulus kelas!")

# Output "Nilai A"