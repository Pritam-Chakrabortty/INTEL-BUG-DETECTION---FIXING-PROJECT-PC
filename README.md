# **Intel Bug Detection & Fixing Project**

## **📌 Overview**
This project is designed to detect and fix bugs in code using AI-powered techniques. Users can enter any random code, and the model will analyze, detect bugs, and suggest fixes. The application is built using Python and runs in VS Code.

## **🚀 Features**
- ✅ Automatic bug detection
- 🤖 AI-powered bug fixing using the Gemini API
- 🖥️ User-friendly interface for inputting code
- ⚡ Real-time error detection and correction

## **🛠 Tech Stack**
### **Frontend:**
- HTML, CSS, JavaScript
- Flask (for rendering frontend templates)

### **Backend:**
- Python
- Flask (for API handling)
- Google Gemini-2.0-Flash Model

### **Deployment:**
- Google Colab (for model training)
- Render (for live deployment)

## **🌍 Live Demo**
🔗 **[Intel Bug Detection & Fixing Project](https://intel-bug-detection-fixing-project-pc-2.onrender.com)**

## **📁 Project Structure**
```
INTEL-BUG-DETECTION---FIXING-PROJECT-PC/
│── __pycache__/             # Compiled Python files
│── static/                  # Static assets (images, downloads)
│   │── images/
│── templates/               # HTML templates
│   │── index.html
│── app.py                   # Main application file
│── bug_fixer.py             # Bug detection and fixing logic
│── requirements.txt         # Dependencies list
│── .env                     # Environment variables file
│── README.md                # Project documentation
│── demo.mp4                 # Demo video
│── Documentation.pdf        # Project report/documentation
│── Presentation.pptx        # Project presentation slides
│── .gitignore               # Git ignore file
│── LICENSE                  # License file
```

## **⚡ Installation**
### **Prerequisites**
Ensure you have the following installed:
- Python 3.x
- VS Code
- Pip (Python package manager)

### **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/Pritam-Chakrabortty/INTEL-BUG-DETECTION---FIXING-PROJECT-PC.git
   cd INTEL-BUG-DETECTION---FIXING-PROJECT-PC
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the environment variables:
   - Open the `.env` file in the root directory.
   - Update the values as needed. Example:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   - Save the file.
4. Run the application:
   ```bash
   python app.py
   ```
5. Open a browser and navigate to:
   ```
   http://localhost:5000
   ```

## **🎯 Usage**
1. **Select a Programming Language:** Choose Python, C, Java, or JavaScript from the dropdown menu.
2. **Enter Code:** Paste the buggy code into the input field.
3. **Click 'Detect & Fix Bug':** The AI model analyzes the code and suggests fixes.
4. **View the Fixed Code:** The corrected code will appear in the result section.
5. **Download Fixed Code:** You can copy or download the corrected version.

## **🔗 API Endpoints**
- `POST /detect` - Detects bugs in the provided code.
- `POST /fix` - Returns a fixed version of the provided buggy code.

## **📹 Demo Video**
📺 **[Watch the Demo](https://github.com/Pritam-Chakrabortty/INTEL-BUG-DETECTION---FIXING-PROJECT-PC/raw/refs/heads/main/demo.mp4.mp4)**

## **📄 Project Documentation**
📄 **[Download Documentation](https://github.com/Pritam-Chakrabortty/INTEL-BUG-DETECTION---FIXING-PROJECT-PC/raw/refs/heads/main/Bug_Detection_and_Fixing%5B1%5D.docx)**

## **🎤 Presentation**
📊 **[View Presentation](https://github.com/Pritam-Chakrabortty/INTEL-BUG-DETECTION---FIXING-PROJECT-PC/raw/refs/heads/main/Intel_Bug_Detection_Fixing_Project_Presentation(P.C).pptx)**

## **📈 Future Enhancements**
- Implementing a CI/CD pipeline for real-time feedback
- Enhancing bug detection accuracy with more training data
- Adding unit testing for improved reliability

## **🤝 Contributing**
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first.

## **📝 License**
This project is licensed under the MIT License.

## **📞 Contact**
- **Author:** Pritam Chakrabortty  
- **GitHub:** [Pritam-Chakrabortty](https://github.com/Pritam-Chakrabortty)  
- **Email:** bwubta22388@brainwareuniversity.ac.in

