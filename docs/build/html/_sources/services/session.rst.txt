Get User Sessions
------------------------------

.. http:get:: /api/sessions
   :noindex:

   :synopsis: Get user sessions.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int id: Id of the session.
   :>json int module_id: Id of the module executed on that session.
   :>json int user_id: The session belongs to this user.
   :>json boolean ended: Flag that indicates that a session was terminated by the user. 

   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Sessions successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve sessions.

**Example Response**

.. sourcecode:: json

   {
      "/api/sessions":{
         "content":[
            {
               "id":1,
               "module_id":1,
               "user_id":2,
               "ended":0,
               "updatedOn":"Sat, 20 Nov 2021 10:31:41 GMT",
               "createdOn":"Sat, 20 Nov 2021 10:31:41 GMT"
            }
         ],
         "status":200
      }
   }

.. note::

   The ``end`` flag should be set to true when all the questions of a module were answered by a user.  

.. raw:: html

   <hr/>

.. http:get:: /api/session/(int:id)
   :noindex:

   :synopsis: Get user session identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: id of the session.

   :>json int id: Id of the session.
   :>json int module_id: Id of the module executed on that session.
   :>json int user_id: The session belongs to this user.
   :>json boolean ended: Flag that indicates that a session was terminated by the user. 

   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Sessions successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve sessions.

**Example Response**

.. sourcecode:: json

   {
      "/api/sessions":{
         "content":[
            {
               "id":1,
               "module_id":1,
               "user_id":2,
               "ended":0,
               "updatedOn":"Sat, 20 Nov 2021 10:31:41 GMT",
               "createdOn":"Sat, 20 Nov 2021 10:31:41 GMT"
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/session/user/(string:email)
   :noindex:

   :synopsis: Get sessions of a user identified by ``email``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param string email: Email of the user.

   :>json int id: Id of the session or module.
   :>json string user_email: The email of the user.
   :>json boolean ended: Flag that indicates that a session was terminated by the user. 
   :>json int type_id: Module type id.
   :>json string shortname: Unique short name or abbreviation.
   :>json string fullname: Full name of the module.
   :>json string displayname: Module display name that can be used by a frontend.
   :>json array dependencies: An array that contains the set of modules that the current module depends on.
   :>json string description: Module description.
   :>json string avatar: Avatar of the user (i.e., location in disk).
   :>json string logic_filename: Filename of the file containing the dynamic logic of the module.
   :>json boolean plugin: A flag that sets if the current module is a plugin. 
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Sessions successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve sessions.

**Example Response**

.. sourcecode:: json

   {
      "/api/sessions/user/forrest@sam.pt":{
         "content":[
            {
               
               "id":1,
               "user_email":"forrest@sam.pt",
               "user_id":2,
               "ended":0,
               "module":{
                  "id":1,
                  "shortname":"SRE",
                  "fullname":"Security Requirements Elicitation",
                  "displayname":"Security Requirements",
                  "description":null,
                  "dependencies":[],
                  "logic_filename":null,
                  "type_id":null,
                  "avatar":null,
                  "createdon":"Fri, 19 Nov 2021 15:29:18 GMT",
                  "updatedon":"Fri, 19 Nov 2021 15:29:18 GMT"
               },
               "createdOn":"Sat, 20 Nov 2021 10:31:41 GMT",
               "updatedOn":"Sat, 20 Nov 2021 10:31:41 GMT"
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/session/closed
   :noindex:

   :synopsis: Get user sessions that were set as closed or terminated.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int id: Id of the session, question, answer, or recommendation.
   :>json int module_id: Id of the module executed on that session.
   :>json int user_id: The session belongs to this user.
   :>json boolean ended: Flag that indicates that a session was terminated by the user. 

   :>json string content: The content of question, answer, or recommendation.
   :>json array answer: Selected answers for the current question and session.
   :>json string recommendation_guide: The filename of the recommendation guide.
   
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Sessions successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve sessions.

**Example Response**

.. sourcecode:: json

   {
      "/api/sessions/closed":{
         "content":[
            {
               "id":1,
               "user_id":2,
               "module_id":1,
               "ended":1,
               "questions":[
                  {
                     "id":1,
                     "content":"What is the domain of your IoT system ?",
                     "answer":[{"id":1,"content":"Smart home"}],
                  }
               ],
               "recommendations":[
                  {
                     "id":1,
                     "content":"Confidentiality",
                     "description":null,
                     "recommendation_guide":null
                  }
               ],
               "createdOn":"Sat, 20 Nov 2021 10:31:41 GMT",
               "updatedOn":"Sat, 20 Nov 2021 11:31:29 GMT"
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/session/(int:id)/closed
   :noindex:

   :synopsis: Get user sessions identified by ``id`` that were flagged as closed.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the session.
   
   :>json int id: Id of the session, question, answer, or recommendation.
   :>json int module_id: Id of the module executed on that session.
   :>json int user_id: The session belongs to this user.
   :>json boolean ended: Flag that indicates that a session was terminated by the user. 

   :>json string content: The content of question, answer, or recommendation.
   :>json array answer: Selected answers for the current question and session.
   :>json string recommendation_guide: The filename of the recommendation guide.
   
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Sessions successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve sessions.

**Example Response**

.. sourcecode:: json

   {
      "/api/sessions/closed":{
         "content":[
            {
               "id":1,
               "user_id":2,
               "module_id":1,
               "ended":1,
               "questions":[
                  {
                     "id":1,
                     "content":"What is the domain of your IoT system ?",
                     "answer":[{"id":1,"content":"Smart home"}],
                  }
               ],
               "recommendations":[
                  {
                     "id":1,
                     "content":"Confidentiality",
                     "description":null,
                     "recommendation_guide":null
                  }
               ],
               "createdOn":"Sat, 20 Nov 2021 10:31:41 GMT",
               "updatedOn":"Sat, 20 Nov 2021 11:31:29 GMT"
            }
         ],
         "status":200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/session/module/(int:id)/user/(int:id)
   :noindex:

   :synopsis: Get user sessions that were flagged as closed for a particular user ``id`` and module ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the module or user.
   
   :>json int id: Id of the session.
   :>json int user_id: The session belongs to this user.
   :>json string user_email: The email of the user.
   :>json int module_id: Id of the module executed on that session.
   :>json boolean ended: Flag that indicates that a session was terminated by the user.    
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Sessions successfully retrieved.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to retrieve sessions.

**Example Response**

.. sourcecode:: json

   {
      "/api/sessions/module/1/user/2":{
         "content":[
            {
               "id":1,
               "user_id":2
               "user_email":"forrest@sam.pt",
               "module_id":1,
               "ended":1,
               "createdOn":"Sat, 20 Nov 2021 10:31:41 GMT",
               "updatedOn":"Sat, 20 Nov 2021 11:31:29 GMT"
            }
         ],
         "status":200
      }
   }

Create User Session
------------------------------

.. http:post:: /api/session
   :noindex:

   :synopsis: Starts a new user session taking into account a user selected module identified by ``module_id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json int module_id: Id of the module that will be executed on that user session.
   :<json string email: Email of the user who started the session.

   :>json int id: Id of the new session.
   :>json string shortname: Unique short name or abbreviation of the module.
   :>json string fullname: Full name of the module.
   :>json string displayname: Module display name that can be used by a frontend.
   :>json string description: Module description.
   :>json array tree: Array of questions and answers mapped to the module.
   :>json array dependencies: An array that contains the set of modules that the current module depends on.
   :>json array recommendations: Array of recommendations that contains the mapping between question ``id`` and answer ``id``.
   :>json array tree: Array of questions and answers mapped to the module.
  
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: Session successfully created.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to create session.

**Example Request**

.. sourcecode:: json

	{"module_id":1,"email":"forrest@sam.pt"}

**Example Response**

.. sourcecode:: json

   {
      "/api/session":{
         "id":1,
         "module":[
            {
               "id":1,
               "shortname":"SRE",
               "displayname":"Security Requirements",
               "fullname":"Security Requirements Elicitation",
               "description":"Module description",
               "avatar":null,
               "logic_filename":null,
               "type_id":null,
               "dependencies":[],
               "recommendations":[
                  {
                     "id":1,
                     "content":"Confidentiality",
                     "questions_answers":[
                        {
                           "id":1,
                           "question_id":1,
                           "answer_id":1,
                           "createdon":"Sat, 20 Nov 2021 11:55:12 GMT",
                           "updatedon":"Sat, 20 Nov 2021 11:55:12 GMT"
                        }
                     ],
                     "createdon":"Sat, 20 Nov 2021 11:55:12 GMT",
                     "updatedon":"Sat, 20 Nov 2021 11:55:12 GMT"
                  }
               ],
               "tree":[
                  {
                     "id":1,
                     "order":0,
                     "name":"What is the domain of your IoT system ?",
                     "multipleAnswers":0,
                     "type":"question",
                     "expanded":false,
                     "children":[
                        {"id":1, "name":"Smart home", "type":"answer", "children":[]},
                        {"id":2, "name":"Smart Healthcare", "type":"answer", "children":[]}
                     ]
                  }
               ],
               "createdon":"Sat, 20 Nov 2021 11:55:12 GMT",
               "updatedon":"Sat, 20 Nov 2021 11:55:12 GMT"
            }
         ],
         "status":200
      }
   }


Edit User Session
------------------------------

.. http:put:: /api/session
   :noindex:

   :synopsis: Update a session. Specifically, by adding an answer to a question for the session module.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   
   :<json int question_id: Id of the module that will be executed on that user session.
   :<json int answer_id: Email of the user who started the session.
   :<json string input: (optional) User direct answer that was not choosen from a predefined set of answers.

   :>json int status: Status code.

   :status 200: Session successfully created.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to create session.

**Example Request**

.. sourcecode:: json

	{"question_id":1, "answer_id":1}

.. important::

   The ``input`` parameter should only be included in the request body if the question is not a multi-choice one where the user has to include a direct answer:

   .. sourcecode:: json

	   {"question_id":1, "input":"This is the user answer"}

**Example Response**

.. sourcecode:: json

   {"/api/session/1":{"status":200}}


Close User Session
------------------------------

.. http:put:: /api/session/{id}/end
   :noindex:

   :synopsis: Close or terminate a user session through the session ``id``. 
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the session.

   :>json int id: Id of the session that was closed.
   :>json array recommendations: An array that contains the recommendations based on the answers given by the user in the session.
   :>json int status: Status code.

   :status 200: Session successfully closed.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to close session.

.. note::

   This service will return the set of recommendations based on the answers given by the user in that session.

**Example Response**

.. sourcecode:: json

   {
      "/api/session/1/end":{
         "id":1,
         "recommendations":[
            {
               "id":1,
               "content":"Confidentiality",
               "description":null,
               "recommendation_guide":null
            }
         ],
         "status":200
      }
   }