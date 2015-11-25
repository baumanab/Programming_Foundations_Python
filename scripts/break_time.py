import time
import webbrowser

'''
function accepts a time and url and executes opening the url in a
web browser per unit time.
'''

# add a start time message

the_time = time.ctime()

print("This program started on {}").format(the_time)

# wrap time and url open code in loop

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    
    ## pause for requisite period

    time.sleep(10)

    ## open url with song

    webbrowser.open('https://www.youtube.com/watch?v=FKscaLcO7ko')

    break_count +=1
