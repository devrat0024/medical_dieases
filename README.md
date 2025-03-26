# Cancer Treatment Recommendation System
##  Project Overview
This is a **Flask-based web application** that recommends cancer treatments based on the **cancer type** and **stage** entered by the user. The system uses a JSON file as a knowledge base for storing treatment recommendations.

---

##  Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** JSON (for storing treatment recommendations)

---

##  Features
- **User-friendly interface** to input cancer type and stage
- **Dynamic treatment recommendation** based on JSON data
- **Flask API** to process and return treatment suggestions
- **Scalable JSON-based knowledge base**

---

##  Project Structure
```
Cancer-Treatment-Recommendation/
│-- static/
│   ├── style.css  # Frontend styling
│-- templates/
│   ├── index.html  # User Interface
│-- treatments.json  # Knowledge Base (Treatment Data)
│-- app.py  # Flask Application
│-- README.md  # Project Documentation
```

---

##  Installation & Setup
### 1 Clone the Repository
```bash
git clone https://github.com/your-username/Cancer-Treatment-Recommendation.git
cd Cancer-Treatment-Recommendation
```

### 2 Install Dependencies
```bash
pip install flask
```

### 3 Run the Flask App
```bash
python app.py
```

### 4 Open in Browser
Visit **`http://127.0.0.1:5000/`** to access the web interface.

---

##  JSON Knowledge Base (treatments.json)
The knowledge base stores treatments in the following format:
```json
{
    "lung_cancer": {
        "1": "Surgery and regular monitoring",
        "2": "Radiation therapy and chemotherapy",
        "3": "Targeted therapy and immunotherapy"
    }
}
```
To add more treatments, simply modify `treatments.json`.

---

##  API Endpoints
| Endpoint          | Method | Description |
|------------------|--------|-------------|
| `/`              | GET    | Renders the homepage |
| `/get_treatment` | POST   | Returns treatment based on user input |

---

##  Future Enhancements
- Integrate Machine Learning for smarter recommendations
- Add a database (MySQL/PostgreSQL) for large-scale data handling
- Enhance UI with Bootstrap or TailwindCSS

---

##  Contributing
Feel free to submit issues and pull requests to improve the project.

---

##  License
This project is licensed under the **MIT License**.

---

##  Author
Developed by **Devvrat Shukla** 

