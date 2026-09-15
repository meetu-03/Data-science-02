
import requests

# =========================
# MSG91 DETAILS
# =========================

AUTH_KEY = "570537Ab9gkby536aa552c6P1"

# =========================
# MOBILE NUMBER
# =========================

phone = input("Enter mobile number with country code: ")

# Example:
# 919876543210
# Don't use +


# =========================
# SEND OTP
# =========================

send_url = "https://api.msg91.com/api/sendotp.php"

send_params = {
    "authkey": AUTH_KEY,
    "mobile": phone,
    "sender": "SMSIND",
    "otp_length": 4,
    "otp_expiry": 5
}

response = requests.get(send_url, params=send_params)

print("\nSend OTP response:")
print(response.text)


# =========================
# ENTER OTP
# =========================

otp = input("\nEnter OTP received on phone: ")


# =========================
# VERIFY OTP
# =========================

verify_url = "https://api.msg91.com/api/verifyRequestOTP.php"

verify_params = {
    "authkey": AUTH_KEY,
    "mobile": phone,
    "otp": otp
}

verify_response = requests.get(
    verify_url,
    params=verify_params
)

print("\nVerify response:")
print(verify_response.text)


# =========================
# RESULT
# =========================

if "number_verified_successfully" in verify_response.text:
    print("\n✅ OTP VERIFIED!")
else:
    print("\n❌ OTP verification failed.")