def titleize(sentence):
    return  ' '.join([word[0].upper() + word[1:] for word in sentence.split()])


print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"
    