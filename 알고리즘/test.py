def to_jaden_case(string):
    # ...
	list_text=string.split(' ')
	result_text=[]

	for i in list_text:
		s=i[0].upper()
		s=s+i[1:]
		result_text.append(s)
	return ' '.join(result_text)

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))