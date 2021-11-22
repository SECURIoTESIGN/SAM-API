Get Questions
------------------------------

.. http:get:: /api/questions
   :noindex:

   :synopsis: Get all questions.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :>json int id: Id of the current question.
   :>json string content: The question.
   :>json string description: Question description.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: status code.
   
   :status 200: Questions successfully retrieved.
   :status 500: Fail to retrieve questions.

**Example Response**

.. sourcecode:: json

   {
      "/api/questions":{
         "content":[
            {
               "id":3,
               "content":"What is the name of ... ?",
               "description":"Test question description",
               "modules":[],
               "createdon":"Sun, 20 Sep 2020 09:00:00 GMT",
               "updatedon":"Sun, 20 Sep 2020 09:00:00 GMT"
            }
         ],
         "status":200
      }
   }


.. raw:: html

   <hr/>

.. http:get:: /api/question/(int:id)
   :noindex:

   :synopsis: Get a question identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :param int id: id of the question.
   
   :>json int id: Id of the question.
   :>json string content: The question.
   :>json int status: Status code.

   :status 200: Question successfully retrieved.
   :status 500: Fail to retrieve question.

**Example Response**

.. sourcecode:: json

   {
      "/api/question/1":{
         "content":[
            {
               "id":1,
               "content":"What is the domain of your IoT system ?"
            }
         ],
         "status":200
      }
   }


Get Questions Answers
------------------------------

.. http:get:: /api/questions/answers
   :noindex:

   :synopsis: Get the list of answers mapped to questions
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :>json int question_id: The id of the question.
   :>json string question_content: The question content. 
   :>json int answer_id: The id of que answer mapped to that question.
   :>json string answer_content: The answer content. 
   :>json question_answer_id: The relation id between question and answer. 
   :>json int status: Status code.

   :status 200: Questions answers successfully retrieved.
   :status 500: Fail to retrieve questions answers.

**Example Response**

.. sourcecode:: json

   {
      "/api/questions/answers":{
         "content":[
            {
               "question_id":1
               "question_content":"What is the domain of your IoT system ?",
               "answer_id":1,
               "answer_content":"Smart home",
               "question_answer_id":1,
            },
            {
               "question_id":1
               "question_content":"What is the domain of your IoT system ?",
               "answer_id":2,
               "answer_content":"Smart Healthcare",
               "question_answer_id":2,
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/question/(int:id)/answers
   :noindex:

   :synopsis: Get the list of answers mapped to question identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :param int id: id of the question.
   
   :>json int question_id: The id of the question.
   :>json string question_content: The question content. 
   :>json int answer_id: The id of que answer mapped to that question.
   :>json string answer_content: The answer content. 
   :>json question_answer_id: The relation id between question and answer. 
   :>json int status: Status code.

   :status 200: Question answers successfully retrieved.
   :status 500: Fail to retrieve question answers.

**Example Response**

.. sourcecode:: json

   {
      "/api/question/1/answers":{
         "content":[
            {
               "question_id":1,
               "question_content":"What is the domain of your IoT system ?",
               "answer_id":1,
               "answer_content":"Smart home",
               "question_answer_id":1
            },
            {
               "question_id":1,
               "question_content":"What is the domain of your IoT system ?",
               "answer_id":2,
               "answer_content":"Smart Healthcare",
               "question_answer_id":2
            }
         ],
         "status":200
      }
   }



Add Question
------------------------------

.. http:post:: /api/question
   :noindex:

   :synopsis: Add a new question.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json string content: The question content.
   :<json string description: The question description.

   :>json int id: The id of the new question.
   :>json string status: Status code.

   :status 200: Question successfully added.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to add question.

**Example Request**

.. sourcecode:: json

   {
      "content":"Test Question",
      "description":"Test question description",
   }

**Example Response**

.. sourcecode:: json

   {"/api/question":{"id":1, "status":200}}


Edit Question
------------------------------

.. http:put:: /api/question
   :noindex:

   :synopsis: Update a question identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json int id: The id of the question to update.
   :<json string content: The question content.
   :<json string description: The question description.

   :>json string status: Status code.

   :status 200: Question successfully updated.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to update question.

**Example Request**

.. sourcecode:: json

   {
      "id": 1,
      "content":"Test Question Updated",
      "description":"Test question description updated",
   }

**Example Response**

.. sourcecode:: json

   {"/api/question":{"status":200}}



Remove Question
------------------------------

.. http:delete:: /api/question/(int:id)
   :noindex:

   :synopsis: Removes a question identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :param int id: Id of the question to remove.
   :>json string status: Status code.

   :status 200: Question successfully removed.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to remove question.

**Example Response**

.. sourcecode:: json

   {"/api/question":{"status":200}}