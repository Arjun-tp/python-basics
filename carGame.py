command = input('>')
started = False
stopped = True
cmd = '''
start - to start the car
stop - to stop the car
quit - to exit
'''
if command.lower() == 'help':
    print(cmd)

    while command.lower() != 'quit':
        carCommand = input('>')
        if carCommand.lower() == 'start':
            if started == True:
                print('Car is already started')
            else:
                print('Car Started... Ready to go!!')
                started = True
                stopped = False
        elif carCommand.lower() == 'stop':
            if stopped == True:
                print('Car is already stopped')
            else:
                started = False
                stopped = True
                print('Car Stopped.')
        else:
            break

else:
    print("I don't understand that!!")
