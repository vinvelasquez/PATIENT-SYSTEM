def check_age(age):
    if age >= 18:
        return "Legal Age"
    else:
        return "Minor"

def check_height(height):
    if height < 160:
        return "Small"
    elif 160 <= height <= 175:
        return "Normal"
    else:
        return "Tall"

def check_weight(weight):
    if weight < 50:
        return "Underweight"
    elif 50 <= weight <= 70:
        return "Normal"
    elif 70 < weight <= 90:
        return "Overweight"
    else:
        return "Obese"

patients = []  

print("---------Patient Health Check------------")

while True:
    print("-------Enter Patient Details---------")
    
    name = input("Enter your name: ")
    
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Error! Age must be a number. Try Again")
    
    while True:
        try:
            height = float(input("Enter your Height: "))
            break
        except ValueError:
            print("Error! Height must be a number. Try Again")
    
    while True:
        try: 
            weight = float(input("Enter your Weight: "))
            break
        except ValueError:
            print("Error! Weight must be a number. Try Again")
    
    age_cat = check_age(age)
    height_stat = check_height(height)
    weight_stat = check_weight(weight)
    
    
    patients.append([name, age_cat, height_stat, weight_stat])
    
    
    print("----Patient Result----")
    print("Name: ", name)
    print("Age Category: ", age_cat)
    print("Height Status: ", height_stat)
    print("Weight Status: ", weight_stat)
    print("-----------------------")
    
    again = input("\nCheck another Patient? (Y/N): ")
    
    if again == "Y":
        continue
    elif again == "N":
        
        print("---- Summary of Patients Checked ----")
        for p in patients:
            print(p[0], "-", p[1], "-", p[2], "-", p[3])
        print("Thank you!")
        break
    else:
        print("Please enter Y or N only.")