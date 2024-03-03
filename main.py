def convert_str_into_list():
    """
    This function asks a user to input a list of numbers, then it asks for a specific index to return.
    And returns its index element. Handling Value and Index Errors on the way.
    :return:
    """
    user_input = input("Enter a list of numbers separated by commas: ")

    try:
        user_input_list = [abs(int(number)) for number in user_input.split(",")]
    except ValueError:
        return "It has to be whole numbers only."

    try:
        index_to_return = int(input("What element from your list would you want to return?: "))
    except ValueError:
        return "Enter only numbers."

    try:
        element_to_return = user_input_list[index_to_return]
    except IndexError:
        return "Your index doesn't exist."
    else:
        return element_to_return
