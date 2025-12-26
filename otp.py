import random

# User details stored as tuple (username, password)
user_details = ("hasini", "1234")

print("===== OTP Login System =====")

while True:
    uname = input("Enter username: ").strip().lower()
    pwd = input("Enter password: ").strip()

    if uname == user_details[0] and pwd == user_details[1]:
        print("\nUser verified successfully!")
        break
    else:
        print("Incorrect credentials. Please try again.\n")

# Generate 4-digit OTP
otp_value = str(random.randint(1000, 9999))
print("\nGenerated OTP:", otp_value)
print("(OTP shown for demo purpose)")

attempts_left = 3

while attempts_left > 0:
    entered = input("Enter OTP: ").strip()

    if entered == otp_value:
        print("\nAccess Granted! Login Successful ✅")
        break
    else:
        attempts_left -= 1
        print(f"Invalid OTP. Attempts remaining: {attempts_left}")

if attempts_left == 0:
    print("\nLogin blocked due to multiple incorrect attempts ❌")
