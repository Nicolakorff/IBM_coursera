#Write a function that takes two integers namely hours & minutes, converts them to seconds, and adds them together to display the total seconds.

hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))

secondsh = hours*3600
secondsm = minutes*60

seconds = secondsh+secondsm

print('Total seconds:', seconds)
