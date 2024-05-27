#  "AI Pharma Insights: Prescription Analysis and Drug Recommendation"

 "AI Pharma Insights:  is a powerful tool for analyzing prescription drug data using artificial intelligence and machine learning techniques. By leveraging advanced algorithms and interactive visualization, PrescriptionAI aims to provide valuable insights into drug prescriptions, optimize treatment recommendations, and enhance patient care.

## Algorithm Explanation

### Data Loading and Initial Exploration:

- Load the dataset and print its shape.
- Print the first few rows to understand the structure.
- Count unique drugs and conditions.
- Determine the date range of the data collection.

### Descriptive Statistics:

- Summarize numerical columns like rating and usefulCount.
- Identify drugs with zero useful counts and analyze them.

### Data Cleaning:

- Check for missing values and drop rows with missing condition.

### Data Visualization:

- Plot distributions of rating and usefulCount.
- Plot the relationship between rating and usefulCount.

### Text Processing:

- Remove punctuation, stopwords, and numbers from the reviews.
- Calculate sentiment scores using NLTK's VADER.

### Feature Engineering:

- Scale ratings to create an effective score (eff_score).
- Calculate a usefulness score combining rating, useful count, and effective score.

### Interactive Analysis:

- Use ipywidgets to create interactive visualizations for conditions.

### Advanced Analysis:

- Visualize the relationship between conditions and effective drug counts.
- Identify the most common conditions and the most useful drugs.
- Find the highest and lowest rated drugs for each condition.

## Features

- **Data Analysis**: Analyze prescription drug data to identify patterns, trends, and correlations.
- **AI-driven Insights**: Utilize machine learning algorithms to uncover valuable insights and recommendations.
- **Interactive Visualization**: Visualize prescription data through interactive charts and graphs for intuitive exploration.
- **Personalized Recommendations**: Generate personalized treatment recommendations based on patient history and condition.
- **Scalable Architecture**: Built on scalable architecture to handle large datasets and ensure fast processing.

## Technology Stack

- **NumPy**: Used for numerical operations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualization.
- **ipywidgets**: For interactive widgets in Jupyter notebooks.
  
## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/PrescriptionAI.git
   ```
2. Install dependencies
    ```
    pip install -r requirements.txt
    ```
3. Run the Application
   ```
   python app.py
    ```
# API Endpoints

## Drug Information

### GET `/drug_info`

Retrieve drug information based on the provided condition.

#### Parameters

- `condition` (required): The medical condition for which drugs are to be retrieved.

#### Response

- Status: 200 OK
- Content: JSON object containing drug information with the following fields:
  - `drugName`: Name of the drug
  - `usefulness_score`: Usefulness score of the drug for the provided condition
###Example
Request :

GET /usage_stats?drug_name=Drug A

Response:

```json
[
    {
        "drugName": "Drug A",
        "usefulness_score": 8.5
    },
    {
        "drugName": "Drug B",
        "usefulness_score": 7.2
    },
    ...
]
 ```
### Error Handling:
If a request is made with missing or invalid parameters, the API will respond with an appropriate error message and status code.

- Status: 400 Bad Request
- Content: JSON object containing an error message
### Example Error Response:

```
{
    "error": "Missing required parameter: condition"
}
  ```
## Usage

1. Upload prescription data in CSV format.
2. Explore various analysis and visualization options.
3. Generate insights and recommendations based on the analyzed data.
4. Save and export results for further use.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/yourfeature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/yourfeature`).
5. Create a new Pull Request.


## Contact

For inquiries or support, please contact [Mahendran R](mailto:mahendran.06335@gmail.com).

