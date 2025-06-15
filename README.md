# Free Music Recommendation System (Spotify + Streamlit)
## 🌟 Project Title
Free Music Recommendation System using Spotify API & Streamlit

🔹 Overview
This application lets you search for a song and get tailored recommendations based on its audio features (like energy, danceability, and mood) — powered by Spotify’s API and displayed through Streamlit.

🔹 Features
✅ Search for a song by its title
✅ View song details (artist, album, preview link)
✅ Get song recommendations with similar audio profiles
✅ 100% Free — just a Spotify Developer account is needed
✅ Streamlit UI — lightweight, simple, and easy to deploy

🔹 Tech Stack
Python 3.x

Spotify API (Spotify for Developers)

Spotipy (Spotify API wrapper)

Streamlit (Rapid UI framework)

Pandas, Scikit-learn (for data processing and similarity)

🔹 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/music-recommendation.git
cd music-recommendation
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
🔹 Requirements
bash
Copy
Edit
pip install -r requirements.txt
🔹 Spotify API Credentials
Create a Spotify Developer App at Spotify Developer Dashboard.

Then:

Get your Client ID

Get your Client Secret

Set a Redirect URI (like http://127.0.0.1:8888/callback) or your Streamlit deploy URL

Enable user-read-private

🔹 Environment Variables or Streamlit Secrets
Save your credentials in Streamlit secrets:

Create a .streamlit/secrets.toml:

toml
Copy
Edit
SPOTIPY_CLIENT_ID = "<your_client_id>"
SPOTIPY_CLIENT_SECRET = "<your_client_secret>"
SPOTIPY_REDIRECT_URI = "<your_redirect_uri>"
🔹 How to Run (Local)
bash
Copy
Edit
streamlit run main.py
🔹 How to Deploy (Streamlit Cloud)
Push your code to Github.

Go to https://share.streamlit.io/.

Link your repository.

Set your Streamlit secrets in Streamlit Cloud’s Dashboard.

Deploy and share with friends! 🚀

🔹 File Structure
css
Copy
Edit
your-repo/
 └ main.py
 └ spotify_backend.py
 └ requirements.txt
 └ .streamlit/
      └ secrets.toml
 └ README.md
🔹 Contributing
Contributions are welcome!
Please feel free to submit a Pull Request or raise an Issue if you have any suggestions or bug fixes.

🔹 Contact
If you have questions or want to collaborate, reach me at: [your.email@example.com]

✨ Happy coding and happy listening! 🍻
