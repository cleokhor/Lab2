def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (eg. 5,67,32)")
def get_user_input(): 
    numbers = input()
    number_list = numbers.split(",")
    float_list = [] 
    for numbers in number_list: 
        float_list.append(float(numbers))
        return float_list 
def calc_average(float_list):
    total_sum = sum(float_list) 
    total_numbers = len(float_list)
    average_temp = total_sum/total_numbers
    print("average temp", average_temp)
    
    return average_temp
def calc_min_max_temperature(float_list):
    min_temp = min(float_list)
    max_temp = max(float_list)
    print("min temp", min_temp)
    print("max temp", max_temp)
    return(min_temp,max_temp)


def main():
    display_main_menu()
    float_list=get_user_input()
    calc_average(float_list)
    calc_min_max_temperature(float_list)



if __name__ == "__main__":
    main()

  
  
     







    
    