def main():
    word = input('Please enter your first word that you want to find: ')
    second_word = input('Please enter your second word that you want to find: ')
    found_first = False
    found_second = False
    closest_distance = float('inf')  
    closest_sequence = None
    with open('sequence/seq.txt', 'r') as file:
        sequence_number = 0
        for line in file:
            sequence_number += 1
            words = line.strip().split()
            if word in words:
                found_first = True
            if second_word in words:
                found_second = True

            if found_first and found_second:
                index_word = -1
                index_second_word = -1
                for indx in range(len(words)):
                    if words[indx] == word:
                        index_word = indx
                    elif words[indx] == second_word:
                        index_second_word = indx
                    
                    if index_word != -1 and index_second_word != -1:
                        distance = abs(index_word - index_second_word)
                        if distance < closest_distance:
                            closest_distance = distance
                            closest_sequence = sequence_number

    if found_first and found_second and closest_sequence is not None:
        print(f'Min distance: sequence {closest_sequence} (distance={closest_distance})')
    elif not found_first or not found_second:
        print('These words are not in the text')
    else:
        print('These words never appear in the same sequence')
if __name__ == "__main__":
    main()





















