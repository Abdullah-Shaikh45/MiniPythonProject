import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re

# Step 1: Load .env and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# Step 2: Create model and prompt
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = """
Generate a complete step-by-step roadmap to learn Python programming.
Return only valid pure JSON (NO markdown code blocks like ```json), with this structure:
{
  "title": "Python Roadmap",
  "steps": [
    { "title": "Step 1: ...", "description": "..." },
    ...
  ]
}
"""

response = model.generate_content(prompt)

# Step 3: Clean and parse JSON
text = response.text.strip()
cleaned_text = re.sub(r"^```json|^```|```$", "", text, flags=re.MULTILINE).strip()

try:
    roadmap = json.loads(cleaned_text)

    # Step 4: Save to file
    with open("python_roadmap.json", "w") as f:
        json.dump(roadmap, f, indent=4)
    print("JSON saved to 'python_roadmap.json'")

    # Step 5: Print it beautifully
    print(f"\n📘 {roadmap['title']}\n" + "="*50)
    for step in roadmap["steps"]:
        print(f"\n{step['title']}\n{step['description']}\n" + "-"*50)

except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)
    print("Raw Response:\n", cleaned_text)
