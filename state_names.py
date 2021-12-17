"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention


def main():
    CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                    "WA": "Western Australia",
                    "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
    display_dic(CODE_TO_NAME)
    del_state(CODE_TO_NAME)


def display_dic(CODE_TO_NAME):
    for item, value in CODE_TO_NAME.items():
        print(f"{item} is {value}")


def del_state(CODE_TO_NAME):
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()


main()
