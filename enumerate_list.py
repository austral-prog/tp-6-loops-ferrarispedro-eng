# Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):

    result = []
    index = 0
    for item in lst:
        if item != "":
            result.append(f"{index}. {item}")
            index += 1

    return result


def enumerate_backwards(lst):

    result = []
    index = 0
    for item in lst:
        if item != "":
            result.append(f"{index}. {item[::-1]}")
            index += 1

    return result  
