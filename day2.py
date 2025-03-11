PRINT_DEBUG = False
PRINT_DEBUG_BRIEF = True 
RUN_FIRST_PART = False 
RUN_SECOND_PART = True

def retrieve_input_data():
    input_data = []

    with open("input/day2_input.txt", "r") as file:
        for line in file:
            input_data.append(line)

    return input_data

def is_diff_safe(first_val, second_val, trend):
    diff = second_val - first_val

    if not (diff in range (-3, 0)) and not (diff in range (1, 4)):
        return False 
    
    if (trend * diff <= 0):
        return False 
    
    return True

def check_safety(values, trend):

    for i in range(len(values) - 2):
        first_val = int(values[i + 1])
        second_val = int(values[i + 2])

        if not (is_diff_safe(first_val, second_val, trend)):
            return False 

    return True  

def check_safety_with_tolerance(values, trend, tolerance):

    is_safe = True
    new_values = []
    new_trend_needed = True 

    if (PRINT_DEBUG):
        print("Loop for values: " + str(values))

    for i in range(len(values)):
        new_values = values[:i] 
        new_values.extend(values[i + 1:])

        if (PRINT_DEBUG):
            print("New range: " + str(new_values))

        for i in range(len(new_values) - 1):
            first_val = int(new_values[i])
            second_val = int(new_values[i + 1])

            if (new_trend_needed):
                trend = second_val - first_val
                new_trend_needed = False

            if (PRINT_DEBUG):
                print("second_val: " + str(second_val) + ", - first_val: " + str(first_val))

            is_safe = is_diff_safe(first_val, second_val, trend)

            if not (is_safe):
                if (PRINT_DEBUG):
                    print("Not safe. Break!")
                break
            
        # if is safe, found values that are safe, can stop looking
        if (is_safe):
            if (PRINT_DEBUG):
                print("Safe new range. Ready to return True")
            return True
        else:
            if (PRINT_DEBUG):
                print("Unsafe new range.")

        # reset trend 
        new_trend_needed = True 

    # iterated through all permutations - no values found safe
    if (PRINT_DEBUG):
        print("No safe ranges found in all permutations of the new ranges. Ready to return False")
    return False 

def calculate_safe_reports(input, default_tolerance):
    safe_reports = 0

    for report in input: 
        is_safe = True
        values = report.split()
        
        # first pass 
        first_val = int(values[0])
        second_val = int(values[1])

        is_safe = is_diff_safe(first_val, second_val, second_val - first_val)
        
        if (is_safe) and (default_tolerance == 0):
            is_safe = check_safety(values, second_val - first_val)
        
        if (default_tolerance == 1):
            is_safe = check_safety_with_tolerance(values, second_val - first_val, default_tolerance)

        if (PRINT_DEBUG):
            print ("Report " + str(values) + " is safe? --- ")

        if (PRINT_DEBUG_BRIEF):
            print (str(is_safe))

        if (is_safe):
            safe_reports = safe_reports + 1
            
    return str(safe_reports)

def main():
    input = retrieve_input_data()

    if (RUN_FIRST_PART):
        print("There are " + calculate_safe_reports(input, 0) + " safe reports!")

    if (RUN_SECOND_PART):
        print("With tolerance for 1 unsafe reading, there are now " + calculate_safe_reports(input, 1) + " safe reports!")

if __name__ == "__main__":
    main()