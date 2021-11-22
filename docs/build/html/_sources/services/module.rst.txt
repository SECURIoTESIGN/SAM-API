Get Modules
------------------------------

.. http:get:: /api/module
   :noindex:

   :synopsis: Get the list of modules installed in the platform.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int id: Id of the module.
   :>json int type_id: Module type id.
   :>json string shortname: Unique short name or abbreviation.
   :>json string description: Module description.
   :>json string fullname: Full name of the module.
   :>json string displayname: Module display name that can be used by a frontend.
   :>json string avatar: Avatar of the user (i.e., location in disk).
   :>json string logic_filename: Filename of the file containing the dynamic logic of the module.
   :>json boolean plugin: A flag that sets if the current module is a plugin. 
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time. 
   :>json int status: status code.
   :status 200: Module successfully retrieved.
   :status 500: Fail to retrieve module.

**Example Response**

.. sourcecode:: json

   {
      "/api/modules":{
         "content":[
            {
               "id":1,
               "type_id":null,
               "shortname":"SRE",
               "fullname":"Security Requirements Elicitation",
               "description":null,
               "displayname":"Security Requirements",
               "avatar":null,
               "logic_filename":null,
               "plugin":false,
               "createdon":"Tue, 28 Sep 2021 13:42:48 GMT",
               "updatedon":"Tue, 28 Sep 2021 13:48:19 GMT"
            }
         ],
         "status":200
      }
   }


.. raw:: html

   <hr/>

.. http:get:: /api/module/(int:id)
   :noindex:

   :synopsis: Get a module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :param id: Id of the module.
   :>json int id: Id of the module.
   :>json int type_id: Module type id.
   :>json array dependencies: An array that contains the set of modules that the current module depends on.
   :>json string shortname: Unique short name or abbreviation.
   :>json string displayname: Module display name that can be used by a frontend.
   :>json string fullname: Full name of the module.
   :>json string description: Module description.
   :>json string logic_filename: Filename of the file containing the dynamic logic of the module.
   :>json string avatar: Avatar of the user (i.e., location in disk).
   :>json array recommendations: Set of recommendations mapped to this module. 
   :>json array tree: An array that contains the set of questions and answers mapped for the current module.
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time. 
   :>json int status: Status code.
   :status 200: Module successfully retrieved.
   :status 500: Fail to retrieve module.

**Example Response**

.. sourcecode:: json

   {
      "/api/module/1":{
         "content":[
            {
               "id":1,
               "type_id":null,
               "dependencies":[],
               "shortname":"SRE",
               "displayname":"Security Requirements",
               "fullname":"Security Requirements Elicitation",
               "description":null,
               "logic_filename":null,
               "avatar":null,
               "recommendations":[
                  {
                     "id":1,
                     "content":"Confidentiality",
                     "questions_answers":[
                        {
                           "id":1,
                           "answer_id":1,
                           "question_id":1,
                           "createdon":"Fri, 19 Nov 2021 12:54:49 GMT",
                           "updatedon":"Fri, 19 Nov 2021 12:54:49 GMT"
                        }
                     ],
                     "createdon":"Fri, 19 Nov 2021 12:54:49 GMT",
                     "updatedon":"Fri, 19 Nov 2021 12:54:49 GMT"
                  }
               ],
               "tree":[
                  {
                     "id":1,
                     "order":0,
                     "name":"What is the domain of your IoT system ?",
                     "multipleAnswers":0,
                     "type":"question",
                     "children":[
                        {
                           "id":1,
                           "name":"Smart home",
                           "type":"answer",
                           "children":[],
                        },
                        {
                           "id":2,
                           "name":"Smart Healthcare",
                           "type":"answer",
                           "children":[]
                        }
                     ],
                  }
               ],
               "createdon":"Fri, 19 Nov 2021 12:54:49 GMT",
               "updatedon":"Fri, 19 Nov 2021 12:54:49 GMT"
            }
         ],
         "status":200
      }
   }


Get Module Type
------------------------------

.. http:get:: /api/module/(int:id)/type
   :noindex:

   :synopsis: Get the type of module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param id: Id of the module.
   :>json boolean status: A flag that sets if the current module is a plugin, true if the correct module is a plugin, false otherwise. 
   :status 200: Module type successfully retrieved.
   :status 500: Fail to retrieve module type information.

.. note::
  
  A module plugin comprises questions and answers, while a module that is not a plugin fully depends on other modules to produce output.

**Example Response**

.. sourcecode:: json

   {
      "/api/module/1/type":{
         "status":false
      }
   }


Get Questions/Answers of a Module
----------------------------------

.. http:get:: /api/module/(int:id)/tree
   :noindex:

   :synopsis: Get the ``tree`` array of questions and answers of a module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :param id: Id of the module.
   :>json int id: Id of the current question or answer in the array depending of the ``type``.
   :>json int order: The sequencial number of the question.
   :>json array children: The current module has a set of questions or answers that are mapped to this array. 
   :>json string name: The content/text of the current question.
   :>json string type: Defines if the current element in the tree array is a ``question`` or an ``answer``.
   :>json boolean multipleAnswers: Defines if the user can select multiple answers for the current question.
   :>json int status: status code.
   :status 200: Module tree successfully retrieved.
   :status 500: Fail to retrieve tree of the module.

.. note::
  
   Please, consider using something like, for example, the `react-sortable-tree <https://github.com/frontend-collective/react-sortable-tree/>`_ react component to develop a proper user interface to interact and manage the data returned by this service.
   
**Example Response**

.. sourcecode:: json

   {
      "/api/module/1/tree":{
         "tree":[
            {
               "id":1,
               "order":0,
               "name":"What is the domain of your IoT system ?",
               "multipleAnswers":0,
               "type":"question"
               "children":[
                  {
                     "id":1,
                     "name":"Smart home",
                     "type":"answer",
                     "children":[]
                  },
                  {
                     "id":2,
                     "name":"Smart Healthcare",
                     "type":"answer",
                     "children":[]
                  }
               ],
            }
         ],
         "status":200
      }
   }


Get Questions of Modules
----------------------------------

.. http:get:: /api/module/questions
   :noindex:

   :synopsis: Get the list of questions mapped to each module.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int id: Module or question id.
   :>json array questions: Array of questions.
   :>json int status: status code.
   :status 200: Module's questions successfully retrieved.
   :status 500: Fail to retrieve module's questions.

**Example Response**

.. sourcecode:: json

   {
      "/api/modules/questions": {
         "content": [
            {
            "id": 1,
            "questions": [
               {
                  "id": 1,
                  "content": "What is the domain of your IoT system ?",
                  "createdon": "Fri, 19 Nov 2021 15:29:18 GMT",
                  "updatedon": "Fri, 19 Nov 2021 15:29:18 GMT"
               }
            ]
            }
         ],
         "status": 200
      }
   }

.. raw:: html

   <hr/>

.. http:get:: /api/module/(int:id)/questions
   :noindex:

   :synopsis: Get the list of questions mapped to a module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :param id: Id of the module.
   :>json int id: Module or question id.
   :>json array questions: Array of questions.
   :>json int status: status code.
   :status 200: Module's questions successfully retrieved.
   :status 500: Fail to retrieve module's questions.

**Example Response**

.. sourcecode:: json

   {
      "/api/modules/questions": {
         "content": [
            {
            "id": 1,
            "questions": [
               {
                  "id": 1,
                  "content": "What is the domain of your IoT system ?",
                  "createdon": "Fri, 19 Nov 2021 15:29:18 GMT",
                  "updatedon": "Fri, 19 Nov 2021 15:29:18 GMT"
               }
            ]
            }
         ],
         "status": 200
      }
   }


Get Modules Answers
----------------------------------

.. http:get:: /api/module/answers
   :noindex:

   :synopsis: Get the list of answers mapped to each module.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :>json int id: Module or answer id.
   :>json array answers: Array of answers.
   :>json int status: status code.
   :status 200: Module's answers successfully retrieved.
   :status 500: Fail to retrieve module's answers.

**Example Response**

.. sourcecode:: json

   {
      "/api/modules/answers":{
         "content":[
            {
               "id":1
               "answers":[
                  {
                     "id":1,
                     "content":"Smart home",
                     "createdon":"Fri, 19 Nov 2021 15:29:18 GMT",
                     "updatedon":"Fri, 19 Nov 2021 15:29:18 GMT"
                  },
                  {
                     "id":2,
                     "content":"Smart Healthcare",
                     "createdon":"Fri, 19 Nov 2021 15:29:18 GMT",
                     "updatedon":"Fri, 19 Nov 2021 15:29:18 GMT"
                  }
               ]
            }
         ],
         "status":200
      }
   }


.. raw:: html

   <hr/>

.. http:get:: /api/module/(int:id)/answers
   :noindex:

   :synopsis: Get the list of answers mapped to a module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :param id: Id of the module.
   :>json int id: Module or answer id.
   :>json array answers: Array of answers.
   :>json int status: status code.
   :status 200: Module's answers successfully retrieved.
   :status 500: Fail to retrieve module's answers.

**Example Response**

.. sourcecode:: json

   {
      "/api/modules/answers":{
         "content":[
            {
               "id":1
               "answers":[
                  {
                     "id":1,
                     "content":"Smart home",
                     "createdon":"Fri, 19 Nov 2021 15:29:18 GMT",
                     "updatedon":"Fri, 19 Nov 2021 15:29:18 GMT"
                  },
                  {
                     "id":2,
                     "content":"Smart Healthcare",
                     "createdon":"Fri, 19 Nov 2021 15:29:18 GMT",
                     "updatedon":"Fri, 19 Nov 2021 15:29:18 GMT"
                  }
               ]
            }
         ],
         "status":200
      }
   }


Add Module
------------------------------

.. _addmodule:

.. http:post:: /api/module
   :noindex:

   :synopsis: Add a new module. 
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :<json string shortname: Unique short name or abbreviation of the module.
   :<json string fullname: Full name of the module.
   :<json string displayname: Module display name that can be used by a frontend.
   :<json string description: Module description.
   :<json array tree: Array of questions and answers mapped to the module.
   :<json array recommendations: Array of recommendations mapped to a question ``id`` and answer ``id``.
   :<json array dependencies: An array that contains the set of modules that the current module depends on.

   :status 200: Module successfully added.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to add module.

.. important::

   The ``client_id`` field is a temporary id for a question or an answer that may not yet exist in the database -- This temporary id is assigned by a client. An identical situation exists for ``client_question_id`` and ``client_answer_id``: 

.. note::

   Each question can trigger a set of answers or questions (``tree`` field).

.. note::

   Each module can only be triggered if a module dependency was satisfied (i.e., the module described in the field ``dependencies`` was previously executed by the user).

**Example Request**

.. sourcecode:: json

   {
      "shortname":"SRE",
      "fullname":"Security Requirements Elicitation",
      "displayname":"Security Requirements",
      "description":"Module description",
      "tree":[
         {
            "id":null,
            "client_id":0,
            "type":"question",
            "name":"What is the domain of your IoT system ?",
            "multipleAnswers":false,
            "children":[
               {
                  "id":null,
                  "client_id":1,
                  "name":"Smart home",
                  "type":"answer",
                  "multipleAnswers":false,
                  "children":[
                     {
                        "id":null,
                        "client_id":2,
                        "name":"Will the sytem have a user LogIn ?",
                        "type":"question",
                        "children":[
                           {
                              "id":null,
                              "client_id":3,
                              "name":"Yes",
                              "type":"answer",
                              "children":[
                                 
                              ]
                           },
                           {
                              "id":null,
                              "client_id":4,
                              "name":"No",
                              "type":"answer",
                              "children":[
                                 
                              ]
                           }
                        ]
                     }
                  ]
               },
               {
                  "id":null,
                  "client_id":5,
                  "name":"Smart Healthcare",
                  "type":"answer",
                  "multipleAnswers":false,
                  "children":[
                     {
                        "id":null,
                        "client_id":6,
                        "name":"Yes",
                        "type":"answer",
                        "children":[
                           
                        ]
                     },
                     {
                        "id":null,
                        "client_id":7,
                        "name":"No",
                        "type":"answer",
                        "children":[
                           
                        ]
                     }
                  ]
               }
            ]
         }
      ],
      "recommendations":[
         {
            "id":null,
            "content":"Confidentiality",
            "questions_answers":[
               {
                  "client_question_id":0,
                  "client_answer_id":1
               }
            ]
         }
      ],
      "dependencies":[
         {
            "module":{
               "id":2
            }
         }
      ]
   }



Edit Module
------------------------------

.. http:put:: /api/module
   :noindex:

   :synopsis: Edit a module.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json

   :<json int id: Id of the module to edit.
   :<json string shortname: Unique short name or abbreviation of the module.
   :<json string fullname: Full name of the module.
   :<json string displayname: Module display name that can be used by a frontend.
   :>json int status: Status code
   :status 200: Module successfully updated.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to update module.

**Example Request**

.. sourcecode:: json

   {
      "id":1,
      "shortname":"SREU",
      "fullname":"Security Requirements Elicitation Updated",
      "displayname":"Security Requirements Updated"
   }

.. note::

   Questions, answers, recommendations and dependencies of the module can also be updated using this service by following the same JSON object provide as example in the ``/api/module`` (add module) service.


**Example Response**

.. sourcecode:: json

   {"/api/module":{"status":200}}



Remove Module
------------------------------

.. http:delete:: /api/module/(int:id)
   :noindex:

   :synopsis: Performs a partial delete of a Module. That is, only the module and those sessions linked are deleted - Linked questions and associated answers are not delete.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the module to partially delete.
   :status 200: Module successfully removed.
   :status 500: Fail to remove module.

.. http:delete:: /api/module/(int:id)/full
   :noindex:

   :synopsis: Fully removes a module (including sessions, linked questions, and answers).
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the module to fully delete.
   :status 200: Module successfully removed.
   :status 500: Fail to remove module.

.. http:delete:: /api/module/(int:id)/questions
   :noindex:

   :synopsis: Removes all questions mapped to the module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the module.
   :status 200: Module questions successfully removed.
   :status 500: Fail to remove module questions.


.. http:delete:: /api/module/(int:id)/answers
   :noindex:

   :synopsis: Removes all answers mapped to the module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the module.
   :status 200: Module answers successfully removed.
   :status 500: Fail to remove module answers.


.. http:delete:: /api/module/(int:id)/logic
   :noindex:

   :synopsis: Removes the logic file mapped to the module identified by ``id``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param int id: Id of the module.
   :status 200: Module answers successfully removed.
   :status 500: Fail to remove module answers.