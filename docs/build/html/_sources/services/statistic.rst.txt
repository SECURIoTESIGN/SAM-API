.. http:get:: /api/statistics
   :noindex:

   :synopsis: Get the global statistics of the plataform.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :>json int answers: The total number of responses.
   :>json int modules: The total number of modules.
   :>json int recommendations: The total number of recommendations.
   :>json int sessions: The total number of sessions executed by users.
   :>json int users: The total number of registered users.
   :>json int status: Status code.

   :status 200: Statistics successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve statistics.

**Example Response**

.. sourcecode:: json

   {
      "/api/statistics":{
         "users":2
         "modules":2,
         "questions":30,
         "answers":60,
         "recommendations":10,
         "sessions":2,
         "status":200,
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/statistic/users
   :noindex:

   :synopsis: Get the total number of users of the platform.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int size: The total number of registered users.

   :status 200: Statistics successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve statistics.

**Example Response**

.. sourcecode:: json

   {"/api/statistic/users":{"size":2, "status":200}}

.. raw:: html

   <hr/>


.. http:get:: /api/statistic/modules
   :noindex:

   :synopsis: Get the total number of modules of the platform.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int size: The total number of modules.
   :>json array top: An array that contains the topmost used modules.
   :>json int status: Status code.

   :status 200: Statistics successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve statistics.

**Example Response**

.. sourcecode:: json

   {
      "/api/statistic/modules":{
         "size":2,
         "top":[
            {
               "shortname":"SRE"
               "displayname":"Security Requirements",
               "occurrences":2,
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/statistic/questions
   :noindex:

   :synopsis: Get the total number of questions of the platform.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int size: The total number of questions.
   :>json int status: Status code.

   :status 200: Statistics successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve statistics.

**Example Response**

.. sourcecode:: json

   {"/api/statistic/questions":{"size":30, "status":200}}

.. raw:: html

   <hr/>


.. http:get:: /api/statistic/answers
   :noindex:

   :synopsis: Get the total number of answers of the platform.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int size: The total number of answers.
   :>json int status: Status code.

   :status 200: Statistics successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve statistics.

**Example Response**

.. sourcecode:: json

   {"/api/statistic/answers":{"size":60, "status":200}}

.. raw:: html

   <hr/>


.. http:get:: /api/statistic/recommendations
   :noindex:

   :synopsis: Get the total number of recommendations of the platform.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int size: The total number of recommendations.
   :>json array top: An array that contains the topmost given recommendations.
   :>json int status: Status code.

   :status 200: Statistics successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve statistics.

**Example Response**

.. sourcecode:: json

   {
      "/api/statistic/recommendations":{
         "size":10,
         "top":[
            {
               "content":"Confidentiality",
               "occurrences":2
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>


.. http:get:: /api/statistic/sessions
   :noindex:

   :synopsis: Get the total number of sessions per day created by users of the platform.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json array top: An array that contains the number of sessions per day. 
   :>json int status: Status code.

   :status 200: Statistics successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve statistics.

**Example Response**

.. sourcecode:: json

   {
      "/api/statistic/sessions":{
         "top":[
            {
               "date":"Sat, 20 Nov 2021 00:00:00 GMT",
               "occurrences":2
            }
         ],
         "status":200
      }
   }
