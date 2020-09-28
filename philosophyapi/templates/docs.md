
<a id="intro"></a>
# Introduction

Welcome to the <span>Movies API Documentation</span> here you will better understand the details about the available resources and also learn how to consume them through [HTTP requests](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html).

- - -

<a id="start"></a>
## Getting Started

Movies API is an API focused on reading resources, for this reason we will use the [GET method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) with it in most scenarios to obtain our resources in JSON format and use it in the way that is most convenient for us.

There are several ways to execute HTTP requests, either through a web browser, a programming language like [Python](https://requests.readthedocs.io/en/master/) or [Javascript](https://github.com/axios/axios), or with software like [curl](https://github.com/curl/curl) or [httpie](https://httpie.org/). For this specific task we will use httpie for its simplicity. So let's start by asking for resources about the game genres. Open up your terminal and type

```
http https://mooviesapi.herokuapp.com/api/genres/
```

We will immediately receive the following resource in response

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 307
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 13:05:25 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 13,
	    "next": "http://127.0.0.1:8000/api/genres/?page=2",
	    "previous": null,
	    "results": [
	        {
	            "id": 1,
	            "name": "Horror"
	        },
	        {
	            "id": 2,
	            "name": "Adventure"
	        },
	        {
	            "id": 3,
	            "name": "Science Fiction"
	        },
	        {
	            "id": 4,
	            "name": "Action"
	        },
	        {
	            "id": 5,
	            "name": "Drama"
	        },
	        {
	            "id": 6,
	            "name": "Fantasy"
	        },
	        {
	            "id": 7,
	            "name": "Historical"
	        },
	        {
	            "id": 8,
	            "name": "Mystery"
	        }
	    ]
	}

As we can see, several game genres are returned to us with their respective ids and names

- - -

<a id="base"></a>
## Base URL

The base URL is the root URL of the API's and it can serve as a map to locate us and understand the resources that are at our disposal. The base URL for the Video Games API is as follows

```
https://mooviesapi.herokuapp.com/api/
```

Consider this root URL as the basis for our future requests

- - -