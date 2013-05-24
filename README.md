---

APIs
====

---

In general
----------

API = Application Programming Interface.  This is a means by which you interact with the software.  Every piece of software or database has an API.

* In R, `lm()` is a function.  Behind the scenes, there are many other functions that are used by `lm`.  For example, `lm` calls various Fortran functions to do matrix multiplication.  You don't need to know about these functions in order to use `lm()`.  They are "hidden" from the user.  They are not part of the API.  The API of `lm()` is the specification of inputs and outputs.

INPUT SPECIFICATIONS:

    function (formula, data, subset, weights, na.action, method = "qr", 
      model = TRUE, x = FALSE, y = FALSE, qr = TRUE, singular.ok = TRUE, 
      contrasts = NULL, offset, ...) 

OUTPUT SPECIFICATIONS:
    
    Parameter estimates, p-values,...

Web APIs
--------

A *web API* is a specification for interacting with a website.  For example, the *Rotten Tomatoes* API:

INPUT SPECIFICATIONS:

    http request (query), such as http://api.rottentomatoes.com/api/public/v1.0/movies.json

OUTPUT SPECIFICATIONS:

    Data (response), in this case json data

You tell the website what you want to search for, and it passes back the results!

To use a web API you need a way to perform requests, and a way to get the resultant data.

* Using a web browser
* Using Python or R libraries


Rotten Tomatoes Web API
-----------------------

* Start [here](http://developer.rottentomatoes.com/)
* Meant for developers to interact with a website and build apps.  Because companies *love* people building apps, they often make an API.
* Data scientists can use them to extract data!
* Why is data stored?

API Resources
-------------

* Intro to APIs in Python by [code academy](http://www.codecademy.com/tracks/apis-python)

R packages
----------


Python packages
---------------

**Requests:**  A module used to request information from URLs.
**json:** Module to read/write json objects

---

Python
======

---

* High-level language like R
* Originally designed as a "gluing language", meant to piece together code written in *C* and *Java* and *C++* and so on.
* This flexibility has allowed developers to connect high performance C and Fortran libraries to Python.
* Over the last 10 years, much of the scientific community has adopted Python

Why should you learn Python?
----------------------------

* Can be naturally used for scientific computing, scraping webpages, simple text scripts, transforming text files from one form to another
* Python code is often very simple and easy to read

Python resources
----------------

* Software Carpentry [Lessons](http://software-carpentry.org/4_0/index.html)
  * [Python](http://software-carpentry.org/4_0/python/intro.html)
  * The unix [shell](http://software-carpentry.org/4_0/shell/index.html)
* Python introductory [course](http://www.codecademy.com/tracks/python)

Rotten Tomatoes Demo
--------------------

* An interesting source of data for social scientists
* Could be joined to the GetGlue data to add movie attributes





