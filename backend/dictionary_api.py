from groq import Groq

client = Groq(api_key="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")  # Replace with your actual, valid API key

def get_word_details(word):
    try:
        prompt = f"Provide a dictionary entry for the word '{word}' including meaning, synonyms (with example sentences), antonyms (with example sentences), and usage example."
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        content = response.choices[0].message.content
        lines = content.split('\n')
        details = {
            "word": word,
            "meaning": next((line.split(': ')[1] for line in lines if line.startswith("Meaning")), "Not found"),
            "synonyms": [
                {"word": s.split(' (')[0], "example": s.split(' (')[1].rstrip(')')}
                for s in next((line.split(': ')[1].split(', ') for line in lines if line.startswith("Synonyms")), [])
            ],
            "antonyms": [
                {"word": a.split(' (')[0], "example": a.split(' (')[1].rstrip(')')}
                for a in next((line.split(': ')[1].split(', ') for line in lines if line.startswith("Antonyms")), [])
            ],
            "usage": next((line.split(': ')[1] for line in lines if line.startswith("Usage")), "Not found")
        }
        return details
    except Exception as e:
        return {"error": f"Failed to fetch details: {str(e)}"}