weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))
BMI = weight / (height ** 2)
if BMI > 40:
    print ("béo phì cấp độ III")
elif 35 <= BMI < 40:
    print ("béo phì cấp độ II")
elif 30 <= BMI < 35:
    print ("béo phì cấp độ I")
elif 25 <= BMI < 30:
    print ("thừa cân")
elif 18.5 <= BMI < 25:
    print ("bình thường")
elif 17 <= BMI < 18.5:
    print ("gầy cấp độ I")
elif 16 <= BMI < 17:
    print ("gầy cấp độ II")
else:
    print ("gầy cấp độ III")