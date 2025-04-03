import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("API Key not found. Make sure to set it in the .env file.")

genai.configure(api_key=GEMINI_API_KEY)
def detect_and_fix_bug(language, code):
    prompt = f"""
    You are an expert in {language} programming. Your task is to:
    1. **Identify bugs** in the given code.
    2. **Categorize the errors** (Syntax, Logical, Runtime, etc.).
    3. **Provide a correct fixed version** that is **fully executable**.
    4. **Explain each fix clearly**.

    ### Given Code:
    ```{language}
    {code}
    ```

    ### Output Format:
    - **Bug Identification:**
        - **Type of Error:** [Error Type]
        - **Explanation:** [Why the error occurs]
    
    - **Fixed Version:**
    ```{language}
    [Corrected code here]
    ```

    - **Explanation of Fix:**
        - [Describe the exact changes made]
    
    - **Expected Output (after fix):**
        - [The correct expected output of the fixed code]
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    return response.text