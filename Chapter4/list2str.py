def list2str(elems):
    string = ""
    for elem in elems[:-1]:
        string += str(elem) + ", "
    string += "and " + str(elems[-1])
    return string

def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(list2str(spam))