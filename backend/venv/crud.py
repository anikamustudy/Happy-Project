from flask import Flask, request, jsonify

app = Flask(__name__)

post = []
#create
@app.route("http://127.0.0.1:5000/api/post" , methods= ['POST'])
def create_post():
    data = request.json
    title= data.get('title')
    content = data.get('content')
    author = data.get('author')
    
    new_post = {
        'id' : len(posts) +1,
        'title' : title,
        'content' : content,
        'author' : author     
    }
    posts.append(new_post)
    return jsonify(new_post), 201

#Read (all posts)
@app.route('/api/posts', methods = ['GET'])
def get_posts():
    return jsonify(posts), 200

#Read (single post)
@app.route('/api/posts/<int:post_id>', methods = ['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post), 200
    return jsonify({'error' : 'Post not found'}), 404

#Update
@app.route('/api/post/<int:post_id>', mehods =['PUT'])
def update_post(post_id):
    data = request.json
    post = next((post for post in posts if post ['id'] == post_id) ,None )
    if post:
        post['title'] = data.get('title', post['title'])
        post['content'] = data.get ('content', post['content'])
        
        post['author'] = data.get('author', post['author'])
        return jsonify(post), 200
    return jsonify({'error': 'Post not found'}), 404


#Delete
@app.route('/api/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in pots if post ['id']! = post_id]
    return jsonify({'message': 'Post deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
