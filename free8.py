print('This is the helper center')
question = input('What is your question? : '.lower())
if question == 'how to use this program':
    print('You can use this program by typing your question and I will try to answer it.')
elif question == 'what is this program':
    print('This program is a helper center that can answer your questions.')
elif question == '':
    print('You did not ask a question.')
else:
    print("I don't know the answer to that question. Please try again.")
