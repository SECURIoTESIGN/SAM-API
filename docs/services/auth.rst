Authenticate User
------------------------------
.. _authenticate:

.. http:post:: /api/user/login
   :noindex:

   :synopsis: Authenticate user with an email and password. The authentication process returns a bearer JWT used to grant users access to SAM's Web services.
   :resheader Content-Type: multipart/form-data
   :formparameter email: The email of the user to be authenticated.
   :formparameter psw: The user password.
   :>json int id: The id of the user. 
   :>json string email: The email of the user.
   :>json string avatar: Avatar of the user (i.e., location in disk).
   :>json boolean is_admin: Is the user an administrator.
   :>json int exp: Expiration time of the token in seconds.
   :>json string token: The bearer JWT.
   :>json int status: status code.
   :status 200: Users successfully authenticated.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 401: Fail to authenticate user / Unauthorized.
   :status 500: Internal server error.
   
**Example Response**

.. sourcecode:: json

   {
      "/api/user/login":{
         "id":1,
         "email":"forrest@sam.pt",
         "avatar":null,
         "is_admin":0,
         "exp":1637410963,
         "token":"eyJ0eXAiOiJKV1QiLCJhb..."
         "status":200,
      }
   }

.. note::

   By default the JSON Web Token (JWT) authentication token will expire after 15 minutes.


Logout User
------------------------------

.. http:post:: /api/user/logout
   :noindex:

   :synopsis: Logout user with the provided authentication token that should be available in the ``Authorization`` request header. 
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :>json int status: status code.
   :status 200: User was successfully logged out.
   :status 500: Unable to logout user. 
   
**Example Response**

.. sourcecode:: json

   {
      "/api/user/logout":{
         "status":200
      }
   }
