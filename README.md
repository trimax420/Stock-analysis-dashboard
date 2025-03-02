# Air Route Suggestion System

A Django-based web application that provides intelligent suggestions for air routes, airport feasibility, and route analysis based on geographic and economic data.

## Overview

The Air Route Suggestion System (also known as SAD 2.0) helps airlines and aviation planners make data-driven decisions about:

1. **Route Availability Check**: Determine if a direct route exists between two cities
2. **Airport Availability**: Check if a city has an existing airport
3. **Airport Demand Analysis**: Predict if a city can support an airport based on population and GDP
4. **Distance-based Route Feasibility**: Analyze if a direct route, connecting flight, or land transport is more suitable based on distance

## Features

- **Route Analysis**: Check if direct routes exist between two cities
- **Airport Availability**: Verify if a city has an existing airport
- **Demand-based Airport Planning**: Use machine learning to predict if a city can sustain an airport based on economic and demographic factors
- **Distance-based Recommendations**: Suggest the most appropriate transportation mode based on distance analysis
- **Data-driven Decision Making**: Leverages real-world aviation data including routes, demand, population, and GDP figures

## Dataset Information

The system uses multiple datasets:
- `data_new.csv`: City information including population, coordinates, GDP, and airport availability
- `routes.csv`: Existing air routes between cities
- `routeswithdist.csv`: Route information with calculated distances
- `fromdemand.csv` & `todemand.csv`: Demand data for flights from and to various cities

## Technologies Used

- **Backend**: Django 4.1
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (Decision Tree Regressor)
- **Frontend**: Bootstrap
- **Deployment**: Vercel

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/air-route-suggestion-system.git
   cd air-route-suggestion-system
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Django development server:
   ```
   python manage.py runserver
   ```

4. Access the application at `http://127.0.0.1:8000/`

## Project Structure

```
.
├── app/                # Django app configuration
│   ├── settings.py     # Django settings
│   ├── urls.py         # Main URL routing
│   └── wsgi.py         # WSGI configuration
├── dataset/            # Data files
│   ├── data_new.csv    # City information
│   ├── fromdemand.csv  # Origin demand data
│   ├── routes.csv      # Route information
│   ├── routeswithdist.csv # Routes with distance calculations
│   └── todemand.csv    # Destination demand data
├── route/              # Main application module
│   ├── forms.py        # Form definitions
│   ├── models.py       # Data models
│   ├── urls.py         # URL routing for the app
│   └── views.py        # View controllers
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
│   ├── airport.html    # Airport availability page
│   ├── demand.html     # Airport demand check page
│   ├── distance.html   # Distance-based feasibility page
│   └── index.html      # Home page
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── vercel.json         # Vercel deployment configuration
```

## Usage

1. **Route Check**:
   - Select departure and arrival cities
   - The system will check if a direct route exists

2. **Airport Availability**:
   - Select a city
   - The system will verify if an airport exists in that city

3. **Airport Demand Check**:
   - Enter city population and GDP
   - The system will predict if the city can sustain an airport

4. **Distance-based Route Feasibility**:
   - Enter coordinates for departure and arrival locations
   - The system will recommend the most suitable transportation mode

## Deployment

The application is configured for deployment on Vercel. The `vercel.json` file includes the necessary configuration.

To deploy:
1. Make sure you have the Vercel CLI installed
2. Run `vercel` from the project directory
3. Follow the prompts to complete the deployment

## Machine Learning Model

The system uses a Decision Tree Regressor to predict airport feasibility based on:
- Population size
- GDP per city

The model is trained on existing cities' data with known airport availability status.

## Project Background

This project (SAD 2.0) was developed by the SAD 2.0 team as a submission for the R2 Data Labs Hackathon. The system demonstrates how data science and machine learning techniques can be applied to optimize air travel planning and infrastructure development decisions.
