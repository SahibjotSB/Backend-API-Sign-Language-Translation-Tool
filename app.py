from flask import Flask, request, jsonify 

app = Flask(__name__)
"""
Input:
    text - (string) (Given via URL)
    
Possible Responses:
    Successfull ------- 200
    Error/Bad Request - 400
    Unexpected Error -- 500
"""
#Route
@app.route('/endpoint', methods=['GET'])
def translate(): 
    try:
        input_text = request.args.get('text')
        if not input_text:
            return jsonify({'error': 'Missing required parameter: text'}), 400 #Error/Bad Request
        return jsonify({'message': 'Translation was successful'}), 200 #Successful 
    except Exception as er:
        return jsonify({'error': 'Translation Failure, unexpected error', 'details': str(er)}), 500 #Unexpected Error
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    
