from rest_framework import serializers

class OTPSerializer(serializers.Serializer):
    otp_code = serializers.CharField(max_length=6)
