Upload File
------------------------------

.. _upload:

.. http:post:: /api/file/(string:filename)
   :noindex:

   :synopsis: Uploads a file to the predefined ``UPLOAD_DIRECTORY``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: multipart/form-data
   :param filename: The name of the file. 
   :formparameter file: The file to be uploaded.
   :>json int status: status code.
   :status 201: The file was successfully uploaded.
   :status 400: Fail to upload file.

**Example Response**

.. sourcecode:: json

   {
      "/api/file/example.md":{
         "status":201
      }
   }


Request File
------------------------------

.. http:get:: /api/file/(string:filename)
   :noindex:

   :synopsis: Returns a file from the predefined ``UPLOAD_DIRECTORY``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param filename: The name of the file. 
   :status 201: The file was successfully uploaded.
   :status 400: Fail to upload file.


Get Files
------------------------------

.. http:get:: /api/file/(string:filename)
   :noindex:

   :synopsis: Returns the list of files available on the predefined ``UPLOAD_DIRECTORY``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param filename: The name of the file. 
   :status 200: The list of files was successfully retrieved.

**Example Response**

.. sourcecode:: json

   ["example.md","example_2.md"]


Get Session Files
------------------------------

.. http:get:: /api/file/module/(string:shortname)/session/(int:id)
   :noindex:

   :synopsis: Returns a zip containing all recommendations for a specific session ``id`` and module identified by ``shortname``.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :param shortname: The short name of the module.
   :param id: The id of the session.
   :status 200: The zip file was successfully created.
