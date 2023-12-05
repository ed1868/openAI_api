import openai
from flask import Flask, render_template, request, jsonify
from dotenv import dotenv_values

# Load API key from .env file
config = dotenv_values('.env')
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__,
            template_folder='templates',
            static_url_path='', 
            static_folder='static')

def generate_images(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=3,  # Generate 3 images
            size="1024x1024"  # Size of each image
        )
        images = [img["url"] for img in response.data]  # Extract image URLs
        return images
    except Exception as e:
        print(f"Error generating images: {e}")
        return []

@app.route("/generate-images", methods=["POST"])
def prompt_to_images():
    prompt = request.form.get("prompt")
    images = generate_images(prompt)
    return jsonify(images=images)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return "YOU NEED TO CREATE A SIGNUP PAGE"

if __name__ == "__main__":
    app.run(debug=True)