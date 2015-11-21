import time
import webbrowser

'''
function accepts a time and url and executes opening the url in a
web browser per unit time.
'''



# wrap time and url open code in loop

count = 0

while count < 3:
    
    ## pause for requisite period

    time.sleep(10)

    ## open url with song

    webbrowser.open('https://www.youtube.com/watch?v=FKscaLcO7ko')

    count +=1
