"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""
silent = False
reverse = False
empty_list = []

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'replay reversed', 'replay reversed silent']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100



def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name.upper()


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
        


    history(command.lower())
    return command.lower()


def history(command):
    global empty_list
    empty_list.append(command)
    if 'off' == command:
        empty_list = []

def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
   
    (command_name, arg1) = split_command_input(command)
    if arg1.lower() == "silent" or arg1.lower() == 'reversed' or arg1.lower()== "reversed silent" or arg1.lower() == "replay":
        return command_name.lower() in valid_commands and arg1
    
    elif "-" in arg1:
        new_arg = arg1.split("-")
        if new_arg[0].isdigit() and new_arg[1].isdigit():
            return command_name.lower() in valid_commands and arg1
        else:
            return False
    
    elif "silent" in arg1 or "reversed" in arg1:
        return command_name.lower() in valid_commands and arg1

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1)) 


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


    
def replay(robot_name, listt):
    listt = ["forward", "back", "left", "right", "sprint"]
    lisst = [i for i in empty_list if i.split()[0] in listt]

    for j in lisst:
        handle_command(robot_name, j)

    return True, f" > {robot_name} replayed {len(lisst)} commands."


def replay_silent(robot_name, listt):
    global silent
    listt = ["forward", "back", "left", "right", "sprint"]
    lisst = [i for i in empty_list if i.split()[0] in listt]
    silent = True
    for j in lisst:
        handle_command(robot_name, j)
    silent = False

    return True, f" > {robot_name} replayed {len(lisst)} commands silently."


def replay_reversed(robot_name,listt):
    listt = ["forward", "back", "left", "right", "sprint"]
    lisst = [i for i in empty_list if i.split()[0] in listt]
    # lisst.sort(reverse = True)
    lisst.reverse()
    for j in lisst:
        handle_command(robot_name, j)

    return True, f" > {robot_name} replayed {len(lisst)} commands in reverse."

def replay_reversed_silent(robot_name, lisst):
    global silent
    listt = ["forward", "back", "left", "right", "sprint"]
    lisst = [i for i in empty_list if i.split()[0] in listt]
    # lisst.sort(reverse = True)
    lisst.reverse()
    silent = True
    for j in lisst:
        handle_command(robot_name, j)
    silent = False

    return True, f" > {robot_name} replayed {len(lisst)} commands in reverse silently."

def replay_n(robot_name, arg,command):
    (command_name, arg) = split_command_input(command)
    listt = ["forward", "back", "left", "right", "sprint"]
    lisst = [i for i in empty_list if i.split()[0] in listt]

    for j in lisst[-int(arg):]:
        handle_command(robot_name, j)

    return True, f" > {robot_name} replayed {len(lisst[-int(arg):])} commands."
   

def replay_range(robot_name,list):
    listt = ["forward", "back", "left", "right", "sprint"]
    lisst = [i for i in list if i.split()[0] in listt]

    for j in lisst:
        handle_command(robot_name, j)

    if silent == True:
        return True, f" > {robot_name} replayed {len(lisst)} commands silently."
    
    elif reverse == True:
        return True, f" > {robot_name} replayed {len(lisst)} commands in reverse."
    
    return True, f" > {robot_name} replayed {len(lisst)} commands."


def replay_nm():
    pass

    

def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global silent, reverse

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay' and len(arg) == 0:
        (do_next, command_output) = replay(robot_name, empty_list)
    elif command_name == 'replay' and arg == "silent":
        (do_next, command_output) = replay_silent(robot_name, empty_list)
    elif command_name == 'replay' and arg == 'reversed':
        (do_next, command_output) = replay_reversed(robot_name, empty_list)
    elif command_name == 'replay' and arg == 'reversed silent':
        (do_next, command_output) = replay_reversed_silent(robot_name, empty_list)

    elif command_name == 'replay' and arg.isdigit():
        (do_next, command_output) = replay_n(robot_name,arg, command )

    elif command_name == 'replay' and "silent" in arg:
        silent = True
        new_arg = arg.split()
        num1 = int(new_arg[0])
        new_list = empty_list[-num1 -1:]
        (do_next, command_output) = replay_range(robot_name, new_list)
        silent = False

    elif command_name == 'replay' and "reversed" in arg:
        reverse = True
        new_arg = arg.split()
        empty_list.reverse()
        num1 = int(new_arg[0])
        new_list = empty_list[-num1:]
        (do_next, command_output) = replay_range(robot_name, new_list)
        reverse = False

    elif command_name == 'replay' and "-" in arg:
        num_list = arg.split("-")
        num1 = int(num_list[0])
        num2 = int(num_list[1])
        new_list = empty_list[-num1 -1:-num2 -1]
        (do_next, command_output) = replay_range(robot_name, new_list)
        

    if silent == False:
        print(command_output)
        show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
