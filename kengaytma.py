# son1 = int(input("son 1 kiriting"))
# son2 = int(input("son 2 kiriting"))

# operator = input("obeatorni tanlang +, -, * - , / ")

# if operator == "+":
#     print(son1 + son2)

# elif operator == "-":
#     print(son1 - son2)

# elif operator == "*":
#     print(son1 * son2)

# elif operator == "/":
#     print(son1 / son2)
# else:
#     print("notogri operator")





# ism = input(("ismingiz ni kiriting"))
# yosh = int(input("yoshingizni kiriting"))
# vazn = float(input("vazningizni kirting"))
# dasturchi = input("dasturchi misiz? ha/yoq")
# loyihalar =[]

# while True:
#     loyihalar_nomi = input("loyihalar nomi yoki stop:")

#     if loyihalar_nomi == "stop":
#       break
#     loyihalar.append(loyihalar_nomi)



# natija = f"malumotlar:"
# natija = f"ism: {ism}\n"
# natija = f"yosh: {yosh}\n"
# natija = f"vazn: {vazn}\n"
# natija += f"{True if dasturchi == "ha" else "false"}"
# natija += f"loyihalar{loyihalar}"




# print(natija)

    



# ismlar = ["shukurjon", "jahongir", "jora", "xusanboy"]
# user_ism = input("isim kiriting\n")
# ismlar.append(ismlar)

# if user_ism in ismlar:
#     print(f"siz kiritgan ism {user_ism}")
# else:
#     ismlar.append(user_ism)
#     print(f"Sizning ismingiz bn {ismlar}")






# o'quvchilar ismi  list mavjud
# userdan ism so'raysiz va o'sha ism listda mavjudligini tekshirasiz. Agar mavjud bo'lsa, ism shunchaki bu ism mavjud emas va ismni kiriting: ismni kiritgandan keyin o'sha ismlar listiga qo'shib qo'yish kerak

# menu chiqadi 
# 1. student ismlar ro'yhatini ko'rish
# 2. ism olib tashlash 
# 3. yangi ism qo'shish(oxiriga)
# 4. yangi ism qo'shish(aynan bir indexga) insert
# 5. stop


    
student_ismlar = ["shukurjon", "jora", "xusanboy", "jahon"]

while True:
    print("1. student ismlar ro'yhatini ko'rish\n2. ism olib tashlash\n3. yangi ism qo'shish(oxiriga)\n4. yangi ism qo'shish(aynan bir indexga) insert\n5. stop")

    user = input("qaysi ni tanlesz: ")

    if user == "1":
        print(student_ismlar)
    elif user == "5":
        break





    elif user == "2":
        ism = input("ochrmoqchi bolgan ismni kiriting :")
        if ism in student_ismlar:
            student_ismlar.remove(ism)
        else:
      
           print("bunday ism mavjud emas")




    elif user == "3":
         yangi = input("yangi ism kirting") 
         student_ismlar.append(yangi) 

    
    
    elif user == "4":
        oquvchi = input("istalgan index orniga ism kiritng")
        index = int(input("Qaysi indeksga qo'shilsin: "))
        student_ismlar.insert(index,oquvchi)


    elif user == "5":
        break