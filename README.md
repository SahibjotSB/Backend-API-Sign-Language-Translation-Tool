<<<<<<< HEAD
## Backend Api Sign Language Translator
=======
## Backend Api Sign Language Translator 
>>>>>>> 87fbe1ace1bea1538f3edeb28953e59957bee42b

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

[http://127.0.0.1:5000/endpoint?text=Hello]()
