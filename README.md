# Shelf Life Prediction System

This project predicts the shelf life of perishable items using a combination of the **Arrhenius equation** (scientific modeling of spoilage processes) and a **VGG16-based classification model** for detecting freshness levels. The system enables real-time predictions of freshness and remaining shelf life based on environmental conditions like temperature.


# The Role of the Arrhenius Equation

The Arrhenius equation is key to understanding the relationship between temperature and reaction rates, which directly impacts the spoilage of perishable goods. Here's how it works in the context of shelf life:
   ![Alt text](https://cdn1.byjus.com/wp-content/uploads/2015/12/Arrhenius-Equation-1.png "Optional title")


---

## Features

- **Freshness Classification**:
  - Uses a fine-tuned **VGG16 model** to classify the freshness of perishable items into categories (e.g., Fresh, Moderately Fresh, Spoiled).
  
- **Shelf Life Estimation**:
  - Implements the **Arrhenius equation** to calculate the time remaining until spoilage under given temperature conditions.

- **Integration**:
  - Combines freshness classification with scientific modeling for accurate shelf life predictions.

---

## Project Structure

```plaintext
app/
├── model/
│   ├── New2Freshness50...  # Trained VGG16 model file for freshness classification
├── templates/
│   ├── index.html          # UI template for interacting with the application
├── __init__.py             # Flask application initialization
├── helpers.py              # Contains the Arrhenius equation logic
├── models.py               # Defines the structure for working with the trained model
├── routes.py               # Defines API routes for freshness and shelf life prediction
.env                        # Environment variables
.gitignore                  # Files to be ignored by Git
config.py                   # Configuration settings
README.md                   # Documentation
requirements.txt            # Python dependencies
wsgi.py                     # WSGI entry point for deployment
