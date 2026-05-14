app = Flask(__name__)
@app.route('/register')
def register():
# Pre-written WhatsApp message with form details
message = "Hello, I want to learn tech!"
# Replace with your WhatsApp number
whatsapp_url = f"https://wa.me/YOUR_NUMBER?text={message}"
return redirect(whatsapp_url)
if name == 'main':
app.run()`
