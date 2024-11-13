from flask import Flask, render_template, request
from transformers import pipeline

# Initialize Flask application
app = Flask(__name__)

# Initialize paraphrasing model
paraphraser = pipeline("text2text-generation", model="t5-base")

# Main page with input text form
@app.route("/", methods=["GET", "POST"])
def home():
    paraphrased_text = ""
    if request.method == "POST":
        original_text = request.form["original_text"]
        if original_text:
            result = paraphraser(original_text, max_length=50, num_return_sequences=1)
            paraphrased_text = result[0]['generated_text']
    return render_template("index.html", paraphrased_text=paraphrased_text)

if __name__ == "_main_":
    print("Memulai aplikasi...")
    print("Aplikasi berjalan di http://127.0.0.1:5001")
    app.run(debug=True, port=5001)