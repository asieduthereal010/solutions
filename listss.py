if __name__ == '__main__':
    N = int(input())
    myList = []
  
    for command in range(N):
        command = input()

        keyword = command.split()[0]
        if keyword == "insert":
            _, pos, val = command.split()
            myList.insert(int(pos), int(val))
        elif keyword == "print":
            print(myList);
        elif keyword == "remove":
            _, val = command.split()
            myList.remove(int(val))
        elif keyword == "append":
            _, val = command.split()
            myList.append(int(val))
        elif keyword == "sort":
            myList.sort();
        elif keyword == "pop":
            myList.pop()
        elif keyword == "reverse":
            myList.reverse()
