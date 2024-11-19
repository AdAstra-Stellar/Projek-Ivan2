# Program Menghitung Body Mass Index

# Penulisasn kategori BMI
Category1 = "Underweight"
Category2 = "Normal"
Category3 = "Overweight"
Category4 = "Obese"

# Penulisan fungsi dan pengkategorian hasil BMI
def BMI_Formula(Weight,Height):
    BMI = (Weight / (Height ** 2))
    if BMI < 18:
        print(f'''Anda termasuk ke dalam kategori {Category1}''')
    elif 18 <= BMI < 25:
        print(f'''Anda termasuk ke dalam kategori {Category2}''')
    elif 25 <= BMI < 30:
        print(f'''Anda termasuk ke dalam kategori {Category3}''')
    elif BMI > 30:
        print(f'''Anda termasuk ke dalam kateegori {Category4}''')
    else:
        print("Error")
    

# Masukkan Biodata
print("Selamat datang di\nKalkulator penghitung BODY MASS INDEX(BMI)")
import time
print("Masukkan nama Anda")
time.sleep(1)
User = input("Jawaban Anda: ")
Weight = int(input(f"{User} silahkakn masukkan berat badan Anda!: "))
Height = float(input(f"{User} silahkan masukkan tinggi badan anda!\n(m, dalam bentuk desimal): "))


# Eksekusi Sistem
BMI_Formula(Weight,Height)

