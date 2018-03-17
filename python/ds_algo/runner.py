from adt import Stack

def main():
    ss = Stack()
    ss.push(10)
    ss.pop()
    ss.push(20)
    print(ss.get_stack())
    import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()
