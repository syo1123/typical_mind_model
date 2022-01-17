import os
from app.app import app

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9999)
