from A2Q2_1890_Class import RandomIntList


def main():
    print("Random Integer List")
    while True:
        try:
            number = int(input("\nHow many random integers should the list contain?: \n"))
            if number > 0:
                rand_int_list = RandomIntList(number)
            # Ensuring integer is positive, cannot have negative list values or even list of 0 items.
            else:
                print("Integer cannot be negative. Please try again.")
                continue
        # Ensuring user entry is an integer only.
        except ValueError:
            print("Invalid Entry. Please enter an integer.")
            continue

        print("\nRandom Integers")
        print("================")
        print(f'Number: {str(rand_int_list)}')
        print(f'Count: {rand_int_list.getCount()}')
        print(f'Total: {rand_int_list.getTotal()}')
        print(f'Average: {rand_int_list.getAverage()}')

        selection = input("\nContinue (y/n)?: ")
        if selection == 'y':
            continue
        elif selection == 'n':
            print("\nBye!")
            break
        else:
            print("\nInvalid selection. Please try again.")
            continue


if __name__ == '__main__':
    main()