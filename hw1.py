# HW 1
#!python3
import sys, getopt

CALCULATIONS = 0

def generate_final_step(n):
    n = int(n)
    elements_number = (2*n)+1
    final_step = [0] * elements_number
    for i in range(0, elements_number):
        if (i < n):
            final_step[i] = 1;
        elif (i == n):
            final_step[i] = 0;
        else:
            final_step[i] = -1;
        
    return final_step


def generate_start_step(n):
    n = int(n)
    elements_number = (2*n)+1
    final_step = [0] * elements_number
    for i in range(0, elements_number):
        if (i < n):
            final_step[i] = -1;
        elif (i == n):
            final_step[i] = 0;
        else:
            final_step[i] = 1;
    return final_step


def next_step(current_step = [], wrong_paths = []):
    n = len(current_step)
    zero_position = current_step.index(0)
    next_zero_pos1 = zero_position - 2
    next_zero_pos2 = zero_position - 1
    next_zero_pos3 = zero_position + 1
    next_zero_pos4 = zero_position + 2
    current_step1 = current_step[:]
    current_step2 = current_step[:]
    current_step3 = current_step[:]
    current_step4 = current_step[:]

    global CALCULATIONS
    CALCULATIONS+=1

    if next_zero_pos1 >= 0 and current_step1[next_zero_pos1] == -1:
        current_step1[next_zero_pos1] = 0
        current_step1[zero_position] = -1
        if current_step1 not in wrong_paths:
            return current_step1
    
    if next_zero_pos2 >= 0 and current_step2[next_zero_pos2] == -1:
        current_step2[next_zero_pos2] = 0
        current_step2[zero_position] = -1
        if current_step2 not in wrong_paths:
            return current_step2

    # print(next_zero_pos3 , current_step3)
    if next_zero_pos3 < n and current_step3[next_zero_pos3] == 1:
        current_step3[next_zero_pos3] = 0
        current_step3[zero_position] = 1
        if current_step3 not in wrong_paths:
            return current_step3

    if next_zero_pos4 < n and current_step4[next_zero_pos4] == 1:
        current_step4[next_zero_pos4] = 0
        current_step4[zero_position] = 1
        if current_step4 not in wrong_paths:
            return current_step4

    if current_step == generate_final_step((n-1)/2):
        return True

    return False


def path_finder(last_step = [], path = [], wrong_paths = []):

    next_step_path = next_step(last_step, wrong_paths)
    if type(next_step_path) is list:
        path.append(next_step_path)
        return path_finder(next_step_path, path, wrong_paths)
    elif next_step_path:
        return [True, path]
    else:
        return [False, path]


def find_solution(n = 7):

    first_step = generate_start_step(n)
    final_solution_list = [first_step]
    wrong_paths = []
    iters = 0
    while True:
        temp_solution = path_finder(first_step, [], wrong_paths) 
        if temp_solution[0]:
            if temp_solution[0] == 42:
                temp_solution[1][0]
                wrong_paths.append(temp_solution[1][1])
            else:
                final_solution_list.extend(temp_solution[1])
                break
        else:
            wrong_paths.append(temp_solution[1].pop())

    return final_solution_list

# print(find_solution())

if __name__ == "__main__":
    path = find_solution(sys.argv[1:][0])
    for node in path:

        for index, item in enumerate(node):
            if item == -1:
                node[index] = '>'
            elif item == 1:
                node[index] = '<'
            else:
                node[index] = '_'

        print(' '.join(node))

    print('You need to make', len(path), 'moves!')
    print('Computer makes', CALCULATIONS, 'checks until gets correct solution!')

