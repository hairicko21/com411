import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.user_input as user_input
import basics.input.string_operators as string_operators
import basics.input.review_ as review_
import basics.input.data_types as data_types
import basics.input.ascii_robot as ascii_robot
import basics.decisions.simple_decision.modulo_operator as modulo_operator
import basics.decisions.simple_decision.if_ as if_
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.counter as counter
import basics.decisions.simple_decision.comparison_operators as comparison_operators




def run_block_a():
    print("Which program in 'Block A: Basics/output' do you wish to run?")
    response = input()
    if (response == "simple_message"):
        simple_message.run()
    elif (response == "multiline_message"):
        multiline_message.run()
    elif (response == 'escape_characters'):
        escape_characters.run()
    elif (response == ascii_art):
        ascii_art.run()
    else:
      print('try something else...')

def run_block_a_input():
    print('Which program in ''Block A: Basics/input'' do you wish to run?')
    response = input()
    if (response == 'user_input'):
        user_input.run()
    elif (response == 'string_operators'):
        string_operators.run()
    elif (response == 'review'):
        review_.run()
    elif (response == 'data_types'):
        data_types.run()
    elif (response == 'ascii_robot'):
        ascii_robot.run()
    else:
      print('try something else...')

def run_block_a_sim_dec():
    print('Which program in ''Block A: Basics/decisions/simple_decision'' do you wish to run?')
    response = input()
    if (response == 'modulo_operator'):
        modulo_operator.run()
    elif (response == 'if_'):
        if_.run()
    elif (response == 'if_else'):
        if_else.run()
    elif (response == 'if_elif_else'):
        if_elif_else.run()
    elif (response == 'counter'):
        counter.run()
    elif (response == 'comparison_operators'):
        comparison_operators.run()
    else:
      print('try something else...')      


def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics/output' programs")
        print('[b] Run ''Block A: Basics/input'' programs')
        print('[c] Run ''Block A: Basics/decisions/simple_decision'' programs')
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == 'b'):
            run_block_a_input()
        elif (response == 'c'):
            run_block_a_sim_dec()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()