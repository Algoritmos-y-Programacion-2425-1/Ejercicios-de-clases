def validate_word(character,row):
    return character in row

def ejercicio1():
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    words = ["Hello", "Alaska", "Dad", "Peace"]
    result_list = []
    for word in words:
        word_is_in_row = True
        word = word.lower()
        for character in word:
            word_is_in_row = validate_word(character,row1)
            if not word_is_in_row:
                break
        if word_is_in_row:
            result_list.append(word)
            continue
        for character in word:
            word_is_in_row = validate_word(character,row2)
            if not word_is_in_row:
                break
        if word_is_in_row:
            result_list.append(word)
            continue
        for character in word:
            word_is_in_row = validate_word(character,row3)
            if not word_is_in_row:
                break
        if word_is_in_row:
            result_list.append(word)
            continue
    print(result_list)

def ejercicio2():
    mountain = [1,4,3,8,5]
    result_list = []
    if len(mountain) < 3:
        print(result_list)
    else:
        for index in range(len(mountain)):
            if index == 0 or index == len(mountain) - 1:
                continue
            else:
                if mountain[index] > mountain[index - 1] and mountain[index] > mountain[index + 1]:
                    result_list.append(index)
        print(result_list)
        
def ejercicio3():
    path = "NES"
    current_position = [0,0]
    result_list = []
    result_list.append(current_position)
    print(result_list)
    for direction in path:
        if direction == "N":
            current_position = (current_position[0],current_position[1]+1)
            if current_position in result_list:
                return True
            else:
                result_list.append(current_position)
        elif direction == "S":
            current_position = (current_position[0],current_position[1]-1)
            if current_position in result_list:
                return True
            else:
                result_list.append(current_position)
        elif direction == "E":
            current_position = (current_position[0]-1,current_position[1])
            if current_position in result_list:
                 return True
            else:
                result_list.append(current_position)
        elif direction == "W":
            current_position = (current_position[0]+1,current_position[1])
            if current_position in result_list:
                 return True
            else:
                result_list.append(current_position)
    return False

def main():
    while True:
        option = input("Please enter a option \n1-Ej1 \n2-Ej2 \n3-Ej3 \n-> ")
        if option == "1":
            ejercicio1()
        elif option == "2":
            ejercicio2()
        elif option == "3":
            if ejercicio3():
                print("Se repitieron")
            else:
                print("No se repitieron")
main()