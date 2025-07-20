# Tweet Agent - AI-Powered Trending Tweet Generator

## Project Overview
Tweet Agent is a Flask-based web application that leverages AI to discover trending topics in India and generate engaging tweets. It integrates Google Gemini for content generation, DuckDuckGo for web search, and the Twitter API for posting tweets.

---

## Multi-Agent Features
- **AI-Powered Tweet Generation:** Uses Google Gemini to craft human-like, catchy tweets under 250 characters.
- **Web Search Integration:** Finds trending topics in India using DuckDuckGo.
- **Twitter API Integration:** Allows direct posting of generated tweets to your Twitter/X account.
- **Simple Web Interface:** Easy-to-use interface for generating and posting tweets.

---

## Project Structure
- All files should be in the `Tweet_Agent` directory.
- Main application logic is in `app.py`.
- API keys and secrets are managed via a `.env` file (not included in version control).

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd Tweet_Agent
   ```

2. **Create and Activate a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Create a `.env` file in the project root with the following keys:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     TWITTER_API_KEY=your_twitter_api_key
     TWITTER_API_SECRET=your_twitter_api_secret
     TWITTER_ACCESS_TOKEN=your_twitter_access_token
     TWITTER_ACCESS_SECRET=your_twitter_access_secret
     TWITTER_BEARER_TOKEN=your_twitter_bearer_token
     ```

---

## Usage

1. **Start the Application**
   ```bash
   python app.py
   ```

2. **Open your browser and go to**
   ```
   http://127.0.0.1:5000/
   ```

3. **Generate and Post Tweets**
   - Use the web interface to generate a tweet based on trending topics and post it directly to your Twitter/X account.

---

## Notes
- Ensure all API keys are valid and have the necessary permissions.
- The application is set to debug mode for development. Disable debug mode in production.
- For any issues, check your `.env` configuration and installed dependencies.

---

## License
This project is for educational and demonstration purposes.
