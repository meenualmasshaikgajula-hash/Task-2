# Task-2
# Tableau Data Visualization & Storytelling - Sample Superstore

This project uses Tableau to create data visualizations and a storytelling interface based on the SampleSuperstore_cleaned.csv dataset. The goal is to extract business insights, understand sales and profitability patterns, and present findings through an interactive dashboard and story.

## Dataset

- File: SampleSuperstore_cleaned.csv
- Fields include:
  - Order Date, Ship Date, Sales, Profit, Discount
  - Category, Sub-Category, Region, State, City
  - Customer Name, Segment, Ship Mode

## Objectives

- Analyze trends in sales and profits by time and geography.
- Identify top-performing and underperforming sub-categories.
- Investigate how discounting affects profitability.
- Create a functional and visually appealing dashboard.
- Develop a data story to communicate key findings.

## Tools Used

- Tableau Desktop or Tableau Public
- Cleaned CSV dataset

## Project Steps

### Step 1: Load Data
- Imported the CSV file into Tableau.
- Verified data types and structure.

### Step 2: Data Exploration
- Reviewed for missing or inconsistent data.
- Created calculated fields such as Profit Ratio.

### Step 3: Visualizations Created

| Visualization         | Purpose                                 |
|-----------------------|-----------------------------------------|
| Bar Chart             | Sales and profit by sub-category        |
| Map                   | Sales and profit distribution by state  |
| Line Chart            | Monthly sales trend                     |
| Scatter Plot          | Sales vs profit by category             |
| Bubble Chart          | Discount vs profit relationship         |
| Top N Customers       | Top 10 customers by sales               |

### Step 4: Dashboard Development
- Fixed dashboard size: 1200 x 800 pixels
- Used layout containers for clean structure
- Added filters for region and category
- Included tooltips and color legends for clarity

### Step 5: Storytelling
- Developed story with multiple points:
  - Executive Summary
  - Regional Performance
  - Seasonal Trends
  - Profitability Challenges
  - Strategic Recommendations

## Key Insights

- Furniture category shows frequent losses, especially in Tables.
- High discounts often result in negative profits.
- Western and Eastern regions are generally more profitable.
- Sales increase significantly during the fourth quarter.

## How to Access the Dashboard

1. Open Tableau Desktop or Tableau Public.
2. Import the Tableau workbook (.twb or .twbx).
3. Interact with filters and explore the story points.

## Files Included

| File Name                   | Description                          |
|----------------------------|--------------------------------------|
| SampleSuperstore_cleaned.csv | Dataset used for analysis            |
| Superstore_Analysis.twbx   | Tableau Packaged Workbook (optional) |
| README.md                  | Project documentation                |
