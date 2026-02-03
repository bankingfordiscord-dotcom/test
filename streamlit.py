import streamlit as st
def finder(NRIC):
    addFour = False
    num = NRIC[1:]

    if len(NRIC) != 8 or not num.isdigit():
        st.write("Error: Invalid input")
        return False

    if NRIC[0] == "S" or NRIC[0] == "F":
        addFour=False
    elif NRIC[0] == "T" or NRIC[0] == "G":
        addFour = True
    elif NRIC[0] == "M":
        st.write("uh idk man gl")
        return False
    else:
        st.write('Error: Invalid input')
        return False
    match = sum(int(a) * int(b) for a, b in zip(str(num), "2765432"))
    match = (match + 4) % 11 if addFour else match % 11
    lastLetter = ''
    if NRIC[0] == "S" or NRIC[0] == "T":
        match match:
            case 0:
                lastLetter = 'J'
            case 1:
                lastLetter = 'Z'
            case 2:
                lastLetter = 'I'
            case 3:
                lastLetter = 'H'
            case 4:
                lastLetter = 'G'
            case 5:
                lastLetter = 'F'
            case 6:
                lastLetter = 'E'
            case 7:
                lastLetter = 'D'
            case 8:
                lastLetter = 'C'
            case 9:
                lastLetter = 'B'
            case 10:
                lastLetter = 'A'
            case _:
                lastLetter = None
    elif NRIC[0] == "T" or NRIC[0] == "G":
        match match:
            case 0:
                lastLetter = 'X'
            case 1:
                lastLetter = 'W'
            case 2:
                lastLetter = 'U'
            case 3:
                lastLetter = 'T'
            case 4:
                lastLetter = 'R'
            case 5:
                lastLetter = 'Q'
            case 6:
                lastLetter = 'P'
            case 7:
                lastLetter = 'N'
            case 8:
                lastLetter = 'M'
            case 9:
                lastLetter = 'L'
            case 10:
                lastLetter = 'K'
            case _:
                lastLetter = None
    st.write("your NRIC is " + NRIC + lastLetter + '.')

st.header("Welcome to NRIC doxxer.")
st.subheader("Enter your NRIC excluding the last letter")

# Form prevents live updating
with st.form("my_form"):
    user_input = st.text_input("")
    submitted = st.form_submit_button("Submit")

# This only appears/updates after submit is pressed
if submitted:
    finder(user_input)


