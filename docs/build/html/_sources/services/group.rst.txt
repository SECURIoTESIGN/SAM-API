Get Groups
------------------------------

.. http:get:: /api/group
   :noindex:

   :synopsis: Get all groups.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :>json int id: Id of the group.
   :>json string designation: Description of the group.
   :>json array modules: Array of modules mapped to the group.
   :>json array users: Array of users.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: status code. 
   :status 200: Groups successfully retrieved.
   :status 500: Fail to retrieve groups.

**Example Response**

.. sourcecode:: json

   {
      "/api/groups":{
         "content":[
            {
               "createdon":"Thu, 18 Nov 2021 12:38:43 GMT",
               "designation":"Administrators",
               "id":1,
               "modules":[],
               "updatedon":"Thu, 18 Nov 2021 12:38:43 GMT",
               "users":[
                  {
                     "avatar":null,
                     "email":"admin@sam.pt",
                     "firstName":"Administrator",
                     "id":1,
                     "lastName":null
                  }
               ]
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/group/(int:id)
   :noindex:

   :synopsis: Get a group by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param id: The id of the group to be retrieved.
   :>json int id: Id of the group.
   :>json string designation: Description of the group.
   :>json array modules: Array of modules mapped to the group.
   :>json array users: Array of users.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: status code.  
   :status 200: Groups successfully retrieved.
   :status 500: Fail to retrieve groups.

**Example Response**

.. sourcecode:: json

   {
      "/api/groups":{
         "content":[
            {
               "createdon":"Thu, 18 Nov 2021 12:38:43 GMT",
               "designation":"Administrators",
               "id":1,
               "modules":[],
               "updatedon":"Thu, 18 Nov 2021 12:38:43 GMT",
               "users":[
                  {
                     "avatar":null,
                     "email":"admin@sam.pt",
                     "firstName":"Administrator",
                     "id":1,
                     "lastName":null
                  }
               ]
            }
         ],
         "status":200
      }
   }

Add Group
------------------------------

.. http:post:: /api/group
   :noindex:

   :synopsis: Adds a new group.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :<json string designation: The name of the group.
   :<json array users: The id of each user that will belong to the new group.
   :<json array modules: The id of each module that will belong to the new group.
   :>json int id: Id assigned to the new group.
   :>json int status: status code.
   :status 200: New group added with `id` (see **example response**).
   :status 500: Fail to add a new group.

**Example Request**

.. sourcecode:: json

	{"designation":"New Group","users":[{"id":1}],"modules":[{"id":1}]}

**Example Response**

.. sourcecode:: json

   {"/api/group":{"id":3,"status":200}}


Edit Group
------------------------------

.. http:put:: /api/group
   :noindex:

   :synopsis: Updates the information of a group.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :<json int id: The id of the group you want to update.
   :<json string designation: The new name of the group.
   :>json int status: status code.
   :status 200: Group successfully updated.
   :status 500: Fail to update group.

**Example Request**

.. sourcecode:: json

	{"id":3,"designation":"New Group Updated"}

**Example Response**

.. sourcecode:: json

   {"/api/group":{"status":200}}


Remove Group
------------------------------

.. http:delete:: /api/group/(int:id)
   :noindex:

   :synopsis: Remove a group by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param id: The id of the group to be removed.
   :>json int status: status code.
   :status 200: Group successfully removed.
   :status 500: Fail to remove group.

**Example Response**

.. sourcecode:: json

   {"/api/group/3":{"status":200}}