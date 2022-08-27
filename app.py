from flask import Flask, render_template

# 패키지 빠짐 request, jsonify

# 패키지 설치 flask, pymongo, dnspython
# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://test:sparta@Cluster0.qizmaae.mongodb.net/?retryWrites=true&w=majority')
# db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')



# @app.route("/mars", methods=["POST"])
# def web_mars_post():
#     name_receive = request.form['name_give']
#     address_receive = request.form['address_give']
#     size_receive = request.form['size_give']
#
#     # name, address, size를 위에 자료를 받아서 밑에 코드(서버에 올리는 코드)를 이용해서 저장해라
#     # 서버에 올리는 코드
#
#     doc = {
#         'name':name_receive,
#         'address':address_receive,
#         'size':size_receive
#     }
#     db.mars.insert_one(doc)
#
#
#     print(name_receive)
#     return jsonify({'msg': '주문완료!!'})
#
# @app.route("/mars", methods=["GET"])
# def web_mars_get():
#     order_list = list(db.mars.find({}, {'_id': False}))
#     return jsonify({'orders': order_list})
#
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
