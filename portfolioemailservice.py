from flask import Flask, jsonify, request


app = Flask(__name__)

contact_details = []

@app.route('/',methods=['GET'])
def get_stored_contacts():
    return jsonify(contact_details)

@app.route('/', methods=['POST'])
def add_contact_card():
    request_data = request.get_json()
    for item in request_data:
        contact_card = \
            {
            "name" : item["name"]
        }
        contact_details.append(contact_card)




    return jsonify({"status": "200","data": contact_details})

if __name__ == '__main__':
    app.run()