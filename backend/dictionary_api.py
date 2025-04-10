from groq import Groq

client = Groq(api_key="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")  # Replace with your actual, valid API key

def get_word_details(word):
    try:
        # Refined prompt for consistent, structured output
        prompt = f"Provide a dictionary entry for the word '{word}' in this exact format:\n" \
                 f"Meaning: [definition]\n" \
                 f"Synonyms: [syn1 (example sentence), syn2 (example sentence)]\n" \
                 f"Antonyms: [ant1 (example sentence), ant2 (example sentence)]\n" \
                 f"Usage: [example sentence using '{word}']"
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        content = response.choices[0].message.content.strip()
        print(f"Raw Groq response for '{word}':\n{content}")  # Debug: Log raw response

        # Split the response into lines
        lines = content.split('\n')
        
        # Helper function to extract value after a label
        def extract_value(label, default="Not found"):
            for line in lines:
                if line.startswith(label):
                    value = line[len(label):].strip()
                    return value if value else default
            return default

        # Helper function to parse synonyms/antonyms with examples
        def parse_items(text):
            if not text or text == "Not found":
                return []
            items = text.split(', ')
            result = []
            for item in items:
                if '(' in item and ')' in item:
                    word, example = item.split(' (', 1)
                    example = example.rstrip(')')
                    result.append({"word": word.strip(), "example": example.strip()})
                else:
                    result.append({"word": item.strip(), "example": "No example provided"})
            return result

        # Extract and parse the data
        meaning = extract_value("Meaning: ")
        synonyms_raw = extract_value("Synonyms: ")
        antonyms_raw = extract_value("Antonyms: ")
        usage = extract_value("Usage: ")

        details = {
            "word": word,
            "meaning": meaning,
            "synonyms": parse_items(synonyms_raw),
            "antonyms": parse_items(antonyms_raw),
            "usage": usage
        }
        return details
    except Exception as e:
        return {"error": f"Failed to fetch details: {str(e)}"}