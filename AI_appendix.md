# AI Use Appendix

## Use of Generative AI

Generative AI tools were used as a development assistant during this project. 
AI was primarily used to support the development of the Streamlit application and to assist with debugging Python code. 

## Streamlit Application Development

AI was used to convert the analysis and functions developed in the Jupyter Notebook into a Streamlit application. A project-specific `notebook-to-streamlit` skill was created to guide this process and ensure that the existing notebook logic was preserved when developing the application.

The following prompt was used to generate the Streamlit application:

> Convert the Rosa’s Pizza Jupyter Notebook analysis into a Streamlit app 
> (`app.py`) using the `notebook-to-streamlit` skill. Use the existing notebook 
> functions and calculations. Let the user select a zone and time block, set the 
> minimum and maximum promises to test in 5-minute increments, and adjust profit 
> margin, churn, and refund cost, using the imported values as defaults. A 
> “Find Best Promise” button should run the existing optimization and display the 
> recommended promise and net profit. Keep the result in `session_state`, use a 
> consistent simulation seed, validate the promise range, and keep the app simple 
> and focused on the assignment requirements.

AI-generated code was reviewed and tested to ensure that the Streamlit  application remained consistent with the calculations and functions developed in the Jupyter Notebook.

## Debugging Assistance

AI was also used as a coding assistant throughout the project to help identify and resolve errors in the Python code. This included explaining error messages, identifying potential causes of errors, and suggesting corrections to the code.

AI assistance was particularly useful for debugging issues involving list and NumPy array handling, dictionary keys, and differences in results caused by the randomness of the delivery-time simulator. Suggested solutions were reviewed 
before being incorporated into the project.

