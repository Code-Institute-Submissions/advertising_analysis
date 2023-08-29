# JWS Advertising Analysis App

Open a new terminal and <code>pip3 install -r requirements.txt</code>

In the terminal type <code>pip3 install jupyter</code>

In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start jupyter server.

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.
2. Click the button Not Trusted and choose Trust.

In the terminal type <code>streamlit run app.py</code>

Deployment on Heroku

1.  <code>heroku login -i</code>
2.  Email & API Key
3.  <code>heroku stack:set heroku-20 -a jws-advertising-analysis</code>

<https://jws-advertising-analysis-576a7866f352.herokuapp.com/>

## Business Requirements

JWS is an emerging startup in its initial stages, specializing in
providing comprehensive programs focused on cutting-edge technologies.
These programs facilitate upskilling for students and professionals.

**Challenge**

The company aims to efficiently identify high-potential leads from
the generated leads, crucial for effective resource allocation.

**Objectives**

- **Develop an ML Model:** Create a model to predict leads likely
to convert into paying customers accurately.

- **Understand Conversion Factors:** Gain insights into critical
factors influencing lead conversion for informed decisions.

- **Create Lead Profiles:** Generate detailed profiles of leads
with higher potential to tailor effective engagement strategies.

**Approach**

- **Data Overview:** Analyze available data comprehensively to
understand its nature and structure.

- **Exploratory Data Analysis (EDA):** Uncover patterns, correlations,
and insights through univariate and bivariate analysis.

- **Model Evaluation:** Assess Decision Tree and Random Forest models
to predict lead conversions effectively.

JWS seeks to enhance lead management, optimize resource allocation,
and improve lead conversion rates through this approach.


## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision validating it (them).


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.


## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

