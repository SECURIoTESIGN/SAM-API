Get Dependencies
------------------------------

.. http:get:: /api/dependencies
   :noindex:

   :synopsis: Get dependencies of a ``module``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int id: Id of the dependency.
   :>json int module_id: Id of the module.
   :>json int depends_on: Id of the module that the ``module_id`` depends on.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Dependencies successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve dependencies.

**Example Response**

.. sourcecode:: json

   {
      "/api/dependencies":{
         "content":[
            {
               "id":1,
               "module_id":1,
               "depends_on":2,
               "createdon":"Sat, 20 Nov 2021 13:00:50 GMT",
               "updatedon":"Sat, 20 Nov 2021 13:00:50 GMT"
            }
         ],
         "status":200
      }
   }

.. note::

   The ``depends_on`` parameter describes the id of the module that the current ``module_id`` depends on.

.. raw:: html

   <hr/>

.. http:get:: /api/dependency/(int:id)
   :noindex:

   :synopsis: Get dependency identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the dependency.

   :>json int id: Id of the dependency.
   :>json int module_id: Id of the module.
   :>json int depends_on: Id of the module that the ``module_id`` depends on.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Dependency successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve dependency.

**Example Response**

.. sourcecode:: json

   {
      "/api/dependency/1":{
         "content":[
            {
               "id":1,
               "module_id":1,
               "depends_on":2,
               "createdon":"Sat, 20 Nov 2021 13:00:50 GMT",
               "updatedon":"Sat, 20 Nov 2021 13:00:50 GMT"
            }
         ],
         "status":200
      }
   }

.. note::

   The ``depends_on`` parameter describes the id of the module that the current ``module_id`` depends on.

.. raw:: html

   <hr/>


.. http:get:: /api/dependency/module/(int:id)
   :noindex:

   :synopsis: Get dependencies of a module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the module.

   :>json int id: Id of the dependency and dependecy module.
   :>json object module: Information of the module that module ``id`` depends on.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Dependencies successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve dependencies.

**Example Response**

.. sourcecode:: json

   {
      "/api/dependency/module/2":{
         "content":[
            {
               "id":1,
               "module":{
                  "id":1,
                  "shortname":"SRE",
                  "fullname":"Security Requirements Elicitation",
                  "displayname":"Security Requirements"
               },
               "createdon":"Wed, 17 Nov 2021 14:14:26 GMT",
               "updatedon":"Wed, 17 Nov 2021 14:14:26 GMT"
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>


.. http:get:: /api/dependency/module/(int:id)/depends/(int:id)
   :noindex:

   :synopsis: Get dependency information of a module ``id`` that depends on module ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the module or id of the module it depends on.

   :>json int id: Id of the dependency.
   :>json int module_id: Id of the module.
   :>json int depends_on_module_id: Id of the module that the ``module_id`` depends on.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Dependency successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve dependency.

**Example Response**

.. sourcecode:: json

   {
      "/api/dependency/module/2/depends/1":{
         "id":1,
         "module_id":2,
         "depends_on_module_id":1,
         "createdon":"Sat, 20 Nov 2021 13:00:50 GMT",
         "updatedon":"Sat, 20 Nov 2021 13:00:50 GMT",
         "status":200
      }
   }



Add Dependency
------------------------------

.. http:post:: /api/dependency
   :noindex:

   :synopsis: Add a new dependency.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json int id: Id of the dependency.
   :<json int module_id: Id of the module.
   :<json int depends_on: Id of the module that the ``module_id`` depends on.
   
   :>json int id: The id of new dependency.
   :>json int status: Status code.

   :status 200: Dependency successfully added.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to add dependency.

**Example Request**

.. sourcecode:: json

   {"module_id":1, "depends_on":2}

**Example Response**

.. sourcecode:: json

   {"/api/dependency":{"id":2, "status":200}}


Edit Dependency
------------------------------

.. http:put:: /api/dependency
   :noindex:

   :synopsis: Updated a dependency identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json int id: Id of the dependency.
   :<json int module_id: Id of the module.
   :<json int depends_on: Id of the module that the ``module_id`` depends on.
   :<json int depends_on_p: Id of the module that the ``module_id`` previously depended on.
   
   :>json int id: The id of new dependency.
   :>json int status: Status code.

   :status 200: Dependency successfully updated.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to updated dependency.

**Example Request**

.. sourcecode:: json

   {"id":2, "module_id":1, "depends_on":3, "p_depends_on":2}

**Example Response**

.. sourcecode:: json

   {"/api/dependency":{"id":3, "status":200}}



Remove Dependency
------------------------------

.. http:delete:: /api/dependency/(int:id)
   :noindex:

   :synopsis: Remove a dependency identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :formparameter id: The id of dependency to remove.
   
   :>json int status: Status code.

   :status 200: Dependency successfully removed.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to remove dependency.

**Example Response**

.. sourcecode:: json

   {"/api/dependency":{"status":200}}