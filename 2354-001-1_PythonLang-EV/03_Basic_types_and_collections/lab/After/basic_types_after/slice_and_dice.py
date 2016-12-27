print("Working with slices")


print("Let's slice up some strings. Note that this would work on lists as well")
print("All of the follow is generated using slices (e.g. text[0:index])")
text = "Today it is the beginning of spring. Let's rejoice, the sun is out!"
print("We will start with this string: " + text)
print()
index = text.find(' ')
print("The first word ends at index {0} and is {1}.".format(index, text[:index]))
index = text.find('.')
print("The last sentence is: '{0}'".format(text[index+1:].strip()))
print("The last six characters of the string are: '{0}'".format(text[-6:]))

print("The first five characters of the second sentence are: '{0}'".format(
    text[index+1:].strip()[:5]
))