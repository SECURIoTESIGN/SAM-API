.. SAM-APIs documentation master file, created by
   sphinx-quickstart on Sat May 15 11:07:08 2021.

Welcome to SAM API's Documentation
======================================

.. toctree::
   :caption: Contents:

.. image:: images/sam_logo.png
  :alt: SAM

Welcome to SAM API's documentation. This document is aimed at developers and it is highly recommended to start with the :ref:`Installation<install>` section  
and then go forward with the API sections. The main purpose of this documentation is to provide insights into how one should use 
SAM's core API services in the development of a frontend (e.g., the default one provided at `https://github.com/SECURIoTESIGN/SAM <https://github.com/SECURIoTESIGN/SAM>`_).

Project Overview
======================================

Security Advising Modules (SAM) is a framework that aggregates and connects all the various modules developed under the scope of the `SECURIoTESIGN <https://lx.it.pt/securIoTesign>`_
project while providing a graphical interface to interact with them. SAM is modular, allowing for both quick integrations of newly developed modules and updates 
to existing modules. SAM works as a personal security assistant, more relatable, and capable of communicating with the end-user through a series of easily 
understandable questions, which the user can answer directly or through a set of predefined answers.


Installation
======================================

.. _install:

The installation, **for development proposes only**, can be accomplished through a group of `Docker <https://www.docker.com/>`_ containers.

1. **Clone the public repository.**

2. **Create the API and database docker imagens and subsequent containers:**

.. code-block:: bash

   cd sam-api
   make

.. note::

   The database and API container will be deployed with API port set to 8080 and database port set to 3306. 
   The database user will be ``root`` and the password ``secure``.

3. **Deploy the database into the database container:**

.. code-block:: bash
   
   sudo docker exec -it sam-db python3 install_db.py

You can access the database using DBeaver or similar (use ``sudo docker inspect sam-db`` to get the IP of the sam-db container).

4. **Develop away!**

You can start both containers as follows: 

.. code-block:: bash
   
   sudo docker stop sam-api && sudo docker start sam-api
 
SAM's REST services can be tested and accessed through `insomnia <https://insomnia.rest/download>`_ -- The Insomnia JSON file of this project can be found on the following `link <https://github.com/SECURIoTESIGN/SAM-API/blob/master/docs/insomnia/Insomnia-SAM-API-Services.json>`_.

.. important:: 
   
   The contents of folder ``sam-api`` are mapped to the sam-api container, any local changes will be reflected. 

Core and Community Modules/Plugins
======================================

Several module and plugins have been developed by the SECURIoTESIGN team and the community. Namely:

* **Security Requirements Elicitation (SRE)** - This module will elicit the main security requirements and properties, e.g., confidentiality, integrity, authentication, access control, availability or accountability that the system should implement from the basic information of what composes it and defines it (e.g., type of system, methods of authentication, types of users, sensitive information storage).
* **Security Best Best Practices (SBPG)** - This module will provide best practices guildelines that will highlight common potential vulnerabilities that need to be taken into account during development, and provide information on secure practices that should be implemented.
* **Lightweight Criptographic Algorithms Recommendation (LWCAR)** - This module will take the information on the system hardware requirements and defined security requirements. It also proposes algorithms that can be implemented to ensure the security requirements are fulfilled. It specifically recommends lightweight cryptographic algorithms, for both software and hardware implementations.
* **Threat Modeling Solution (TMS)** - This modules provides a set of threats that based on the answers given by a user.
* **Assessment of the Correct Integration of Security Mechanisms (ACISM)** - This module outputs system tests to check for the presence of threats.

These modules can be found at `https://github.com/SECURIoTESIGN/SAM-Modules <https://github.com/SECURIoTESIGN/SAM-Modules>`_.

.. important::
   
   A module is defined as a component that incorporates questions and answers and an output designated as recommendations, while a plugin is a special module similar to 
   the latter but it only provides the output (i.e., recommendations) -- These plugins are dependent on the input of other modules.
   
Installing Core Modules 
------------------------

To install core modules into SAM:

.. code-block:: bash

   cd sam-api
   make modules

.. important:: 
   
   *Beware*, this process will recreate SAM's database - All data will be lost!


Developing Modules 
--------------------

The development of modules can be accomplished by using the services detailed in section :ref:`Modules Services API<modules>`.  If there is a need to develop modules with some logic -- 
that is, without being dependent on the mapping between question, answer, and recommendation provided by core services -- an example is available on the following `link <https://github.com/SECURIoTESIGN/SAM-API/blob/master/docs/example_module_logic.py>`_.

.. note::

   If a logic file is developed for a module those services detailed in section :ref:`Add module<addmodule>` should be used in conjuntion with the file API detailed in :ref:`Upload File<upload>`.

Statistics Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the statistic entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>statistic.py</i></a>.</summary>

.. literalinclude:: ../views/statistic.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/statistic.rst

Authentication Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the authentication entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>user.py</i></a>.</summary>

.. literalinclude:: ../views/user.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/auth.rst

User Services API
==================================
.. raw:: html

   This section includes details concerning services developed for the group entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>user.py</i></a>.</summary>

.. literalinclude:: ../views/user.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/user.rst

Group Services API
==================================
.. raw:: html

   This section includes details concerning services developed for the group entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>group.py</i></a></summary>

.. literalinclude:: ../views/group.py
   :language: python
   :linenos:

.. raw:: html

   </details>


.. include:: services/group.rst

File Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the file entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>file.py</i></a>.</summary>

.. literalinclude:: ../views/file.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/file.rst

Types Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the type entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>type.py</i></a>.</summary>

.. literalinclude:: ../views/type.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/type.rst


Module Services API
==========================================

.. _modules:

.. raw:: html

   This section includes details concerning services developed for the module entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>module.py</i></a>.</summary>

.. literalinclude:: ../views/module.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/module.rst


Dependencies Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the dependency entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>dependency.py</i></a>.</summary>

.. literalinclude:: ../views/dependency.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/dependency.rst

Questions Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the question entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>question.py</i></a>.</summary>

.. literalinclude:: ../views/question.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/question.rst

Answers Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the answer entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>answer.py</i></a>.</summary>

.. literalinclude:: ../views/answer.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/answer.rst

Recommendations Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the recommendation entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>recommendation.py</i></a>.</summary>

.. literalinclude:: ../views/recommendation.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/recommendation.rst


Sessions Services API
==========================================
.. raw:: html

   This section includes details concerning services developed for the session entity implemented in <details style="display:inline;margin-bottom:15px">
   <summary style="list-style: none"><a><i>session.py</i></a>.</summary>

.. literalinclude:: ../views/session.py
   :language: python
   :linenos:

.. raw:: html

   </details>

.. include:: services/session.rst


Acknowledgment
==========================================

This work was performed under the scope of Project SECURIoTESIGN with funding from FCT/COMPETE/FEDER with reference number POCI-01-0145-FEDER-030657. This work is funded by Portuguese FCT/MCTES through national funds and, when applicable, co-funded by EU funds under the project UIDB/50008/2020, research grants BIL/Nº11/2019-B00701, BIL/Nº12/2019-B00702, and FCT research and doctoral grant SFRH/BD/133838/2017 and BIM/n°32/2018-B00582, respectively, and also supported by project CENTRO-01-0145-FEDER-000019 - C4 - Competence Center in Cloud Computing, Research Line 1: Cloud Systems, Work package WP 1.2 - Systems design and development processes and software for Cloud and Internet of Things ecosystems, cofinanced by the European Regional Development Fund (ERDF) through the Programa Operacional Regional do Centro (Centro 2020), in the scope of the Sistema de Apoio à Investigação Científica e Tecnológica - Programas Integrados de IC&DT.

License
==========================================

Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS
