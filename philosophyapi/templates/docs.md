
<a id="intro"></a>
# Introduction

Welcome to the <span>Philosophy API Documentation</span> here you will better understand the details about the available resources and also learn how to consume them through [HTTP requests](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html).

- - -

<a id="start"></a>
## Getting Started

**Philosophy API** is an API focused on reading resources, for this reason we will use the [GET method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) with it in most scenarios to obtain our resources in JSON format and use it in the way that is most convenient for us.

There are several ways to execute HTTP requests, either through a web browser, a programming language like [Python](https://requests.readthedocs.io/en/master/) or [Javascript](https://github.com/axios/axios), or with software like [curl](https://github.com/curl/curl) or [httpie](https://httpie.org/). For this specific task we will use httpie for its simplicity. So let's start by asking for resources about some of the philosophers ideas. Open up your terminal and type:

```
http https://philosophyapi.herokuapp.com/api/ideas/
```

We will immediately receive the following resource in response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 1920
	Content-Type: application/json
	Date: Mon, 28 Sep 2020 18:56:08 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 254,
	    "next": "http://127.0.0.1:8000/api/ideas/?page=2",
	    "previous": null,
	    "results": [
	        {
	            "author": "René Descartes",
	            "id": 1,
	            "quote": "I think, therefore I am"
	        },
	        {
	            "author": "René Descartes",
	            "id": 2,
	            "quote": "It is not enough to have a good mind; the main thing is to use it well."
	        },
	        {
	            "author": "René Descartes",
	            "id": 3,
	            "quote": "The greatest minds are capable of the greatest vices as well as of the greatest virtues."
	        },
	        {
	            "author": "René Descartes",
	            "id": 4,
	            "quote": "The reading of all good books is like a conversation with the finest minds of past centuries."
	        },
	        {
	            "author": "René Descartes",
	            "id": 5,
	            "quote": "Divide each difficulty into as many parts as is feasible and necessary to resolve it."
	        },
	        {
	            "author": "René Descartes",
	            "id": 6,
	            "quote": "Each problem that I solved became a rule, which served afterwards to solve other problems."
	        },
	        {
	            "author": "René Descartes",
	            "id": 7,
	            "quote": "If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things"
	        },
	        {
	            "author": "René Descartes",
	            "id": 8,
	            "quote": "Perfect numbers like perfect men are very rare."
	        },
	        {
	            "author": "René Descartes",
	            "id": 9,
	            "quote": "Everything is self-evident"
	        },
	        {
	            "author": "René Descartes",
	            "id": 10,
	            "quote": "Except our own thoughts, there is nothing absolutely in our power"
	        },
	        {
	            "author": "René Descartes",
	            "id": 11,
	            "quote": "When it is not in our power to follow what is true, we ought to follow what is most probable"
	        },
	        {
	            "author": "Immanuel Kant",
	            "id": 12,
	            "quote": "He who is cruel to animals becomes hard also in his dealings with men. We can judge the heart of a man by his treatment of animals."
	        },
	        {
	            "author": "Immanuel Kant",
	            "id": 13,
	            "quote": "Happiness is not an ideal of reason, but of imagination."
	        },
	        {
	            "author": "Immanuel Kant",
	            "id": 14,
	            "quote": "Science is organized knowledge. Wisdom is organized life."
	        },
	        {
	            "author": "Immanuel Kant",
	            "id": 15,
	            "quote": "Live your life as though your every act were to become a universal law."
	        }
	    ]
	}

As we can see, several philosopher's ideas are returned to us with their respective **ids** and **author**

- - -

<a id="base"></a>
## Base URL

The base URL is the root URL of the API's and it can serve as a map to locate us and understand the resources that are at our disposal. The base URL for the Philosophy API is as follows

```
https://philosophyapi.herokuapp.com/api/
```

Consider this root URL as the basis for our future requests

- - -

<a id="auth"></a>
## Authentication

<span>Philosophy API</span> is a completely open API, without the need for authentication or token generation to obtain the data.

- - -

<a id="search"></a>
## Search Filter

The SearchFilter class supports simple single query parameter based searching, and is based on the Django admin's search functionality. Each resource has a field in which we can query specific data. Let's look at an example to illustrate the idea!

Let's make an HTTP request to the following URL

```
http http://philosophyapi.herokuapp.com/api/ideas/?search=God
```

We will get a filtered response only from the keyword we want, in this case, **God**:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 2875
	Content-Type: application/json
	Date: Mon, 28 Sep 2020 19:01:17 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 12,
	    "next": null,
	    "previous": null,
	    "results": [
	        {
	            "author": "Gottfried Wilhelm Leibniz",
	            "id": 50,
	            "quote": "it is the knowledge of necessary and eternal truths that distinguishes us from the mere animals and gives us Reason and the sciences, raising us to the knowledge of ourselves and of God"
	        },
	        {
	            "author": "Georg Wilhelm Friedrich Hegel",
	            "id": 119,
	            "quote": "Art does not simply reveal God: it is one of the ways in which God reveals, and thus actualizes, himself"
	        },
	        {
	            "author": "Ludwig Andreas von Feuerbach",
	            "id": 121,
	            "quote": "It is not as in the Bible, that God created man in his own image. But, on the contrary, man created God in his own image."
	        },
	        {
	            "author": "Ludwig Andreas von Feuerbach",
	            "id": 122,
	            "quote": "My only wish isto transform friends of God into friends of man, believers into thinkers, devotees of prayer into devotees of work, candidates for the hereafter into students of the world, Christians who, by their own procession and admission, are half animal, half angel into persons, into whole persons."
	        },
	        {
	            "author": "Ludwig Andreas von Feuerbach",
	            "id": 124,
	            "quote": "Christianity set itself the goal of fulfilling man’s unattainable desires, but for that very reason ignored his attainable desires. By promising man eternal life, it deprived him of temporal life, by teaching him to trust in God’s help it took away his trust in his own powers; by giving him faith in a better life in heaven, it destroyed his faith in a better life on earth and his striving to attain such a life. Christianity gave man what his imagination desires, but for that very reason failed to give him what he really and truly desires."
	        },
	        {
	            "author": "Ludwig Andreas von Feuerbach",
	            "id": 139,
	            "quote": "Faith is essentially intolerant ... essentially because necessarily bound up with faith is the illusion that one's cause is also God's cause"
	        },
	        {
	            "author": "Søren Aabye Kierkegaard",
	            "id": 144,
	            "quote": "The function of prayer is not to influence God, but rather to change the nature of the one who prays"
	        },
	        {
	            "author": "Søren Aabye Kierkegaard",
	            "id": 167,
	            "quote": "God creates out of nothing. Wonderful you say. Yes, to be sure, but he does what is still more wonderful: he makes saints out of sinners"
	        },
	        {
	            "author": "Søren Aabye Kierkegaard",
	            "id": 170,
	            "quote": "The proud person always wants to do the right thing, the great thing. But because he wants to do it in his own strength, he is fighting not with man, but with God"
	        },
	        {
	            "author": "Aldous Leonard Huxley",
	            "id": 184,
	            "quote": "But I don't want comfort. I want God, I want poetry, I want real danger, I want freedom, I want goodness. I want sin"
	        },
	        {
	            "author": "Aldous Leonard Huxley",
	            "id": 230,
	            "quote": "It is natural to believe in God when you're alone-- quite alone, in the night, thinking about death"
	        },
	        {
	            "author": "Aldous Leonard Huxley",
	            "id": 235,
	            "quote": "All gods are homemade, and it is we who pull their strings, and so, give them the power to pull ours"
	        }
	    ]
	}

In this example the search was made in the quote's.

- - -

<a id="pagination"></a>
## Pagination

Philosophy API provides data through chunks that can be paged. Let's request the second page of schools of thought to get an idea of how this mechanism works

Let's request the following URL

```
http https://philosophyapi.herokuapp.com/api/schools/?page=2
```

Immediately we obtain the respective data on the second page of schools of thought

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 763
	Content-Type: application/json
	Date: Mon, 28 Sep 2020 19:04:33 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 24,
	    "next": null,
	    "previous": "http://127.0.0.1:8000/api/schools/",
	    "results": [
	        {
	            "id": 19,
	            "name": "Empirical realism",
	            "philosophers": []
	        },
	        {
	            "id": 20,
	            "name": "Absolute idealism",
	            "philosophers": []
	        },
	        {
	            "id": 21,
	            "name": "Anthropological materialism",
	            "philosophers": [
	                "Ludwig Andreas von Feuerbach"
	            ]
	        },
	        {
	            "id": 22,
	            "name": "Secular humanism",
	            "philosophers": [
	                "Ludwig Andreas von Feuerbach"
	            ]
	        },
	        {
	            "id": 23,
	            "name": "Young Hegelians",
	            "philosophers": [
	                "Ludwig Andreas von Feuerbach"
	            ]
	        },
	        {
	            "id": 25,
	            "name": "Existentialism",
	            "philosophers": [
	                "Søren Aabye Kierkegaard",
	                "Martin Heidegger"
	            ]
	        },
	        {
	            "id": 26,
	            "name": "Phenomenology",
	            "philosophers": [
	                "Martin Heidegger"
	            ]
	        },
	        {
	            "id": 27,
	            "name": "Hermeneutics",
	            "philosophers": [
	                "Martin Heidegger"
	            ]
	        },
	        {
	            "id": 28,
	            "name": "Perennialism",
	            "philosophers": [
	                "Aldous Leonard Huxley"
	            ]
	        }
	    ]
	}

Through pagination we can browse all available data.

- - -

<a id="encoding"></a>
## Encoding

JSON is the standard data format provided by Philosophy API by default. You can see details about Schema at the following URL: [API Schema](https://philosophyapi.herokuapp.com/api/schema/)

- - -

<a id="root"></a>
## Root

The Root resource provides information on all available resources within the API.

Example request:

```
http https://philosophyapi.herokuapp.com/api/
```

We will get the following response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 191
	Content-Type: application/json
	Date: Mon, 28 Sep 2020 19:06:18 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "books": "http://127.0.0.1:8000/api/books/",
	    "ideas": "http://127.0.0.1:8000/api/ideas/",
	    "philosophers": "http://127.0.0.1:8000/api/philosophers/",
	    "schools": "http://127.0.0.1:8000/api/schools/"
	}

### Root Attributes

- <span>Books</span>: String, The URL root for Books resources
- <span>Ideas</span>: String, The URL root for Ideas resources
- <span>Philosophers</span>: String, The URL root for Philosophers resources
- <span>Schools</span>: String, The URL root for Schools of Thought resources

- - -

<a id="philo"></a>
## Philosophers

A Philosopher resource represents a philosopher object with several attributes

### Endpoints

- <span>/api/philosophers/</span>: Get all the philosophers resources
- <span>/api/philosophers/{id}</span>: Get a specific philosopher

Example request:

```
http https://philosophyapi.herokuapp.com/api/philosophers/1/
```

We will get the following response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 1361
	Content-Type: application/json
	Date: Mon, 28 Sep 2020 19:09:35 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "books": [
	        "Discourse on the Method of Rightly Conducting One's Reason and of Seeking Truth in the Sciences"
	    ],
	    "born_date": "1596-03-31",
	    "death_date": "1650-02-11",
	    "era": "17th-century philosophy",
	    "id": 1,
	    "ideas": [
	        "I think, therefore I am",
	        "It is not enough to have a good mind; the main thing is to use it well.",
	        "The greatest minds are capable of the greatest vices as well as of the greatest virtues.",
	        "The reading of all good books is like a conversation with the finest minds of past centuries.",
	        "Divide each difficulty into as many parts as is feasible and necessary to resolve it.",
	        "Each problem that I solved became a rule, which served afterwards to solve other problems.",
	        "If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things",
	        "Perfect numbers like perfect men are very rare.",
	        "Everything is self-evident",
	        "Except our own thoughts, there is nothing absolutely in our power",
	        "When it is not in our power to follow what is true, we ought to follow what is most probable"
	    ],
	    "name": "René Descartes",
	    "nationality": "French",
	    "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg/800px-Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg",
	    "school": [
	        "Rationalism",
	        "Cartesianism",
	        "Mechanism",
	        "Augustinianism",
	        "Foundationalism"
	    ]
	}

### Philosopher's Attributes

- <span>id</span>: Integer, Unique id representing a philosopher
- <span>name</span>: String, Represents the name of the respective philosopher
- <span>photo</span>: String, Image URL representing the philosopher's photography
- <span>born_date</span>: String, Represents the date in which the philosopher was born
- <span>death_date</span>: String, Represents the date in which the philosopher died
- <span>nationality</span>: String, Represents the nation of the philosopher
- <span>era</span>: String, Represents the era in which the philosopher lived
- <span>school</span>: Array, An array of schools of thought that represents the philosopher
- <span>ideas</span>: Array, An array of ideas from the philosopher
- <span>books</span>: Array, An array of the books written by the philosopher

- - -

<a id="ideas"></a>
## Ideas

An Idea resource represents ideas of philosophers

### Endpoints

- <span>/api/ideas/</span>: Get all the ideas resources
- <span>/api/ideas/{id}</span>: Get a specific idea

Example request:

```
http https://philosophyapi.herokuapp.com/api/ideas/10/
```

We are going to receive the following response from the server:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 112
	Content-Type: application/json
	Date: Mon, 28 Sep 2020 19:20:23 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "author": "René Descartes",
	    "id": 10,
	    "quote": "Except our own thoughts, there is nothing absolutely in our power"
	}

### Ideas Attributes

- <span>id</span>: Integer, Unique id representing a idea
- <span>author</span>: String, Represents the author of the idea
- <span>quote</span>: String, Represents the idea itself

- - -

<a id="books"></a>
## Books

A Book resource represents a philosopher's book

### Endpoints

- <span>/api/books/</span>: Get all the books resources
- <span>/api/books/{id}</span>: Get a specific book

Example request:

```
http https://philosophyapi.herokuapp.com/api/books/1/
```

We are requesting the book which has the id 1. We will get the following response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 1006
	Content-Type: application/json
	Date: Mon, 28 Sep 2020 19:24:04 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "abstract": "Discourse on the Method of Rightly Conducting One's Reason and of Seeking Truth in the Sciences (French: Discours de la Méthode Pour bien conduire sa raison, et chercher la vérité dans les sciences) is a philosophical and autobiographical treatise published by René Descartes in 1637. It is best known as the source of the famous quotation \"Je pense, donc je suis\" (\"I think, therefore I am\", or \"I am thinking, therefore I exist\"),[1] which occurs in Part IV of the work. A similar argument, without this precise wording, is found in Meditations on First Philosophy (1641), and a Latin version of the same statement Cogito, ergo sum is found in Principles of Philosophy (1644).",
	    "author": "René Descartes",
	    "country": "France",
	    "cover": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Descartes_Discours_de_la_Methode.jpg",
	    "id": 1,
	    "language": "French",
	    "published": "1637-01-01",
	    "title": "Discourse on the Method of Rightly Conducting One's Reason and of Seeking Truth in the Sciences"
	}

### Books Attributes

- <span>id</span>: Integer, Unique id representing a book
- <span>title</span>: String, Represents the title of the book
- <span>author</span>: String, Represents the author of the book
- <span>cover</span>: String, Image URL representing the book cover
- <span>published</span>: String, Represents the date in which the book was published
- <span>language</span>: String, Represents the language in which the book was written
- <span>country</span>: String, Represents the country in which the book was written
- <span>abstract</span>: String, Represents an introduction to the book

- - -

<a id="schools"></a>
## Schools

A School resource represents a School of Thought

### Endpoints

- <span>/api/schools/</span>: Get all the schools resources
- <span>/api/schools/{id}</span>: Get a specific school

Example request:

```
http https://philosophyapi.herokuapp.com/api/schools/?page=1
```

Realize that we are requesting the first page of schools and we will get the following response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 1386
	Content-Type: application/json
	Date: Mon, 28 Sep 2020 19:51:27 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 24,
	    "next": "http://127.0.0.1:8000/api/schools/?page=2",
	    "previous": null,
	    "results": [
	        {
	            "id": 4,
	            "name": "Kantianism",
	            "philosophers": [
	                "Immanuel Kant"
	            ]
	        },
	        {
	            "id": 5,
	            "name": "Transcendental idealism",
	            "philosophers": [
	                "Immanuel Kant",
	                "Arthur Schopenhauer"
	            ]
	        },
	        {
	            "id": 6,
	            "name": "Classical liberalism",
	            "philosophers": [
	                "Immanuel Kant"
	            ]
	        },
	        {
	            "id": 7,
	            "name": "Rationalism",
	            "philosophers": [
	                "René Descartes",
	                "Gottfried Wilhelm Leibniz"
	            ]
	        },
	        {
	            "id": 8,
	            "name": "Cartesianism",
	            "philosophers": [
	                "René Descartes"
	            ]
	        },
	        {
	            "id": 9,
	            "name": "Mechanism",
	            "philosophers": [
	                "René Descartes"
	            ]
	        },
	        {
	            "id": 10,
	            "name": "Augustinianism",
	            "philosophers": [
	                "René Descartes"
	            ]
	        },
	        {
	            "id": 11,
	            "name": "Optimism",
	            "philosophers": [
	                "Gottfried Wilhelm Leibniz"
	            ]
	        },
	        {
	            "id": 12,
	            "name": "Conceptualism",
	            "philosophers": [
	                "Gottfried Wilhelm Leibniz",
	                "Georg Wilhelm Friedrich Hegel"
	            ]
	        },
	        {
	            "id": 13,
	            "name": "Foundationalism",
	            "philosophers": [
	                "René Descartes",
	                "Gottfried Wilhelm Leibniz"
	            ]
	        },
	        {
	            "id": 14,
	            "name": "Continental philosophy",
	            "philosophers": [
	                "Arthur Schopenhauer",
	                "Georg Wilhelm Friedrich Hegel",
	                "Søren Aabye Kierkegaard",
	                "Martin Heidegger"
	            ]
	        },
	        {
	            "id": 15,
	            "name": "Philosophical pessimism",
	            "philosophers": [
	                "Arthur Schopenhauer"
	            ]
	        },
	        {
	            "id": 16,
	            "name": "German idealism",
	            "philosophers": [
	                "Georg Wilhelm Friedrich Hegel"
	            ]
	        },
	        {
	            "id": 17,
	            "name": "Objective idealism",
	            "philosophers": [
	                "Georg Wilhelm Friedrich Hegel"
	            ]
	        },
	        {
	            "id": 18,
	            "name": "Hegelianism",
	            "philosophers": [
	                "Georg Wilhelm Friedrich Hegel"
	            ]
	        }
	    ]
	}

### Schools Attributes

- <span>id</span>: Integer, Unique id representing a school
- <span>name</span>: String, Represents the name of the school of thought
- <span>philosopher</span>: Array, An array of philosophers connected with these schools of thought

- - -

<a id="schema"></a>
## Schema

API schemas are a useful tool that allow for a range of use cases, including generating reference documentation, or driving dynamic client libraries that can interact with your API.

You can find Schema for the Philosophy API by visiting the following link: [Schema API](https://philosophyapi.herokuapp.com/schema)

- - -

<a id="contribution"></a>
## Contribution

You can contribute to the Philosophy API project in several ways

- Fork or Star the project on [Github](https://github.com/the-akira/PhilosophyAPI)
- Share it with your friends in Social Medias
- Help to improve the Code, Data Models and Documentation

- - -

<a id="playground"></a>
## Playground

Django Rest framework provides us with an interface that we can [try the API](https://philosophyapi.herokuapp.com/api) without the need for any tool.