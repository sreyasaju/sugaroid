.. _header-n2:

Sugaroid
========

|image0|

   **IMPORTANT** : Sugaroid is an open source software. The web server
   is deployed on Microsoft Azure. Your support for this open source
   software is highly necessary to make this project continued to be
   served on the world wide web. Consider being my patron to help
   Sugaroid host its servers or if you are willing to lend servers for
   Sugaroid, press the sponsor button and email me. Thanks. However,
   Sugaroid will always remain free forever 😄

.. _header-n191:

Acknowledgements 
----------------

**Sugaroid AI** has become possible to millions of open source
developers. Particularly to mention, I would like to thank
`@GuntherCox <https://github.com/gunthercox>`__ for the ``chatterbot``
library and
`@explosion <https://explosion.ai>`__\ **for**\ ```spaCy`` <https://github.com/explosion/spaCy>`__
, the machine learning library with which it was possible to make
natural language processing easy as pie. Also, the millions of word
collection on ``en_core_web_sm``, ``en_core_web_md`` was contributed by
developers across the globe for translation and linguistic
differentiation. I would also like to thank, Sugar Labs 2019 GCI Team,
**Sashreek Magan** (aka `@smag <https://github.com/smag>`__), **Andrea
Gonzales** (aka `@andreagon <https://github.com/AndreaGon>`__),
**Zakiyah Hasanah** (aka `@kiy4h <https://github.com/Kiy4h>`__),
**Rishikesh Joshi** (aka `@Creatune <https://github.com/Creatune>`__),
**Szymon** (aka `@sdziuda <https://github.com/sdziuda>`__) and **Marcus
Chong** (aka `@pidddgy <https://github.com/pidddgy>`__) for continuous
testing on servers and reporting bugs. It is only possible to rectify
bugs with the help of repeated testing. I would also like to thank
friends and family who also helped me to work on this project. Along
with this, I would like to extend gratitude to **Microsoft** for
sponsoring `Sugaroid’s hosting on
Azure <https://sugaroid.azurewebsites.net>`__.

<br>

.. _header-n236:

Table of Contents
-----------------

.. contents::
<br>

.. _header-n258:

Introduction
------------

Sugaroid is a new Artificial Intelligence which uses Natural Language
Processing (NLP) with Machine Learning and neural networks to manipulate
user input to provide a intuitive response. The AI is built on
``Python 3.8.2`` and was built out of personal interest, to tackle three
important issues in the Python framework

-  Natural Language Processing / Machine Learning

-  Graphical User Interface

-  Database Management, Configuration file management and Web
   Development

Sugaroid Chatbot has a comprehensive and modular interface utilizing
Object Oriented Programming to benefit activities of
`Sugarlabs <www.sugarlabs.org>`__, a non-profit educational
organization. Initially built to serve as a companion bot, the Sugaroid
Virtual Assistant helps to comprehend most of the messages, to generate
a probable response. The future plans of sugaroid aims to extend
Sugaroid as a documentation reader of which beta previews are
``still under testing``.

The Sugaroid bot is deployed in production servers particularly for
testing.

-  `The web interface <https://sed.lol/sugaroid>`__

-  The discord bot

-  IRC bot hosted on self when necessary

<br>

.. _header-n24:

Installation
------------

.. _header-n25:

Installing from PYPI
~~~~~~~~~~~~~~~~~~~~

The Sugaroid Chatbot is built on `wheels <https://pythonwheels.com/>`__
and is also published on the `Python Packaging Index
(PYPI) <pypi.org>`__. This was done, so as to provide easy access to the
bot without the end-user undergoing a lot of hassle

.. code:: shell

   pip3 install sugaroid

The Sugaroid Chatbot depends indirectly on ``ChatterBot`` by
@Gunthercox. However, it was quite important to create a fork of the
``ChatterBot`` repo due to the conflicting and outdated dependencies. It
is possible that, the installation and procedural working of sugaroid
will fail, provided you have previously installed ``ChatterBot`` or
``chatterbot-corpus``. As an alternative, a beta tracking branch of
``Chatterbot`` and ``Chatterbot-corpus`` have been released under the
alias ``sugaroid-chatterbot`` and ``sugaroid-chatterbot-corpus``. In any
such case , the following method of installation might be useful

.. code:: shell

   pip3 uninstall chatterbot chatterbot-corpus
   pip3 install -U sugaroid
   pip3 install -U sugaroid-chatterbot sugaroid-chatterbot-corpus

In addition, on Windows, it is possible that the absence of a valid
``Git`` executable can cause failure to start. These are very rare
cases. In that case, we have to install the latest git from git-scm.org

<br>

.. _header-n30:

Installation from Source
~~~~~~~~~~~~~~~~~~~~~~~~

Sugaroid chatbot can also be installed from the latest commits by

.. code:: 

   pip3 install https://github.com/srevinsaju/sugaroid/archive/master.zip

Alternatively

.. code:: shell

   git clone https://github.com/srevinsaju/sugaroid
   cd sugaroid
   python3 setup.py install --user

<br>

.. _header-n36:

Execution
---------

Running ``sugaroid`` is easy as pie

Just execute

.. code:: shell

   $ sugaroid

from the Terminal (Linux, Mac OS) and PowerShell (on Windows)

There are few arguments that can be passed to sugaroid

-  ``qt`` : Running ``sugaroid qt`` will start the ``sugaroid``
   graphical user interface

-  ``audio`` : Running ``sugaroid audio`` will include audio support for
   ``sugaroid`` (Data charges may apply)

-  ``train``: Running ``sugaroid train`` will start the sugaroid
   trainer, which you can use to train sugaroid for some responses

-  ``update`` : Running ``sugaroid update`` will clear the current
   database and train the new data and store it persistently to the
   configuration path as ``sugaroid.db`` . (See
   `Configuration <#Configuraton>`__ for more details)

To launch the sugaroid web server on any ``IP`` address, do a local
clone of the package by

.. code:: shell

   git clone https://github.com/srevinsaju/sugaroid-wsgi --depth=1
   cd sugaroid-wsgi
   python manage.py runserver

Follow the on-screen instructions to get it running on your web browser.
If the command completed with a status ``OK``, you should be able to see
sugaroid running on https://0.0.0.0:8000

<br>

.. _header-n268:

Interfaces
----------

.. _header-n55:

Command Line Interface 
~~~~~~~~~~~~~~~~~~~~~~

``sugaroid`` was initially built to be a command line. This was
beneficial for testing an development of new algorithms without calling
the GUI every time. A CLI is more familiar to developers. Logging could
be manually adjusted to show the verbose outputs. This was implemented
within ``sugaroid.sugaroid`` and could be toggled, by setting

.. code:: python

   sugaroid.sugaroid.verbosity = logging.INFO

The ``INFO`` can be replaced to match any of the following ``WARNING``,
``ERROR`` , ``INFO``

.. figure:: /run/media/ss/ARCH_DATA/git/sugaroid/docs/img/sugaroid_console.png
   :alt: 

.. _header-n60:

Graphical User Interface (Local)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /home/ss/repo/sugaroid/docs/img/sugaroid_qt.gif
   :alt: 

The modular capacity of Sugaroid makes it easy to implement a GUI
without rewriting the code. This is highly efficient because it reuses
objects and reduces the size of the end distribution. The GUI for
sugaroid is built on ``LGPL`` based open source GUI framework, viz.
``PyQt5``. The implemented ``PyQt5`` framework in ``Sugaroid`` looks
similar to the following image. (Image may vary with updates)

.. _header-n63:

Django (Web) Interface
~~~~~~~~~~~~~~~~~~~~~~

In order to provide a server side chatbot server, the sugaroid AI was
configured to be used to Django. This used open source bootstrap
templates to create a chatbot appearance that was pretty neat and
effective way to host it on a Django server (if one exists)

.. figure:: /run/media/ss/ARCH_DATA/git/sugaroid/docs/img/sugaroid_django.gif
   :alt: 

The current work left on the Django system is to enable cookies to store
the data on the client side temporarily and not on the server side. The
current Django implementation is based on server-side, which implies the
chat history is saved on the server

<br>

.. _header-n67:

Similarity Algorithms
---------------------

.. _header-n68:

Jaccard Similarity
~~~~~~~~~~~~~~~~~~

Jaccard Similarity / sigma similarity uses a simple, but less memory
intensive algorithm to analyze the statements. The equation is given as
follows

.. math:: \theta = \frac {n}{x+y}

Where n, number of common words in list x and list y, and (x+ y) shows
the union of x and y similarity.

The benefits of using Jaccard similarity is that, sugaroid can implement
``can_process`` methods in an object with optimal resource usage. There
is no need to use complex cosine dot product for finding similarity in
cases there are only one word as list x and list y respectively. This
helped to optimize the sugaroid bot partly

Jaccard Similarity can be accessed by
``sugaroid.brain.preprocessors.sigma_similarity``

<br>

.. _header-n74:

Cosine Dot product 
~~~~~~~~~~~~~~~~~~

The Sugaroid AI selectively uses Cosine Dot product for comparing
statements on the ratio of similarity and selects an appropriate
statement stored to the database.

.. math::

   \vec A.\vec B = ABcos\theta \\
   cos \theta = \frac{\vec A . \vec B}{A.B}

Words are classified as vectors in this case. Similar words are given
similar but unique vector quantity, such that only equal phrases can
have the common cosine dot product. This vector model was downloaded
from the universal ``nltk.wordnet`` is a collection of word and their
classification

.. figure:: /home/ss/repo/sugaroid/docs/img/wordnet-event.png
   :alt: 

This complex collection of details helped to club similar nouns and
verbs together and provide customized answers, reduce training data and
increasing program logic. Therefore, each data was not to be separately
forced to the sugaroid bot to understand and learn but also learn the
phrases of message input by itself and store it in the SQL Database for
future reference

Cosine Dot product can be accessed within sugaroid by
``sugaroid.brain.postprocessors.cosine_similarity``

<br>

.. _header-n81:

Jensen Shannon Distance (JSD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Jensen Shannon
Distance <https://en.wikipedia.org/wiki/Jensen–Shannon_divergence>`__ is
the last and the complex algorithm used inside ``sugaroid`` bot. The
equation for finding Jensen Shannon Distance is not directly used within

.. math::

   D(M || Q) = \sum M(i) . \log \frac {M(i)}{Q(i)} \\
   JSD (M || Q) = \frac 12\sum ( \log(\frac {M(i)}{\frac12M(i) + Q(i)}) + \log(\frac{Q(i)}{\frac 12 M(i) + Q(i)}))

This being a complex and CPU intensive process, is handled
systematically by a Natural Language Processing library with Industrial
Processing support, viz, SpaCy. The `SpaCy <spacy.io>`__ library handles
this effectively by loading data from ``en_core_web_sm`` and
``en_core_web_lg``

The difference between ``sm`` and ``lg`` is that, ``en_core_web_sm`` is
collection of all the word in the dictionary with vectors only and
weighs 7.5 MB. The ``en_core_web_lg`` weighs 880 MB, and has data for
``tensors`` too. This dataset is more efficient because, the data so
obtained has tensor data and this helps to correctly measure Jensen
Shannon Distance.

The JSD is internally implemented in an ``nlp`` object called
``LanguageProcessor`` and handles most of the complex conversations
inside ``sugaroid.brain.utils.LanguageProcessor`` is a signed class with
two methods ``tokenize`` and ``similarity`` The ``similarity`` method
return the resultant net vector displacement of the given vectors.

.. _header-n87:

Sentiments Analyzer
^^^^^^^^^^^^^^^^^^^

The ``sugaroid.brain`` features another comprehensive object derived
from ``wordnet`` called ``SentimentsIntensityAnalyzer`` or ``sia`` for
short. The ``SentimentIntensityAnanlyzer`` has a list of words with
positivity, negativity and neutrality. ``sugaroid`` bot uses
``vader_lexicon`` to classify sentences as attributive or corruptive and
then gives an equal answer.

.. _header-n89:

Faults in Similarity Algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes, the similarity algorithms may give a completely incorrect
answer that may lead to false response by the bot to the user. This is
because tensors have no resultant displacement and has multiple
direction. To compute zero vectors, SpaCy uses an approximation
algorithm called Word Mover Distance. This might lead to unknown
predictions. Such predictions should be raised as an issue on the
Sugaroid repository to create a tackler adapter that would override the
answer with a suitable confidence value.

The other complex and efficient algorithms have been neglected. This is
to reduce the size of the distribution as well as reduce the time of
installation on an end-user's PC. Complex and accurate Natural Language
Processing systems like ``pytorch`` and ``tensorflow`` exists, but this
may result in the net user installation size to be approximately 2 GB +,
which is probably not what the end-user requires.

<br>

.. _header-n92:

Configuration
-------------

Sugaroid saves some data to your PC. The path where ``sugaroid`` saves
the data is ``~/.config/sugaroid`` on Linux and Mac OS, but on Windows
it is in ``C:\Users\<username>\AppData\sugaroid\``

This is the training database used my sugaroid to answer your questions.
Particularly related to ``sugaroid`` brain, the files are
``sugaroid.db`` and ``sugaroid.trainer.json``

-  ``sugaroid.db`` : The Sugaroid bot uses ``SQLite`` to read data from
   a persistent database. Remove ``sugaroid.db`` will reset
   ``sugaroid``'s brain, and a fresh database will be created from
   scratch

-  ``sugaroid.trainer.json`` : Is a JavaScript Object Notation file
   which stores trained responses in order to reset or retrain them
   whenever there is a necessity. This file may or may not be present in
   end user's systems and depends solely on the type of release ``dev``
   or ``stable``

There might also be additional files in the configuration directory.
These are Audio files, In the case that the ``audio`` keyword is passed
as an argument, it creates samples of audio files downloaded from the
``Google`` server to serve `TTS (Text to
Speech) <https://cloud.google.com/text-to-speech>`__ to the end user.

.. _header-n101:

TTS Configuration files
~~~~~~~~~~~~~~~~~~~~~~~

The TTS configuration files are created by the
``sugaroid.tts.Text2Speech`` class. This follows an optimization
algorithm. The following is the steps followed by it in short:

.. code:: mermaid

   graph LR
       C{Path Exists}
       C -->|False| D[Create folder]
       C -->|True| E{Audio exists}
       E -->|True| F[Play]
       E -->|False| G[Download]
       G --> F

This algorithm is implemented to prevent the download of Audio files on
each request by the sugaroid bot.

.. _header-n106:

Memory 
------

The Sugaroid bot has been designed to provide an acceptable answer and
the author had been focusing on refining the response by the bot more
and more better. However this has resulted in bad PEP practices and dis
allocated memory modules.

========================= =========== ===========
Time                      Memory (KB) Memory (MB)
========================= =========== ===========
Initial Loading           83500 KB    83.5 MB
Pause after loading       173800 KB   173.8 MB
First Question (Hello)    266500 KB   266.5 MB
Second Question (Hey)     287500 KB   287.5 MB
Third Question (Emotion)  289500 KB   289.5 MB
Fourth Question (Emotion) 289950 KB   290 MB
========================= =========== ===========

This is because, a lot of unnecessary objects have been created in the
memory. This should be removed before the release of ``sugaroid``
version 1.0

.. _header-n138:

Update v0.5.2+
~~~~~~~~~~~~~~

The unnecessary ``spaCy`` tokenizers were forced to be implemented into
a single function called ``sugaroid.sugaroid.SugaroidStatement`` which
calculates the ``spacy.nlp.Doc`` on each object initialization. All the
rest of the statement tokenizers were replaced by the base class usage.
This prevents the recalculation of the similarity and tokens for each
adapter. However, the number of adapters have increased considerably.
The net memory decrease cannot be plotted, nevertheless. On the addition
of each Adapter, the average RAM increases logarithmically as far as 1%
of the total RAM used. This increases exponentially until the bases
state where the coverage of sugaroid has been achieved to be above 75%
and all the adapters have been significantly used to process at least 1
statement.

.. _header-n140:

CPU Usage
---------

The Sugaroid bot does not have significant CPU usage. Tested on Linux
Manjaro running with 1.8 GHz with other applications running did not
affect system stability.

.. _header-n142:

Adapters
--------

The brain of sugaroid relies in the modules it uses. Sugaroid uses many
modules to process statements called ``Adapters`` to process statements.
Each statement is checked against two functions
``LogicAdapter.can_process()`` and ``LogicAdapter.process()``.
``LogicAdapter.can_process()`` gives a boolean response if the statement
can or cannot be processed. If the statement can be processed,
``LogicAdapter.process()`` is called.

As of Sugaroid ``v0.7``, it has:

-  ``BoolAdapter``: Processes Boolean based answers

-  ``AkinatorAdapter``: Adapter which ports the wrapper of the Akinator
   game to Sugaroid

-  ``HangmanAdapter``: Plays hangman with you

-  ``OrAdapter``: Selects a random operand of the provided statement

-  ``OkayAdapter``: Handles statements with a plain old okay

-  ``ByeAdapter``: Destroys Sugaroid on bye

-  ``TimeAdapter``: Provides time and time related functions except time
   conversion

-  ``CurrencyAdapter``: Gives a random response, because Sugaroid tries
   not to say I don't know

-  ``LearnAdapter``: a specific adapter for learning responses

-  ``TriviaAdapter``: Plays a short game of trivia

-  ``WhoAdapter``: Handles statements with 'who' as one of the tokens

-  ``NewsAdapter``: Ports the ``SugaroidNews`` Wrapper for easier access
   by the ``SugaroidChatbot`` Class

-  ``JokeAdapter``: Gets a random joke from the Chuck Norris Database

-  ``PlayAdapter``: ``[DEPRECATED]`` Plays a game on desktops only

-  ``CanAdapter``: Processes statements which features a Modal question
   (can, may)

-  ``BecauseAdapter``: Processes statements which starts with Because or
   gives a reason

-  | ``ReReverseAdapter``: Processes statements featuring conversational
     flow. It scans the previous statements
   | and takes a cosine similarity of the statements, and ``TFiD``
     Vector cross product to get
   | the most probable answer

-  ``ReverseAdapter:`` A random adapter. Top Secret

-  ``MyNameAdapter``: Handles sentences featuring 'my' and 'name'

-  ``MeAdapter``: Processes the statements showing possessive

-  ``AboutAdapter``: Defines the personality of sugaroid

-  ``WikiAdapter``: Handles Wikipedia based questions

-  ``DoLikeAdapter``: Handles likes of Sugaroid

-  ``FeelAdapter``: Handles sentences containing the word feel

-  ``DoAdapter``: Processes statements beginning with 'Do' and 'know'

-  ``EmotionAdapter``: Handles positive and negative emotional
   statements

-  | ``DisAdapter``: A complex algorithm sorting the words beginning
     with negative based on the probability.
   |  and achieving a similar confidence ratio of the word percentage.
   |  The ``DisAdapter`` keeps the confidence below 0.5 so that the
     ``BestAdapte``\ r may find some
   |  other answer similar to

-  ``TwoWordAdapte``: Handles sentences having two words

-  ``OneWordAdapter``: Logical adapter for processing data with one
   words

-  ``DebugAdapter``: Internal administrator feature to debug Sugaroid
   statements

-  ``WhyWhenAdapter``: Processes wh-adverbs

-  ``ReaderAdapter``: Logical adapter for processing data with one words

-  ``ImitateAdapter``: Handles statements involving imitations of some
   sentences

-  ``FunAdapter``: Gives a random response, because Sugaroid tries not
   to say I don't know

-  ``UnitConversion``: The ``UnitConversion`` logic adapter parse inputs
   to convert values

.. |image0| image:: https://c5.patreon.com/external/logo/become_a_patron_button.png
   :target: https://www.patreon.com/srevinsaju?fan_landing=true
