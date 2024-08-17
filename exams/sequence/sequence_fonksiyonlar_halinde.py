def get_words():   
    word = input('Please enter your first word that you want to find: ')
    second_word = input('Please enter your second word that you want to find: ')
    return word,second_word

def reader(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def process(lines,word,second_word,):
    sequence_number = 0
    found_first = False
    found_second = False
    closest_distance = float('inf')  
    closest_sequence = None
    for line in lines:
        sequence_number += 1
        words = line.strip().split()
        if word in words:
            found_first = True
        if second_word in words:
            found_second = True
        if found_first and found_second:
            index_word = None
            index_second_word = None
            for indx in range(len(words)):
                if words[indx] == word:
                    index_word = indx
                elif words[indx] == second_word:
                    index_second_word = indx
                    
                if index_word is not None and index_second_word is not None:
                    distance = abs(index_word - index_second_word)
                    if distance < closest_distance:
                        closest_distance = distance
                        closest_sequence = sequence_number
    return found_first, found_second, closest_distance, closest_sequence

def printer(found_first, found_second, closest_distance, closest_sequence):
    if found_first and found_second and closest_sequence is not None:
        print(f'Min distance: sequence {closest_sequence} (distance={closest_distance})')
    elif not found_first or not found_second:
        print('These words are not in the text')
    else:
        print('These words never appear in the same sequence')

def main():
    filename = 'sequence/seq.txt'
    word,second_word =  get_words()
    lines=reader(filename)
    found_first, found_second, closest_distance, closest_sequence =process(lines,word,second_word)
    
    printer(found_first, found_second, closest_distance, closest_sequence)

if __name__ == "__main__":
    main()