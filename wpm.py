import time


phrase = 'I am going to be a Python Developer'

word_count = len(phrase.split())

begin = input('Please type: ' + phrase + '/n' +
               'Press enter when ready.')
t0 = time.time()
attempt = input('/n')
t1 = time.time()
attempt_time = (t1 - t0)/60
wpm = str(round(word_count / attempt_time, 2))

if attempt == phrase:
    print('/n' + 'YourWPM: ' + wpm)
else:
    print('/n'+ 'Typed incorrectly. Please try again.')
