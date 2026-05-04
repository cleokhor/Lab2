def calculate_bmi(height, weight): 
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    bmi = weight / (height * height)
    print("BMI= " + str(bmi))
    if bmi < 18.5: 
      print ("user is underweight")
      return -1
    elif bmi <= 25.0: 
      print (" user is normal weight")
      return 0
    else :
     print ("user is over weight")
     return 1 
  

calculate_bmi(weight=57 ,height=1.73)
