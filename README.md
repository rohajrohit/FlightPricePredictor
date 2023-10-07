# Flight Price Predictor


Welcome to the Flight Price Predictor, a user-friendly web application that predicts the cost of your flight journey based on various input parameters such as source, destination, stoppages, airline company, and departure/arrival details.

![Flight Price Predictor Demo](demo.gif)

## Table of Contents

- [Getting Started](#getting-started)
- [Screenshot](#screenshot)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Getting Started

To get started with Flight Price Predictor, follow these simple steps:
   

1. Clone the repository to your local machine:

       git clone https://github.com/rohajrohit/FlightPricePredictor.git
2.Navigate to the project directory:

    cd FlightPricePredictor
    
3.Install the required dependencies using pip:

    pip install -r requirements.txt

## Screenshot

Here are some screenshots of the model after predicting the price:

   <img src='FlightPredictorImage/Screenshot (351).png' >
  <img src='FlightPredictorImage/Screenshot (354).png' >

## Usage
Run the Flight Price Predictor:

    streamlit run app.py
Access the application in your web browser via the provided link.

Input your flight details:
Select the source and destination.
Choose the number of stoppages between them.
Pick the airline company for your flight.
Enter the departure and arrival dates.
Specify the departure and arrival times.

Click the "Predict Price" button to obtain the predicted flight price.


## Project Structure

The project is structured as follows:
- `app.py`: Main Streamlit application code.
- `rf_random.pkl`: Trained Random Forest model for flight price prediction.
- `df.pkl`: Preprocessed data for feature engineering.

## Dependencies

The Flight Price Predictor relies on the following key dependencies:
- Streamlit: A Python library for creating web applications.
- Scikit-learn: Machine learning library for Python.
- Pandas: Data manipulation and analysis library.
- NumPy: Numerical computing library.

## Acknowledgments

We'd like to express our gratitude to the Streamlit, Scikit-learn, Pandas, and NumPy communities for their invaluable open-source contributions and support.

## Contact

If you have any questions, suggestions, or need assistance, please feel free to reach out.Please open an issue on the GitHub repository or contact us at rohitrajcricketer@gmail.com
