from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=('username','email','first_name','password','password_confirm')
        extra_kwargs = {
            'password': {'write_only': True,'required':True},
            'email': {'required': True},
            }
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Must Enter Email")

        return value

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username')
        )

        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {'detail': "Password Didn't Match"}
            )

        user.set_password(self.validated_data.get('password'))
        user.save()
        # return user