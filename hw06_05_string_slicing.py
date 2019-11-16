# hw06_05_string_slicing.py

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end
# of the line below. Convert the extracted value to a floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475";
end = text.find('.')
print(end)

number = float(text[end-1:])
print(number)
#print(type(number))

