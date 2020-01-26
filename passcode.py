def incorrectPasscodeAttempts(passcode, attempts):
    if len(attempts) < 10:
        return False
    wrong = 0
    for i in attempts:
        if wrong >= 10:
            return True
        if i != passcode:
            wrong += 1
        else:
            wrong = 0
    return wrong >= 10


attempts = ["1111",  "4444",  "9999",  "3333",  "8888",  "2222",  "7777", "0000",  "6666",  "7285",  "5555",  "1111" ]
print(incorrectPasscodeAttempts('1111', attempts))