brain_impluse = ""
motor_nerve_signal = ""
organs = ['lungs', 'muscles', 'heart', 'stomach']
condition = {"lungs": "normal", "muscles": "relaxed", "heart": "normal", "stomach": "digestion"}

print("WELCOME TO THE CENTRAL NERVOUS SIMULATION!")
print("Type 'end' to exit the simulation")
print("*" * 43)

# Simulation of nervous system
while True:
    brain_impluse = input("Brain: What is your message? ").lower()
    if brain_impluse == "end":
        print("SIMULATION ENDED!")
        break
    elif brain_impluse not in ["control heart", "control lungs", "control stomach", "control muscles", "run"]:
        print("Invalid brain message:")
    if brain_impluse == "run":
        print("CONTINUE THE SIMULATION:")
        continue
    motor_nerve_signal = input("Nerve: What message to send: ")
    if motor_nerve_signal == "":
        print("Nerve: There is no message found, skipping the simulation!")
        break

    # heart organ
    if brain_impluse == "control heart":
        if motor_nerve_signal == "increase":
            print("INCREASE HEART RATE!")
        elif motor_nerve_signal == "decrease":
            print("DECREASE HEART RATE!")
        else:
            print("INVALID SIGNAL FOR HEART!")

    # lungs organ
    elif brain_impluse == "control lungs":
        if motor_nerve_signal == "faster":
            print("FASTER BREATHING!")
        elif motor_nerve_signal == "slower":
            print("SLOWER BREATHING!")
        else:
            print("INVALID SIGNAL FOR LUNGS!")

    # muscles organ
    elif brain_impluse == "control muscles":
        if motor_nerve_signal == "tense":
            print("MUSCLES ARE TENSED!")
        elif motor_nerve_signal == "relax":
            print("MUSCLES ARE RELAXED!")
        else:
            print("INVALID SIGNAL FOR MUSCLES!")

    # stomach organ
    elif brain_impluse == "control stomach":
        if motor_nerve_signal == "start":
            print("STOMACH STARTED DIGESTION!")
        elif motor_nerve_signal == "stop":
            print("STOMACH STOPPED DIGESTION!")
        else:
            print("INVALID SIGNAL FOR STOMACH!")

    else:
        print("Try again, invalid message:")

    # Print conditions for each organ
    for organ in organs:
        print(f"Condition of {organ}: {condition[organ]}")

    print("*" * 43)

    