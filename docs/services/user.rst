Get Users
------------------------------

.. http:get:: /api/user
   :noindex:

   :synopsis: Get all users
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :>json int id: Id of the user.
   :>json string email: email of the user.
   :>json string avatar: avatar of the user (i.e., location in disk).
   :>json string firstname: First name of the user.
   :>json string lastname: Last name of the user.
   :>json boolean user_status: Is the user active.
   :>json boolean administrator: Is the user an admin. 
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time. 
   :>json int status: status code.
   :status 200: Users successfully retrieved.
   :status 500: Fail to retrieve users.

**Example Response**

.. sourcecode:: json

   {
      "/api/users":{
         "content":[
            {
               "administrator":1,
               "avatar":null,
               "createdon":"Thu, 18 Nov 2021 12:38:43 GMT",
               "email":"admin@sam.pt",
               "firstName":"Administrator",
               "id":1,
               "lastName":null,
               "updatedon":"Thu, 18 Nov 2021 12:38:43 GMT",
               "user_status":1
            },
            {
               "administrator":0,
               "avatar":null,
               "createdon":"Thu, 18 Nov 2021 12:38:43 GMT",
               "email":"forrest@sam.pt",
               "firstName":"Forrest",
               "id":2,
               "lastName":"Gump",
               "updatedon":"Thu, 18 Nov 2021 12:38:43 GMT",
               "user_status":1
            }
         ],
         "status":200
      }
   }


.. raw:: html

   <hr/>

.. http:get:: /api/user/(string:email)
   :noindex:

   :synopsis: Get a user by ``email``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param email: The email of the user to be retrieved.
   :>json int id: Id of the user.
   :>json string email: email of the user.
   :>json string avatar: avatar of the user (i.e., location in disk).
   :>json string firstname: First name of the user.
   :>json string lastname: Last name of the user.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: status code.
   :status 200: User successfully retrieved.
   :status 500: Fail to retrieve user.

**Example Response**

.. sourcecode:: json

   {
      "/api/user/forrest@sam.pt":{
         "avatar":null,
         "email":"forrest@sam.pt",
         "firstName":"Forrest",
         "id":2,
         "lastName":"Gump",
         "status":200
      }
   }


Get User Groups
------------------------------
.. http:get:: /api/user/(string:email)/groups
   :noindex:

   :synopsis: Get the list of groups mapped to a user identified by ``email``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param email: The email of the user.
   :>json int user_id: Id of the user.
   :>json string user_email: email of the user.
   :>json string user_group: Group of the user.
   :>json int status: status code.
   :status 200: User groups successfully retrieved.
   :status 500: Fail to retrieve user groups.

**Example Response**

.. sourcecode:: json

   {
      "/api/user/admin@SAM.pt/groups":{
         "content":[
            {
               "user_email":"admin@sam.pt",
               "user_group":"Administrators",
               "user_id":1
            },
            {
               "user_email":"admin@sam.pt",
               "user_group":"Users",
               "user_id":1
            }
         ],
         "status":200
      }
   }


Check if User is an Admin
------------------------------
.. http:get:: /api/user/(string:email)/admin
   :noindex:

   :synopsis: Check if the user identified by ``email`` is an administrator.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param email: The email of the user to be checked.
   :>json boolean admin: Is the user an admin.
   :>json int status: status code.
   :status 200: Check performed to see if the user is an administrator.
   :status 500: Fail to verify user group.

**Example Response**

.. sourcecode:: json

   {
      "/api/user/admin@sam.pt/admin":{
         "admin":1,
         "status":200
      }
   }


Add User
------------------------------
.. http:post:: /api/user
   :noindex:

   :synopsis: Add a new user.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :<json string email: User email.
   :<json string psw: User password.
   :<json string firstname: User first name.
   :<json string lastname: User last name.
   :<json string avatar: avatar of the user (i.e., location in disk).
   :<json Object g-recaptcha-response:  Google ReCaptcha response object.
   :>json int status: status code.
   :status 200: New user added.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to add user.

.. important::

   On a production environment, please, do not post the password without SSL enabled.

**Example Request**

.. sourcecode:: json

   {
      "email":"new_user@user.com",
      "psw":"123",
      "firstname":"First Name",
      "lastname":"Last Name",
      "avatar":"new_user.png",
      "g-recaptcha-response": null
   }

.. note::

   The g-recaptcha-response should not be ``null``, a Google ReCaptcha response should be included in the JSON request object. 
   

**Example Response**

.. sourcecode:: json

   {
      "/api/user":{
         "status":200
      }
   }

Update User
------------------------------
.. http:put:: /api/user/(string:email)
   :noindex:

   :synopsis: Updates a user by ``email``
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param email: The email of the user to be updated.
   :<json string email: User email.
   :<json string psw: User password.
   :<json string firstname: User first name.
   :<json string lastname: User last name.
   :<json string avatar: avatar of the user (i.e., location in disk).
   :>json int status: status code.
   :status 200: User updated.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to update user.

.. important::

   On a production environment, please, do not post the password without SSL enabled.

**Example Request**

.. sourcecode:: json

   {
      "email":"new_user_updated@user.com",
      "firstname":"First Name Updated",
      "lastname":"Last Name Updated",
      "psw":"1234",
      "avatar":"new_user_updated.png",
   }

**Example Response**

.. sourcecode:: json

   {
      "/api/user":{
         "status":200
      }
   }

Remove User
------------------------------
.. http:delete:: /api/user/(string:email)
   :noindex:

   :synopsis: Removes a user by ``email``
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param email: The email of the user to be removed.
   :>json int status: status code.
   :status 200: User successfully removed.
   :status 500: Fail to remove user.

**Example Response**

.. sourcecode:: json

   {
      "/api/user/new_user@user.com":{
         "status":200
      }
   }