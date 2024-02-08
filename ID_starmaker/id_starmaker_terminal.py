def create_new_id(id_list):
    new_id = []
    for number in id_list:
        new_id.append(add_star(number.strip()))  #remove end of line character
    return new_id

def add_star(number): #adds stars to the 7 numbers in the middle of the id
    if len(number) != 11:
        return number

    left_index = 2
    right_index = 9

    new_id = number[:left_index] + "*******" + number[right_index:]
    return new_id

def main():
    file_name = input("enter the name of the txt file: ")
    try:
        with open(file_name, 'r') as file:
            ids = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    new_id = create_new_id(ids)


    output_file_name = "new_id.txt" # save as a txt
    with open(output_file_name, 'w') as output_file:
        for number in new_id:
            output_file.write("%s\n" % number)

    print("Done. New starred ids saved as 'new_id.txt'.")

if __name__ == "__main__":
    main()
