# My solution
This is my solution to the take-home task. The assessment showcases my ability to build a reliable and scalable backend with an accompanying relational database.


## What did you choose to focus on, and why?
Given the limited time, I decided to focus on the reliability of the API and database. This meant prioritizing error handling and ensuring that loaded data follows the database rules, so users can only retrieve the metric they want by its ID.

I focused on reliability because, with the time constraints and limited scope of the test, I did not want to add features that might not align with the business value of the system. Additionally, the provided data was not very clear regarding its references or intended use. The sample data was small, so I worked with what was available to ensure the system can validate both the provided data and any new data that follows the same structure.

I also focused on readability and modularity, so the project can be easily expanded and provide a platform for integrating potential future features listed in the README.

## What would you do next if you had more time?
If I had more time, I would definitely include security features. I would add JWT authorization to the metric endpoint so only authorized users can view the metrics.

Furthermore, I would add more detailed OpenAPI documentation. I relied on the Pydantic models for this, but I would like to include sample data as examples.

Additionally, I would add more endpoints to allow more flexible database queries, such as selecting a time range for metrics, deleting metrics, and retrieving multiple metrics from a single endpoint.

## Anything you'd like us to know while reviewing your work.

There is no data or table provided for the queries in queries.csv. Therefore, there is no way for me to demonstrate the system working end-to-end as described in the project tasks. I have only been able to test this through mocks in my tests. As a result, I am not sure how to create a Loom video to showcase my solution.

## Include a quick [Loom video](https://www.loom.com/) showcasing the solution

N/A