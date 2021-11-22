Get Answers
------------------------------

.. http:get:: /api/answers
   :noindex:

   :synopsis: Get the list of answers mapped to questions.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :>json int id: The id of the answer or question mapped to the current answer.
   :>json string content: The answer or question content. 
   :>json string description: Description of the answer.
   :>json array questions: Array of questions mapped to the current answer.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Answers successfully retrieved.
   :status 500: Fail to retrieve answers.

**Example Response**

.. sourcecode:: json

   {
      "/api/answers":{
         "content":[
            {
               "id":1,
               "content":"Smart home",
               "description":"Smart home description",
               "questions":[
                  {
                     "id":1,
                     "content":"What is the domain of your IoT system ?"
                  }
               ],
               "createdon":"Fri, 19 Nov 2021 15:29:18 GMT",
               "updatedon":"Fri, 19 Nov 2021 15:29:18 GMT"
            },
            {
               "id":2,
               "content":"Smart Healthcare",
               "description":"Smart healthcare description",
               "questions":[
                  {
                     "id":1,
                     "content":"What is the domain of your IoT system ?"
                  }
               ],
               "createdon":"Fri, 19 Nov 2021 15:29:18 GMT",
               "updatedon":"Fri, 19 Nov 2021 15:29:18 GMT"
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/answers/(int:id)
   :noindex:

   :synopsis: Get an answer identify by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :>json int id: The id of the answer. 
   :>json string content: The answer content.
   :>json string description: Description of the answer.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Answers successfully retrieved.
   :status 500: Fail to retrieve answers.

**Example Response**

.. sourcecode:: json

   {
      "/api/answer/1":{
         "content":[
            {
               "id":1,
               "content":"Smart home",
               "description":"Smart home description",
               "createdon":"Fri, 19 Nov 2021 15:29:18 GMT",
               "updatedon":"Fri, 19 Nov 2021 15:29:18 GMT"
            }
         ],
         "status":200
      }
   }

Add Answer
------------------------------

.. http:post:: /api/answer
   :noindex:

   :synopsis: Add a new answer.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json string content: The answer content.
   :<json string description: The answer description.

   :>json int id: The id of the new answer.
   :>json string status: Status code.

   :status 200: Answer successfully added.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to add answer.

**Example Request**

.. sourcecode:: json

   {
	   "content":"Test Answer",
	   "description":"Test answer description"
   }

**Example Response**

.. sourcecode:: json

   {"/api/answer":{"id":4, "status":200}}


Edit Answer
------------------------------

.. http:put:: /api/answer
   :noindex:

   :synopsis: Update an answer identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json int id: The id of the answer to update.
   :<json string content: The answer content.
   :<json string description: The answer description.

   :>json string status: Status code.

   :status 200: Answer successfully updated.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to update answer.

**Example Request**

.. sourcecode:: json

   {
      "id":1,
      "content":"Test Answer Updated",
      "description":"Test answer description updated"
   }

**Example Response**

.. sourcecode:: json

   {"/api/answer":{"status":200}}



Remove Answer
------------------------------

.. http:delete:: /api/answer/(int:id)
   :noindex:

   :synopsis: Removes a answer identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :param int id: Id of the answer to remove.
   :>json string status: Status code.

   :status 200: Answer successfully removed.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to answer question.

**Example Response**

.. sourcecode:: json

   {"/api/answer":{"status":200}}