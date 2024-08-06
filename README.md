S

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

[http://127.0.0.1:5000/endpoint?text=Hello]()

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"></button></span></div></div></div></pre>
