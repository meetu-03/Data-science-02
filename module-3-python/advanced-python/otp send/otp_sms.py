import os
from twilio.rest import Client 


# =========================
# YOUR TWILIO DETAILS
# =========================

ACCOUNT_SID = "ACefe286227c9b537269f734cb7e76a593"
AUTH_TOKEN = "1a29879925b2b9f8c300c51b5b08951b"
VERIFY_SERVICE_SID = "VA912a7e2808378fced2c708d66bb220c2"

# Create Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# =========================
# ENTER PHONE NUMBER
# =========================

phone = input("Enter mobile number with country code: ")

# Example:
# +919998003879


# =========================
# SEND OTP
# =========================

verification = client.verify.v2.services(
    VERIFY_SERVICE_SID
).verifications.create(
    to=phone,
    channel="sms"
)

print("OTP sent successfully!")
print("Status:", verification.status)


# =========================
# ENTER OTP
# =========================

otp = input("Enter the OTP you received: ")


# =========================
# VERIFY OTP
# =========================

result = client.verify.v2.services(
    VERIFY_SERVICE_SID
).verification_checks.create(
    to=phone,
    code=otp
)

if result.status == "approved":
    print("✅ OTP verified successfully!")
else:
    print("❌ Wrong OTP")