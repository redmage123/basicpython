print("Working with collections:")
print()

print("First, let's create some collections.")
l = [1, 1, 2, 3, 5, 8]
d = {"first": 1, "second": 1, "third": 2, "fourth": 3, "fifth": 5, "sixth": 8}
s = {1, 1, 2, 3, 5, 8}

print("l is a {1}, values = {0} ".format(l, type(l).__name__))
print("d is a {1}, values {0}".format(d, type(d).__name__))
print("s is a {1}, values {0}".format(s, type(s).__name__))

print("The number in the sequence is {0}+{1} = {2}".format(
    l[-1], l[-2], l[-1] + l[-2]
))
l.append(l[-1] + l[-2])
l.append(l[-1] + l[-2])
l.append(l[-1] + l[-2])

print("Is 'seventh' in the dictionary?")
print( 'seventh' in d)

print("let's add it...")
d['seventh'] = 13
print("Is 'seventh' in the dictionary?")
print( "{0}, the value is {1}.".format('seventh' in d, d['seventh']))

print("Let's add some items to the set, s: adding 13 => ")
s.add(13)
print(s)
print("try adding it a few more times")
s.add(13)
s.add(13)
s.add(13)
print(s)

print()
