# Project---Nutrition-Paradox-A-Global-View-on-Obesity-and-Malnutrition
Imagine you are a Data Analyst working for a global health organization. Your task is to investigate the complex challenge of undernutrition and overnutrition across different countries, age groups, and genders. You will use publicly available WHO data to uncover trends, patterns, and disparities in obesity and malnutrition rates around the world.

 **Domain: Public Health / Epidemiology / Global Health Statistics**
 
This dataset appears to be focused on obesity statistics across different countries, segmented by demographic factors and statistical measures.

| Column Name        | Description                                                                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Region**         | Geographical region classification (e.g., Asia, Europe, Africa) as defined by WHO or another global body.                                                                         |
| **Gender**         | Biological sex of the population segment: typically **Male**, **Female**, or **Both**.                                                                                            |
| **Year**           | The year when the data was recorded or estimated.                                                                                                                                 |
| **LowerBound**     | Lower limit of the **confidence interval** for the estimate – gives the minimum expected value within statistical confidence.                                                     |
| **UpperBound**     | Upper limit of the **confidence interval** – gives the maximum expected value.                                                                                                    |
| **Mean\_Estimate** | The **average obesity rate** (often in %) for the given group (region, gender, year, etc.).                                                                                       |
| **Country**        | The specific country to which the data applies.                                                                                                                                   |
| **age\_group**     | The age bracket of the population (e.g., 18–25, 30–49 years).                                                                                                                     |
| **CI\_Width**      | **Confidence Interval Width** = UpperBound − LowerBound. Shows the uncertainty in the estimate.                                                                                   |
| **obesity\_level** | Could be a **categorical label** based on Mean\_Estimate (e.g., Low, Moderate, High obesity). May be derived using thresholds (e.g., <20% = Low, 20–30% = Moderate, >30% = High). |


Typical Use Cases

----> Policy-making: Governments use this to plan healthcare interventions.

----> Public Health Research: To analyze obesity trends over time and across regions.

----> Statistical Modeling: To predict future obesity rates or compare regions/countries.

----> Health Inequality Analysis: By comparing gender, age, and geography.
