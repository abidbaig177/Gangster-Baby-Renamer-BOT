import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20124301")

API_HASH = os.environ.get("API_HASH", "8f39dd0f8b439da5e64c1fab71991a6b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6247178492:AAFuT1NASzuyTD2VE2xOyUx2-RwTeyQGicg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "cyber_robots") 

DB_NAME = os.environ.get("DB_NAME","clusters0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://AMERICAN:ULTRA123@cluster0.2qwwxm1.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ac82c3a764c6e8d58983e.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
