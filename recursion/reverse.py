def strng_reverse(name):
    if name == "":
        return ''
    return name[-1]+strng_reverse(name[:-1])

print(strng_reverse('nihala'))