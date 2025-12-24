# Nexus-app
Summary steps (do in order):

**Register Page API**
- CustomUserManager is created with email required with password
- User Model created with delete username field from default BaseUser and override email as a username.
- in serializers created a UserSerializer with repeat_password new field , also written the logic for match password and repeat_password fields and save it in database
- give a path /account/register 
- http://127.0.0.1:8000/account/register

**Login Page API**
- In the user model i have created a tokens function to assign the user with Refresh and Access Tokens
- i have created a LoginSerializer with email verification and check that account is active - after confirm assign a jwt token to the user 
- in the url define Login url which has permission AllowAny and check register data match email and password and provide jwt token.
- http://127.0.0.1:8000/account/login
 - created a homwview for verify jwt token verification