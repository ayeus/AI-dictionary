from groq import Groq
import random

client = Groq(api_key="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")  # Replace with your actual, valid API key

def get_daily_word():
    try:
        prompt = "Suggest a random English word suitable for daily learning with a brief explanation."
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        content = response.choices[0].message.content
        return content.split()[0]  # Extract the first word
    except Exception as e:
        return {"error": f"Failed to fetch daily word: {str(e)}"}