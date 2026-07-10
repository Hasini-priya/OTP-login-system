import random
import time
import getpass

# Simulated database
users = {
    "hasini": "1234",
    "priya": "abcd"
}

print("===== 🔐 Advanced OTP Login System =====")

# Login attempt limit
login_attempts = 3

while login_attempts > 0:
    uname = input("Enter username: ").strip().lower()

    # Password input choice
    print("\nChoose password input mode:")
    print("1. Show password")
    print("2. Hide password")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "2":
        pwd = getpass.getpass("Enter password: ")
    else:
        pwd = input("Enter password: ")

    if uname in users and users[uname] == pwd:
        print("\n✅ User verified successfully!")
        break
    else:
        login_attempts -= 1
        print(f"❌ Incorrect credentials. Attempts left: {login_attempts}")

        # Log failed login
        with open("log.txt", "a") as f:
            f.write(f"{uname} failed login attempt\n")

        if login_attempts == 0:
            print("\n🚫 Account locked due to multiple failed attempts")
            exit()

# Generate OTP
otp_value = str(random.randint(1000, 9999))
otp_time = time.time()

print("\n📲 OTP sent successfully!")
print("(Demo OTP:", otp_value, ")")

attempts_left = 3

while attempts_left > 0:
    entered = input("Enter OTP (or type RESEND): ").strip()

    # OTP expiry check (30 seconds)
    if time.time() - otp_time > 30:
        print("⏳ OTP expired. Generating new OTP...")
        otp_value = str(random.randint(1000, 9999))
        otp_time = time.time()
        print("(New OTP:", otp_value, ")")
        continue

    # Resend OTP
    if entered.lower() == "resend":
        otp_value = str(random.randint(1000, 9999))
        otp_time = time.time()
        print("🔄 New OTP generated:", otp_value)
        continue

    if entered == otp_value:
        print("\n🎉 Access Granted! Login Successful ✅")

        # Log success
        with open("log.txt", "a") as f:
            f.write(f"{uname} logged in successfully\n")
        break
    else:
        attempts_left -= 1
        print(f"❌ Invalid OTP. Attempts remaining: {attempts_left}")

if attempts_left == 0:
    print("\n🚫 Login blocked due to multiple incorrect OTP attempts")

    with open("log.txt", "a") as f:
        f.write(f"{uname} failed OTP verification\n")