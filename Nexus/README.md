# Nexus-app
Summary steps (do in order):

**Register Page API**
- CustomUserManager is created with email required with password
- User Model created with delete username field from default BaseUser and override email as a username.
- in serializers created a UserSerializer with repeat_password new field , also written the logic for match password and repeat_password fields and save it in database
- give a path /account/register 
- http://127.0.0.1:8000/account/register
