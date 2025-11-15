from django.shortcuts import render, redirect
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import base58
import base64

def connect_wallet(request):
    if request.method == "POST":
        public_key_b58 = request.POST.get("public_key")
        message = request.POST.get("message")
        signature_b64 = request.POST.get("signature")

        try:
            # Convert Solana public key from Base58 to bytes
            public_key_bytes = base58.b58decode(public_key_b58)
            verify_key = VerifyKey(public_key_bytes)

            # Decode signature from Base64
            signature = base64.b64decode(signature_b64)

            # Verify the signed message
            verify_key.verify(message.encode(), signature)

            # Success → redirect
            return redirect("wallet_success")

        except (BadSignatureError, ValueError):
            return render(request, "connect.html", {
                "error": "Signature verification failed. Please reconnect wallet."
            })

    return render(request, "connect.html")


def wallet_success(request):
    return render(request, "success.html")
