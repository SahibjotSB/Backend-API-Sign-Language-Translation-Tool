## Backend Api Sign Language Translator

**Description: Receives text input and returns a message confirming successful translation.**

**Input Parameters ('text)**

'text' is the input, text is a string.

**Responses** **(200, 400, 500)**

**200 OK**:

```json
{"message": "Translation was successful"}
```

**400 Error/Bad Request**:

```json
{"error": "Missing required parameter: text"}
```

**500 Unexpected Error**:

```json
{"error": "Translation Failure, unexpected error", "details": "error details"}
```

## Request (URL)

[http://127.0.0.1:5000/endpoint?text=Hello]() 										Local Link
[https://murmuring-refuge-76686-324ef957f012.herokuapp.com/endpoint?text=Hello](https://murmuring-refuge-76686-324ef957f012.herokuapp.com/endpoint?text=Hello)  	Deployed Link
