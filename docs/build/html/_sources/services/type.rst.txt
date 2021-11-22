Get Types
------------------------------

.. http:get:: /api/types
   :noindex:

   :synopsis: Get types.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int id: Id of the type.
   :>json string name: Name of the type.
   :>json string description: Description of the type.
   :>json array modules: Array of modules mapped to the current type.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: status code.
   :status 200: Types successfully retrieved.
   :status 500: Fail to retrieve types.

**Example Response**

.. sourcecode:: json

   {
      "/api/types":{
         "content":[
            {
               "id":1,
               "name":"Test Type",
               "description":"Test Type Description",
               "modules":[],
               "createdon":"Mon, 20 Sep 2021 09:00:00 GMT",
               "updatedon":"Mon, 20 Sep 2021 09:00:00 GMT"
            }
         ],
         "status":200
      }
   }


.. raw:: html

   <hr/>

.. http:get:: /api/type/(int:id)
   :noindex:

   :synopsis: Get a type identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: id of the type.
   :>json int id: Id of the type.
   :>json string name: Name of the type.
   :>json string description: Description of the type.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: status code.
   :status 200: Type successfully retrieved.
   :status 500: Fail to retrieve type.

**Example Response**

.. sourcecode:: json

   {
      "/api/type/1":{
         "content":[
            {
               "id":1,
               "name":"Test Type",
               "description":"Test Type Description",
               "createdon":"Mon, 20 Sep 2021 09:00:00 GMT",
               "updatedon":"Mon, 20 Sep 2021 09:00:00 GMT"
            }
         ],
         "status":200
      }
   }


Add Type
------------------------------

.. http:post:: /api/type
   :noindex:

   :synopsis: Add a new type.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :<json string name: Name of the type.
   :<json string description: Description of the type.
   :>json int status: status code.
   :status 200: Type successfully added.
   :status 500: Fail to add type.

**Example Request**

.. sourcecode:: json

   {
      "name":"Test Type",
      "description":"Test Type Description"
   }

**Example Response**

.. sourcecode:: json

   {"/api/type":{"status":200}}

Edit Type
------------------------------

.. http:put:: /api/type
   :noindex:

   :synopsis: Update a type.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :<json int id: Id of the module to update. 
   :<json string name: Name of the type.
   :<json string description: Description of the type.
   :>json int status: status code.
   :status 200: Type successfully updated.
   :status 500: Fail to update type.

**Example Request**

.. sourcecode:: json

   {
      "id":1,
      "name":"Test Type Updated",
      "description":"Test Type Updated"
   }

**Example Response**

.. sourcecode:: json

   {"/api/type":{"status":200}}


Remove Type
------------------------------

.. http:delete:: /api/type/(int:id)
   :noindex:

   :synopsis: Remove a type identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param id: The id of the type to be removed.
   :>json int status: status code.
   :status 200: Type successfully removed.
   :status 500: Fail to remove type.

**Example Response**

.. sourcecode:: json

   {"/api/type/1":{"status":200}}