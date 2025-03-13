FILE_PATH = "input/day3_input.txt"
NUMERIC_CHARS = '0123456789'
MUL_COMMAND = 'mul'
COMMA_CHAR = ','
BEGIN_PAREN_CHAR = '('
END_PAREN_CHAR = ')'
M_CHAR = 'm'
D_CHAR = 'd'
DEBUG_PRINT = True

def load_input():
    input = ""

    with open(FILE_PATH, "r") as file:
        for line in file:
            input = str(input) + str(line)

    return input

def check_valid_char(input, validator):
    return (input == validator)

def check_valid_substring(input, validator):
    if not(input):
        return False 
    
    return (input == validator)

def check_numeric_parameters(input, validator, stop_sequence):
    results = {
        "first_number": -1,
        "second_number": -1,
        "end_index": -1 
    }

    # Check if first character is numeric
    if (input[0]) and (validator.find(input[0]) > -1):
        pass
    else:
        return results

    # Check for remaining numeric chars
    continue_checking = True
    curr_index = 1

    while (continue_checking):
        if (input[curr_index]):
            if (validator.find(input[curr_index]) > -1):
                pass
            elif (stop_sequence.find(input[curr_index]) > -1):
                continue_checking = False
            else:
                return results
        else:
            return results
        
        curr_index += 1 
    
    results["first_number"] = int(input[0:curr_index - 1])

    # Check for first and remiaining numeric chars after comma 
    second_number_begin_index = curr_index + 1
    continue_checking = True 
    curr_index += 1

    while (continue_checking):
        if (input[curr_index]):
            if (validator.find(input[curr_index]) > -1):
                pass
            elif (END_PAREN_CHAR.find(input[curr_index]) > -1):
                continue_checking = False
            else:
                return results
        else:
            return results
        
        curr_index += 1 
    
    results["second_number"] = int(input[second_number_begin_index - 1:curr_index - 1])
    results["end_index"] = curr_index

    return results

def add_mul_instructions(input):
    sum_result = 0
    curr_index = 0
    end_index = 0
    first_numeric = 0
    second_numeric = 0
    valid_instruction = True
    invalid_error_printed = False 
    mult_instruction_enabled = True

    for char in input: 

        if (DEBUG_PRINT):
            print("At index " + str(curr_index) + ", char: " + str(char) + " - " + str(input[curr_index:curr_index + 20]))

        # check if first character is "M"
        valid_instruction = check_valid_char(char, M_CHAR)



        # check if "mul" instruction is present
        if (valid_instruction):
            end_index = curr_index + len(MUL_COMMAND)
            valid_instruction = check_valid_substring(input[curr_index:end_index], MUL_COMMAND)
        else:
            if not (invalid_error_printed) and DEBUG_PRINT:
                print("\tBADCHAR: Does not start with m")
                invalid_error_printed = True

        # check if "(" exists afterwards
        if (valid_instruction): 
            end_index = curr_index + len(MUL_COMMAND) + len(BEGIN_PAREN_CHAR)
            valid_instruction = check_valid_char(input[end_index - 1], BEGIN_PAREN_CHAR)
        else:
            if not (invalid_error_printed) and DEBUG_PRINT:
                print("\tBADCHAR: Does not have valid prefix - mul")
                invalid_error_printed = True

        # check numeric parameters
        if (valid_instruction):
            results = check_numeric_parameters(input[end_index:], NUMERIC_CHARS, COMMA_CHAR)

            if (results["first_number"] == -1) or (results["second_number"] == -1):
                valid_instruction = False 
            else:
                first_numeric = results["first_number"]
                second_numeric = results["second_number"]
                end_index = results["end_index"]
        else:
            if not (invalid_error_printed) and DEBUG_PRINT:
                print("\tBADCHAR: Does not have begin parens")
                invalid_error_printed = True

        # check if ")" exists afterwards
        if (valid_instruction): 
            end_index = curr_index + end_index + len(MUL_COMMAND) + len(BEGIN_PAREN_CHAR)
            valid_instruction = check_valid_char(input[end_index - 1], END_PAREN_CHAR)       
        else:
            if not (invalid_error_printed) and DEBUG_PRINT:
                print("\tBADCHAR: Invalid numeric parameters") 
                invalid_error_printed = True

        # if valid instruction, multiply the numerics and add to result
        if (valid_instruction):
            product = first_numeric * second_numeric
            sum_result += product
            print("\t***SUCCESS***: " + str(first_numeric) + " * " + str(second_numeric) + " = " + str(product) + "")
        else:
            if not (invalid_error_printed) and DEBUG_PRINT:
                print("\tFirstNumeric: " + str(first_numeric) + ", secondNumeric: " + str(second_numeric))
                print("\tBADCHAR: Does not have end parens: " + str(input[end_index - 1]) + " at end index: " + str(end_index - 1))
                invalid_error_printed = True

        # increment
        curr_index += 1

        # reset 
        end_index = 0
        first_numeric = 0
        second_numeric = 0
        valid_instruction = True
        invalid_error_printed = False

        print("\tSum Result: " + str(sum_result) + "\n")

    return sum_result

def main():
    input = load_input()

    sum_result = add_mul_instructions(input)

    print("The sum of all the multiplications is " + str(sum_result) + ".")

if __name__ == "__main__":
    main()