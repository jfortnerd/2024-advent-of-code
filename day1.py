def retrieve_input_data():
    first_list = []
    second_list = []

    with open("input/day1_input.txt", "r") as file:
        for line in file:
            tokens = line.split()
            first_list.append(int(tokens[0]))
            second_list.append(int(tokens[1]))

    return [first_list, second_list]     

def calculate_total_sum(first_list, second_list):
    total_sum = 0

    for i in range(len(first_list)): 
        curr_left_num = first_list[i]
        curr_right_num = second_list[i]

        curr_sum = curr_right_num - curr_left_num

        if curr_sum < 0:
            curr_sum = curr_sum * -1

        total_sum = curr_sum + total_sum

    return str(total_sum)

def calculate_sim_score(first_list, second_list):
    sim_score = 0
    frequency = 0

    for i in range(len(first_list)):
        curr_left_num = first_list[i]

        for j in range(len(second_list)):
            curr_right_num = second_list[j]

            if (curr_left_num == curr_right_num):
                frequency = frequency + 1

        sim_score = (curr_left_num * frequency) + sim_score
        frequency = 0

    return str(sim_score) 

def main():
    input = retrieve_input_data()
    first_list = input[0]
    second_list = input[1]

    first_list.sort()
    second_list.sort()

    print("Total sum is: " + calculate_total_sum(first_list, second_list))
    print("Similarity score is: " + calculate_sim_score(first_list, second_list))

if __name__ == "__main__":
    main()