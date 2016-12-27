import random
import tree as tree_module


def run():
    print()
    print()
    print("Some (efficient) information about fibonacci numbers:")
    print()
    fib = get_fibonacci()

    sum_total = 0
    for n in fib:
        if n >= 100000:
            break
        sum_total += n
        print(n, end=',')
    print()

    print("Sum of fib less than 100,000 => {0:,}".format(sum_total))
    print()
    print()

    tree = tree_module.Tree()

    for n in range(10):
        tree.insert(random.randint(0, 100))
    print("Here is a ordered tree (raw):")
    print(tree)
    print()

    # TODO: Add iteration to Tree class (see tree.py)
    print("This might make more sense (in order):")
    for n in tree:
        print(n, end=',')
    print()
    print()


def get_fibonacci():
    # Algorithm:
    # 1. use two values current and nxt (next is a builtin)
    # 2. current and nxt start at 1
    # 3. nxt is current+nxt
    # 4. return each entry
    # 5. First few values are: 1,1,2,3,5,8
    # Note: the return value of this method should be an infinite sequence.
    raise NotImplementedError("fibonacci generator method not implemented")
