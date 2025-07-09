#flask.......................................
from flask import Flask, render_template, request, jsonify, session, redirect, url_for

# Agents.....................................
from agno.agent import Agent 
from agno.models.google.gemini import Gemini

# Tools......................................
from agno.tools.duckduckgo import DuckDuckGoTools
import tweepy

import os
from dotenv import load_dotenv

load_dotenv()

#App-Setup...................................
app = Flask(__name__, static_url_path='/static')

# API Integration............................
gemini_api_key = os.getenv("GEMINI_API_KEY")

if gemini_api_key:
    os.environ["GOOGLE_API_KEY"] = gemini_api_key

API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

# Agno agents setup...........................
ws_agent = Agent(
    name="Web Search Agent",
    role="Search the web for trending Twitter/X topics.",
    model=Gemini(id="gemini-2.5-flash"),
    instructions="Provide the collected content in a short format suitable for a tweet.",
    tools=[DuckDuckGoTools()],
    show_tool_calls=False,
    markdown=True
)

tweet_agent = Agent(
    name="Tweet Generator Agent",
    role="Craft engaging tweets based on provided content.",
    model=Gemini(id="gemini-2.5-flash"),
    instructions="Generate a tweet under 250 characters in a human-like, engaging style with relevant hashtags.",
    show_tool_calls=False,
    markdown=True
)

agent_team = Agent(
    team=[ws_agent, tweet_agent],
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "First, Web Search Agent finds trending topics in India.",
        "Then, Tweet Generator Agent converts it to a short, catchy tweet.",
        "Include relevant hashtags. Provide only the tweet as final output."
    ],
    show_tool_calls=False,
    markdown=True
)

client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)


# Route: Home
@app.route('/')
def home():
    return render_template('index.html')

# Route: Generate Tweet
@app.route('/generate', methods=['POST'])
def generate():
    try:
        response = agent_team.run("What's trending in India today? Write a tweet under 250 characters.")
        if hasattr(response, 'content') and response.content:
            tweet = response.content.strip()[:250]
            return jsonify({'success': True, 'tweet': tweet})
        else:
            return jsonify({'success': False, 'error': 'Failed to generate tweet'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Route: Post Tweet
@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    tweet = data.get('tweet')

    try:
        client.create_tweet(text=tweet)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)