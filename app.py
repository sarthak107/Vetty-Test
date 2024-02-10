from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def file_content():
    filename = request.args.get('filename') if request.args.get('filename') else 'file1.txt'
    start = request.args.get('start') 
    end = request.args.get('end')
    file_path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(file_path):
        return "Error: File not found", 404
    encodings_to_try = ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be']
    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                lines = file.readlines()
            break 
        except UnicodeDecodeError:
            continue
    result = []
    if start and end:
        try:
            start = int(start)
            end = int(end)
            if start < 0 or end > len(lines):
                return "Error: Invalid line number", 400
            result = lines[start:end+1]
        except ValueError:
            return "Error: start or end should be an integer", 400
    elif start:
        try:
            start = int(start)
            end = len(lines) - 1
            if start < 0 or end > len(lines):
                return "Error: Invalid line number", 400
            result = lines[start:end+1]
        except ValueError:
            return "Error: lineNo should be an integer", 400
    elif end:
        try:
            start = 1
            end = int(end)
            if start < 0 or end > len(lines):
                return "Error: Invalid line number", 400
            result =  lines[start:end+1]
        except ValueError:
            return "Error: lineNo should be an integer", 400
    else:
        result = lines
    response = ""
    for line in result:
        response += f"<p>{line}</p>"
    return response

if __name__ == '__main__':
    app.run(debug=True)