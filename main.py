from flask import request, jsonify
from config import app, db
from models import BlogPost

def seed_data():
    if BlogPost.query.first():
        print("Database already contains data. Skipping seeding.")
        return

    blog_posts = [
        BlogPost(
            title="First Blog Post",
            author="Alice",
            content="This is the content of the first blog post."
        ),
        BlogPost(
            title="Second Blog Post",
            author="Bob",
            content="This is the content of the second blog post."
        ),
        BlogPost(
            title="Third Blog Post",
            author="Charlie",
            content="This is the content of the third blog post."
        )
    ]
    
    db.session.add_all(blog_posts)
    db.session.commit()
    print("Seed data inserted!")

@app.route("/blogs", methods=["GET"])
def get_blogs():
    blogs = BlogPost.query.all()
    json_blogs = [blog.to_json() for blog in blogs]
    return jsonify({"blogs": json_blogs})


@app.route("/blogs/<int:blog_id>", methods=["GET"])
def get_blog(blog_id):
    blog = BlogPost.query.get(blog_id)

    if not blog:
        return jsonify({"message": "Blog post not found"}), 404

    return jsonify(blog.to_json())


@app.route("/create_blog", methods=["POST"])
def create_blog():
    title = request.json.get("title")
    author = request.json.get("author")
    content = request.json.get("content")

    if not title or not author or not content:
        return jsonify({"message": "All fields are required"}), 400

    new_blog = BlogPost(title=title, author=author, content=content)

    try:
        db.session.add(new_blog)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Blog post created", "blog": new_blog.to_json()}), 201


@app.route("/update_blog/<int:blog_id>", methods=["PATCH"])
def update_blog(blog_id):
    blog = BlogPost.query.get(blog_id)

    if not blog:
        return jsonify({"message": "Blog post not found"}), 404

    data = request.json
    blog.title = data.get("title", blog.title)
    blog.author = data.get("author", blog.author)
    blog.content = data.get("content", blog.content)

    db.session.commit()

    return jsonify({"message": "Blog post updated", "blog": blog.to_json()})


@app.route("/delete_blog/<int:blog_id>", methods=["DELETE"])
def delete_blog(blog_id):
    blog = BlogPost.query.get(blog_id)

    if not blog:
        return jsonify({"message": "Blog post not found"}), 404

    db.session.delete(blog)
    db.session.commit()

    return jsonify({"message": "Blog post deleted"})


if __name__ == "__main__":
    with app.app_context():
        
        db.create_all()
        
        seed_data()

    app.run(debug=True)
