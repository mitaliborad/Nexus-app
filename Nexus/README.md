# Nexus-app : Social Media Application
Summary steps (do in order):
1. clone the repository and create a virtual environment and activate it 
2. set .env from .env.example and run the server using command : python manage.py runserver

## Register 
**Register Page API**
- CustomUserManager is created with email required with password
- User Model created with delete username field from default BaseUser and override email as a username.
- in serializers created a UserSerializer with repeat_password new field , also written the logic for match password and repeat_password fields and save it in database
- give a path /account/register 
- http://127.0.0.1:8000/account/register

## Login 
**Login Page API**
- In the user model i have created a tokens function to assign the user with Refresh and Access Tokens
- i have created a LoginSerializer with email verification and check that account is active - after confirm assign a jwt token to the user 
- in the url define Login url which has permission AllowAny and check register data match email and password and provide jwt token.
- http://127.0.0.1:8000/account/login
 - created a homwview for verify jwt token verification

## Logout
**Logout Page API**
- At the Logout serializer i added a refresh field and according to that field it will find the user and after that according to that it will blacklist that refresh token 
- also added ROTATE_REFRESH_TOKENS for blacklisting previos token after refresh a token.
- also added refresh token api and url path for get a new token
- http://127.0.0.1:8000/account/refresh
- http://127.0.0.1:8000/account/logout

## User Profile
**User Profile API**
- authentication required
- first of at account.user model i ave http://127.0.0.1:8000/profile/1/added two fields like bio and profile picture fields which are allow to null
- also added Multipartparsers for parse image and form data in settings
- after that created a Userprofile serializer and define serializer method field for return name from the email
- and created a userprofile view using RetrieveUpdateDestroyAPIView generic 
- also in the url path add primary key that's why using primary key user can update the data
- images are saving in the profile_pictures folder.
- http://127.0.0.1:8000/profile/1/
- also add liked_post and created_post fields using serializer method fields for show user to liked_posts and created_posts by that particular user.

## Post

**Create Post**
- i have created a new post model in new app post and define many-to-one relationship from user model.
- also i have added a filefield in media field so user can upload a post as image or video whatever they want and in the serializer class i have added a validate data logic which will handle the file upload types like jpeg, mp4,etc...
- also in serializers intialize a new field called username which use serializer method and return a username from the user model.
- for create and list vies i have used ListCreateAPIView.
- so when user will create a post that will return a related username also : http://127.0.0.1:8000/post/create/

**Get Feed**
- for show a feed i have added a read logic in ListCreateAPIView and also simply get all objects with order by latest created at and added a path : http://127.0.0.1:8000/post/feed/

**Update-Delete Post**
- i have added RetrieveUpdateDestroyAPIView which will contains logic of put, patch, delete and also added url path , in the url path i have added primary key also.

## Like
- first of all create a model for like post and define user and post model using forign key
- after that add fields in serializer and validate the data and also add function for user likes count
- in the views use ListCreateAPIView and define post method in it and add the logic for like , likes count and dislike

## Comment
- create a comment model which has fields like post_id , content - so user can podt a comment using post id and also create a total counts serializer field which will count the total numbers of comments of that post

