[Name of the Service]
------------------------------

.. http:get:: /api/group/(int:id)
   :noindex:

   :synopsis: Synopsis of the service.
   :reqheader Authorization: Bearer token provided by :ref:`/api/user/login<authenticate>`.
   :resheader Content-Type: application/json
   :resheader Content-Type: multipart/form-data
   :formparameter email: The email of the user to be authenticated.

   :param int id: id of the element.
   :<json int id: The id of the group you want to update.
   
   :>json datetime createdon: Creation date and time.
   :>json datetime updatedon: Update date and time.
   :>json int status: Status code.

   :status 200: X successfully updated.
   :status 400: The server was unable to process the request (e.g., malformed request syntax).
   :status 500: Fail to update X.

**Example Request**

.. sourcecode:: json

	{"id":3,"designation":"New Group Updated"}

**Example Response**

.. sourcecode:: json

   {"/api/group":{"status":200}}

.. raw:: html

   <hr/>
