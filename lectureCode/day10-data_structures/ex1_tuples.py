screen_size = (800, 600)
print screen_size[0]
#TypeError: 'tuple' object does not support item assignment
try:
    screen_size[0] += 1
except Exception as e:
    print e

# BUT
screen = [800,600]
print screen[0]
screen[0] += 1 
print screen[0]
print "yay it changed."