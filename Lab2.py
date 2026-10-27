def main():
    print("ET0735 (DevOps for AIot) - Lab 2 - Introduction to python")
    display_main_input()
    num_list =  get_user_input()

def display_main_input():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    float_input = []

    Input = input("Enter your numbers: ")

    split_input = Input.split(",")

    for numbers in split_input:
        float_input.append(float(numbers))

    return float_input

def calc_average(List):
    sum = 0

    for numbers in List:
        sum += numbers

    average_number = sum / len(List)

    return average_number

def find_min_max(List):
    min_max = []
    min_number = 0
    max_number = 0
    for numbers in List:
        if numbers < min_number:
            min_number = numbers
        elif numbers > max_number:
            max_number = numbers

    min_max.append(min_number)
    min_max.append(max_number)

    return min_max

def sort_temperature(List):
    List.sort()
    return List

def calc_median_temperature(List):
    sorted_list = sort_temperature(List)
    length = len(List)
    if length % 2 == 0:
        median = (sorted_list[(length // 2) - 1] + sorted_list[(length // 2)]) / 2
    elif length % 2 == 1:
        median = sorted_list[length // 2]
    else: 
        print("Invalid list")
        return
    return median

if __name__ == "__main__":
    main()