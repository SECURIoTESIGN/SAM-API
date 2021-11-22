Get Recommendations
------------------------------

.. http:get:: /api/recommendations
   :noindex:

   :synopsis: Get recommendations.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
  
   :>json int id: Id of the recommendation.
   :>json string content: Recommendation name.
   :>json string description: Description of the recommendation.
   :>json string guide: The filename of the recommendation guide.
   :>json array modules: Array of modules mapped to the current recommendation.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Recommendations successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve recommendations.

**Example Response**

.. sourcecode:: json

   {
      "/api/recommendations":{
         "content":[
            {
               "id":1,
               "content":"Confidentiality",
               "description":null,
               "guide":null,
               "modules":[
                  {
                     "id":1,
                     "shortname":"SRE",
                     "displayname":"Security Requirements",
                     "fullname":"Security Requirements Elicitation",
                     "description":"test",
                     "avatar":null,
                     "logic_filename":null,
                     "type_id":null,
                     "createdon":"Sat, 20 Nov 2021 13:29:49 GMT",
                     "updatedon":"Sat, 20 Nov 2021 13:29:49 GMT"
                  }
               ],
               "createdOn":"Sat, 20 Nov 2021 13:29:49 GMT",
               "updatedOn":"Sat, 20 Nov 2021 13:29:49 GMT"
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/recommendation/(int:id)
   :noindex:

   :synopsis: Get recommendation identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :formparameter id: The id of the recommendation.
   
   :>json int id: Id of the recommendation.
   :>json string content: Recommendation name.
   :>json string description: Description of the recommendation.
   :>json string guide: The filename of the recommendation guide.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Recommendation successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve recommendation.

**Example Response**

.. sourcecode:: json

   {
      "/api/recommendation/1":{
         "content":[
            {
               "id":1,
               "content":"Confidentiality",
               "description":null,
               "guide":null,
               "createdOn":"Sat, 20 Nov 2021 13:29:49 GMT",
               "updatedOn":"Sat, 20 Nov 2021 13:29:49 GMT"
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/recommendations/module/(int:id)
   :noindex:

   :synopsis: Finds the set of recommendations for a module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :formparameter id: The id of the module.
   
   :>json int id: Id of the recommendation.
   :>json string content: Recommendation name.
   :>json array questions_answers: An array that contains the mapping between questions and answers for the current recommendation and module.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Recommendations successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve recommendations.

**Example Response**

.. sourcecode:: json

   {
      "/api/recommendations/module/1":{
         "content":[
            {
               "id":1,
               "content":"Confidentiality",
               "questions_answers":[
                  {
                     "question_id":1,
                     "answer_id":1,
                     "createdon":"Sat, 20 Nov 2021 13:29:49 GMT",
                     "updatedon":"Sat, 20 Nov 2021 13:29:49 GMT"
                  }
               ],
               "createdon":"Sat, 20 Nov 2021 13:29:49 GMT",
               "updatedon":"Sat, 20 Nov 2021 13:29:49 GMT"
            }
         ],
         "status":200
      }
   }

.. note:: 

   In this example, for module 1 the recommendation 1 is given if for ``question_id`` the ``answer_id`` is given by a user.

.. raw:: html

   <hr/>



Add Recommendation
------------------------------

.. http:post:: /api/recommendation
   :noindex:

   :synopsis: Add a new recommendation.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json string content: The name of the new recommendation.
   :<json string description: The description of the new recommendation.
   :<json string guide: The filename of the recommendation guide.
   :<json array questions_answers: An array that contains the mapping between questions and answers for the new recommendation.

   :>json int id: The id of the new recommendation.
   :>json int status: Status code.

   :status 200: Recommendation successfully added.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to add recommendation.

**Example Request**

.. sourcecode:: json

   {
      "content":"New Recommendation",
      "description":"New Recommendation Description",
      "guide":"new_recommendation.md",
      "questions_answers":[
         {
            "question_id":1,
            "answer_id":1
         }
      ]
   }

.. important::

   In order to upload a guide for the new recommendation you need to use this service in conjunction with the service detailed in :ref:`/api/file/(string:filename)<upload>`.


**Example Response**

.. sourcecode:: json

   {"/api/recommendation":{"id":4, "status":200}}


Edit Recommendation
------------------------------

.. http:put:: /api/recommendation
   :noindex:

   :synopsis: Update a recommendation identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json string id: The id of the recommendation to update.
   :<json string content: The name of the new recommendation.
   :<json string description: The description of the new recommendation.
   :<json string guide: The filename of the recommendation guide.
   
   :>json int status: Status code.

   :status 200: Recommendation successfully updated.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to update recommendation.

**Example Request**

.. sourcecode:: json

   {
      "id":4,
      "content":"New Recommendation updated",
      "description":"New recommendation description updated",
      "guide":"recommendation_updated_guide.md"
   }

.. important::

   In order to upload a new guide you need to use this service in conjunction with the service detailed in :ref:`/api/file/(string:filename)<upload>`.


**Example Response**

.. sourcecode:: json

   {"/api/recommendation":{"status":200}}



Remove Recommendation
------------------------------

.. http:delete:: /api/recommendations/(int:id)
   :noindex:

   :synopsis: Remove a recommendation identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :formparameter id: The id of the recommendation to remove.
 
   :>json int status: Status code.

   :status 200: Recommendation successfully removed.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to remove recommendation.

**Example Response**

.. sourcecode:: json

   {"/api/recommendation":{"status":200}}

.. raw:: html

   <hr/>

.. http:delete:: /api/recommendations/module/(int:id)
   :noindex:

   :synopsis: Removes the mapping between a module identified by ``id`` and its recommendations.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :formparameter id: The id of the module.
 
   :>json int status: Status code.

   :status 200: Mapping successfully removed.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to remove mapping.

**Example Response**

.. sourcecode:: json

   {"/api/recommendations/modules/1":{"status":200}}

.. raw:: html

   <hr/>

.. http:delete:: /api/recommendations/(int:id)/module/(int:id)
   :noindex:

   :synopsis: Removes the mapping between a module ``id`` and a recommendation ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :formparameter id: The id of the recommendation or module.
 
   :>json int status: Status code.

   :status 200: Mapping successfully removed.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to remove mapping.

**Example Response**

.. sourcecode:: json

   {"/api/recommendations/1/modules/1":{"status":200}}