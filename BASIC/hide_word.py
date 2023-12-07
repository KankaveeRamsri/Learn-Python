user_input = str(input("Enter text: "))
hide_text = str(input("Enter filter word: "))

print('Text after filter is "{}"'.format(user_input.replace(hide_text,'*'*len(hide_text))))