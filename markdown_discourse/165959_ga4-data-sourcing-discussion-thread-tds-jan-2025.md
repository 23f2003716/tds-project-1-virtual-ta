# GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1

## Topic Metadata
- **ID**: 165959
- **Slug**: ga4-data-sourcing-discussion-thread-tds-jan-2025
- **Created**: 2025-01-31T16:13:36.376Z
- **Views**: 1234
- **Replies**: 271
- **Likes**: 81
- **Tags**: announcement, term1-2025, graded-assignment, week-4

## Original Post
**Author**: Anand S
**Posted**: 2025-01-31T16:13:36.640Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1

Please post any questions related to [Graded Assignment 4 - Data Sourcing](https://exam.sanand.workers.dev/tds-2025-01-ga4).

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline: Sunday, February 9, 2025 6:29 PM

@Jivraj @Saransh_Saini @carlton

---

## Reply 1
**Author**: Anand S
**Posted**: 2025-01-31T16:14:00.363Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/2

*No content*

---

## Reply 2
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-01T07:54:31.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/3

**Image: Screenshot 2025-02-01 132301**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a snippet of JSON data and an error message. The JSON data is presented within a rounded-corner box, suggesting it's part of a user interface element. The error message is displayed below the JSON data.

**2. Any text content visible:**

*   **Question:** "What is the JSON data?"
*   **JSON Data:**
    *   `"id": "tt7144296",`
    *   `"title": "1. Kiss and Kill",`
    *   `"year": 2017,`
    *   `"rating": 2.9`
    *   `},`
*   **Error Message:** "Error: Expected: 2.9 Actual: 2.9"

**3. The context or purpose of what's displayed:**

The image likely represents a scenario where a user is being asked to identify or provide JSON data. The error message suggests a comparison or validation process is taking place. The system expected a certain value (2.9) and the actual value received was also 2.9, yet an error is still being displayed. This could indicate a problem with the validation logic, data type mismatch, or a more complex comparison issue.

**4. Technical details if it's a code screenshot or technical diagram:**

*   The JSON data represents a structured data format, likely describing a movie or similar item. The fields include an ID, title, year, and rating.
*   The error message indicates a potential issue with data validation or comparison. The fact that the "Expected" and "Actual" values are identical suggests a bug in the validation logic or a misunderstanding of the data type. It's possible the system is expecting a string representation of the number, or there's a precision issue.

what is the error here?? sir @Jivraj

---

## Reply 3
**Author**: Vikram Jeet
**Posted**: 2025-02-01T18:26:06.664Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/5

I have the Same doubt.

---

## Reply 4
**Author**: Anand S
**Posted**: 2025-02-02T05:30:16.417Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/6

@22f3001315 @21f3002277 @24ds2000024 – please try again after reloading the page. The new error message will be clearer, like this:

Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4

FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.

---

## Reply 5
**Author**: Sakthivel S
**Posted**: 2025-02-02T05:41:42.494Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/7

In Question 2, it is specifically said to filter the movies however, the evaluator is expecting a TV show there. Should we also include TV shows now?

edit:  This is an everchanging dataset, so will our answers be saved, as, this json might not be in this order tomorrow?

---

## Reply 6
**Author**: Anand S
**Posted**: 2025-02-02T05:45:48.804Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/8

@23f2000237 A good point. Yes, please include *all* titles. I’ve reworded the question accordingly. Thanks.

---

## Reply 7
**Author**: VIKASH PRASAD
**Posted**: 2025-02-02T06:31:48.149Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/9

Q3. How to handle the error ? @Jivraj

TypeError: Cannot read properties of null (reading ‘0’)

http://127.0.0.1:8000/api/outline?country=Russia

{"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}

error resolved

---

## Reply 8
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-02T10:06:04.746Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/11

in my output which is correct

there are two \n instead of one .

---

## Reply 9
**Author**: VIKASH PRASAD
**Posted**: 2025-02-02T10:38:33.945Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/12

it should one(for newline), my code is working now

---

## Reply 10
**Author**: Vikram Jeet
**Posted**: 2025-02-02T11:54:35.123Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/13

Dear Sir,

I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB question.

---

## Reply 11
**Author**: VIKASH PRASAD
**Posted**: 2025-02-02T13:00:36.181Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/14

Q4. How to handle the error ? @Jivraj

Error: At 2025-02-05: Values don’t match

---

## Reply 12
**Author**: K Hari Prasath
**Posted**: 2025-02-03T00:37:01.721Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/15

There is no submit button is available in below screen. Is it fine to save the link url only. Please clarify (unless we click submit button the log of Graded Assignment 4 remains red)

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a web browser displaying a course assignment page from an online learning platform. The platform appears to be associated with the Indian Institute of Technology (IIT) Madras. The page shows the details of "Graded Assignment 4" within a course module. The UI elements include a navigation menu on the left, the main content area displaying assignment details, and standard browser elements like the address bar, tabs, and system tray.

**2. Text Content:**

*   **Page Title:** "Graded Assignment 4 :: IITM On"
*   **Course Information:** "IIT Madras", "Jan 2025-TDS"
*   **Navigation Menu:**
    *   "Modules"
    *   "Grades"
    *   "Calc"
    *   "Course Introduction"
    *   "Module 1: Development Tools"
    *   "Module 2: Deployment Tools"
    *   "Module 3: Large Language Models"
    *   "Project 1"
    *   "Module 4: Data Sourcing"
    *   "Graded Assignment 4"
*   **Assignment Details:**
    *   "Graded Assignment 4"
    *   "Due date for this assignment: 2025-02-09, 23:59 IST."
    *   "You may submit any number of times before the due date. The final submission will be considered for grading."
    *   A list of potential causes for difficulty accessing the assignment, including:
        *   "Ad blockers need to be disabled/removed."
        *   "The site requires cookies for authentication. So any cookie blocking/tracker blocking extensions or software may prevent access."
        *   "Javascript is required for the site to work correctly."
        *   "Chrome Browser is the recommended software to access the contents."
        *   "Disable any browser extensions that may be interfere with the site from working correctly."
        *   "Overly aggressive anti-virus software may also cause similar access problems."
        *   "Corporate proxies and network policies may also cause access issues. Try and use your mobile internet or another network."
    *   "You must

---

## Reply 13
**Author**: Sakthivel S
**Posted**: 2025-02-03T10:06:13.753Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/16

I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in the assignment, would their mark be recored as 11/10 or just 10?

(Assuming they have interacted in this thread)

---

## Reply 14
**Author**: Anand S
**Posted**: 2025-02-03T11:16:46.279Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/17

Anyone scoring 10/10 on GA4 and replying with a *relevant* message on this thread will get 11/10  :slight_smile:

---

## Reply 15
**Author**: K Hari Prasath
**Posted**: 2025-02-03T11:38:10.970Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/18

For me I just made filter of rating between 2 and 7 in site and typed in console as per  video. with that data got in console worked fine.

copy the coding and save in place use it for data extract when finally submit

---

## Reply 16
**Author**: Maheshwar Ture
**Posted**: 2025-02-03T16:46:46.395Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/19

For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for a search filter section on a website or application. On the left side, there are search filter options. On the right side, there's a "No results found" message with a corresponding icon.

**2. Any text content visible:**

*   **Search filters:** This is the main heading for the filter section.
*   **Expand all:** A link or button to expand all filter options.
*   **Title name:** A filter option label.
*   **Un matrimonio di troppo:** Text entered in the "Title name" filter field.
*   **Title type:** Another filter option label.
*   **No results found:** A message indicating that the search with the current filters yielded no results.
*   **Please adjust your filters or start a new search:** A suggestion to the user to modify their search criteria.

**3. The context or purpose of what's displayed:**

The UI is designed to allow users to refine their search by applying filters. The "No results found" message indicates that the current filter settings are too restrictive or that there are no items matching the specified criteria. The user is prompted to adjust the filters or start a new search.

**4. Technical details:**

*   The UI elements include labels (e.g., "Title name," "Title type"), a text input field (containing "Un matrimonio di troppo"), and potentially expandable sections (indicated by the up arrow next to "Title name" and "Title type").
*   The "Expand all" link suggests that there are more filter options available that are currently collapsed.
*   The "No results found" message is accompanied by a magnifying glass icon with an "X" through it, visually reinforcing the lack of results.

---

## Reply 17
**Author**: Nilay Chugh
**Posted**: 2025-02-04T03:28:57.489Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/20

how to get the BBC weather API key?

---

## Reply 18
**Author**: Joel Jeffrey
**Posted**: 2025-02-04T05:47:12.930Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/21

Just a quick query on the Bonus mark.

Would this be added to the final grade? Say for example, Someone get a full score in the first 4 assignments. So the total comes up to 39.5/39.5, and would be converted to 0.15 or 15 marks. Would the bonus mark be additional to that 15 or would the score change to 40.5/39.5 and then get normalised to 15?

---

## Reply 19
**Author**: Anand S
**Posted**: 2025-02-04T06:15:20.501Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/22

@JoelJeffrey It will be added to the GA4 marks, not the final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the total.

---

## Reply 20
**Author**: Tushar Jalan 
**Posted**: 2025-02-04T07:43:14.240Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/23

you can go and login using your email id in this below mentioned link

[https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)

---

## Reply 21
**Author**: Joel Jeffrey
**Posted**: 2025-02-04T08:14:26.582Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/24

Error: At [10].year: Values don’t match. Expected: "2025– ". Actual: “2025–”

Can someone help me with this?

Thanks

Edit: Resolved

---

## Reply 22
**Author**: K Hari Prasath
**Posted**: 2025-02-04T09:44:51.731Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/25

Q8 I got the Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in. the .yml file contains the following

" name: Daily Commit

on:

schedule:

- cron: ‘0 12 * * *’ # Runs daily at 12:00 PM UTC

workflow_dispatch:  # This allows manual trigger

jobs:

commit:

runs-on: ubuntu-latest

steps:
- name: Checkout repository
  uses: actions/checkout@v2

- name: Make a dummy change with email 23f2003853@ds.study.iitm.ac.in in the commit
  run: |
    echo "This is a daily commit" > daily_commit.txt
    git config --global user.email "23f2003853@ds.study.iitm.ac.in"
    git config --global user.name "23f2003853"
    git add daily_commit.txt
    git commit -m "Daily commit from 23f2003853@ds.study.iitm.ac.in"
    git push"

@Jivraj can help me to fix the issue

---

## Reply 23
**Author**: Sakthivel S
**Posted**: 2025-02-04T14:53:18.679Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/26

Have a step with your email id as its name. (Instead of checkout repository)

Also make sure you give read and write permission so it commits without any error

---

## Reply 24
**Author**: Daksh Agarwal
**Posted**: 2025-02-04T16:03:52.872Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/27

name: Daily Commit

on:

schedule:

- cron: ‘0 0 * * *’  # Runs once a day at midnight UTC

workflow_dispatch:  # Allows manual triggering of the workflow

jobs:

commit:

runs-on: ubuntu-latest

steps:
- name: Checkout repository
  uses: actions/checkout@v3

- name: Make daily commit by 23f3000264@ds.study.iitm.ac.in
  run: |
    echo "Daily commit by 23f3000264@ds.study.iitm.ac.in" >> daily_commit.txt
    git add index.html
    git commit -m "Daily commit"
    git push
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

sir this is my code and im getting a error in this

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Input Field:** A rectangular box, likely a text input field, is highlighted with a red border. This suggests an error or issue related to the input within this field.
*   **Text Labels:** There are text labels above and below the input field, providing context and information.

**2. Text Content:**

*   **"Enter your repository URL (format: https://github.com/USER/REPO):"** This text acts as a prompt, instructing the user to enter a GitHub repository URL. The format example clarifies the expected structure of the URL.
*   **"https://github.com/dakshagarwal76/daily-update"** This is the user's input, representing a specific GitHub repository URL. It includes the username "dakshagarwal76" and the repository name "daily-update."
*   **"Error: No executed job step matches 23f3000264@ds.study.iitm.ac.in"** This is an error message indicating that a specific job step, identified by the email-like string "23f3000264@ds.study.iitm.ac.in," could not be found or matched.

**3. Context and Purpose:**

The image shows a user interface where a user is prompted to enter a GitHub repository URL. The system then validates or processes this URL. The error message suggests that the system is attempting to execute a job or process related to the repository, but it's failing because a specific job step is not found.

**4. Technical Details:**

*   The error message "No executed job step matches..." implies that there's a workflow or automated process associated with the GitHub repository. This workflow likely involves a series of steps or tasks.
*   The string "23f3000264@ds.study.iitm.ac.in" is likely an identifier or key associated with a specific job step within the workflow. The "@ds.study.iitm.ac.in" part suggests it might be related to a study or project at IIT Madras (IITM).
*   The error suggests a configuration issue or a missing component in the workflow definition. The system is expecting a job step with

---

## Reply 25
**Author**: Maheshwar Ture
**Posted**: 2025-02-04T16:15:39.892Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/28

dont remove the space after year- for example “year”: "2023- "

---

## Reply 26
**Author**: Ansh bansal
**Posted**: 2025-02-04T22:17:37.626Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/29

Please anyone help me in doing q1 , my doubt is when i open the website [Advanced search](http://www.imdb.com/search/title) , i have click on movies and then do the coding part if not how to select titles of the movies as there is no movies on the page.

---

## Reply 27
**Author**: Ansh bansal
**Posted**: 2025-02-04T23:37:55.943Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/31

In q4 i got this error someone pls expalin “Error: At root: Property name mismatch”

---

## Reply 28
**Author**: Tushar Jalan 
**Posted**: 2025-02-05T06:21:04.530Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/33

Student marks - Group 100

| Maths | Physics | English | Economics | Biology |
| ----- | ------- | ------- | --------- | ------- |
| 48    | 51      | 15      | 47        | 65      |
| 74    | 70      | 23      | 17        | 70      |
| 81    | 50      | 59      | 45        | 51      |
| 80    | 63      | 43      | 99        | 28      |
| 85    | 72      | 82      | 79        | 14      |
| 76    | 50      | 15      | 55        | 13      |
| 21    | 86      | 25      | 14        | 64      |
| 54    | 72      | 98      | 30        | 96      |
| 15    | 24      | 67      | 19        | 35      |
| 68    | 82      | 16      | 70        | 67      |
| 64    | 94      | 42      | 26        | 10      |
| 31    | 79      | 98      | 21        | 24      |
| 90    | 32      | 88      | 39        | 56      |
| 36    | 72      | 79      | 86        | 96      |
| 91    | 61      | 57      | 28        | 23      |
| 81    | 40      | 95      | 74        | 30      |
| 60    | 31      | 66      | 36        | 83      |
| 81    | 16      | 67      | 25        | 90      |
| 40    | 96      | 57      | 84        | 47      |
| 53    | 92      | 10      | 10        | 82      |
| 33    | 40      | 20      | 68        | 95      |
| 95    | 48      | 69      | 24        | 42      |
| 93    | 84      | 79      | 33        | 17      |
| 40    | 81      | 39      | 31        | 60      |
| 31    | 44      | 96      | 78        | 54      |
| 58    | 21      | 98      | 58        | 44      |
| 47    | 22      | 91      | 77        | 46      |
| 61    | 93      | 75      | 25        | 79      |
| 18    | 19      | 47      | 20        | 58      |
| 77    | 51      | 28      | 14        | 97      |

This is the piece of  markdown that is being generated for the last question of ga4.Even after using the prettier of the mentioned version i am getting incorrect answer.

Anyone like to help.

@Jivraj @carlton @s.anand

---

## Reply 29
**Author**: Joel Jeffrey
**Posted**: 2025-02-05T06:25:36.507Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/34

For Q10, I am extracting the text first using PyMuPDF (fitz) and then using markdownify to convert it to markdown and finally prettier. However despite trying changing it from PyMuPDF to other text extraction libraries, I end up getting

Incorrect. Try Again

errors

---

## Reply 30
**Author**: Sakthivel S
**Posted**: 2025-02-05T06:40:23.675Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/35

I think you have used the wrong document, because, this is the marks list for Q9

---

## Reply 31
**Author**: Tushar Jalan 
**Posted**: 2025-02-05T07:00:03.570Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/36

which tool you are using ?

---

## Reply 32
**Author**: Naman Gupta
**Posted**: 2025-02-05T07:10:34.357Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/37

HOW TO GET BBC API KEY

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for a coding or data processing task. It appears to be part of an online assessment or tutorial. The UI includes instructions, an example output, a question prompt, and an input area for the user to provide an answer. There are also UI elements for checking all options and saving the progress.

**2. Text Content:**

*   **Header:** "Due Sun, 9 Feb, 2025, 11:59 pm IST" "Score: 1/10" "Check all" "Save"
*   **Instructions:**
    *   "1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Tel Aviv. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city)."
    *   "2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId."
    *   "3. Data Transformation: Extract the issueDate and enhancedWeatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each issueDate to its corresponding enhancedWeatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedWeatherDescription."
*   **Example Output:** A JSON-like structure showing how to format the weather forecast data.
    ```json
    {
    "2025-01-01": "Sunny with scattered clouds",
    "2025-01-02": "Partly cloudy with a chance of rain",
    "2025-01-03": "Overcast skies",
    // ... additional days
    }
    ```
*   **Question Prompt:** "What is the JSON weather forecast description for Tel Aviv?"
*   **Error Message:** "SyntaxError: Unexpected end of JSON input"

**3. Context and Purpose:**

The image depicts a task where the user needs to:

1.  Fetch weather data from the BBC Weather API for Tel Aviv.
2.  Extract relevant information (issueDate and

---

## Reply 33
**Author**: Tushar Jalan 
**Posted**: 2025-02-05T07:21:08.047Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/38

in the bbc question what should be starting and the ending date

---

## Reply 34
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-05T08:32:35.339Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/39

you dont need the key you need that file used in 2 lecture videos just look for it.

 :+1:

---

## Reply 35
**Author**: K Hari Prasath
**Posted**: 2025-02-05T09:55:21.354Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/40

Please find below the screen shot showing the committed with step name my iitm email id

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a web browser, specifically a GitHub page. It displays the details of a workflow run for a repository. The UI elements include:

*   **Browser UI:** Address bar, tabs, back/forward buttons, refresh button, star icon, profile icon, and a three-dot menu.
*   **GitHub UI:** Repository name, workflow run number, navigation menu (Summary, Jobs, Run details, Usage, Workflow file), workflow file content, "Re-run all jobs" button, and a three-dot menu.
*   **Code Editor UI:** Line numbers, syntax highlighting for YAML code.

**2. Any text content visible:**

*   **Page Title:** "Updated · 23f2003853/workflow"
*   **Address Bar:** "github.com/23f2003853/workflows/actions/runs/13154595741/workflow"
*   **Repository and Run:** "23f2003853@ds.study.iitm.ac.in #13"
*   **Navigation Menu:** "Summary", "Jobs", "daily-commit", "Run details", "Usage", "Workflow file"
*   **Workflow File Header:** "Workflow file for this run", ".github/workflows/daily-commit.yml at 81c2d99"
*   **YAML Code (Workflow File Content):**
    *   `name: 23f2003853@ds.study.iitm.ac.in`
    *   `on:`
    *   `schedule:`
    *   `cron: '0 10 * * *' # Runs daily at 10:00 AM UTC`
    *   `workflow_dispatch: # Allows for manual triggering`
    *   `permissions:`
    *   `contents: write`
    *   `jobs:`
    *   `daily-commit:`
    *   `runs-on: ubuntu-latest`
    *   `steps:`
    *   `- name: 23f2003853@ds.

But the answer says

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a section of a user interface, likely from a web application or online learning platform. It appears to be a step in a process related to GitHub workflows. The UI elements include:

*   Text instructions and information.
*   An input field for a repository URL.
*   An error message.
*   A "Check" button.

**2. Any text content visible:**

*   "Be located in .github/workflows/ directory"
*   "After creating the workflow:"
*   "Trigger the workflow and wait for it to complete"
*   "Ensure it appears as the most recent action in your repository"
*   "Verify that it creates a commit during or within 5 minutes of the workflow run"
*   "Enter your repository URL (format: https://github.com/USER/REPO):"
*   "https://github.com/23f2003853/workflows" (in the input field)
*   "Error: No executed job step matches 23f2003853@dsstudy.itm.ac.in"
*   "Check" (on the button)

**3. The context or purpose of what's displayed:**

The context is related to setting up and verifying GitHub workflows. The user is instructed to create a workflow, trigger it, and then enter the repository URL. The system then checks if the workflow has been executed correctly. The error message indicates that the system couldn't find a matching executed job step, suggesting a problem with the workflow configuration or execution.

**4. Technical details:**

*   The instructions specify that the workflow file should be located in the `.github/workflows/` directory of the repository. This is the standard location for GitHub workflow files.
*   The error message suggests that the system is trying to match the executed job step with an email address (`23f2003853@dsstudy.itm.ac.in`). This could be related to the user's GitHub account or a specific configuration within the workflow.
*   The input field is expecting a GitHub repository URL in the format `https://github.com/USER/REPO`. The user has entered `https://github.com/

Please help to fix the issue

---

## Reply 36
**Author**: K Hari Prasath
**Posted**: 2025-02-05T10:00:47.264Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/41

Still the issue is there. Have posted screen shot.

---

## Reply 37
**Author**: K Hari Prasath
**Posted**: 2025-02-05T10:03:31.480Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/42

what Mr. Sakthivel S said is correct. could you tell me what tool did you use to convert .md file. I have done as per links in question and used chatgpt also. but nothing is correct

---

## Reply 38
**Author**: Tushar Jalan 
**Posted**: 2025-02-05T11:03:45.090Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/43

Please give the solution if you got any…have you been able to solve the bbc weather question?

---

## Reply 39
**Author**: Ansh bansal
**Posted**: 2025-02-05T14:04:46.408Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/45

@s.anand @carlton

In question 8 i got error

“Enter your repository URL (format: [https://github.com/USER/REPO](https://github.com/USER/REPO)):

[https://github.com/Ansh205/github-actions](https://github.com/Ansh205/github-actions)

Error: No workflow runs found”

But i have successfully commited

**Image: Screenshot 2025-02-05 193233**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) displaying a list of workflow runs. It appears to be a dashboard or log of automated processes, likely from a continuous integration/continuous deployment (CI/CD) system like GitHub Actions, GitLab CI, or similar. The UI includes:

*   A title: "All workflows"
*   A subtitle: "Showing runs from all workflows"
*   A count of workflow runs: "4 workflow runs"
*   A list of individual workflow runs, each with details like name, status, execution time, and branch.
*   A search bar to filter workflow runs.
*   Column headers for sorting and filtering (Event, Status, Branch, Actor).

**2. Any text content visible:**

*   **Titles/Headers:** "All workflows", "Showing runs from all workflows", "4 workflow runs", "Event", "Status", "Branch", "Actor", "Filter workflow runs"
*   **Workflow Names:** "Daily Commit Workflow" (repeated for each run)
*   **Workflow Run Details:** "Daily Commit Workflow #4: Manually run by Ansh205", "Daily Commit Workflow #3: Manually run by Ansh205", "Daily Commit Workflow #2: Manually run by Ansh205", "Daily Commit Workflow #1: Manually run by Ansh205"
*   **Branch Names:** "main" (repeated for each run)
*   **Timestamps:** "5 minutes ago", "37 minutes ago", "54 minutes ago", "1 hour ago", "19s", "14s", "11s", "14s"

**3. The context or purpose of what's displayed:**

The UI is designed to provide a user with an overview of workflow executions. It allows them to:

*   Monitor the status of automated processes (e.g., builds, tests, deployments).
*   Track the history of workflow runs.
*   Filter and search for specific runs based on various criteria (e.g., event, status, branch, actor).
*   Identify successful and failed runs.
*   See who triggered the workflow (in this case, "Ansh205").
*

---

## Reply 40
**Author**: Chinnam Goutham Nischay
**Posted**: 2025-02-05T17:37:33.037Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/46

Just follow the links and notebooks given in the references.

---

## Reply 41
**Author**: Shouvik Roy 
**Posted**: 2025-02-06T03:41:58.369Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/47

@Jivraj @carlton

sir i have submitted my GA3 but its showing not submitted why?

**Image: Untitled design**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page interface for an online assignment or quiz related to "Large Language Models." It includes UI elements like buttons, text instructions, score displays, and assignment details.

**2. Text Content:**

*   **Title:** "TDS 2025 Jan GA3 - Large Language Models"
*   **Instructions:** A numbered list of instructions for the assignment, including:
    *   "Learn what you need."
    *   "Check answers regularly by pressing Check."
    *   "Save regularly by pressing Save."
    *   "Reloading is OK."
    *   "Browser may struggle."
    *   "Use anything."
    *   "It's hackable."
*   **Note:** "You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers."
*   **Question Prompt:** "Have questions? Join the discussion on Discourse"
*   **Login Information:** "You are logged in as 23f1001348@ds.study.iitm.ac.in."
*   **Logout:** Logout
*   **Recent Saves:** "Reload from 2/4/2025, 4:04:47 PM. Score: 9.5"
*   **Module Information:** "Module 3: Large Language Models"
*   **Assignment:**
    *   "Graded Assignment 3"
    *   "Assessment (Due: 5 Feb 2025)"
    *   "Not Submitted"
*   **Score Table:**
    *   "Your Score"
    *   "Peer Average"
    *   "Median Score"
    *   All scores are currently displayed as "-"

**3. Context and Purpose:**

The image depicts the interface for an online assignment or quiz focused on Large Language Models. The instructions suggest a flexible and open approach to the assessment, allowing students to use various resources and even "hack" the code. The interface provides options for checking answers, saving progress, and reloading the page. It also displays the student's login information, recent saves, and assignment details, including the due date and submission status. The score table

---

## Reply 42
**Author**: K Hari Prasath
**Posted**: 2025-02-06T04:24:58.055Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/48

@s.anand Sir no submit button is available. On the top of it say submission is required. Could you clarify us

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a web browser window displaying an online course page. It appears to be a learning management system (LMS) interface. The page is titled "Graded Assignment 4" and is part of a course offered by IIT Madras. The UI elements include:

*   Browser tabs with titles like "Indian Institute of Technology," "My Dashboard - IIT Madras Online," and "Graded Assignment 4: IITM Online."
*   A navigation menu on the left side with sections like "Modules," "Grades," and "Calc."
*   A content area on the right displaying the details of the "Graded Assignment 4."
*   A Windows taskbar at the bottom with icons for various applications.

**2. Text Content:**

The text content includes:

*   **Course Information:** "IIT Madras," "Jan 2025-TDS"
*   **Navigation Menu:** "Course Introduction," "Modules," "Module 1: Development Tools," "Module 2: Deployment Tools," "Module 3: Large Language Models," "Project 1," "Module 4: Data Sourcing," "Grades," "Graded Assignment 4," "Assignment," "Calc"
*   **Assignment Details:**
    *   "Graded Assignment 4" (title)
    *   "Due date for this assignment: 2025-02-09, 23:59 IST."
    *   "You may submit any number of times before the due date. The final submission will be considered for grading."
    *   A list of potential causes for difficulty accessing the assignment, including:
        *   "Ad blockers need to be disabled/removed."
        *   "The site requires cookies for authentication."
        *   "Javascript is required for the site to work correctly."
        *   "Chrome Browser is the recommended software to access the contents."
        *   "Disable any browser extensions that may interfere with the site from working correctly."
        *   "Overly aggressive anti-virus software may also cause similar access problems."
        *   "Corporate proxies and network policies may also cause access issues."
    *   "You must use your Student ID (eg.

---

## Reply 43
**Author**: VIKASH PRASAD
**Posted**: 2025-02-06T04:57:11.068Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/49

what’s your directory structure, is it (.github/workflows/<filename.yaml>) and public

---

## Reply 44
**Author**: K Hari Prasath
**Posted**: 2025-02-06T05:10:27.978Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/50

As per instruction we need to create a directory in that we should have .yml file. But I tried with there were two issues (1) Github has not allowed to run the file (as there was no menu is available to run manually) (I checked with Copolit AI it says it is not correct to have cron jobs in a directory, I am not sure) (2) when I submit the url to iitm I got the following error

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows a section of a user interface, likely from a web application.
*   There's a text input field outlined in red, indicating an error or validation issue.
*   An error icon (a circle with an exclamation mark inside) is present within the input field.

**2. Text Content:**

*   "Be located in .github/workflows/ directory"
*   "After creating the workflow:"
*   "Trigger the workflow and wait for it to complete"
*   "Ensure it appears as the most recent action in your repository"
*   "Verify that it creates a commit during or within 5 minutes of the workflow run"
*   "Enter your repository URL (format: https://github.com/USER/REPO):"
*   "https://github.com/23f2003853/workflows" (This is the content of the input field)
*   "YAMLParseError: Implicit keys need to be on a single line at line 1, column 1: " (This is an error message)

**3. Context and Purpose:**

*   The UI appears to be related to setting up or configuring GitHub workflows.
*   The instructions guide the user on where to place workflow files and what to check after creating a workflow.
*   The input field is for entering a GitHub repository URL.
*   The error message suggests that the provided URL or a related configuration file (likely a YAML file defining the workflow) has a syntax error.

**4. Technical Details (Error Message):**

*   The error message "YAMLParseError: Implicit keys need to be on a single line at line 1, column 1: " indicates a problem with the YAML syntax in a workflow file.
*   The specific error "Implicit keys need to be on a single line" means that a YAML key (a name followed by a colon) is not properly formatted on a single line.
*   The "" part of the error message suggests that the YAML parser is encountering HTML code instead of valid YAML, which is a common cause of this type of error. This could mean the YAML file was accidentally replaced with an HTML file, or that the YAML file contains embedded HTML

I removed the directory and submitted the same url I got the following error

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Input Field:** A rectangular text input field with a red border, indicating an error or validation issue.
*   **Button:** A blue "Check" button.
*   **Error Message:** An error message displayed below the input field.
*   **Information Icon:** A red circle with an exclamation mark inside, likely indicating an error or warning.

**2. Text Content:**

*   **Label:** "Enter your repository URL (format: https://github.com/USER/REPO):"
*   **Input Field Value:** "https://github.com/23f2003853/workflows"
*   **Error Message:** "Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in"
*   **Button Text:** "Check"

**3. Context/Purpose:**

The image shows a UI for a tool or application that requires a GitHub repository URL as input. The user has entered a URL, but the application has flagged it as invalid, displaying an error message. The error suggests that the application is looking for an executed job step associated with a specific email address derived from the repository name.

**4. Technical Details:**

*   The application seems to be validating the GitHub repository URL against some criteria related to executed job steps.
*   The error message indicates that the application is attempting to extract an email address from the repository name (likely for identification or authentication purposes).
*   The format of the expected repository URL is provided as a hint: `https://github.com/USER/REPO`. The user's input deviates from this format by including "/workflows" at the end, which might be causing the error.

I do not know what to do next. Can TA help us

---

## Reply 45
**Author**: Carlton D'Silva
**Posted**: 2025-02-06T05:14:57.186Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/51

The submission is on the Actual assignment page like for all the previous GAs in TDS. This is the **ONLY** valid submission button for GA1, GA2, GA3, GA4, GA5.

**Image: Screenshot 2025-02-06 at 10.43.15 am**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a webpage, likely an online exam or assessment interface. It includes UI elements like a browser address bar, buttons, and text content. An arrow points to the "Save" button.

**2. Text Content:**

*   **Browser Address Bar:** `exam.sanand.workers.dev/tds-2025-01-ga4`
*   **Top Bar:**
    *   `[Admin] Due Sun, 9 Feb, 2025, 11:59 pm IST`
    *   `Score: 0`
    *   `Check all`
    *   `Save`
*   **Main Content:**
    *   `TDS 2025 Jan GA`
    *   `Instructions`
    *   A numbered list of instructions:
        1.  `Learn what you need.` Reading material is provided, but feel free to...
        2.  `Check answers regularly` by pressing `Check`. It shows which...
        3.  `Save regularly` by pressing `Save`. You can save multiple times...
        4.  `Reloading is OK.` Your answers are saved in your browser (not...
        5.  `Browser may struggle.` If you face loading issues, turn off sec...
        6.  `Use anything.` You can use any resources you want. The Intern...
        7.  `It's hackable.` It's possible to get the answer to *some* question...

**3. Context/Purpose:**

The webpage appears to be for an online exam or assessment called "TDS 2025 Jan GA". The instructions provide guidance to the user on how to take the exam, emphasizing the importance of checking and saving answers regularly. The "It's hackable" instruction is unusual and suggests a playful or unconventional approach to the assessment.

**4. Technical Details:**

*   The URL `exam.sanand.workers.dev` suggests the application is hosted on a worker service (likely Cloudflare Workers or similar).
*   The "Save" and "Check" buttons are likely interactive elements that trigger JavaScript functions to save the user's progress and check their answers, respectively.

---

## Reply 46
**Author**: VIKASH PRASAD
**Posted**: 2025-02-06T05:26:10.352Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/52

try with this

name: Set up Git user (23f2003853@ds.study.iitm.ac.in)

run: |

git config --global user.name “GitHub Actions Bot”

git config --global user.email “23f2003853@ds.study.iitm.ac.in”

---

## Reply 47
**Author**: Ansh bansal
**Posted**: 2025-02-06T05:42:11.105Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/53

Thank you  for your help , my repo was not public before and can you also help me in g4 i got this “Error: At root: Property name mismatch”

---

## Reply 48
**Author**: VIKASH PRASAD
**Posted**: 2025-02-06T05:50:34.894Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/54

In g4 which Question have that error you are getting

---

## Reply 49
**Author**: Tushar Jalan 
**Posted**: 2025-02-04T09:14:53.054Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/55

In the last two question of the ga,it is mentioned including both groups.so what is the meaning of this .

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a task description, likely from a coding challenge or assignment. It outlines a problem involving the analysis of student marks data. The task is presented as a set of instructions and context.

**2. Text Content:**

The text content can be broken down as follows:

*   **Title:** "Your Task"
*   **Introduction:** "This file, `q-extract-tables-from-pdf.pdf` contains a table of student marks in Maths, Physics, English, Economics, and Biology." The filename is a clickable link.
*   **Main Task:** "Calculate the total Biology marks of students who scored 17 or more marks in Physics in groups 43-66 (including both groups)."
*   **Steps:**
    *   "1. Data Extraction: Retrieve the PDF file containing the student marks table and use PDF parsing libraries (e.g., Tabula, Camelot, or PyPDF2) to accurately extract the table data into a workable format (e.g., CSV, Excel, or a DataFrame)."
    *   "2. Data Cleaning and Preparation: Convert marks to numerical data types to facilitate accurate calculations."
    *   "3. Data Filtering: Identify students who have scored marks between 17 and Physics in groups 43-66 (including both groups)."
    *   "4. Calculation: Sum the marks of the filtered students to obtain the total marks for this specific cohort."
*   **Contextual Information:** "By automating the extraction and analysis of student marks, EduAnalytics empowers Greenwood High School to make informed decisions swiftly. This capability enables the school to:"
*   **Benefits (Bulleted List):**
    *   "Identify Performance Trends: Quickly spot areas where students excel or need additional support."
    *   "Allocate Resources Effectively: Direct teaching resources and interventions to groups and subjects that require attention."
    *   "Enhance Reporting Efficiency: Reduce the time and effort spent on manual data processing, allowing educators to focus more on teaching and student engagement."
    *   "Support Data-Driven Strategies: Use accurate and timely data to shape educational strategies and improve overall student outcomes."
*   **Reiteration of the Task:** "What is the total Biology marks of students who scored 1

@Jivraj @carlton

---

## Reply 50
**Author**: Carlton D'Silva
**Posted**: 2025-02-06T06:09:22.483Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/56

Hi Tushar,

If you looked at the PDF you might have realised that students have been grouped. The question gives you a range for the groups 43-66. Including both groups implies both group 43 and 66 are included in your calculation.

kind regards

---

## Reply 51
**Author**: Ansh bansal
**Posted**: 2025-02-06T06:15:48.956Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/57

Question 4 "

Sample output

{

“25-02-04”: “Sunny intervals and light winds”,

“25-02-05”: “Light rain and light winds”,

}

Error: At root: Property name mismatch"

---

## Reply 52
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T06:19:39.985Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/58

Hi, even i’m facing the same issue,

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of the GitHub Actions interface for a specific workflow run. It displays details about a workflow named "Daily Commit" within a repository. The UI elements include:

*   **Navigation Bar:** At the top, there's a navigation bar with links to "Code," "Issues," "Pull requests," "Actions," "Projects," "Wiki," "Security," "Insights," and "Settings." The "Actions" tab is currently selected.
*   **Workflow Details:** The main content area shows details for the "Daily Commit" workflow, specifically run #10.
*   **Sidebar:** A sidebar on the left provides navigation within the workflow run, with options like "Summary," "Jobs," "Usage," and "Workflow file." "Summary" is currently selected.
*   **Run Summary:** The main area displays a summary of the workflow run, including its status, duration, and trigger information.
*   **Job Details:** It also shows details of the "daily-commit" job within the workflow.

**2. Text Content:**

*   **Repository Name:** "DigvijaysinhChudasamallTM / TDS\_GA\_4"
*   **Workflow Name:** "Daily Commit #10"
*   **Sidebar Links:** "Summary," "Jobs," "daily-commit," "Usage," "Workflow file"
*   **Run Details:**
    *   "Manually triggered 16 hours ago"
    *   "DigvijaysinhChudasamallTM" (likely the user who triggered the workflow)
    *   "e9aef97" (likely a commit hash)
    *   "main" (the branch)
    *   "Status: Success"
    *   "Total duration: 18s"
    *   "Artifacts: -"
*   **Job Details:**
    *   "daily-commit.yml"
    *   "on: workflow\_dispatch"
    *   "daily-commit" (job name)
    *   "7s" (job duration)

**3. Context and Purpose:**

The image shows the results of a GitHub Actions workflow run. The purpose is to provide information about the execution of the "Daily Commit

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository interface, specifically showing the content of a YAML file. The UI elements include:

*   **GitHub Navigation Bar:** At the top, there's a standard GitHub navigation bar with options like "Code," "Issues," "Pull requests," "Actions," "Projects," "Wiki," "Security," "Insights," and "Settings." There's also a search bar.
*   **Repository Information:** The repository name "DigvijaysinhChudasamalITM / TDS\_GA\_4" is displayed.
*   **File Navigation:** A file tree on the left shows the directory structure, with ".github/workflows" expanded, revealing two files: "daily-commit.yml" (which is currently selected) and "daily-commit.txt."
*   **Code Editor:** The main part of the screen displays the content of the "daily-commit.yml" file in a code editor.
*   **Commit Information:** Above the code editor, there's a message "DigvijaysinhChudasamalITM Update daily-commit.yml -- added pull repo code" indicating the last commit message.
*   **File Details:** Below the commit message, details like "38 lines (30 loc) • 1.14 KB" are shown, indicating the file size and number of lines.
*   **GitHub Copilot Suggestion:** A message "Code 55% faster with GitHub Copilot" is displayed.
*   **Action Buttons:** On the right side, there are buttons for "Raw," copying, downloading, editing, and viewing the file.
*   **Run History:** A "View Runs" button and a "History" button are present, along with information about the last commit (e9aef97, 17 hours ago).

**2. Text Content Visible:**

Here's a breakdown of the key text content:

*   **File Path:** TDS\_GA\_4/.github/workflows/daily-commit.yml
*   **YAML File Content:**
    *   `name: Daily Commit`
    *   `on:`
    *   `schedule:`
    *   `- cron: "0 0 * * *"` `# Runs

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a web application or tool related to GitHub workflows. It includes instructions, an input field for a repository URL, and an error message.

**2. Text Content:**

*   **"After creating the workflow:"** This is a heading or introductory phrase.
*   **"Trigger the workflow and wait for it to complete"**
*   **"Ensure it appears as the most recent action in your repository"**
*   **"Verify that it creates a commit during or within 5 minutes of the workflow run"** These are bullet points providing instructions or checks to perform after creating a workflow.
*   **"Enter your repository URL (format: https://github.com/USER/REPO):"** This is a label and a format example for the input field.
*   **"https://github.com/DigvijaysinhChudasamalITM/TDS\_GA\_4"** This is the URL entered into the input field.
*   **"Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in"** This is an error message.

**3. Context and Purpose:**

The image appears to be part of a tool or application that helps users set up and verify GitHub workflows. The instructions guide the user on what to do after creating a workflow. The input field allows the user to specify the repository URL. The error message indicates that something went wrong during the workflow execution, specifically that no executed job step matches the provided email address.

**4. Technical Details:**

*   The input field is highlighted with a red border, and there's a red exclamation mark icon, indicating an error or validation issue.
*   The error message suggests a problem with the workflow configuration or execution, possibly related to user permissions or the way the workflow is set up to interact with the repository.
*   The email address "21f2000588@ds.study.iitm.ac.in" is likely associated with a user account or a service account that the workflow is trying to use. The error implies that the workflow is trying to execute a job step that requires this account, but it

@Jivraj

@Saransh_Saini

@carlton

Can anyone please help to fix this issue and submit this correctly.

---

## Reply 53
**Author**: K Hari Prasath
**Posted**: 2025-02-06T06:21:39.845Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/59

21f3002277:

Set up Git user (23f2003853@ds.study.iitm.ac.in)

Still the same error appears

---

## Reply 54
**Author**: K Hari Prasath
**Posted**: 2025-02-06T06:23:50.056Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/60

Thanks for providing clarification Sir

---

## Reply 55
**Author**: Telvin Varghese
**Posted**: 2025-02-06T06:29:16.352Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/61

I am also facing same issue can’t resolve.

---

## Reply 56
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T06:30:07.514Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/62

@Jivraj @carlton @Saransh_Saini

In ques 4 Scrap the BBC Weather API,

I scraped the locationId for my city (i.e Mumbai)

and post that also mapped each `issueDate` to its corresponding `enhancedWeatherDescription` .

The sample output mentioned was:

The output would look like this:

{
  "2025-01-01": "Sunny with scattered clouds",
  "2025-01-02": "Partly cloudy with a chance of rain",
  "2025-01-03": "Overcast skies",
  // ... additional days
}

And My Output after scraping (And as explained by professor in Video 2 BBC weather was)

{

“2025-02-05”: “A clear sky and light winds”,

“2025-02-06”: “A clear sky and light winds”,

“2025-02-07”: “A clear sky and light winds”,

“2025-02-08”: “A clear sky and light winds”,

“2025-02-09”: “A clear sky and light winds”,

“2025-02-10”: “A clear sky and light winds”,

“2025-02-11”: “A clear sky and light winds”,

“2025-02-12”: “A clear sky and light winds”,

“2025-02-13”: “A clear sky and light winds”,

“2025-02-14”: “A clear sky and light winds”,

“2025-02-15”: “A clear sky and light winds”,

“2025-02-16”: “A clear sky and light winds”,

“2025-02-17”: “A clear sky and light winds”,

“2025-02-18”: “A clear sky and light winds”,

“2025-02-19”: “A clear sky and light winds”

}

But it’s giving Error::

Error: At root: Different number of properties

Can you please help how to fix this issue.

---

## Reply 57
**Author**: Telvin Varghese
**Posted**: 2025-02-06T06:37:52.150Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/63

Issue resolved for me after following below step

After creating the workflow:

Trigger the workflow and wait for it to complete
Ensure it appears as the **most recent action** in your repository
Verify that it creates a commit during or within 5 minutes of the workflow run

---

## Reply 58
**Author**: Ansh bansal
**Posted**: 2025-02-06T06:38:34.157Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/64

In place of “name: Setup up GIT config” change to “name: add commit {your_email}”

---

## Reply 59
**Author**: VIKASH PRASAD
**Posted**: 2025-02-06T06:45:41.518Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/65

use this [Google Colab](https://colab.research.google.com/drive/1X5IO8K1Xf8Wh7SOZelSrFAfZgRG-mv4A?usp=sharing) with the city name to get the Json Body just change the date format.

@23f2004752

---

## Reply 60
**Author**: Joel Jeffrey
**Posted**: 2025-02-06T07:04:00.243Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/66

@carlton @Jivraj could you please help me with this?

---

## Reply 61
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T07:19:29.059Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/67

On running this colab with city = Mumbai,

I’m gettingh this error: Error: At root: Property name mismatch

---

## Reply 62
**Author**: VIKASH PRASAD
**Posted**: 2025-02-06T07:42:32.535Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/68

it’s getting,

{
    "2025-02-06": "Sunny and a gentle breeze",
    "2025-02-07": "Sunny and a gentle breeze",
    "2025-02-08": "Sunny and a gentle breeze",
    "2025-02-09": "Sunny and a gentle breeze",
    "2025-02-10": "Sunny and a gentle breeze",
    "2025-02-11": "Sunny and a gentle breeze",
    "2025-02-12": "Sunny and a moderate breeze",
    "2025-02-13": "Sunny and a gentle breeze",
    "2025-02-14": "Sunny and a gentle breeze",
    "2025-02-15": "Sunny and a gentle breeze",
    "2025-02-16": "Sunny and a gentle breeze",
    "2025-02-17": "Sunny and a gentle breeze",
    "2025-02-18": "Sunny and a gentle breeze",
    "2025-02-19": "Sunny and a gentle breeze"

}

---

## Reply 63
**Author**: K Hari Prasath
**Posted**: 2025-02-06T08:10:06.762Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/69

can tell me in your .yml which are all place did you use your iitm email id.  Because I got the error No executed job step matches 23f2003853@ds.study.ittm.ac.in. My commit was completed in 11 seconds

---

## Reply 64
**Author**: Telvin Varghese
**Posted**: 2025-02-06T08:30:20.527Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/70

@s.anand @carlton @Jivraj

Is there any way to crack this , I tired multiple time no improvement.

Also what does this " It is *very hard* to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. Reformatting with Prettier helps standardize the output format for comparison." mean.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a web application or online learning platform. It presents a task or exercise related to converting a PDF document to Markdown format. The UI includes instructions, context, an input area for the user's answer, and feedback.

**2. Text Content:**

*   **Title:** "q-pdf-to-markdown.pdf has the contents of a sample document."
*   **Instructions:**
    *   "1. Convert the PDF to Markdown: Extract the content from the PDF file. Accurately convert the extracted content into Markdown format, preserving the structure and formatting as much as possible."
    *   "2. Format the Markdown: Use Prettier version 3.4.2 to format the converted Markdown file."
    *   "3. Submit the Formatted Markdown: Provide the final, formatted Markdown file as your submission."
*   **Section Title:** "Impact"
*   **Impact Description:** "By completing this exercise, you will contribute to EduDocs Inc.'s mission of providing high-quality, accessible educational resources. Automating the PDF to Markdown conversion and ensuring consistent formatting:"
*   **Impact Bullet Points:**
    *   "Enhances Productivity: Reduces the time and effort required to prepare documentation for clients."
    *   "Improves Quality: Ensures all documents adhere to standardized formatting, enhancing readability and professionalism."
    *   "Supports Scalability: Enables EduDocs to handle larger volumes of documentation without compromising on quality."
    *   "Facilitates Integration: Makes it easier to integrate Markdown-formatted documents into various digital platforms and content management systems."
*   **Question:** "What is the markdown content of the PDF, formatted with prettier@3.4.2?"
*   **User Input (Incorrect):**
    *   "Ater vulnero solio tabula."
    *   "Auctus benigne coaegresco defetiscor delinquo."
    *   "Talio balbus cultura vae. Sint deripio tener adfectus agnitio aro cruentus arbustum. Abstergo alii sollers."
    *   "---"
*   **Feedback:** "Incorrect. Try again."
*   **

---

## Reply 65
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-06T09:39:54.578Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/71

Same problem please help me too if you get it right.

---

## Reply 66
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T10:29:37.045Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/72

Yes followed all these steps, and still the error is being seen,

Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in

---

## Reply 67
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T10:33:21.057Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/73

Yes true,

Here’s the output:

{

“2025-02-05”: “Sunny and a gentle breeze”,

“2025-02-06”: “Sunny and a gentle breeze”,

“2025-02-07”: “Sunny and a gentle breeze”,

“2025-02-08”: “Sunny and a gentle breeze”,

“2025-02-09”: “Sunny and a gentle breeze”,

“2025-02-10”: “Sunny and a gentle breeze”,

“2025-02-11”: “Sunny and a moderate breeze”,

“2025-02-12”: “Sunny and a gentle breeze”,

“2025-02-13”: “Sunny and a gentle breeze”,

“2025-02-14”: “Sunny and a gentle breeze”,

“2025-02-15”: “Sunny and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny and a gentle breeze”,

“2025-02-18”: “Sunny and a gentle breeze”

}

But unfortunately this error persists,

Error: At root: Property name mismatch

---

## Reply 68
**Author**: K Hari Prasath
**Posted**: 2025-02-06T10:33:30.127Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/74

Now re-check you answer. May it will give link where the issue exists. if it gives url browsers the link and address.

---

## Reply 69
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T10:33:48.592Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/75

Yes true same happened with me.

---

## Reply 70
**Author**: K Hari Prasath
**Posted**: 2025-02-06T10:36:03.777Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/76

re-check your answer again it may give an url. check the url

---

## Reply 71
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T10:36:09.371Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/77

Now on rechecking, the error message has changed to – “TypeError: Failed to fetch”

---

## Reply 72
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T10:36:50.718Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/78

No its giving such error:

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, specifically a form field for entering a GitHub repository URL. There's an input box with a URL already entered, an error message displayed below the input box, and a "Check" button.

**2. Any text content visible:**

*   "Enter your repository URL (format: https://github.com/USER/REPO):" - This is a label or instruction for the input field.
*   "https://github.com/DigvijaysinhChudasamalITM/TDS\_GA\_4" - This is the URL entered into the input field.
*   "TypeError: Failed to fetch" - This is an error message indicating that the system was unable to retrieve data from the provided URL.
*   "Check" - This is the text on the button, presumably used to validate or process the entered URL.

**3. The context or purpose of what's displayed:**

The UI is likely part of a system or application that requires a GitHub repository URL as input. The user has entered a URL, and the system has attempted to fetch data from that URL, but it failed. The error message "TypeError: Failed to fetch" suggests a network issue, an invalid URL, or a problem with the GitHub repository itself (e.g., it doesn't exist, is private, or has access restrictions).

**4. Technical details:**

*   The error message "TypeError: Failed to fetch" is a common JavaScript error that occurs when the `fetch` API (used for making network requests) encounters a problem. This could be due to:
    *   A network connection issue.
    *   A CORS (Cross-Origin Resource Sharing) issue if the request is being made from a different domain.
    *   An invalid URL.
    *   A server-side error on the GitHub side.
*   The input field is likely validated by the system, as indicated by the error message and the "Check" button.
*   The presence of the "Check" button suggests that the system performs some kind of validation or processing of the URL before proceeding.
*   The red exclamation mark inside a circle next to the input field also indicates an error.

---

## Reply 73
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T10:42:30.147Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/79

Here’s the action’s:

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for managing GitHub Actions workflows. It appears to be a dashboard or a page within a GitHub repository. The UI is divided into a left sidebar and a main content area.

*   **Left Sidebar:** Contains a list of actions and management options.
*   **Main Content Area:** Displays a list of workflow runs, along with a prompt to provide feedback on GitHub Actions.

**2. Text Content:**

*   **Actions:**
    *   All workflows
    *   Daily Commit
*   **Management:**
    *   Caches
    *   Attestations
    *   Runners
    *   Usage metrics
    *   Performance metrics
*   **New workflow**
*   **All workflows:** Showing runs from all workflows
*   **Help us improve GitHub Actions:** Tell us how to make GitHub Actions work better for you with three quick questions.
*   **Give feedback**
*   **15 workflow runs**
*   **Daily Commit:**
    *   Daily Commit #15: Manually run by DigvijaysinhChudasamallTM
    *   Daily Commit #14: Manually run by DigvijaysinhChudasamallTM
*   **main** (appears twice, likely indicating the branch)
*   **Filter workflow runs**
*   **Event, Status, Branch, Actor** (column headers for workflow runs)
*   **13 minutes ago** (appears twice, likely indicating the time since the workflow run)
*   **16s, 17s** (appears twice, likely indicating the duration of the workflow run)

**3. Context and Purpose:**

The UI is designed to allow users to:

*   View and manage their GitHub Actions workflows.
*   See the history of workflow runs.
*   Filter and sort workflow runs based on different criteria (Event, Status, Branch, Actor).
*   Create new workflows.
*   Access management features like caches, attestations, runners, and metrics.
*   Provide feedback to GitHub about their experience with GitHub Actions.

**4. Technical Details:**

*   The UI elements suggest a web-based application, likely built with HTML, CSS, and JavaScript

---

## Reply 74
**Author**: K Hari Prasath
**Posted**: 2025-02-06T10:44:58.593Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/80

Check you Github account and browse Action for your repo. then check All Work flows. Ensure the first item is schedule triggered confirmation

---

## Reply 75
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T10:47:32.686Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/81

What you meant by " Ensure the first item is schedule triggered confirmation"? You meant the latest one should be this right?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of the "Actions" tab within a GitHub repository. It displays a list of workflow runs, specifically for a workflow named "Daily Commit." The UI elements include:

*   **Navigation Bar:** At the top, there's a standard GitHub navigation bar with options like "Code," "Issues," "Pull requests," "Actions," "Projects," "Wiki," "Security," "Insights," and "Settings."
*   **Repository Information:** The repository name "DigvijaysinhChudasamalITM / TDS\_GA\_4" is displayed.
*   **Actions Sidebar:** On the left, there's a sidebar with "Actions" highlighted, and options like "All workflows," "Daily Commit," and management options like "Caches," "Attestations," "Runners," "Usage metrics," and "Performance metrics."
*   **Workflow Runs List:** The main content area shows a list of workflow runs for "All workflows." Each entry includes the workflow name ("Daily Commit"), a status indicator (green checkmark or red cross), details about the run (e.g., "Daily Commit #15: Manually run by DigvijaysinhChudasamalITM"), the branch ("main"), and the time since the run occurred.
*   **Feedback Prompt:** A banner at the top encourages users to provide feedback on GitHub Actions.
*   **Filter:** There is a filter option to filter workflow runs.

**2. Any text content visible:**

*   "DigvijaysinhChudasamalITM / TDS\_GA\_4" (Repository name)
*   "Code," "Issues," "Pull requests," "Actions," "Projects," "Wiki," "Security," "Insights," "Settings" (Navigation menu)
*   "Actions" (Sidebar heading)
*   "All workflows," "Daily Commit," "Caches," "Attestations," "Runners," "Usage metrics," "Performance metrics" (Sidebar options)
*   "New workflow" (Button)
*   "All workflows" (Main content heading)
*   "Showing runs from all workflows"
*   "Help us improve GitHub Actions"
*   "Tell us how to make GitHub Actions work better for you with three

---

## Reply 76
**Author**: K Hari Prasath
**Posted**: 2025-02-06T10:56:41.910Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/82

check this type of screen

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) related to GitHub Actions. It displays a list of workflow runs, along with a prompt to provide feedback on GitHub Actions.

**2. Text Content:**

*   "Showing runs from all workflows" (implied, likely above the visible portion)
*   "Help us improve GitHub Actions"
*   "Tell us how to make GitHub Actions work better for you with three quick questions."
*   "Give feedback"
*   "X" (close button)
*   "71 workflow runs"
*   "Event"
*   "Status"
*   "Branch"
*   "Actor"
*   "23f2003853@ds.study.iitm.ac.in" (appears twice)
*   "23f2003853@ds.study.iitm.ac.in #23: Manually run by 23f2003853"
*   "main"
*   "23 minutes ago"
*   "19s"

**3. Context and Purpose:**

The UI is likely part of a GitHub repository's "Actions" tab. It provides a summary of workflow runs, allowing users to monitor their automated processes. The feedback prompt indicates that GitHub is actively seeking user input to improve the GitHub Actions platform.

**4. Technical Details:**

*   The UI elements suggest a tabular format for displaying workflow runs, with columns for "Event," "Status," "Branch," and "Actor."
*   The email address "23f2003853@ds.study.iitm.ac.in" likely represents the user or account associated with the workflow run.
*   The "#23" likely refers to the run number.
*   "Manually run by 23f2003853" indicates that the workflow was triggered manually by the user.
*   "main" indicates the branch the workflow was run on.
*   The timestamps "23 minutes ago" and "19s" likely refer to the time since the workflow run started and its total duration, respectively.
*   The green checkmark

---

## Reply 77
**Author**: Ansh bansal
**Posted**: 2025-02-06T11:26:21.596Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/84

use name:email inside yml page

---

## Reply 78
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-06T11:27:18.714Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/85

Yep done, thank you!  :smiley:

---

## Reply 79
**Author**: Wasim Ansari
**Posted**: 2025-02-06T13:39:36.309Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/87

Depopulo amoveo curo.
Concego creatinue ancilla vesper conicio cinimatico eribro.  
Custodia anica arbustum coniceto suma corporis aduno commenoro curiositas augero.  
Uredo thesis ancilla alter eun tener vomito praesentium templum.  
Magni deprimo celebre.

### Bellum pelor cornu vorax perspiciatis.

Labore elus umerus voluntarius.  
Vicissitudo cilíctum cicuta campana.  
Desino perspiciatis comodo.

### amarttudo tabesco crinis amissio

tui qui decumbo vobis  
audacia charismatubineus contigo  
aro eum talio elus  
coniuratio cubo ab vere  
validus tam patria deficio  
agnosco spectaculumcoerceo  
spectaculum vulpes valetudo  
minima cado suffragium  
asperiores thesaurus cometes  
vesica amplus cimentarius  
volum curiositas cornu

## Paupertrucido confido triduana ante sublime

# Consequatur comminor

Coadunatio delectus atqui placeat atque copia ventosus aer quae.  
Tatillo causa damatico validus torrena tivpinca.  
Adside nisi atavus aspiente.

[soius tam](https://tds.s-anand.net/#/markdown)

Ceno usilio desino velociter sit aut. Concedo accedo vac congregatio sperno venia sum sordeo animi tametsi. Accusamus suppellex turpis dedecor uliam vaco venusit:

- tu! amicitia ante suppellex studio
- utor debilito suasoria odio
- antea desino despecto magni

[coadunatio voco](https://tds.s-anand.net/#/markdown)

[incidunt aliquam](https://tds.s-anand.net/#/markdown)

Tametsitenuis conscendo.

- tempore vorner aestas commentoro
- absconditus coruscus

## Blanditiis tabula animi succedo

Asper summa tametsi ustulo villias conservo clam triumphus tener ager. Audax conforto adopto vesco arbustum deorsum terror impedit iure. Adsum atrox caries acc

Beatae ducimus aperio amarttudo caries

- cinis solvo unde unde arbustum
- canis civitas viro
- thorax pax demens
- arbustum suficco thorax testimonium ex.
- vinliter sumptus

Explicabo defico adfectus.

Comedo cattus justo tamdiu tumultus confido thesaurus coadunatio volutabrum. Succedo tabula audax copia vinculum.

**cogo audio suffragium**

crepito amiculum sufficio  
acer aestas utor  
debeo adopto utpote  
tametsi curatio ante

## Maxime vulgo depulso decipio atrox

## Career debeo

**conatus cui admoneo**

theatum pauper tego
pecco caeous vulgo
cursim desino arceo
balbus comminor et 

In the question no. 10, I have tried numerous time to get it right markdown content but it was incorrect all the time.

I have tried these steps:

import pymupdf4llm
md_text = pymupdf4llm.to_markdown("/content/q-pdf-to-markdown.pdf")

import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())

Then i run this in bash

prettier --write output.md

And what i got frankly telling was far from this, I did some manual touchups, and this what i have now. This is the best version i could come up with. Saw the preview, it does matches with the pdf.

#Can someone please advise me a better approach?

---

## Reply 80
**Author**: Ansh bansal
**Posted**: 2025-02-05T03:03:39.499Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/89

hey, can you help me in doing this i can’t able to do this.

---

## Reply 81
**Author**: Carlton D'Silva
**Posted**: 2025-02-06T14:01:32.303Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/90

@24ds3000090

We will be changing this question. Even we found it hard  :sweat_smile: 

Kind regards

---

## Reply 82
**Author**: Carlton D'Silva
**Posted**: 2025-02-06T14:02:42.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/91

@JoelJeffrey

We will be changing this question. Even we found it pretty hard  :sweat_smile: 

Kind regards

---

## Reply 83
**Author**: Daksh Agarwal
**Posted**: 2025-02-06T15:06:08.271Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/92

sir in the weather question could you provide from where do we get the bbc api because i have searched a lot and havent been able to find it

---

## Reply 84
**Author**: Carlton D'Silva
**Posted**: 2025-02-06T15:13:07.942Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/93

[https://tds.s-anand.net/#/bbc-weather-api-with-python](https://tds.s-anand.net/#/bbc-weather-api-with-python)

---

## Reply 85
**Author**: Chinnam Goutham Nischay
**Posted**: 2025-02-06T16:42:32.860Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/94

try manually inspecting the output of the api and compare it with your script output.

Or else try refreshing the browser and check.

---

## Reply 86
**Author**: Ansh bansal
**Posted**: 2025-02-06T17:52:55.640Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/95

@carlton

Previously i got correct on q2 but now i am getting the error when i refresh the page “TypeError: Cannot read properties of null (reading ‘textContent’)”

---

## Reply 87
**Author**: Rajalakshmi Rathinasabhapathy
**Posted**: 2025-02-06T19:53:06.705Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/96

Please try city=“Mumbai” as a string literal.

---

## Reply 88
**Author**: Nelson Jochim DSouza
**Posted**: 2025-02-06T20:56:51.582Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/97

Q4 BBC Weather

I don’t understand why I am getting

Error: At root: Different number of properties

Is it because of different dates? Shall I match the dates?

@carlton Please guide. Thank you.

**Image: BBC weather**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from an online coding challenge or tutorial. It presents a task description, an example of the expected output, a question, a user's attempt at answering the question, and an error message. There's also a "Check" button.

**2. Text Content:**

*   **"Your Task"**: This is the title of the section.
*   **"As part of this initiative, you are tasked with developing a system that aut..."**: This is the introductory text describing the overall goal.
*   **"1. API Integration and Data Retrieval: Use the BBC Weather API to fetch weather data for a specific locationId. Include necessary query parameters such as API key, locationId."**: This is the first step of the task.
*   **"2. Weather Data Extraction: Retrieve the weather forecast data using the API."**: This is the second step of the task.
*   **"3. Data Transformation: Extract the issueDate and enhancedWeatherDescription from the API response. Map the issueDate to its corresponding enhancedWeatherDescription. Create a JSON object with the dates as keys and the descriptions as values."**: This is the third step of the task.
*   **"The output would look like this:"**: Introduces an example of the expected output format.
*   **JSON Example**:
    *   `"2025-01-01": "Sunny with scattered clouds"`
    *   `"2025-01-02": "Partly cloudy with a chance of rain"`
    *   `"2025-01-03": "Overcast skies"`
    *   `// ... additional days`
*   **"What is the JSON weather forecast description for Osaka?"**: This is the question the user needs to answer.
*   **User's Answer (JSON)**:
    *   `"2025-02-06": "A clear sky and light winds"`
    *   `"2025-02-07": "Sunny intervals and a moderate breeze"`
    *   `"2025-02-08": "Light rain showers and

---

## Reply 89
**Author**: Mishkat Chougule
**Posted**: 2025-02-02T08:21:23.154Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/98

thema coruscus

cupiditate celebrer
argentum alius voro soluta
sto decor capto suffoco acs tempus deludo deleo ventus odio

Sordeo tergo beatae coniecto ambitus carus. Vae tamdiu debilito verto confugo

territo acies vos patria. Versus surgo degero vester tersus paulatim chirographum

abeo
super
valetudo adhuc

conatus
comptus
spiculum summisse

alienus
addo
demergo conturbo

uberrime
subseco
altus & ea

apto
cursus
infit & summa

tabula necessitatibus beneficium concido
adhaero tepesco ars
adnuo beatae
cursim ahsens culpa animi aestivus

Solium vulgus commodo claro curriculum valens

Aut ipsum spiritus tantillus vacuus adsum crebro animus pel paulatim. Tunc vallum

torqueo aequus valens triduana illo. Uredo cursus fuga vir.

Cultellus adipiscor incidunt tondeo benevolentia capto contabesco bene tardus

harum.

Bos subnecto beatae abeo vulnus terra verus balbus

arguo via vallum usus aliquid
tempus balbus videlicet acquiro

attonbitus tardus versus cuppedia

derelinctuo curatio stalla solen

comburo commodo caveo at

deporto aliquid thymum

confero sortitus ago

triduana umquam acies

Beneficium doloremque aspernatur dolor dolorum despecto attonbitus unus alienus

Capto optio dolores.

Commodi sono denuo molestiae terebro

Benigne anser vulgus brevis coaegresco vinum debeo.

Cras aut ullam error terreo absque aro adstringo sublime thymum

Triumphuslaudantium curto certus

Callide stabilis subito claudeo occaecati depono. Turba thymum bis deludo una.

Sumo consuasor necessitatibus vix solitudo dolorum dolorem vinco inflammatio

apparatus spero sulum desino ultra
nauner necessitatibus bos calculus nlaceat
animadverto defessus triumphus
acquiro artificiose minima sortitus terminatio

Aegrus tot tot aetas. Clinís volva tamen sumptus. Solutio deludo suscipio deputo

demens vero audeo annus alo accendo.

I am getting error: Incorrect. Try again.

@Jivraj @carlton can you please explain the reason for this error

---

## Reply 90
**Author**: Carlton D'Silva
**Posted**: 2025-02-07T03:25:45.448Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/99

Hi Mishkat

Please refer to this post.

    [GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/91) Tools in Data Science

    @JoelJeffrey 
We will be changing this question. Even we found it pretty hard  sweat_smile  
Kind regards

Kind regards

---

## Reply 91
**Author**: 23f3001356
**Posted**: 2025-02-07T05:47:13.914Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/100

@s.anand Sir the question 10 of the Graded Assignment 4 is very tough I have tried everything from custom python codes using different libraries to online converted and also formatted using prettier. Please sir guide me how to do the question.

---

## Reply 92
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-07T05:48:27.982Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/101

Yep figured that, and after matching the data solved the error and got that question correct.

Though thank you.

---

## Reply 93
**Author**: 23f3001356
**Posted**: 2025-02-07T05:49:56.327Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/102

@s.anand Sir I have done the question 2 of the graded assignment but I am very curious to know why the answers language gets periodically change. Is there some kind of backend code which is responsible for that or is something else ?

---

## Reply 94
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-07T05:50:27.393Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/103

Yes we’ll were facing this issue.

@carlton sir mentioned yesterday that they will change the question.

"We will be changing this question. Even we found it hard  :sweat_smile: 

Kind regards"

So need to worry about that question for now.

---

## Reply 95
**Author**: 23f3001356
**Posted**: 2025-02-07T05:52:26.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/104

OK, that is good to hear, you won’t believe that yesterday I was trying this question for 2 hours literally, it can be more also.

---

## Reply 96
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-07T05:54:22.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/105

I was stuck at that question for 2 days, I tried multiple ways but was not able to format the content with prettier as expected, every time I was getting the error “Incorrect. Try again.”

---

## Reply 97
**Author**: Anand S
**Posted**: 2025-02-07T06:01:13.973Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/106

On popular demand, I’ve made Q10 of GA4 easier (converting from PDF to Markdown). The question remains the same, but the check is more liberal and the error messages are more helpful. Please give it a shot now.

(FYI, one person *did* solve it. A colleague, not someone from the IITM DS program.)

---

## Reply 98
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-07T06:44:45.158Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/107

Hello Sir, i tried but unfortunately after extracting the contents and formatting the contents and submitting it, it’s showing various errors like Missing links, Missing tables…

But on checking the file i wasn’t able to find any single table in the contents in that case what could be done to fix these errors?

@Jivraj @carlton @Saransh_Saini

---

## Reply 99
**Author**: Tushar Jalan 
**Posted**: 2025-02-07T07:33:28.651Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/108

same issue with me as well

---

## Reply 100
**Author**: K Hari Prasath
**Posted**: 2025-02-07T08:36:08.903Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/109

Sir I checked the pdf file, there is only one place unorder list is given and the same is available in my answer. But the system throws error Missing List (I tried with other symbols * and + also) . Please inform me where I made mistake

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a UI element, likely a code editor or a display of markdown content. The content is presented within a red-bordered box. There's a scrollbar on the right side of the box. An error message is displayed below the box.

**2. Any text content visible:**

*   **Question:** "What is the markdown content of the PDF, formatted with prettier@3.4.2?"
*   **Markdown Content (with red wavy underlines):**
    *   "- cuppedia tamquam facilis confugo"
    *   "- conservo depereo"
    *   "- consectetur arx"
    *   "- aeternus celebrer"
*   **Error Message:** "Error: Missing lists"

**3. The context or purpose of what's displayed:**

The image shows an attempt to display markdown content that was extracted from a PDF and formatted using the "prettier" code formatter (version 3.4.2). The error message "Missing lists" suggests that the markdown content is not being correctly interpreted as a list. The red wavy underlines under the text indicate that there are errors or issues with the text.

**4. Technical details:**

*   The presence of the "prettier@3.4.2" reference indicates that a specific version of the Prettier code formatter was used.
*   The error message "Missing lists" suggests that the markdown parser is expecting a specific list structure that is not present in the provided content.
*   The red wavy underlines indicate that the text is not being rendered correctly.

---

## Reply 101
**Author**: K Hari Prasath
**Posted**: 2025-02-07T08:39:47.886Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/110

this is table. Check it

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays three columns of text. Each column has a heading in bold font, followed by a list of words.

**2. Text Content:**

Here's the text content, organized by column:

*   **capitulus**
    *   voluptate
    *   quaerat
    *   vestigium
    *   ait
*   **deleniti**
    *   barba
    *   cedo
    *   trans
    *   alioqui
*   **pariatur**
    *   bellum
    *   cursus
    *   sortitus
    *   verumtamen

**3. Context/Purpose:**

The text appears to be a list of Latin words, possibly organized by some thematic or grammatical category. The bold headings might represent these categories or topics. It could be a vocabulary list, a table of related terms, or an example of Latin text.

**4. Technical Details:**

*   The text is rendered in a clear, sans-serif font.
*   The headings are in bold, making them visually distinct.
*   The layout is simple and organized, with the words neatly aligned in columns.

---

## Reply 102
**Author**: Nelson Jochim DSouza
**Posted**: 2025-02-07T08:52:02.503Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/111

Q 10 - PDF to Markdown.

Why it is saying

Incorrect. Try again?

Do I need to add CSS?

`Carbo ventosus tametsi patior. Recusandae ciminatio alienus nisi ventosus apud. Theatrum abutor aperio spargo vestrum virga placeat adulescens. Deripio alveus creator omnis tabula patria cupiditate in virga speculum. Acidu`s alienus vehemens vapulus.`

**earum clamo collum**

curtus careo curatio

tendo sunt culpo

Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

cresco
solio
ademptio
terreo
bis

tardus
carpo
allatus
depono
benevolentia

tunc
atavus
barba
urbs
considero

adulescensamplitudo

verbum
cultura
id

cenaculum
ipsum
sursum
conturbo
nemo

damno
arbitro
quibusdam
articulus
animadverto

ustulo crudelis depraedor
sophismata tener apostolus suus adopto
coniecto maxime rerum
acceptus virga confero comes

cresco vomito

deputo ceno

Cuppedia uberrime socius atque paens
Sto theca testimonium aestus debitis

valde vulgus

---

## Reply 103
**Author**: Nelson Jochim DSouza
**Posted**: 2025-02-07T08:55:44.029Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/112

I checked many times. For me it says “Incorrect. Try again.”

---

## Reply 104
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-07T09:31:43.739Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/113

Ya i know, i added tables, list, blockquote, code, tables have all been added still it’s showing errors. Not sure where am I going wrong.

---

## Reply 105
**Author**: K Hari Prasath
**Posted**: 2025-02-07T09:33:27.992Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/114

Please refer video and document relating to Question 1 of Assignment 3. There it is mentioned how to mark bold, table etc., use those marks

---

## Reply 106
**Author**: Nelson Jochim DSouza
**Posted**: 2025-02-07T10:04:21.710Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/115

I have added all those and pasted the markdown and it appears as [above](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/111).

`` Carbo ventosus tametsi patior.
Recusandae ciminatio alienus nisi ventosus apud.
Theatrum abutor aperio spargo vestrum virga placeat adulescens.
Deripio alveus creator omnis tabula patria cupiditate in virga speculum.
Acidu`s alienus vehemens vapulus. ``

**earum clamo collum**
curtus careo curatio
tendo sunt culpo
Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

| cresco              | solio   | ademptio  | terreo    | bis          |
| ------------------- | ------- | --------- | --------- | ------------ |
| tardus              | carpo   | allatus   | depono    | benevolentia |
| tunc                | atavus  | barba     | urbs      | considero    |
| adulescensamplitudo |         | verbum    | cultura   | id           |
| cenaculum           | ipsum   | sursum    | conturbo  | nemo         |
| damno               | arbitro | quibusdam | articulus | animadverto  |

- ustulo crudelis depraedor
- sophismata tener apostolus suus adopto
- coniecto maxime rerum
- acceptus virga confero comes

[cresco vomito](;;;)

[deputo ceno](;;;)

# Cuppedia uberrime socius atque paens

# Sto theca testimonium aestus debitis

[valde vulgus](;;;)

Below is the screenshot of provided PDF. That font colour strains my eyes. Any particular reason for that PDF?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a block of text, seemingly extracted from a document or a book. The text is in a light color (likely white or a very light gray) against a white background. The text appears to be Latin.

**2. Any text content visible:**

The text content includes several paragraphs and lists of words. Here's a breakdown of some of the visible text:

*   "Carbo ventosus tametsi patior."
*   "Recusandae ciminatio alienus nisi ventosus apud."
*   "Theatrum abutor aperio spargo vestrum virga placeat adulescens."
*   "Deripio alveus creator omnis tabula patria cupiditate in virga speculum."
*   "Acidus alienus vehemens vapulus."
*   "Barum clamo collum"
*   "curtus careo curatio"
*   "tendo sunt culpo"
*   "Suussit magni traho tempora."
*   "Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo justo adfero truculenter."
*   A list of words like "cresco," "solio," "ademptio," "terreo," "bis," "tardus," "carpo," "allatus," "depono," "benevolentia," "tunc," "atavus," "barba," "urbs," "considero," "adulescensamplitudo," "verbum," "cultura," "id," "cenaculum," "ipsum," "sursum," "conturbo," "nemo," "damno," "arbitro," "quibusdam," "articulus," "animadverto."
*   A bulleted list:
    *   "ustulo crudelis depraedor"
    *   "sophismata tener apostolus suus adopto"
    *   "coniecto maxime rerum"
    *   "acceptus virga confero comes"
*   "cresco vomito"
*   "deputo ceno"
*   "Cuppedia uberrime

---

## Reply 107
**Author**: Sujay D
**Posted**: 2025-02-07T10:15:38.429Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/116

I am getting missing link error. I checked in the pdf file also, the blue color text seems a link but its not clickable.

Any suggestion to move nearer to the actual solution.

---

## Reply 108
**Author**: Nelson Jochim DSouza
**Posted**: 2025-02-07T10:16:40.485Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/117

You may try like this: cresco vomito

[cresco vomito](;;;)

---

## Reply 109
**Author**: Swati Kapoor
**Posted**: 2025-02-07T10:30:52.807Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/118

Even I’m getting a similar error in Q2, it is expecting a foreign title whereas my search result gives only English titles.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a question and a JSON data structure, along with an error message. The JSON data is presented within a red-bordered box. There's also a scrollbar on the right side of the red box.

**2. Any text content visible:**

*   **Question:** "What is the JSON data?"
*   **JSON Data:**
    *   `"id": "tt8712204"`
    *   `"title": "25. Batwoman"`
    *   `"year": "2019-2022"`
    *   `"rating": "3.6"`
*   **Error Message:** "Error: At \[12].title: Values don't match. Expected: "13. Pídeme lo que quieras". Actual: "13. Ask Me What You Want""

**3. The context or purpose of what's displayed:**

The image likely represents a scenario where a system is validating JSON data against an expected format or value. The question "What is the JSON data?" suggests that the user is being asked to identify or understand the structure and content of the JSON. The error message indicates that the "title" field in the JSON data did not match the expected value during validation. The expected value is in Spanish ("Pídeme lo que quieras"), while the actual value is in English ("Ask Me What You Want").

**4. Technical details:**

*   **JSON:** The JSON data represents information about a movie or TV show, including its ID, title, year of release/airing, and rating.
*   **Error Message:** The error message indicates a data validation failure. The `[12].title` part suggests that the error occurred at the 12th element (likely in a list or array) and specifically in the "title" field. The "Expected" and "Actual" values highlight the mismatch that caused the error. This suggests a localization or translation issue, where the system expected the title to be in Spanish but received it in English.

Please help.

---

## Reply 110
**Author**: Siddhardh Devulapalli
**Posted**: 2025-02-07T11:06:49.504Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/119

I think the idea behind this font is to make it difficult for people to manually work on the markdown file from scratch. I guess they want us to use the tools (like PyMuPDF4LLM, markitdown) they provided as resources to convert pdf into a markdown and then may be we can do some manual intervention to make it to the result as the scraping tools are not 100% accurate.

Could be another reason too. TAs’ can feel free to pitch in.

---

## Reply 111
**Author**: Carlton D'Silva
**Posted**: 2025-02-07T15:06:56.278Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/120

A post was merged into an existing topic: [Tds: assignment is not submitting](/t/tds-assignment-is-not-submitting/166189/21)

---

## Reply 112
**Author**: Ansh bansal
**Posted**: 2025-02-07T15:08:16.074Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/121

your last saved score (i.e.6 of your’s) will be official score and forgot about seek portal , it is not meant for this type of assignment.

---

## Reply 113
**Author**: Yashvardhan
**Posted**: 2025-02-07T15:34:36.903Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/122

Thank you for the update! I gave Q10 another shot, and I was able to solve it this time. The more liberal checks and improved error messages made a big difference in understanding where I was going wrong.

Thank again.

---

## Reply 114
**Author**: Akshit Mittal
**Posted**: 2025-02-07T15:49:48.266Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/123

Can we use hacking to get answers to some questions? Has anyone ever done it?

---

## Reply 115
**Author**: Peter Paul Pooppally
**Posted**: 2025-02-07T16:00:15.001Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/124

What format is required for the “missing links” here

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a web application or a document processing tool. It displays text content, including a title, a description of the exercise, a list of benefits, a question, a code snippet, and an error message. There's also a scrollbar on the right side of the code snippet area.

**2. Any text content visible:**

*   **Title:** "Impact"
*   **Description:** "By completing this exercise, you will contribute to EduDocs Inc.'s mission of providing high-quality, accessible educational resources. Automating the PDF to Markdown conversion and ensuring consistent formatting:"
*   **List of benefits:**
    *   "Enhances Productivity: Reduces the time and effort required to prepare documentation for clients."
    *   "Improves Quality: Ensures all documents adhere to standardized formatting, enhancing readability and professionalism."
    *   "Supports Scalability: Enables EduDocs to handle larger volumes of documentation without compromising on quality."
    *   "Facilitates Integration: Makes it easier to integrate Markdown-formatted documents into various digital platforms and content management systems."
*   **Question:** "What is the markdown content of the PDF, formatted with prettier@3.4.2?"
*   **Code snippet:**
    *   "Audax teneo centum cilicium vigor venio."
    *   "Patria credo tonsor."
    *   "Defessus pax volup vomito creator video campana cedo vita votum."
    *   "Laudantium victoria aer via tepidus."
    *   "Adulescens corporis triumphus coruscus sordeo trans dolorum."
    *   "..."
*   **Error message:** "Error: Missing links"
*   **Additional text:** "It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things."

**3. The context or purpose of what's displayed:**

The image appears to be part of an educational exercise or a challenge related to converting PDF documents into Markdown format. The exercise aims to highlight the benefits of automating this process and the difficulties involved in achieving accurate Markdown output from

Here is my markdown

- statua demulceo amaritudo tametsi

- tam ante

- dens spiritus

- thema succurro sollers audio

Conforto conor tum deputo caecus cervus coepi aegrotatio totam xiphias. Repudiandae ducimus acerbitas ademptio . Delectatio tamquam suus.

Centum usitas tamen cedo auctus turpis video clibanus. Correptius beatus crepusculum decens succedo alias aperte decumbo trado. Talio universe deduco caute sui u

vester undique

- subito umbra

- caritas saepe

- taceo concido bos

Tenetur exercitationem numquam ultio tyrannus aeger vindico. Subvenio ambulo vacuus. Quidem quam tactus tracto aureus cupiditas.

thema astrum

# Spero uter

Harum cometes damnatio theologus virgo aperiam velut cursim.

**venustaspeccatus adsum**

acidus quisquam torrens

clam adeptio virga

Depulso claro consectetur concedo aveho bis pectus traho nobis. Cura adicio colligo corporis eligendi soluta ducimus carus. Allatus sapiente summa atqui deludo cur

Terebro vallum rem velociter currus suppellex.

Viduo damno ustilo valetudo.

Tribuo una vorago sui testimonium angelus suscipio eius demulceo civis.

Delectus coniecto repellendus amoveo amissio incidunt

Audax teneo centum cilicium vigor venio.

Patria credo tonsor.

Defessus pax volup vomito creator video campana cedo vita votum.

Laudantium victoria aer via tepidus.

Adulescens corporis triumphus coruscus sordeo trans dolorum.

- doloremque cum allatus aduro

- inventore thalassinus

- aperiam tergiversatio

- contigo alienus aranea cito cogo

Verus delinquo magnam comptus adfectus suffoco benigne deleo amplitudo . Cura deleniti theologus vestigium aranea denique vester doloribus . Venio cimentarius cr

depereo subvenio

---

---

## Reply 116
**Author**: Yashvardhan
**Posted**: 2025-02-07T16:24:40.970Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/125

In the pdf you see some blue color font for specific words write that word in format

[word](#)

---

## Reply 117
**Author**: NK
**Posted**: 2025-02-07T16:25:22.704Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/126

There are only four texts which look like link texts in the pdf.

All four properly coded in link markdown syntax, in the preview, they appear as  link texts same as in pdf.

Link text

Even after chaning all the 4 texts which appered in blue color in the pdf to link texts,

below error is still observed.

Error: Missing links

Did anyone else face same issue ?

Also, no text in the pdf looks like a code block.

But, Missing Code error was seen and after changing one of the paragraph by using markdown code syntax that error is gone.

Appreciate any suggestions on the link error.

---

## Reply 118
**Author**: Yashvardhan
**Posted**: 2025-02-07T16:33:35.165Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/127

Replace actual text to expected text until you got correct

---

## Reply 119
**Author**: Sanchay Naresh Gupta
**Posted**: 2025-02-07T16:44:13.037Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/128

same kind of error is arising with me too.Any suggestion what is wrong with it??

---

## Reply 120
**Author**: NK
**Posted**: 2025-02-07T16:51:10.877Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/129

the rating should be treated as string.

Format is as “2.9” instead of number 2.9

---

## Reply 121
**Author**: SHAON BALLAV
**Posted**: 2025-02-07T17:23:44.829Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/130

Yes it can be done. Got the 10th one correct by implementing breakpoint by printing the expected answer which is being used to validate the user answer in the js script.

---

## Reply 122
**Author**: GURVEER SINGH SEKHON
**Posted**: 2025-02-07T18:20:02.449Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/131

i am facing a similar issue

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from an interactive coding tutorial or exercise. It presents a code snippet (JSON format) and a question related to it. There are two code blocks, a question, an error message, and a "Check" button.

**2. Text Content:**

*   **"The output would look like this:"** (followed by a JSON code block)
*   **JSON Code Block 1:**
    *   `{`
    *   `"2025-01-01": "Sunny with scattered clouds",`
    *   `"2025-01-02": "Partly cloudy with a chance of rain",`
    *   `"2025-01-03": "Overcast skies",`
    *   `// ... additional days`
    *   `}`
*   **"What is the JSON weather forecast description for Shanghai?"**
*   **JSON Code Block 2:**
    *   `{`
    *   `"2025-02-07": "A clear sky and a moderate breeze",`
    *   `"2025-02-08": "Sunny and a moderate breeze",`
    *   `"2025-02-09": "Sunny and a gentle breeze",`
    *   `"2025-02-10": "Sunny and a gentle breeze",`
    *   `"2025-02-11": "Sunny intervals and a moderate breeze",`
    *   `}`
*   **"Error: At root: Different number of properties"**
*   **"Check"** (button)

**3. Context and Purpose:**

The image depicts a coding exercise where the user is asked to provide a JSON weather forecast description for Shanghai. The first code block shows an example of the expected output format. The second code block is the user's attempt at providing the forecast. The error message indicates that the user's JSON structure has an issue, specifically related to the number of properties at the root level. The "Check" button is likely

---

## Reply 123
**Author**: Shahil Khan
**Posted**: 2025-02-07T18:23:37.588Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/132

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page, likely from an online course or assignment platform. It displays UI elements such as:

*   A header with the due date, score, and buttons for "Check all" and "Save."
*   A question prompt with a link to a discussion forum.
*   Information about bonus marks for posting on a specific discussion thread.
*   User login information and a "Logout" button.
*   A section displaying recent saves with timestamps and scores.

**2. Text Content:**

Here's a breakdown of the visible text:

*   **Header:** "Due Sun, 9 Feb, 2025, 11:59 pm IST", "Score: 10/10", "Check all", "Save"
*   **Question Prompt:** "Have questions? Join the discussion on Discourse"
*   **Bonus Marks:** "Bonus marks for posting on Discourse", "To encourage discussions, IITM BS students who reply to the discussion on GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] with a relevant question or reply will get 1 bonus mark on this graded assignment."
*   **Login Information:** "You are logged in as 23f2005275@ds.study.iitm.ac.in.", "Logout"
*   **Recent Saves:** "Recent saves (most recent is your official score)", "Reload from 07/02/2025, 23:51:21. Score: 10", "Reload from 07/02/2025, 20:30:21. Score: 5", "Reload from 07/02/2025, 18:17:58. Score: 3"

**3. Context and Purpose:**

The image shows a student's view of an online assignment or quiz. The purpose of the page is to:

*   Inform the student about the assignment's due date and their current score.
*   Provide a way for the student to ask questions and participate in discussions.
*   Encourage participation in the discussion forum by offering bonus marks.

succesfully completed GA4 with 10/10 Marks

---

## Reply 124
**Author**: Daksh Agarwal
**Posted**: 2025-02-07T19:06:13.783Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/133

sir how will we know if we have been awarded with the bonus mark. Will it be reflected in our ga score and the marks would be 11/10 or will it be added later

---

## Reply 125
**Author**: Dabgar Milav Jayeshkumar
**Posted**: 2025-02-07T19:09:24.706Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/134

In Q2. getting , able to fix most of the errors but

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser window with two main sections:

*   **Left Side:** A list of movies from IMDb (Internet Movie Database). The list is filtered to show movies with user ratings between 4.0 and 8.0.
*   **Right Side:** The browser's developer console, specifically the "Console" tab. It displays a JSON array of movie data.

**2. Text Content Visible:**

*   **IMDb Movie List (Left Side):**
    *   "IMDb ratings: 4.0 to 8.0 X" (Indicates the applied filter)
    *   Movie titles, release years, runtimes, and ratings for several movies, including:
        *   "15. Anora" (2024, 2h 19m, R, Rating: 7.8, 86K votes, Metascore: 91)
        *   "16. Blink Twice" (2024, 1h 42m, R, Rating: 6.5, 87K votes, Metascore: 66)
        *   "17. Back in Action" (2025, 1h 54m, PG-13, Rating: 5.9, 40K votes, Metascore: 46)
        *   "18. Flight Risk" (2025, 1h 31m, R, Rating: 5.5, 6.8K votes, Metascore: 38)
        *   "19. The Recruit"
    *   Short plot summaries for each movie.
    *   "Back to top" button.
*   **Developer Console (Right Side):**
    *   JSON data with fields like "id", "title", "year", and "rating" for several movies. Examples:
        *   `"id": "tt9218128", "title": "12. Gladiator II", "year": "2024", "rating": "6.6"`
        *   `"id": "tt3005

Error: At [18].title: Values don’t match. Expected: “19. Graymail”. Actual: “19. The Recruit”

this kind of errors for some titles, even though i only applied Rating filter and nothing else, then why i’m getting different titles then the test cases?

---

## Reply 126
**Author**: Sarang Tambe
**Posted**: 2025-02-07T19:28:00.399Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/135

Hello Sir, thank you for changing the question.

@carlton I’m getting the below error:

Words like https, webbed, impact are missing (or not separated as words). 

However, in the source PDF file itself these words are not available.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a UI element, likely from a code editor or a text processing tool. It displays two rows of words, separated by vertical bars. Below the words, there's an error message. Red wavy lines appear under some of the words in the first and second rows.

**2. Text Content:**

*   **First Row:**
    *   quos
    *   utrum
    *   tredecim
    *   valetudo
    *   cras
*   **Second Row:**
    *   videlicet
    *   laudantium
    *   aetas
    *   canis
    *   tantum
*   **Error Message:** "Error: Words like https, webbed, impact are missing (or not separated as words)"

**3. Context/Purpose:**

The image likely represents a text analysis or processing task. The words displayed might be part of a larger text corpus. The red wavy lines probably indicate potential errors or issues with the words, such as spelling mistakes or words not found in a dictionary. The error message suggests that the tool is having trouble identifying or separating certain words (like "https", "webbed", and "impact") within the text.

**4. Technical Details:**

*   The UI element has a dark background.
*   The words are displayed in a monospaced font.
*   The red wavy lines are a common visual cue for errors in text editors and word processors.
*   The vertical bars likely serve as delimiters or separators between the words.
*   The error message indicates a problem with word tokenization or recognition. The tool is unable to correctly identify or separate the words "https", "webbed", and "impact". This could be due to the tool's dictionary, the way it handles compound words, or the presence of special characters.

---

## Reply 127
**Author**: Mohd Atif
**Posted**: 2025-02-07T20:01:46.758Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/136

Copy the row name that is use to change and paste it in your answers

---

## Reply 128
**Author**: Debjeet Singha
**Posted**: 2025-02-07T20:38:38.238Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/137

the ranking changes from time to time. you might need to scrape the data again.

---

## Reply 129
**Author**: GURVEER SINGH SEKHON
**Posted**: 2025-02-07T20:46:04.301Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/138

i am facing issue in Q7.

I am using this command : “[https://api.github.com/search/users?q=location:Seattle+followers:](https://api.github.com/search/users?q=location:Seattle+followers:)>120&sort=created&order=desc”

and the output on evaluating is : 2011-05-07T08:30:48Z

But i am getting the error :

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a coding challenge or tutorial. It presents a task description, instructions, and an input field for the user to provide an answer. There's also feedback indicating whether the provided answer is correct or incorrect.

**2. Any text content visible:**

The text content includes:

*   **Task Description:** "Using the GitHub API, find all users located in the city Seattle with over 120 followers."
*   **Question:** "When was the newest user's GitHub profile created?"
*   **Instructions (numbered list):**
    1.  "API Integration and Data Retrieval: Leverage GitHub's search endpoints to query users by location and filter them by follower count."
    2.  "Data Processing: From the returned list of GitHub users, isolate those profiles that meet the specified criteria."
    3.  "Sort and Format: Identify the "newest" user by comparing the `created_at` dates provided in the user profile data. Format the account creation date in the ISO 8601 standard (e.g., "2024-01-01T00:00:00Z")."
*   **Section Title:** "Impact"
*   **Impact Description:** "By automating this data retrieval and filtering process, CodeConnect gains several strategic advantages:"
*   **Strategic Advantages (bullet points):**
    *   "Targeted Recruitment: Quickly identify new, promising talent in key regions, allowing for more focused and timely recruitment campaigns."
    *   "Competitive Intelligence: Stay updated on emerging trends within local developer communities and adjust talent acquisition strategies accordingly."
    *   "Efficiency: Automating repetitive data collection tasks frees up time for recruiters to focus on engagement and relationship-building."
    *   "Data-Driven Decisions: Leverage standardized and reliable data to support strategic business decisions in recruitment and market research."
*   **Input Prompt:** "Enter the date (ISO 8601, e.g. "2024-01-01T00:00:00Z") when the newest user joined GitHub."
*   **User Input:** "2011-05-07T

Can someone please help me on this ?

---

## Reply 130
**Author**: Debjeet Singha
**Posted**: 2025-02-07T22:02:11.674Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/139

I am also facing the same issue. What is the problem here?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for a coding exercise or assessment. It presents a problem description, an example output, a text input area for the user to provide a solution, and a "Check" button to evaluate the solution. There's also a score displayed at the top.

**2. Text Content:**

*   **Header:** "Due Sun, 9 Feb, 2025, 11:59 pm IST", "Score: 9/10", "Check all", "Save"
*   **Problem Description:**
    *   "1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for London. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city)."
    *   "2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId."
    *   "3. Data Transformation: Extract the issueDate and enhancedweatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each issueDate to its corresponding enhancedweatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedWeatherDescription."
*   **Example Output:**
    ```json
    {
    "2025-01-01": "Sunny with scattered clouds",
    "2025-01-02": "Partly cloudy with a chance of rain",
    "2025-01-03": "Overcast skies",
    // ... additional days
    }
    ```
*   **Question:** "What is the JSON weather forecast description for London?"
*   **User Input Area:** Contains a JSON-like structure with weather forecasts for specific dates in February 2025.
    ```json
    {
    "2025-02-17": "Sunny and light winds",
    "2025-02-18": "Sunny intervals and light winds",
    "2025-02-1

---

## Reply 131
**Author**: Anand S
**Posted**: 2025-02-08T03:23:12.990Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/140

@21F1005510 Actually, some IMDb titles have multiple names. For example, [The Recruit](https://www.imdb.com/title/tt16030542/) is [also known as Graymail in India](https://www.imdb.com/title/tt16030542/releaseinfo/?ref_=tt_dt_aka#akas). My server checks from a different region from yours. Hence the need for manual corrections for a few titles.

**Why didn’t I pick an exercise that could be fully automated?** Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

## Reply 132
**Author**: Anand S
**Posted**: 2025-02-08T03:31:12.813Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/141

To evaluate the bonus mark for replying to this Discourse topic, At around the time of the deadline, we’ll close this thread, load all posts here, and run this in the Console:

[...new Set($$('.names a[href^="/u/"]').map(d => d.textContent))]

… to get the Discourse IDs who posted. Then we’ll match it to the email IDs and pass it to the operations team who will add it to the portal by 2025-02-22T18:30:00Z.

---

## Reply 133
**Author**: Karthik V
**Posted**: 2025-02-08T04:54:21.666Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/142

I am getting the error in Q4 as “Error: At root: Property name mismatch”

what could me the cause of this error? Any please help.

@carlton

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a coding exercise or a learning platform. It presents a question, a code snippet (JSON data), an error message, and a "Check" button.

**2. Text Content:**

*   **Question:** "What is the JSON weather forecast description for Sao Paulo?"
*   **JSON Data:**
    ```json
    {
    "2025-02-08": "Partly cloudy and light winds",
    "2025-02-09": "Thundery showers and a gentle breeze",
    "2025-02-10": "Sunny and a gentle breeze",
    "2025-02-11": "Thundery showers and light winds",
    "2025-02-12": "Sunny intervals and a gentle breeze"
    }
    ```
*   **Error Message:** "Error: At root: Property name mismatch"
*   **Button:** "Check"

**3. Context and Purpose:**

The image depicts a scenario where a user is likely attempting to provide a JSON response to a question about a weather forecast for Sao Paulo. The JSON data represents a weather forecast for several days in February 2025. The error message suggests that the provided JSON structure or content does not match the expected format or data. The "Check" button is likely used to submit the user's answer for validation.

**4. Technical Details (JSON Data):**

*   The JSON data is a dictionary (or object) where the keys are dates in the format "YYYY-MM-DD" (e.g., "2025-02-08").
*   The values associated with each date key are strings describing the weather conditions for that day (e.g., "Partly cloudy and light winds").
*   The error message "Property name mismatch" indicates that the keys in the JSON data might not be what the system expects. It could be that the system expects a different date format, different keys altogether, or that the root element of the JSON is incorrect.

---

## Reply 134
**Author**: Sarang Tambe
**Posted**: 2025-02-08T05:37:22.199Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/143

This is the only thing which worked for me.

@carlton Sir, can I suggest to replace the snapshot of example output which expects the year to be an integer and the ratings as to be floats (instead of actual evaluation which expects them to be strings). Also, it would help to clarify that “Movie 1” should carry the numerical prefix as reported in IMDB.  The current example on the portal is:

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a snippet of code, specifically a JSON-like data structure. It appears to be an array of objects, where each object represents a movie.

**2. Any text content visible:**

The text content includes:

*   `[` and `]` : These are the opening and closing brackets of an array.
*   `{` and `}` : These are the opening and closing curly braces of an object.
*   `"id"`: A key representing the movie's ID.
*   `"tt1234567"`: A sample movie ID.
*   `"title"`: A key representing the movie's title.
*   `"Movie 1"`: A sample movie title.
*   `"year"`: A key representing the movie's release year.
*   `2021`: A sample release year.
*   `"rating"`: A key representing the movie's rating.
*   `5.8`: A sample movie rating.
*   `"tt7654321"`: Another sample movie ID.
*   `"Movie 2"`: Another sample movie title.
*   `2019`: Another sample release year.
*   `6.2`: Another sample movie rating.
*   `// ... more titles`: A comment indicating that there are more movie objects in the array that are not shown in the snippet.

**3. The context or purpose of what's displayed:**

The code snippet represents a dataset of movies, likely used for a movie database, API response, or configuration file. Each movie object contains information about its ID, title, release year, and rating. The comment suggests that the displayed data is only a portion of a larger dataset.

**4. Technical details:**

*   The data is structured in a key-value pair format, which is characteristic of JSON (JavaScript Object Notation).
*   The keys are enclosed in double quotes, and the values are either strings (movie ID, title), numbers (year, rating), or other data structures (like the array itself).
*   The code is likely intended to be machine-readable and easily parsed by programming languages.
*   The syntax

---

## Reply 135
**Author**: Naveen Yadav
**Posted**: 2025-02-08T05:52:49.272Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/144

Your dot of 2.9 may be the dot from alphabet or numeric one

Try to copy the value and then replace it

---

## Reply 136
**Author**: Naveen Yadav
**Posted**: 2025-02-08T05:55:01.173Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/145

Try to copy the error data

The problem might be off dot

check one dot is on right of m and other right of 0 in keyboard

these two dots may represent different meanings

---

## Reply 137
**Author**: Raj Rohit Singh
**Posted**: 2025-02-08T06:10:10.342Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/146

is it resolved?

i too am getting the same error,even if it was working fine yesterday.

---

## Reply 138
**Author**: Karthik V
**Posted**: 2025-02-08T06:13:28.798Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/147

https will be part of the link (provided ‘link’ is one of the checkpoints of evaluation)

---

## Reply 139
**Author**: LAKSHAY
**Posted**: 2025-02-08T06:40:39.010Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/148

Sir, In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I use different classes to extract values for various fields. Could there be any other element on the portal affecting this extraction?

In Q4, one of my classmates is encountering a “root property” error despite using the same extraction method as I do. Upon checking, I found that this issue occurs because the city’s time is displayed as the previous day compared to our time. The portal results seem to be based on the city’s actual time rather than IST.

I would appreciate your guidance on these issues.

---

## Reply 140
**Author**: Anand S
**Posted**: 2025-02-08T06:45:07.380Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/149

Good idea @23f2005138 and thanks. I fixed this. The example now reads:

[
  { "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
  { "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },

… with the year and ratings quoted.

---

## Reply 141
**Author**: Pradeep Mondal
**Posted**: 2025-02-08T07:56:59.322Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/150

lakshaygarg654:

In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I guess for the year part, there are certain series having multiple seasons, for which hyphenated “years” are given.

For the particular instance - `“2024–”`, it appears another season/part is announced, thats why it is written that way.

---

## Reply 142
**Author**: LAKSHAY
**Posted**: 2025-02-08T08:27:29.717Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/153

Thanks @21f2000709 for this information. I figure out where i made mistake. During writing console code I added to remove non numeric values in year field which i guess removed that hyphen (“–”). I will rectify that.

---

## Reply 143
**Author**: GOVARDHANAN N 
**Posted**: 2025-02-08T08:28:27.587Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/154

GA 4 Q2

My JSON matches the titles of the movies as in the website, but in portal it is showing error and expecting something different from what is given in the website. How to handle this ?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a movie listing, likely from a streaming service or movie database website. It includes the movie's poster, title, year of release, runtime, rating, user rating, and Metascore.

**2. Text Content:**

*   **Title:** "2. Winnie-the-Pooh: Blood and Honey"
*   **Year:** "2023"
*   **Runtime:** "1h 24m"
*   **Rating:** "Not Rated"
*   **User Rating:** "2.9 (33K)" (presumably out of 5 stars, based on 33,000 ratings)
*   **Action:** "Rate"
*   **Metascore:** "16"
*   **Movie Poster Text:** "WINNIE THE POOH BLOOD AND HONEY"

**3. Context and Purpose:**

The image is a snippet of a movie listing, designed to provide potential viewers with key information about the film. It allows users to quickly assess the movie's title, release year, duration, critical reception (Metascore), and user ratings before deciding whether to watch it.

**4. Technical Details:**

*   **UI Elements:** The image includes a movie poster thumbnail, text labels, and potentially interactive elements like a "Rate" button.
*   **Visual Hierarchy:** The movie title is prominent, followed by the year and runtime. The user rating and Metascore are also clearly displayed.
*   **Data Presentation:** The user rating is presented as a star rating and a numerical value with the number of ratings in parentheses. The Metascore is presented as a number.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a question and a JSON data structure, followed by an error message indicating a mismatch between expected and actual values. The "Expected" and "Actual" values are highlighted with red and green boxes, respectively.

**2. Text Content:**

*   **Question:** "What is the JSON data?"
*   **JSON Data:**
    ```json
    {
        "title": "25. Battlefield Earth",
        "year": "2000",
        "rating": "2.5"
    }
    ]
    ```
*   **Error Message:** "Error: At \[1].title: Values don't match. Expected: '2. Winnie the Pooh: Blood and Honey'. Actual: "2. Winnie-the-Pooh: Blood and Honey""

**3. Context/Purpose:**

The image likely represents a test case or validation scenario where a JSON data structure is being checked against expected values. The error message indicates that the "title" field in the JSON data at index \[1] does not match the expected value. The expected title is "2. Winnie the Pooh: Blood and Honey", but the actual title in the JSON data is "2. Winnie-the-Pooh: Blood and Honey".

**4. Technical Details:**

*   **JSON:** The image shows a simple JSON object with three key-value pairs: "title", "year", and "rating".
*   **Error Message:** The error message indicates that the validation process is checking the "title" field at index \[1] of a JSON array (or a similar data structure). The error message highlights the expected and actual values that caused the mismatch.
*   **The difference between the expected and actual values is the quotation marks. The expected value is enclosed in single quotes, while the actual value is enclosed in double quotes.**
*   **The word "the" in "Winnie-the-Pooh" is underlined in blue.**

contradiction :

" 2. Winnie-the-Pooh: Blood and Honey" (in web page) & ( delivered by the JSON)

" 2. Winnie the Pooh: Blood and Honey" (expected in portal ) & ( raising error statement )

Regards

GOVADHANAN N

---

## Reply 144
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-08T08:40:07.981Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/155

so just exchange it.

---

## Reply 145
**Author**: GOVARDHANAN N 
**Posted**: 2025-02-08T08:44:44.640Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/156

Thanks for your response.

Many such titles have contradiction from what is expected and what is there in the website. This case the samples are 25 your approach is accepted to some extent, but on a larger sample space, need to work it right !

---

## Reply 146
**Author**: Yash Arabhavi
**Posted**: 2025-02-08T09:33:54.075Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/157

thanks for this, was wondering why it wasn’t working!

---

## Reply 147
**Author**: umra
**Posted**: 2025-02-08T09:48:12.602Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/158

**Image: question4**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of code or data, likely related to a weather forecast. It presents an example of a JSON-like structure and then asks a question about a specific weather forecast.  There's also an error message at the bottom.

**2. Text Content:**

*   **"The output would look like this:"** - This introduces an example of the expected data format.
*   **JSON-like structure:**
    *   `{`
    *   `"2025-01-01": "Sunny with scattered clouds",`
    *   `"2025-01-02": "Partly cloudy with a chance of rain",`
    *   `"2025-01-03": "Overcast skies",`
    *   `// ... additional days`
    *   `}`
*   **"What is the JSON weather forecast description for Kuala Lumpur?"** - This is the question being posed.
*   `{"2025-02-01": "Thundery showers and light winds"}` - This is the provided answer.
*   **"Error: At root: Different number of properties"** - This indicates an error related to the structure of the JSON data.

**3. Context and Purpose:**

The image appears to be part of a coding exercise or a problem-solving scenario. The goal is likely to understand the structure of the JSON data representing weather forecasts and then provide the correct forecast for a specific location (Kuala Lumpur). The error message suggests that the provided answer doesn't conform to the expected format.

**4. Technical Details:**

*   **JSON-like structure:** The example shows a JSON object where keys are dates (in "YYYY-MM-DD" format) and values are weather descriptions.
*   **Error Message:** The "Different number of properties" error suggests that the expected JSON structure might require more than one key-value pair (e.g., forecasts for multiple days), while the provided answer only includes one. It could also indicate that the structure is expecting a different format altogether.

sir,  we are getting this error. My  Actual output is after get request on the given api i get only one day forcast data. I have show in above image

---

## Reply 148
**Author**: Tanya kamboj
**Posted**: 2025-02-08T11:45:56.252Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/159

yes replace manually until you got correct ans . Error will suggest you what to change.

---

## Reply 149
**Author**: Arya Agrahari 
**Posted**: 2025-02-08T12:13:42.491Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/160

{

“2025-02-08”: “Light snow and light winds”,

“2025-02-09”: “Light snow and light winds”,

“2025-02-10”: “Light cloud and light winds”,

“2025-02-11”: “Sunny intervals and a gentle breeze”,

“2025-02-12”: “Sunny and light winds”,

“2025-02-13”: “Sunny and light winds”,

“2025-02-14”: “Light snow and a gentle breeze”,

“2025-02-15”: “Light snow and a gentle breeze”,

“2025-02-16”: “Sleet and a gentle breeze”,

“2025-02-17”: “Light rain and a gentle breeze”,

“2025-02-18”: “Light rain showers and a gentle breeze”,

“2025-02-19”: “Drizzle and a gentle breeze”,

“2025-02-20”: “Light rain and light winds”,

“2025-02-21”: “Light rain and light winds”

}

i got this after running my python script for question 4 but, got

Error: At root: Property name mismatch" this error message

---

## Reply 150
**Author**: Saravanan
**Posted**: 2025-02-08T12:25:18.374Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/161

@s.anand sir,

I don’t understand this error. In the website, the movie name doesn’t have a colon “:”, but in the result it is expecting so.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of JSON data, likely representing movie information.  Below the JSON snippet, there's an error message. The JSON data is enclosed in a red rounded rectangle.

**2. Text Content:**

*   **JSON Data:**
    *   `"id": "tt8790086"`
    *   `"title": "11. Kraven the Hunter"`
    *   `"year": "2024"`
    *   `"rating": "5.4"`
*   **Error Message:**
    *   `Error: At [10].title: Values don't match. Expected: "11. Kraven: The Hunter". Actual: "11. Kraven the Hunter"`

**3. Context/Purpose:**

The image likely shows the result of a data validation or comparison process. The JSON data represents the actual data being processed. The error message indicates that the value of the "title" field at index 10 in a larger dataset does not match the expected value.

**4. Technical Details:**

*   **JSON:** The data is formatted as JSON (JavaScript Object Notation), a common format for data exchange.
*   **Data Validation:** The error message suggests that a data validation process is in place to ensure data consistency.
*   **Error Analysis:** The error message points to a discrepancy in the "title" field, specifically at index \[10] of a larger dataset. The error message indicates that the expected and actual values are the same, which is strange. This could be a bug in the validation logic, or a subtle difference in the strings that isn't immediately apparent (e.g., whitespace, encoding issues).

---

## Reply 151
**Author**: LAKSHAY
**Posted**: 2025-02-08T12:27:12.734Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/162

For this question, you may use the Google Colab file referenced in the assignment. This file will provide you with the date and description. Additionally, you can generate a weather location ID for the city specified in your assignment. Using this ID, you will obtain the weather URL, which you can then use to verify the date and description.

---

## Reply 152
**Author**: Tanya kamboj
**Posted**: 2025-02-08T13:13:07.988Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/163

here is the difference of  ‘:’ in the expected ans. so make it manually correct . i did the same and got correct ans .

and in the question also it is mentioned that may be manually you need to correct.  just give a try.

---

## Reply 153
**Author**: Tanya kamboj
**Posted**: 2025-02-08T13:14:34.661Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/164

run your console script again and match the description.

---

## Reply 154
**Author**: Tanya kamboj
**Posted**: 2025-02-08T13:15:53.963Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/165

yes, same happened with me . correct it manually.

---

## Reply 155
**Author**: Chandapara Atul Ramabhai 
**Posted**: 2025-02-08T13:20:13.430Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/166

In q10 links are not accessible through pdf and also creating problems while converting to markdown

---

## Reply 156
**Author**: Akash Kumar
**Posted**: 2025-02-08T13:26:41.508Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/167

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from an interactive coding tutorial or challenge. It presents a task related to weather data integration for a company called "AgroTech Insights." The UI includes:

*   **Instructions:** Text explaining the task and steps involved.
*   **Example Output:** A code snippet showing the expected format of the output.
*   **Input Field:** A text area where the user can enter their code or solution.
*   **Check Button:** A button to submit the solution for evaluation.

**2. Text Content:**

The image contains the following text:

*   **Title:** "Weather Data Integration for AgroTech Insights"
*   **Introduction:** A paragraph describing AgroTech Insights and the importance of weather data.
*   **Task Description:**
    *   "As part of this initiative, you are tasked with developing a system that automates the following:"
    *   "1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Manila. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city)."
    *   "2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId."
    *   "3. Data Transformation: Extract the issueDate and enhancedweatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each issueDate to its corresponding enhancedweatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedweatherDescription."
*   **Example Output:**
    *   `{`
    *   `"2025-01-01": "Sunny with scattered clouds"`
    *   `"2025-01-02": "Partly cloudy with a chance of rain"`
    *   `"2025-01-03": "Overcast skies"`
    *   `// ... additional days`
    *   `}`
*   **Question:** "What is the JSON weather forecast description for Manila?"
*   

Why question 4 starts failing. It was working correct yesterday. Because of it I am getting 9/10 marks.

---

## Reply 157
**Author**: GOVARDHANAN N 
**Posted**: 2025-02-08T13:53:07.468Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/168

The result is dynamic with changes made in the API. So try re-executing your code today and it will automatically solve. Your code is right ! Just make a re-run and things will work out  :slight_smile:

---

## Reply 158
**Author**: Adarsh kumar
**Posted**: 2025-02-08T13:56:29.524Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/169

try running the console again and it will work, make sure the data matches with the one in api as it changes regularly

---

## Reply 159
**Author**: Saravanan
**Posted**: 2025-02-08T14:00:19.459Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/170

Thanks!.

It is working now. I had to manually correct 5 movie titles to get it correct.

---

## Reply 160
**Author**: Deepanshu Tomar
**Posted**: 2025-02-08T14:12:53.748Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/171

**Image: Screenshot 2025-02-08 at 7.41.55 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code editor or a similar interface displaying JSON data. The JSON data appears to be a list of objects, with each object representing information about a movie or TV show. The interface also displays an error message related to the JSON data.

**2. Any text content visible:**

*   **Title:** "What is the JSON data?"
*   **JSON Data:**
    *   `},`
    *   `{`
    *   `"id": "tt10078772",`
    *   `"title": "9. Flight Risk",`
    *   `"year": "2025",`
    *   `"rating": "5.5"`
*   **Error Message:** "Error: At \[10].year: Values don't match. Expected: "2025-". Actual: "2025-"

**3. The context or purpose of what's displayed:**

The image likely represents a scenario where JSON data is being validated or parsed. The error message indicates that there's a mismatch between the expected value and the actual value for the "year" field at a specific location (\[10]) in the JSON data. The purpose is to highlight an error in the JSON data that needs to be corrected.

**4. Technical details (code screenshot):**

*   The JSON data structure consists of key-value pairs.
*   The keys are enclosed in double quotes (e.g., "id", "title", "year", "rating").
*   The values are strings (e.g., "tt10078772", "9. Flight Risk"), numbers (e.g., 5.5), or other JSON objects/arrays.
*   The error message suggests that the expected value for the "year" field should have a hyphen at the end ("2025-"), but the actual value does not.
*   The error message also indicates that the error is located at index 10 of the array.

What 's the solution?

---

## Reply 161
**Author**: Neelakandan R
**Posted**: 2025-02-08T14:15:05.761Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/172

Titles (from the output json) should be replaced by the titles which shows in the error message “Expected”. It can only be done manually. There may be multiple titles need to be translated by this method.

Please refer the instruction.

**Image: 1000095240**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a UI element, likely a notification or alert box within a software application or website. It contains a message and a button.

**2. Text Content:**

The text content is as follows:

*   "IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code."
*   "Check" (on a button)

**3. Context/Purpose:**

The message indicates that the user is likely interacting with a tool or application that scrapes data from IMDb (Internet Movie Database). The message warns the user that:

*   IMDb search results can vary based on the user's geographical region.
*   Manual translation of titles might be necessary.
*   The data on IMDb can change over time, requiring the user to re-run their scraper code to get updated information.

The "Check" button likely serves as an acknowledgment or confirmation button, perhaps to dismiss the message or proceed with the scraping process.

**4. Technical Details:**

The message refers to "scraper code," which implies the user is using a program or script to automatically extract data from the IMDb website. The message is a warning about the potential inconsistencies and dynamic nature of the data source.

---

## Reply 162
**Author**: Preethika Ranganathan
**Posted**: 2025-02-08T14:15:27.390Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/173

you can manually add space after the hyphen

---

## Reply 163
**Author**: Rajalakshmi Rathinasabhapathy
**Posted**: 2025-02-08T15:27:30.122Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/174

I face the same error, also thinking of issueDate, the value seems to be constant in every loop inside forecasts array (is it because the data is issed on that particular date) that gives same issue date key across the json outcome. Anyways the new json with same issueDate also gives the same Root error

---

## Reply 164
**Author**: Harshit Chaturvedi
**Posted**: 2025-02-08T16:50:28.081Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/175

Double-check that the rating field in the JSON is indeed a float (`2.9`) and not a string (`"2.9"`) in your code.

---

## Reply 165
**Author**: Shambhavi Verma
**Posted**: 2025-02-08T16:55:58.503Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/176

That is perhaps to ensure we don’t manually write the markdown for the pdf. Converting the pdf to markdown and getting the correct output is extremely hard, I tried doing that multiple times yet wasn’t able to get that right by the original method.

But since it is mentioned that the GAA is hackable and we are allowed to do so, for some of the questions, therefore you can try solving that by establishing a breakpoint in the sources and then write the code in the console to get the expected output.

---

## Reply 166
**Author**: Shambhavi Verma
**Posted**: 2025-02-08T17:02:30.525Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/177

Write the code referencing the provided collab file and make sure to use the API key

The output actually changes once in a while so you might need to run the code a few times before getting in right

[https://tds.s-anand.net/#/bbc-weather-api-with-python](https://tds.s-anand.net/#/bbc-weather-api-with-python)

---

## Reply 167
**Author**: JOHANA PRISCY JOHN PONRAJ 
**Posted**: 2025-02-08T18:05:32.112Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/178

your most recently saved score will be evaluated

---

## Reply 168
**Author**: Avinash Kumar
**Posted**: 2025-02-08T18:26:01.657Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/179

I am getting this error again and again after running the code in collab this city  `Nur-Sultan`?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code traceback, specifically an error message from a Python environment (likely Jupyter Notebook or a similar interactive Python interpreter). It displays a `NameError` indicating that a variable named `location_id` is not defined.

**2. Any text content visible:**

*   **Error:** Could not find location ID for Nur-Sultan
*   **NameError**
*   **Traceback (most recent call last)**
*   ` in ()`
*   `33`
*   `34 # BBC Weather URL`
*   `---> 35 weather_url = f'https://www.bbc.com/weather/{location id}'`
*   `36`
*   `37 # Fetch weather data`
*   **NameError: name 'location_id' is not defined**

**3. The context or purpose of what's displayed:**

The code snippet is attempting to construct a URL for the BBC Weather website. The URL is intended to include a `location_id` to specify the city for which weather information is being requested. The error message indicates that the variable `location_id` has not been assigned a value before being used in the f-string to create the `weather_url`. The initial error message "Could not find location ID for Nur-Sultan" suggests that the code is trying to find or retrieve a location ID for the city of Nur-Sultan, but it's failing to do so, leading to the `NameError` when the undefined variable is used.

**4. Technical details (code screenshot):**

*   The code is written in Python.
*   The traceback indicates the error occurred on line 35 of a cell in an IPython environment.
*   Line 34 is a comment indicating the purpose of the following line: "# BBC Weather URL".
*   Line 35 attempts to create a URL using an f-string. The f-string includes a placeholder `{location id}` which is intended to be replaced with the value of the `location_id` variable.
*   Line 37 is a comment indicating the

---

## Reply 169
**Author**: Muhammed Adhil Pt
**Posted**: 2025-02-08T18:38:24.317Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/180

In the second question are we supposed to edit the JSON manually until we reach a correct answer ? I think the expected result has some difference from what shows up in the website

---

## Reply 170
**Author**: Raghusrini
**Posted**: 2025-02-08T18:44:53.523Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/181

Not able to get the missing links in Q10

Any suggestions welcome please

---

## Reply 171
**Author**: Anushka Ghosh
**Posted**: 2025-02-08T19:11:13.889Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/182

For question 10 I’ve tried everything. Links and headings work fine, but I’m not able to fix the “missing tables” issue (I’ve also tried using pdfplumber and tabulate). In the pdf as well, I don’t see any tables, any hints or suggestions would be very helpful. Thanks!

---

## Reply 172
**Author**: Jayesh Bansal
**Posted**: 2025-02-08T19:15:03.641Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/184

there is no location id mentioned as it is mentioned of the different city. please check the city for which you need to find the location id and then proceed

---

## Reply 173
**Author**: Swati Kapoor
**Posted**: 2025-02-08T19:19:06.435Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/185

I’m getting the same error in Q4:

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from an interactive coding tutorial or a coding challenge platform. It presents a code snippet, a question, a text input area, and a "Check" button. There's also an error message displayed.

**2. Text Content:**

*   **"The output would look like this:"** This indicates that the following code snippet is an example of the expected output.
*   **Code Snippet (JSON-like):**
    ```json
    {
        "2025-01-01": "Sunny with scattered clouds",
        "2025-01-02": "Partly cloudy with a chance of rain",
        "2025-01-03": "Overcast skies",
        // ... additional days
    }
    ```
*   **"What is the JSON weather forecast description for Los Angeles?"** This is the question being posed to the user.
*   **Text Input Area (with user's attempt):**
    ```json
    {
        "25-02-16": "Sunny and light winds",
        "25-02-17": "Sunny and light winds",
        "25-02-18": "Sunny and light winds",
        "25-02-19": "Sunny and light winds",
        "25-02-20": "Sunny and light winds",
        "25-02-21": "Sunny and light winds"
    }
    ```
*   **Error Message:** "Error: At root: Property name mismatch"
*   **"Check"** (Button label)

**3. Context and Purpose:**

The image depicts a coding exercise where the user is asked to provide a JSON representation of a weather forecast for Los Angeles. The first code snippet shows the expected format of the JSON output. The user has attempted to provide the JSON data in the text input area. The error message indicates that the user's JSON structure has a "Property name mismatch" error, meaning the keys in the JSON are not in the expected format.

**4. Technical Details (Code Sni

---

## Reply 174
**Author**: Harsh Raj
**Posted**: 2025-02-08T19:39:26.546Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/186

How to actually do the HNRSS one…i can’t find much.

---

## Reply 175
**Author**: Harsh Raj
**Posted**: 2025-02-08T19:40:40.906Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/187

How did u do the links? I’m unable to do links

---

## Reply 176
**Author**: Tanmay Sahu
**Posted**: 2025-02-08T20:31:47.253Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/188

Just copy paste the expected value in place of actual value in json. Keep doing this eventually it would be the answer would be correct.

This is a format issue when the json is scrapped from the browser.

---

## Reply 177
**Author**: Koustubh Ramakrishnan
**Posted**: 2025-02-08T21:53:13.622Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/189

Request help on Q4 aboutBBC weather data, the instructions in the question tell us to use BBC broker API and get issueDate & enhancedWeatherdescription value pairs. However, it seems there are only 2 unique values of issueDate (not the expected 14 days)

Please clarify, sharing code and output below for reference.

Code:

import requests

url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/" + getlocid('Bogota')
response = requests.get(url)
json_data=response.json()
print(f"The number of days data is {len(json_data['forecasts'])}")

weather_data = {}

for i in range(len(json_data['forecasts'])): # Use range to create an iterable sequence of indices
  issue_date = json_data['forecasts'][i]['summary']['issueDate']
  weather_description = json_data['forecasts'][i]['summary']['report']['enhancedWeatherDescription']
  weather_data[issue_date]=weather_description
  print("Iteration No. " + str(i))
  print(issue_date)
  print(weather_description)
  
print("Final Weather Data json below")
print(weather_data)

Output

The number of days data is 14
Iteration No. 0
2025-02-08T04:00:00-05:00
Light rain showers and a gentle breeze
Iteration No. 1
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 2
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 3
2025-02-08T04:00:00-05:00
Thundery showers and light winds
Iteration No. 4
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 5
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 6
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 7
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 8
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 9
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 10
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 11
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 12
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 13
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Final Weather Data json below
{'2025-02-08T04:00:00-05:00': 'Thundery showers and a gentle breeze', '2025-02-08T16:01:58-05:00': 'Thundery showers and a gentle breeze'}

Edit: For now, I have worked around with code posted by @21f3002277. But the doubt about the question remains

---

## Reply 178
**Author**: Suhani Thakur
**Posted**: 2025-02-08T23:18:04.439Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/190

same with me. In the project it is written that the form should be submitted but there’s no question in the portal.

---

## Reply 179
**Author**: Rajalakshmi Rathinasabhapathy
**Posted**: 2025-02-09T00:48:22.810Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/191

I have got the same error as well, verified there are workflows run in my repo/actions/runs

When I checked the reasons, it could be due to API limit exceeded in a hour, but tried even after some time but no workflows found.

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Header:** "All workflows" with a subtitle "Showing runs from all workflows".
*   **Search Bar:** A search bar with the placeholder text "Filter workflow runs".
*   **Feedback Prompt:** A dark-themed box prompting the user to "Help us improve GitHub Actions" by answering three quick questions. It includes a "Give feedback" button and a close ("X") button.
*   **Workflow Runs List:** A section titled "2 workflow runs".
*   **Table Headers:** Column headers for the workflow runs list: "Event", "Status", "Branch", and "Actor".
*   **Workflow Run Entries:** Two entries representing workflow runs. Each entry includes:
    *   A green checkmark indicating success.
    *   The workflow name "Action runs everyday".
    *   A description of the run (e.g., "Action runs everyday #6: Scheduled").
    *   The branch name "main".
    *   A timestamp indicating when the run occurred (e.g., "2 hours ago").
    *   The duration of the run (e.g., "15s").
    *   A three-dot menu (likely for more options).

**2. Text Content:**

*   "All workflows"
*   "Showing runs from all workflows"
*   "Filter workflow runs"
*   "Help us improve GitHub Actions"
*   "Tell us how to make GitHub Actions work better for you with three quick questions."
*   "Give feedback"
*   "X" (close button)
*   "2 workflow runs"
*   "Event"
*   "Status"
*   "Branch"
*   "Actor"
*   "Action runs everyday"
*   "Action runs everyday #6: Scheduled"
*   "Action runs everyday #5: Manually run by Rajalakshmi12"
*   "main" (branch name)
*   "2 hours ago"
*   "15s"
*   "14s"

**3. Context/Purpose:**

The image shows a user interface for viewing and managing workflow runs in a GitHub repository. The user is presented with a list of recent workflow executions, their status,

---

## Reply 180
**Author**: K Hari Prasath
**Posted**: 2025-02-09T01:05:38.835Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/192

Manual correction will not work. Try to extract - from the console. I did it like that it was not working then I extracted from console then it worked

---

## Reply 181
**Author**: K Hari Prasath
**Posted**: 2025-02-09T01:12:34.834Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/193

Please ensure that your .yml file should have step name as your email Id. then Manually trigger the task (don’t wait till the scheduled time), ensure it was committed within 5 minutes and that commit should be top most item in all workflows. Then check it, it will work

---

## Reply 182
**Author**: K Hari Prasath
**Posted**: 2025-02-09T01:30:53.176Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/194

You can find some text blue in color and underline use some dumy url it will work

---

## Reply 183
**Author**: K Hari Prasath
**Posted**: 2025-02-09T01:35:35.603Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/195

You can find some lines having second, third words are uniformly aligned. Those are tables

---

## Reply 184
**Author**: Suhani Thakur
**Posted**: 2025-02-09T02:30:28.306Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/196

When I resave the questions, the previously correct questions turn wrong which is extremely frustrating and time taking. I wish there is an option which saves the correct answer and does not require us to have multiple processes running in our pc even after getting the answer right previously.

---

## Reply 185
**Author**: Udipth
**Posted**: 2025-02-09T02:41:28.911Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/197

In Q 6 I checked all the startups link at [Hacker News - Newest: "Startup"](https://hnrss.org/newest?q=Startup)… none is greater than 81 then how to submit that link… is there something i am missing

---

## Reply 186
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-02-09T03:33:18.398Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/198

@Jivraj @carlton ,for question 3, even a random response is shown correct

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a web application or a tutorial/testing platform. It presents a question, an input field for a URL, a validation indicator, and a "Check" button.

**2. Any text content visible:**

*   **"5. Enabling CORS:** Configure the web application to include appropriate CORS headers, allowing GET requests from any origin."
*   **"What is the URL of your API endpoint?"**
*   **"http://127.0.0.1:8000"** (This is pre-filled in the input field)
*   **"Correct"** (Indicates the provided URL is valid or meets the expected criteria)
*   **"We'll check by sending a request to this URL with ?country=... passing different countries."**
*   **"Check"** (Button label)

**3. The context or purpose of what's displayed:**

The UI is part of a process to verify that a web application has been correctly configured to handle Cross-Origin Resource Sharing (CORS). The user is asked to provide the URL of their API endpoint. The system then validates the URL and indicates that it's correct. It also explains that it will further test the API by sending requests with different country parameters. The "Check" button likely triggers the validation process.

**4. Technical details:**

*   **CORS (Cross-Origin Resource Sharing):** The context is about enabling CORS, which is a browser security feature that restricts web pages from making requests to a different domain than the one which served the web page.
*   **URL:** The provided URL `http://127.0.0.1:8000` is a local address, indicating that the API is likely running on the user's local machine on port 8000.
*   **Query Parameter:** The text "We'll check by sending a request to this URL with ?country=..." indicates that the system will append a query parameter named "country" to the URL to test the API's behavior with different country values.
*   **UI Elements:** The UI includes a text input field, a validation indicator (a green checkmark), and a

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Browser Window:** The image shows a portion of a web browser window.
*   **Address Bar:** The address bar is visible at the top, displaying the URL.
*   **Tab Bar:** There are multiple tabs open in the browser.
*   **Content Area:** The main content area of the browser displays the text "Pretty-print" and the number "44".

**2. Text Content:**

*   **Address Bar:** The URL in the address bar is "127.0.0.1:8000/?country=india". This indicates a local server running on port 8000, with a query parameter "country" set to "india".
*   **Tab Titles:** The tab titles visible are:
    *   "Mathematics for Da..."
    *   "BS-DS\_Jan 2025 Gr..."
    *   "Untitled1.ipynb - Co..."
    *   "Ch"
*   **Main Content:**
    *   "Pretty-print"
    *   "44"

**3. Context and Purpose:**

*   **Local Server:** The URL "127.0.0.1:8000" suggests that a local web server is running.
*   **Query Parameter:** The "?country=india" part of the URL indicates that the server is likely processing a request based on the country being "india".
*   **Output:** The "44" displayed in the content area is likely the output of the server-side code, possibly related to the "country" parameter. The "Pretty-print" text might be a label or title for the output.
*   **Development/Testing:** The presence of "Untitled1.ipynb" suggests that the user might be working in a Jupyter Notebook environment, possibly developing or testing the server-side code.

**4. Technical Details:**

*   **IP Address:** "127.0.0.1" is the loopback address, meaning the server is running on the same machine as the browser.
*   **Port:** "8000" is the port number the server is listening on.
*   **Query String:** "?country=india" is a query string

---

## Reply 187
**Author**: Ayush Kumar Shaw 
**Posted**: 2025-02-09T03:42:07.409Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/199

Sir I have solved  Q2, But a problem arises that, At the index 11, in the IMdb website it is listed “The Recruit” but it is showing Expected: “Graymail”.

**Image: problem**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a snippet of JSON data, followed by an error message. The JSON data appears to represent a list of movies or TV shows, each with an ID, title, year, and rating.

**2. Any text content visible:**

*   **JSON Data:**
    *   `{"id": "tt26584495", "title": "8. Companion", "year": "2025", "rating": "7.4" }`
    *   `{"id": "tt13406094", "title": "9. The White Lotus", "year": "2021- ", "rating": "8.0" }`
    *   `{"id": "tt26748649", "title": "10. High Potential", "year": "2024-", "rating": "7.6" }`
    *   `{"id": "tt28607951", "title": "11. Anora", "year": "2024", "rating": "7.8" }`
    *   `{"id": "tt16030542", "title": "12. The Recruit", "year": "2022-", "rating": "7.4" }`
    *   `{"id": "tt7597890", "title": "13. The Rookie", "year": "2018", "rating": "8.0" }`
*   **Error Message:**
    *   `Error: At [11].title: Values don't match. Expected: "12. Graymail". Actual: "12. The Recruit"`

**3. The context or purpose of what's displayed:**

The image likely shows a data validation error. The JSON data is being compared against an expected format or dataset. The error message indicates that the "title" field at index 11 (likely referring to the 12th entry in a larger dataset) does not match the expected value. The expected value is "12. Graymail", but the actual

How to fix this?

---

## Reply 188
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-02-09T03:45:34.625Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/200

you have to manually change for a few mismatch.

 s.anand:

@21F1005510 Actually, some IMDb titles have multiple names. For example, [The Recruit](https://www.imdb.com/title/tt16030542/) is [also known as Graymail in India](https://www.imdb.com/title/tt16030542/releaseinfo/?ref_=tt_dt_aka#akas). My server checks from a different region from yours. Hence the need for manual corrections for a few titles.

**Why didn’t I pick an exercise that could be fully automated?** Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

## Reply 189
**Author**: Shambhavi Verma
**Posted**: 2025-02-09T05:52:35.938Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/201

Yes …due to the location difference the search results are different for everyone therefore you need to adjust it accordingly

It might need around 6-7 amendments

---

## Reply 190
**Author**: Shambhavi Verma
**Posted**: 2025-02-09T06:13:36.894Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/203

The API is returning 14 days of forecast data, as evidenced by the output However, the issueDate values are not unique for each day. Instead, they represent the time when the forecast was issued or updated.

In your output, there are only two unique issueDate values:

2025-02-08T04:00:00-05:00

2025-02-08T16:01:58-05:00

This means the forecast was updated twice on February 8, 2025, once at 04:00 AM and again at 4:01 PM (both in EST timezone) …To get a unique weather description for each day, you  need to modify your approach by using the actual forecast day for each day instead.

---

## Reply 191
**Author**: Md Anzar Rabbani
**Posted**: 2025-02-09T06:20:28.925Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/204

While submitting solution, do I need to keep all the local servers running/local URLs like 127.0.0.0 stuff, else I am getting one question as correct & the other one mentions unable to fetch data!? So that means I need to run them in different different ports?

---

## Reply 192
**Author**: Manmeet Kaur
**Posted**: 2025-02-09T06:34:11.908Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/205

I posted this error message but now the first issue got resolved but I am still keeping it in my post so that if anyone faces same issue, they can try if they can fix it similar to how it worked for me.

Please help with the second issue.

For Q8, the workflow is running on Github and commiting the scraped results to the json file (which is so amazing for me btw!). But I am getting this error for my public repo.

How it got resolved: I set up fixed time for cron schedule instead of every 5 min. Now it works.

Error: No daily scheduled triggers found in workflows.

I had all correct results for Q1 to Q7 till yesterday but it keeps giving errors even when I reload same file for some questions. Do I need to keep addressing those errors or if once correct and saved, I can ignore those?

---

## Reply 193
**Author**: Abhay Sharma
**Posted**: 2025-02-09T06:45:07.273Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/206

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a question and a code snippet, followed by an error message. The code snippet appears to be a JSON array containing movie data.

**2. Text Content:**

*   **Question:** "What is the JSON data?"
*   **JSON Data:**
    *   `{ "id": "tt0060196", "title": "The Good, the Bad and the Ugly", "year": "1966", "`
    *   `{ "id": "tt0137523", "title": "Fight Club", "year": "1999", "rating": "8.8" },`
    *   `{ "id": "tt0120737", "title": "The Lord of the Rings: The Fellowship of the Ring"`
    *   `]`
*   **Error Message:** "Error: At \[0].id: Values don't match. Expected: "tt20221436". Actual: "tt0437179""

**3. Context and Purpose:**

The image likely comes from an automated testing or validation environment. The question "What is the JSON data?" suggests that the JSON data is being provided as input to a system or function. The error message indicates that the system expected a specific value for the "id" field in the first element of the JSON array (index 0), but it received a different value.

**4. Technical Details:**

*   **JSON Structure:** The JSON data is an array of objects. Each object represents a movie and has properties like "id", "title", "year", and "rating".
*   **Error Analysis:** The error message "At \[0].id: Values don't match" means that the value of the "id" field in the first object of the array is incorrect. The system expected the value "tt20221436", but it received "tt0437179". This suggests a data validation failure. The "tt" prefix likely refers to the IMDB ID format.
*   **Incomplete JSON:** The JSON is incomplete. The first object is missing a closing curly brace `}`. The

I have tried several times but still recieving this as error. Please help

---

## Reply 194
**Author**: Subramanian V
**Posted**: 2025-02-09T07:01:02.715Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/207

**Image: Screenshot 2025-02-09 at 12.28.48 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web development tutorial or exercise, combined with a browser's developer console. The top portion outlines the steps for building a simple API. The middle section is a form-like area where the user is prompted to enter the URL of their API endpoint. Below that is the browser's developer console, specifically the "Console" tab, displaying error messages.

**2. Text Content:**

*   **Instructions:**
    *   "API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that accepts a `country` query parameter."
    *   "Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML."
    *   "Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, lxml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6) from the page, maintaining order."
    *   "Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #."
    *   "Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin."
    *   "What is the URL of your API endpoint?"
    *   "We'll check by sending a request to this URL with `?country=...` passing different countries."
*   **Input Field:**
    *   `http://localhost:8000/api/outline`
*   **Error Message:**
    *   `TypeError: Load failed`
*   **Button:**
    *   `Check`
*   **Console Errors:**
    *   `[blocked] The page at https://exam.sanand.workers.dev/tds-2025-01-ga4 requested insecure content from http://localhost:8000/api/outline?country=The+Bahamas. This content was blocked and must`
    *   `Not allowed to request resource`
    *   `Fetch API cannot load http://localhost:8000/api/outline?country=The+Bahamas due to access control checks.`

I’m able to see the markdown response for different countries for question 3, GA 4 on my browser but I’m unable to submit it probably because of network issues. Can someone help me with a fix. Thank you.

---

## Reply 195
**Author**: Shashank Tripathi
**Posted**: 2025-02-09T07:07:11.747Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/208

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, specifically a text box containing JSON data, along with instructions and error messages related to a task or assignment. The context appears to be a programming or data-related exercise.

**2. Any text content visible:**

*   **Instructions:**
    *   "4. Submit: Submit the JSON data in the text box below."
    *   "Impact: By completing this assignment, you'll simulate a key component of a streaming service's content acquisition strategy. Your work will enable StreamFlix to make informed decisions about which titles to license, ensuring that their catalog remains both diverse and aligned with subscriber preferences. This, in turn, contributes to improved customer satisfaction and retention, driving the company's growth and success in a competitive market."
    *   "What is the JSON data?"
*   **JSON Data:**
    ```json
    {
        "id": "tt26584495",
        "title": "10. Companion - Die perfekte Begleitung",
        "year": "2025",
        "rating": "7.4"
    }
    ```
*   **Error Message:**
    *   "Error: At \[10].year: Values don't match. Expected: "2021-". Actual: "2021""
*   **Disclaimer:**
    *   "IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code."

**3. The context or purpose of what's displayed:**

The image depicts a step in an assignment where the user is expected to submit JSON data. The assignment simulates a content acquisition strategy for a streaming service (StreamFlix). The user is likely providing data about a movie or TV show. The error message indicates that the "year" value in the JSON data is incorrect, as it expects "2021-" but the actual value is "2021". The disclaimer suggests that the data source is IMDb, and there might be discrepancies due to regional differences or outdated information.

**4. Technical details (code screenshot):**

*   **JSON Format:** The

how to tackle this error  as in 10 th movie year is 2025 but it is showing 2021

---

## Reply 196
**Author**: Avinash Kumar
**Posted**: 2025-02-09T07:21:17.635Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/209

City in my question is `Nur-Sultan` .When i search  `Nur-Sultan` city name in BBC weather page .its show nothing . when i search in google then show Nur Sultan become Astana . then i am going this city  name "Astana ". and got location id 1526273. after i run in collab then showing error.

**Image: WhatsApp Image 2025-02-09 at 12.42.40_7957510c**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a computer screen displaying Python code within what appears to be a Jupyter Notebook or similar interactive coding environment.  An error traceback is also visible, indicating a problem during code execution. The bottom of the screen shows the Windows taskbar.

**2. Text Content:**

*   **Python Code:**
    *   `datelist = pd.date_range(datetime.today(), periods=len(daily_summary_list)).tolist()`
    *   `datelist = [date.date().strftime('%Y-%m-%d') for date in datelist]`
    *   `# Map dates to descriptions`
    *   `weather_data = {date: desc for date, desc in zip(datelist, daily_summary_list)}`
    *   `# Convert to JSON`
    *   `weather_json = json.dumps(weather_data, indent=4)`
    *   `print(weather_json)`
    *   `# Fetch location data`
    *   `result = requests.get(location_url).json()`
    *   `weather_url = 'https://www.bbc.com/weather/' + result['response']['results']['results'][0]['id']`
    *   `# Fetch weather data`

*   **Error Message:**
    *   `IndexError`
    *   `Traceback (most recent call last)`
    *   ` in ()`
    *   `IndexError: list index out of range`

*   **Other Text:**
    *   `EN English (India)`
    *   `English (India)`
    *   `Finance headline`
    *   `India Foreign Ex...`
    *   `2s completed at 12:42 PM`
    *   `Search`

**3. Context and Purpose:**

The code appears to be related to fetching weather data. It likely involves:

1.  Generating a list of dates (`datelist`).
2.  Mapping dates to descriptions (presumably weather descriptions).
3.  Converting the data to JSON format.

---

## Reply 197
**Author**: Sathyavathi S 
**Posted**: 2025-02-09T07:49:44.486Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/210

this error comes, whenever you answer the other ones and click save. Please answer this question lastly, and submit immediately. it changes within a second. If it continues means, do manual correction and change according to the “expected”

---

## Reply 198
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-09T07:49:53.990Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/211

while searching dont put any other filter other than asked in Problem statement.

---

## Reply 199
**Author**: Sathyavathi S 
**Posted**: 2025-02-09T07:54:08.648Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/212

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays what appears to be a question or prompt related to converting a PDF into Markdown format. It shows a snippet of text that is supposedly the Markdown content extracted from a PDF, formatted using "prettier@3.4.2". There are also error messages and explanatory text related to the difficulty of this conversion.

**2. Any text content visible:**

*   **Question:** "What is the markdown content of the PDF, formatted with prettier@3.4.2?"
*   **Markdown Snippet:**
    *   "# Pauci Audentia Sperno Eum"
    *   "Tracto adeptio somnus. Neque tantum desidero porro est civitas caute laboriosam valetudo."
    *   "## Key Points"
    *   "- Vomito antiquus consequuntur"
    *   "- Amplus curis subnecto"
*   **Error Message:** "Error: Words like back, legislature, info are missing (or not separated as words)"
*   **Explanatory Text:** "It is *very hard* to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things."

**3. The context or purpose of what's displayed:**

The image is likely part of a test or challenge related to natural language processing (NLP) or document processing. The goal is probably to assess the ability of a system to accurately extract Markdown content from a PDF, even when the PDF's structure or formatting is imperfect. The error message suggests that the extraction process has identified issues with word separation or missing information. The explanatory text indicates that the question is simplified to focus on basic Markdown elements.

**4. Technical details (based on the code snippet):**

*   The Markdown snippet includes:
    *   A level 1 heading ("# Pauci Audentia Sperno Eum")
    *   A paragraph of text ("Tracto adeptio somnus. Neque tantum desidero porro est civitas caute laboriosam valetudo.")
    *   A level 2 heading ("## Key Points")
    *   A bulleted list with two items ("- Vomito antiquus consequuntur" and "- Am

Can anyone help me with the 10th question. Whatever I changed with the code , it is asking something. I checked that these words are not present in the pdf itself

---

## Reply 200
**Author**: PREMDEEP MAITI
**Posted**: 2025-02-09T08:06:59.795Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/213

I didn’t get any error for Astana.

The error may be due to incorrect loops in your code that’s why it’s going out of range, check for that.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a Jupyter Notebook interface, likely within a Google Colab environment. It displays code and output related to weather data scraping. The notebook is named "bbc-weather-scraping.ipynb".  There's a table-like display of weather data, followed by a code output showing a JSON representation of the same data.

**2. Any text content visible:**

*   **Notebook Title:** "bbc-weather-scraping.ipynb"
*   **Menu Bar:** "File", "Edit", "View", "Insert", "Runtime", "Tools", "Help"
*   **Toolbar:** "+ Code", "+ Text", "Copy to Drive"
*   **Data Table Columns:**
    *   Row numbers (7, 8, 9, 10, 11, 12, 13)
    *   Date (e.g., "25-02-16", "25-02-17", etc.)
    *   High Temperature (e.g., "-11°", "-7°", etc.)
    *   Low Temperature (e.g., "-14°", "-12°", etc.)
    *   Summary (e.g., "Thick cloud and a gentle breeze", "Light snow and a gentle breeze", etc.)
*   **Next Steps:** "Generate code with df", "View recommended plots", "New interactive sheet"
*   **Code Output:** "df.to\_json(orient='records')" followed by a long JSON string. The JSON string contains an array of objects, where each object represents a weather record with "Date", "High", "Low", and "Summary" keys. The degree symbol is represented as "\\u00b0".
*   **Other UI elements:** "Share", "RAM", "Disk", "Gemini"

**3. The context or purpose of what's displayed:**

The notebook is designed to scrape weather data, likely from the BBC website (implied by the filename). The table shows a preview of the scraped data. The `df.to_json(orient='records')` command suggests that the data is stored in a Pandas DataFrame (`df`) and is being converted to a JSON

---

## Reply 201
**Author**: LAKSHAY
**Posted**: 2025-02-09T08:14:05.998Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/214

It worked for me; only 4–5 values caused errors, which I fixed manually. Additionally, I corrected the console code, which now provides the correct result.

---

## Reply 202
**Author**: Naga durga prasad E
**Posted**: 2025-02-09T08:21:43.386Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/215

what is this magic trick… please elaborate …

Error: At [10].id: Values don't match. Expected: "tt16027074". Actual: "tt8008948"

i dont see that value in data …

---

## Reply 203
**Author**: PREMDEEP MAITI
**Posted**: 2025-02-09T08:32:10.545Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/216

You can manually edit that. I also have to manually edit one entry to get the correct answer.

---

## Reply 204
**Author**: Swati Kapoor
**Posted**: 2025-02-09T08:39:35.814Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/217

Hi,

As mentioned in the question, you have to sort by “joined” so it should be “[https://api.github.com/search/users?q=location:Seattle+followers:](https://api.github.com/search/users?q=location:Seattle+followers:)>120&sort=joined&order=desc”

---

## Reply 205
**Author**: Saravanan
**Posted**: 2025-02-09T08:41:16.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/218

There are two “Vienna”. The question4 is referring to which one?

---

## Reply 206
**Author**: K Hari Prasath
**Posted**: 2025-02-09T09:05:31.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/219

Manually make correction in your answer as provided in the error message. If no such words are available insert those and check

---

## Reply 207
**Author**: Taniya Gupta
**Posted**: 2025-02-09T09:32:07.046Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/220

check if the action is commited

---

## Reply 208
**Author**: Tarun eshwar
**Posted**: 2025-02-09T09:40:39.232Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/222

try copying the expected result and pasting it inside the quotations

---

## Reply 209
**Author**: Sudharshini 
**Posted**: 2025-02-09T09:42:45.371Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/223

Check the log of the daily commit .

---

## Reply 210
**Author**: Shivani Adhiyaman
**Posted**: 2025-02-09T09:47:37.836Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/224

Ahh, I have the same doubt too!

---

## Reply 211
**Author**: Anushka Ghosh
**Posted**: 2025-02-09T09:55:06.651Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/225

For the links, this format worked for me:

[ < link text > ] (#)

---

## Reply 212
**Author**: Anushka Ghosh
**Posted**: 2025-02-09T09:58:40.634Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/226

Yes I got it now. Thank you!

---

## Reply 213
**Author**: HARISH. S
**Posted**: 2025-02-09T09:59:13.731Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/227

it should be “2.9” instead of 2.9

---

## Reply 214
**Author**: VivekS
**Posted**: 2025-02-09T10:01:39.752Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/228

looks like formatting or the passed conditions have some issue… can you check and verify it once and see?

---

## Reply 215
**Author**: Aditya Kumar
**Posted**: 2025-02-09T10:24:24.121Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/229

Error: At [3].title: Values don’t match. Expected: “4. 365 Days - Noch Ein Tag”. Actual: “4. The Next 365 Days”

{“id”: “tt21106646”, “title”: “4. The Next 365 Days”, “rating”: “2.9”, “year”: “2022”}

my result , there is no any entry with “4. 365 Days - Noch Ein Tag” on IMDB

---

## Reply 216
**Author**: Nayonika Arora
**Posted**: 2025-02-09T10:24:39.839Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/230

I am getting missing links as error in the 10th question. How to do it?

---

## Reply 217
**Author**: Samarth Goel
**Posted**: 2025-02-09T10:30:18.333Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/231

Mine is giving 1/10 on running without even writing anything? This is happening for Q3? Is it just a glitch?

---

## Reply 218
**Author**: Samarth Goel
**Posted**: 2025-02-09T10:31:15.219Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/232

Yes happened to me too, refresh the page, mine got fixed!

---

## Reply 219
**Author**: K Hari Prasath
**Posted**: 2025-02-09T10:36:15.286Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/233

Check you pdf you can find a word with blue colour and underline. Give some dummy link and use link mark with the word

---

## Reply 220
**Author**: Naga durga prasad E
**Posted**: 2025-02-09T10:41:30.178Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/234

Best way to solve Q2 is , look at the network tab in dev tools and get the url used for assessment and get data from it .

---

## Reply 221
**Author**: Yash kumar
**Posted**: 2025-02-09T10:53:10.517Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/235

u have used a apace (_) after 2.9  which is not visible at front that’s why it is throwing error , it should be just (“2.9”) not ("2.9 ")

---

## Reply 222
**Author**: Koustubh Ramakrishnan
**Posted**: 2025-02-09T11:09:57.380Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/236

Agreed and I have tweaked my approach to get the correct answer. But I feel the question instructions should be adjusted accordingly - the question says to get every issueDate and enhancedweatherDescription key value pair - but only 2 such pairs exist ; whereas in the final answer it is forecast date & weather description total 14  pairs.

---

## Reply 223
**Author**: ABHIJITH VS
**Posted**: 2025-02-09T11:11:32.436Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/237

**Image: Screenshot (7)**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser window displaying the BBC Weather website. The browser's developer tools are open on the right side of the screen, specifically the "Network" tab. The website displays weather information and forecasts.

**2. Any text content visible:**

*   **Website:**
    *   "BBC" (logo)
    *   "WEATHER"
    *   "Home", "News", "Sport", "Business"
    *   "karachi"
    *   "Karachi, Pakistan"
    *   "the latest rates"
    *   "Book Now"
    *   "Weather forecasts for thousands of locations around the world"
    *   Location names on a world map: "London", "Chicago", "Tbilisi", "Dakar", "San José", "Mombasa", "Brasília"
*   **Developer Tools (Network Tab):**
    *   "Elements", "Console", "Sources", "Network", "Performance"
    *   "Preserve log", "Disable cache", "No throttling"
    *   "Invert", "More filters"
    *   "Fetch/XHR", "Doc", "CSS", "JS", "Font", "Img", "Media", "Manifest", "WS", "Wasm", "Other"
    *   "Name", "Status", "Type", "Initiator", "Size", "Time"
    *   "locations?api\_key=AGbFAKx58hyjQScCXIYr...", "200", "xhr", "search.js:2", "486 B", "2.31 s"
    *   "1 / 234 requests", "486 B / 600 kB transferred", "255 B / 4.8 MB resources"
    *   "Console", "AI assistance", "Issues"
    *   "Send feedback"
*   **Windows Notification:**
    *   "Activate Windows"
    *   "How can I help you?"
    *   "Chat messages and the selected network request are sent to Google and may be seen by human reviewers to improve this feature. This is an experimental AI feature and

Open the BBC Weather website.
Press `Ctrl + Shift + I`.
Select the ‘Network’ menu.
Select ‘Fetch/XHR’.
Type ‘Karachi’ in the input field on the website. **Do not press Enter** while entering the location; just type the location. Pressing Enter might cause ‘location?api_key=…’ to disappear.
‘location?api_key=…’ will appear in the inspect menu.
Double-click it to open a web page ([https://locator-service.api.bbci.co.uk/locations?api_key={api_key}](https://locator-service.api.bbci.co.uk/locations?api_key=%7Bapi_key%7D)). This will give the API.
Alternatively, single-clicking ‘location?api_key=…’ will open headers where you can see the Request URL and the API key.

---

## Reply 224
**Author**: HARISH. S
**Posted**: 2025-02-09T11:22:34.616Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/238

type 2025 instead of only using 25 for the year

---

## Reply 225
**Author**: Thereasa Joe J
**Posted**: 2025-02-09T11:28:01.981Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/239

HOW TO DO SCRAPING USING GITHUB ACTIONS

I’m getting no workflow runs error Sir

---

## Reply 226
**Author**: Deveshu Pathak
**Posted**: 2025-02-09T11:37:59.808Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/240

How to resolve “Error: Incorrect latitude. Check OSM ID ending with 2077”

---

## Reply 227
**Author**: Sarthak Singh Gaur
**Posted**: 2025-02-09T11:42:26.613Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/241

@22f3000657

you can try this-

[https://nominatim.openstreetmap.org/search?format=jsonv2&city=Chennai&country=India](https://nominatim.openstreetmap.org/search?format=jsonv2&city=Chennai&country=India)

change the city and country in the url

there will be a bounding_box field: [min_lat, max_lat, min_long, max_long]

---

## Reply 228
**Author**: Ishaan
**Posted**: 2025-02-09T11:43:05.537Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/242

#question 10

Hi, Can anyone help me with Question 10?

No matter how i try to post the markdown, it is always showing that either the words are missing or are different from the original. I have tried every possible way i could think of but it is not working.

---

## Reply 229
**Author**: Shambhavi Verma
**Posted**: 2025-02-09T12:11:40.484Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/243

Getting this question right is a tough nut to crack…so I would rather suggest you to do using the developer tools by inspecting the source code and  putting the breakpoint followed by writing the code in the console to retrieve the expected answer

---

## Reply 230
**Author**: Aryan Tikam
**Posted**: 2025-02-09T12:15:53.311Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/244

**Image: Screenshot from 2025-02-09 17-40-58**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Input Field:** A rectangular text input field is present, outlined in red, indicating an error or validation issue. The field contains the text "https://github.com/AryanTikam/AryanTikam".
*   **Error Icon:** A red circle with an exclamation mark inside is positioned to the right of the input field, further emphasizing the error.
*   **Text Labels:** There are two text labels:
    *   "Enter your repository URL (Format: https://github.com/USER/REPO):" - This provides instructions on what to enter in the input field.
    *   "Error: Latest run does https://github.com/AryanTikam/AryanTikam/actions/runs/13225425496 not include 23f2001216@ds.study.iitm.ac.in in the name" - This is an error message explaining the reason for the validation failure.

**2. Text Content:**

*   **Instruction Text:** "Enter your repository URL (Format: https://github.com/USER/REPO):"
*   **Input Field Value:** "https://github.com/AryanTikam/AryanTikam"
*   **Error Message:** "Error: Latest run does https://github.com/AryanTikam/AryanTikam/actions/runs/13225425496 not include 23f2001216@ds.study.iitm.ac.in in the name"

**3. Context and Purpose:**

The image shows a UI element for entering a GitHub repository URL. The user has entered a URL, but it's triggering an error. The error message suggests that a recent run of a GitHub Action associated with the repository (specifically, run ID 13225425496) does not include a specific email address (23f2001216@ds.study.iitm.ac.in) in its name or configuration. This likely indicates a validation check to ensure that the repository is associated with a particular user or organization.

**4. Technical Details:**

*   The error message references "actions/runs/1322

Can’t seem to get this working, have tried many variations by now like including my email in each of the name sections in every possible permutation. Probably just some silly mistake I haven’t noticed yet but any help would be appreciated. On Linux Mint if that’s relevant.

main.yml:

name: Daily Commit Workflow

on:
  schedule:
    - cron: '10 17 * * *' 
  workflow_dispatch:

jobs:
  commit:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Add commit using 23f2001216@ds.study.iitm.ac.in
        env:
          PAT: ${{ secrets.PAT }}  # PAT stored as a secret
        run: |
          git config --global user.name "Aryan"
          git config --global user.email "23f2001216@ds.study.iitm.ac.in"

          echo "Daily commit on $(date)" >> daily-log.txt

          git add daily-log.txt
          git commit -m "Automated daily commit on $(date)"

          ls -la
          git status

          git push origin main  
          git push "https://${{ secrets.PAT }}@github.com/${{ github.repository }}.git" main

---

## Reply 231
**Author**: Arulvadivelan V
**Posted**: 2025-02-09T12:29:57.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/245

Hi Team,

I have made the JSON from the IMDB website using JS, But do i miss any filter conditions,

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of JSON data and an error message, likely from a data scraping or validation process. The JSON data appears to represent movie information. The error message indicates a mismatch in movie titles.

**2. Text Content:**

*   **Title:** "What is the JSON data?"
*   **JSON Data:**
    *   `title: V. Venom. The Last Dance` (The title is incomplete)
    *   `"year": "2024"`
    *   `"rating": "6.0"`
    *   `{ "id": "tt30292390"`
*   **Error Message:** "Error: At \[10].title: Values don't match. Expected: "11. Sebastian Fitzeks Der Heimweg". Actual: "11. The Calendar Killer""
*   **Disclaimer:** "IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code."

**3. Context and Purpose:**

The image likely comes from a program or script that scrapes movie data from IMDb. The JSON data represents the scraped information for a particular movie. The error message indicates that the scraped title ("11. The Calendar Killer") doesn't match the expected title ("11. Sebastian Fitzeks Der Heimweg"). The disclaimer suggests that the scraping process is susceptible to regional variations and data changes on IMDb, requiring potential manual intervention or code updates.

**4. Technical Details:**

*   **JSON:** The image shows a snippet of JSON (JavaScript Object Notation) data, a common format for data interchange. The data includes fields like "title", "year", "rating", and "id".
*   **Error Handling:** The error message indicates that the program is performing data validation, comparing the scraped title against an expected value. The "At \[10].title" part of the error message suggests that the error occurred at the 10th element in a list or array, specifically in the "title" field.
*   **Data Scraping:** The disclaimer mentions "scraper code," indicating that the program uses web scraping techniques to extract data from IMDb.
*   **IMDb:** The image

I took first 25 films which 5 to 6 rating, but json seems to be different.

Could anyone please tell me what i did wrong here?

---

## Reply 232
**Author**: Arulvadivelan V
**Posted**: 2025-02-09T12:36:29.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/246

Solved the above issue, please ignore it.

---

## Reply 233
**Author**: NamanBeri
**Posted**: 2025-02-09T12:52:04.835Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/247

Believe it or not, I solved it

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a question and answer interface, likely from an online learning platform or coding challenge. It presents a question about markdown content extracted from a PDF, along with a provided answer. The answer is marked as correct.

**2. Text Content:**

*   **Question:** "What is the markdown content of the PDF, formatted with prettier@3.4.2?"
*   **Answer (within a text box):**
    *   `|adficio|chirographum|`
    *   `|---|---|`
    *   `|vitae|ipsam|`
    *   `|spectaculum|claudeo|`
    *   `|comes|celebrer|`
    *   `Decumbo decumbo suadeo totidem apto.`
*   **Feedback:** "Correct"
*   **Explanation:** "It is *very hard* to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things."

**3. Context and Purpose:**

The image depicts a question designed to test the user's understanding of how to represent tabular data and simple text in Markdown format. The question specifically mentions "prettier@3.4.2," indicating that the expected Markdown output should adhere to the formatting conventions of the Prettier code formatter at version 3.4.2. The explanation acknowledges the difficulty of accurately converting PDFs to Markdown and suggests that the question is simplified to focus on fundamental Markdown elements.

**4. Technical Details:**

*   The answer appears to be Markdown code. The lines starting with `|` are likely intended to represent a table. The `|---|---|` line is a common way to define the header separator in a Markdown table.
*   The text "prettier@3.4.2" indicates the use of a code formatter, which suggests that the expected answer should be formatted according to Prettier's rules.
*   The explanation highlights the challenges of PDF-to-Markdown conversion, which often involves dealing with layout complexities, font variations, and other formatting nuances that are difficult to represent accurately in Markdown.

---

## Reply 234
**Author**: Arnav M
**Posted**: 2025-02-09T12:54:22.008Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/248

In the 10th question, how do we add headings and links to the markdown output?(getting error: Headings missing)

---

## Reply 235
**Author**: NamanBeri
**Posted**: 2025-02-09T13:00:26.515Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/249

first convert it roughly to md file then use ai and tell it to add (all the errors one by one). and slowly it will solve all the errors

yes i know it is not the correct way to convert pdf to md file but its just a way to trick the checking system.

but i have an issue it gave me error that it does not contains the word “bash, javascript, whole  redesign, net, suasoria” which is not in the actual pdf, but i added it and it worked. it was just pure trial and error.

---

## Reply 236
**Author**: Vedant Bhanushali
**Posted**: 2025-02-09T13:01:11.101Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/250

this is a changing dataset so make changes to your answer accordingly and you will get it correct

---

## Reply 237
**Author**: Vedant Bhanushali
**Posted**: 2025-02-09T13:02:38.460Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/251

Do the necessary changes as it is said below as it is an everchanging dataset.

You will get the answer correct once you make the changes asked after checking.

---

## Reply 238
**Author**: Vedant Bhanushali
**Posted**: 2025-02-09T13:04:14.674Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/252

check you code and do the changes like max_latitude

replace [0] to [1]

---

## Reply 239
**Author**: Arnav Raj 
**Posted**: 2025-02-09T13:04:24.869Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/253

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a coding tutorial or interactive learning platform. It presents a question related to JSON data and weather forecasts. There are code snippets displayed, a question prompt, a response area, and a "Check" button. An error message is also visible.

**2. Text Content:**

*   **Code Snippet 1 (Top):**
    ```json
    {
        "2025-01-01": "Sunny with scattered clouds",
        "2025-01-02": "Partly cloudy with a chance of rain",
        "2025-01-03": "Overcast skies",
        // ... additional days
    }
    ```
*   **Question:** "What is the JSON weather forecast description for Nur-Sultan?"
*   **Code Snippet 2 (Response Area):**
    ```json
    {
        "2025-02-13": "Light snow and a fresh breeze",
        "2025-02-14": "Light snow and a gentle breeze",
        "2025-02-18": "Sunny intervals and a gentle breeze",
        "2025-02-19": "Light cloud and a gentle breeze",
        "2025-02-20": "Light cloud and a gentle breeze",
        "2025-02-21": "Sunny and a moderate breeze"
    }
    ```
*   **Error Message:** "TypeError: Cannot read properties of undefined (reading 'id')"
*   **Button:** "Check"

**3. Context and Purpose:**

The image depicts an interactive coding exercise. The user is presented with a question about extracting weather forecast data from a JSON structure. The user has provided a JSON response, but it appears to be incorrect or incomplete, resulting in a `TypeError`. The "Check" button likely submits the user's response for evaluation.

**4. Technical Details:**

*   **JSON Data:** The code snippets are in JSON format, representing weather forecasts for specific dates. Each date is a key, and

sir in Q4 i am getting this error:

TypeError: Cannot read properties of undefined (reading 'id')

please help me out with it.

Additionally even if i write anything in the code block the err remains same!

@Jivraj @carlton @s.anand sir please help me out as only this question left.

anyone facing this issue? let me know

{
     "25-02-09": "Partly cloudy and a moderate breeze",
     "25-02-10": "Sunny intervals and a moderate breeze",
     "25-02-11": "Sunny and a gentle breeze",
     "25-02-12": "Light snow and a fresh breeze",
     "25-02-13": "Light snow and a fresh breeze",
     "25-02-14": "Light snow and a gentle breeze",
     "25-02-15": "Light snow and a gentle breeze",
     "25-02-16": "Light snow and a gentle breeze",
     "25-02-17": "Light snow and a gentle breeze",
     "25-02-18": "Sunny intervals and a gentle breeze",
     "25-02-19": "Light cloud and a gentle breeze",
     "25-02-20": "Light cloud and a gentle breeze",
     "25-02-21": "Sunny and a moderate breeze"
}

---

## Reply 240
**Author**: Yogaswetha
**Posted**: 2025-02-09T13:13:32.686Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/254

in my dashboard there is no submit button for ga2,3,and 4 as well and if i check for scores in grades tab for ga2 and ga3 it was given as not submitted , does everyone facing the same ?? if the submit button is visible for anyone plss guide me to rectify that.

regards and thanks.

---

## Reply 241
**Author**: Yogaswetha
**Posted**: 2025-02-09T13:18:09.159Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/255

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) related to API development and testing. It includes:

*   A section with Markdown-formatted headings, likely representing a table of contents or outline.
*   A numbered list outlining steps for API development.
*   An input field for a URL.
*   An error message.

**2. Any text content visible:**

*   **Headings:**
    *   `## Contents`
    *   `# Vanuatu`
    *   `## Etymology`
    *   `## History`
    *   `### Prehistory`
*   **Numbered List:**
    1.  `API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that accepts a country query parameter.`
    2.  `Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML.`
    3.  `Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, lxml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6) from the page, maintaining order.`
    4.  `Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #.`
    5.  `Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.`
*   **Question:** `What is the URL of your API endpoint?`
*   **URL Input:** `http://127.0.0.1:8000/api/outline?country=france`
*   **Error Message:** `TypeError: Failed to fetch`

**3. The context or purpose of what's displayed:**

The image appears to be part of a tutorial or guide for building an API that fetches and processes content from Wikipedia. The steps outline the process of creating an API endpoint, fetching Wikipedia data, extracting headings, generating a Markdown outline, and enabling CORS. The user is prompted to enter the URL of their API endpoint, and the "Failed to fetch" error indicates that the provided URL is not working or accessible.

**4. Technical details

it is showing correct but if i reload the page or press ctrl+c in my terminal its showing this error what should i do now ??

---

## Reply 242
**Author**: D HARICHARAN 
**Posted**: 2025-02-09T13:34:26.111Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/256

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from an online learning platform or coding challenge. It presents a problem description, instructions, and an input field for the user to provide an answer. There's also a "Check" button to submit the answer.

**2. Text Content:**

*   **Title:** "Search Hacker News (1 mark)"
*   **Section Title:** "Media Intelligence for TechInsight Analytics"
*   **Description:** A paragraph describing TechInsight Analytics as a market research firm specializing in technology trends and media intelligence. It mentions that they use Hacker News as a data source.
*   **Problem Context:** Explains that TechInsight Analytics wants to automate the process of identifying and extracting relevant Hacker News posts.
*   **Tool Description:** Describes an internal tool that leverages the HNRSS API to fetch Hacker News posts. The tool performs topic monitoring, engagement filtering, and data extraction.
*   **Program Requirements:** Lists the steps a program needs to take: searching Hacker News, filtering posts based on points, and retrieving the link.
*   **Section Title:** "Your Task"
*   **Task Instructions:**
    *   Search using the Hacker News RSS API for the latest Hacker News post mentioning "WebRTC" and having a minimum of 30 points.
    *   Automate Data Retrieval: Utilize the HNRSS API.
    *   Extract and Present Data: Extract the most recent `` and get the `` tag.
    *   Share the result: Type in just the URL in the answer.
*   **Question:** "What is the link to the latest Hacker News post mentioning WebRTC having at least 30 points?"
*   **Input Field:** Contains the URL "https://news.ycombinator.com/item?id=41699323"
*   **Error Message:** "Error: Incorrect link"
*   **Button:** "Check"

**3. Context and Purpose:**

The image represents a coding challenge or assignment where the user needs to use the Hacker News RSS API to find a specific post (mentioning "WebRTC" with at least 30 points) and provide its link. The platform provides context about a company (TechInsight Analytics

Respected Sir,

How can I Solve this, I’m not able to solve this one

---

## Reply 243
**Author**: Arulvadivelan V
**Posted**: 2025-02-09T13:39:15.522Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/257

Hi,

For the 4th question, We can get the necessary information issueDate and its description from Summary itself right? or am I seeing the stuff in the wrong place?

---

## Reply 244
**Author**: maroof abdullah
**Posted**: 2025-02-09T13:40:26.226Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/258

Change it manually.

add the expected answer

---

## Reply 245
**Author**: Arnav Raj 
**Posted**: 2025-02-09T13:51:57.206Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/259

when you press ctrl+c it turns off the server and same goes for refresh.

also you dont need to manually write ?country… just write till outline and turn on the server n you are good to go.

---

## Reply 246
**Author**: Yogaswetha
**Posted**: 2025-02-09T13:54:54.255Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/260

ok this is fine for now and its showing correct also but at the time of evaluation will my server runs??

---

## Reply 247
**Author**: PREMDEEP MAITI
**Posted**: 2025-02-09T14:06:29.442Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/261

It is written in the ques to get the link in the link tag. Not the post link.  Like this

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays the content of an XML file. It appears to be an RSS feed, specifically from Hacker News, filtered to include items related to "LLM" (likely referring to Large Language Models). The XML structure is visible, with tags like ``, ``, ``, ``, ``, ``, etc. The XML is presented in a text-based format, likely as it would appear in a text editor or code viewer.

**2. Any text content visible:**

*   **Top:** "This XML file does not appear to have any style information associated with it. The document tree is shown below."
*   **`` tag:** `xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0"`
*   **`` tag:**
    *   ``: Hacker News - Newest: "LLM"
    *   ``: `https://news.ycombinator.com/newest`
    *   ``: Hacker News RSS
    *   ``: `https://hnrss.org/`
    *   ``: hnrss v2.1.1
    *   ``: Sun, 09 Feb 2025 08:44:00 +0000
    *   ``: `href="https://hnrss.org/newest?points=78&q=LLM" rel="self" type="application/rss+xml"`
*   **`` tag:**
    *   ``: ``
    *   ``: `

---

## Reply 248
**Author**: D HARICHARAN 
**Posted**: 2025-02-09T14:08:38.790Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/262

Thank you bro, I will try this

---

## Reply 249
**Author**: Arnav Raj 
**Posted**: 2025-02-09T14:11:14.190Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/263

not at all. your last saved marks will be considered

---

## Reply 250
**Author**: DHANUSH.R
**Posted**: 2025-02-09T14:18:30.851Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/264

just replace value instead of it. same problem I also that time I check code and modify serval time I faced same error. so just ignore it and replace expected value instead of actual value in our Json.

---

## Reply 251
**Author**: Thereasa Joe J
**Posted**: 2025-02-09T14:21:38.216Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/265

extract the pdf to markdown format using chatgpt then add links,tables and one blockquote

---

## Reply 252
**Author**: Rajalakshmi Rathinasabhapathy
**Posted**: 2025-02-09T14:22:18.004Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/266

Try to use the key ‘enhancedWeatherDescription’ parsing through the summary object (or) use the BeautifulSoup to find ‘div’ with attributes of

class: wr-day-summary

---

## Reply 253
**Author**: Rajalakshmi Rathinasabhapathy
**Posted**: 2025-02-09T14:35:34.384Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/267

Hi, please  ensure that your repository is public, if private the response would be 404. If workflow runs is not found, it might be that the number of API calls to your profile/repo might have exceeded, it usually gets reset at the end of the day. Please try again after sometime)

---

## Reply 254
**Author**: GIRISH VISHVESHVAR BHAT
**Posted**: 2025-02-09T14:47:12.663Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/268

In question 1 i am getting this error

 {
    "id": "tt21227864",
    "title": "2. You're Cordially Invited",
    "year": "2025",
    "rating": "5.5"
  }

my answer is in above format i tried changing to “2024-”, "2024- " to number tried after reloading the page but still i am getting

Error: At [11].year: Values don’t match. Expected: “2024”. Actual: "2024– "

---

## Reply 255
**Author**: Sagandeep Kaur
**Posted**: 2025-02-09T15:05:50.845Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/269

You have to manually change these thing

from actual change to expected.

For me, error was almost 10 times.

---

## Reply 256
**Author**: Sagandeep Kaur
**Posted**: 2025-02-09T15:06:58.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/270

on your 11th or 12th instance change it

write the actual value

---

## Reply 257
**Author**: Ritwik Trivedi
**Posted**: 2025-02-09T15:11:37.467Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/271

If you have submitted on the assignment site and saved it in time, then that score is the actual score and will be updated directly on the student dashboard.

---

## Reply 258
**Author**: Md anas alam
**Posted**: 2025-02-09T15:21:41.857Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/272

Your answer is correct. Just add a space after the hyphen—it will resolve the problem. Or you can copy and paste from here: '2025– '.

---

## Reply 259
**Author**: D HARICHARAN 
**Posted**: 2025-02-09T15:22:57.529Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/273

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for an online exercise or assessment, likely related to Markdown formatting. It includes instructions, a text input area, and feedback. The UI elements include:

*   A header with a timer ("03:08:26 left"), a score ("Score: 7/10"), and buttons ("Check all", "Save").
*   Instructions for converting a PDF to Markdown.
*   A section describing the "Impact" of the exercise.
*   A text input area where the user is expected to enter Markdown code.
*   An error message indicating "Missing code".

**2. Any text content visible:**

The text content includes:

*   "Markdown and ensuring their consistent formatting. This project is critical for supporting EduDocs' commitment to delivering high-quality, accessible educational resources to its clients."
*   "q-pdf-to-markdown.pdf has the contents of a sample document."
*   Numbered instructions:
    1.  "Convert the PDF to Markdown: Extract the content from the PDF file. Accurately convert the extracted content into Markdown format, preserving the structure and formatting as much as possible."
    2.  "Format the Markdown: Use Prettier version 3.4.2 to format the converted Markdown file."
    3.  "Submit the Formatted Markdown: Provide the final, formatted Markdown file as your submission."
*   "Impact" section:
    *   "By completing this exercise, you will contribute to EduDocs Inc.'s mission of providing high-quality, accessible educational resources. Automating the PDF to Markdown conversion and ensuring consistent formatting:"
    *   Bullet points highlighting the benefits: "Enhances Productivity", "Improves Quality", "Supports Scalability", "Facilitates Integration".
*   "What is the markdown content of the PDF, formatted with prettier@3.4.2?"
*   The user's Markdown input, which includes:
    *   `[tricesimus admitto](https://example.com/tricesimus-admitto)`
    *   `Suggero comes denique argentum.`
    *   `Desipio crudelis antea quis.`
    *   `[adeptio

i wrote everything that was there in the pdf file after converting to markdown, there is no code inside the pdf file then how does it expect to have code in markdown, can anyone help

---

## Reply 260
**Author**: Rishit
**Posted**: 2025-02-09T15:36:39.718Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/274

Yeah! His issue is genuine. Arnav’s JSON seems to be correct, yet these are some issues faced by him.

---

## Reply 261
**Author**: Rishit
**Posted**: 2025-02-09T15:41:57.385Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/275

Yeah! even I am facing this issue. Despite lot of efforts, last question markdown seems to always incorrect. It is always throwing any sort of error for no reason.

---

## Reply 262
**Author**: Sandeep S
**Posted**: 2025-02-09T15:43:25.700Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/276

The IMDB and weather questions was a pain along with the 10th question, wasted so much time @s.anand , the questions were nowhere tough, it was the problems with the evaluation part i had spend hours just to  sit and correct the JSON file and no comments on the 10th question’s part.

I am fine with the academia being challenging to study not the evalation making me manually edit solutions

@Jivraj @carlton

---

## Reply 263
**Author**: Tanya kamboj
**Posted**: 2025-02-09T15:46:29.876Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/278

yes change manually, there are slight changes which we have to do

---

## Reply 264
**Author**: Shahsank J Shetty
**Posted**: 2025-02-09T15:46:42.193Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/279

For the 8th question, i am getting an error that tells me i have not run the action, though i manually triggered it and confirmed the commit was made. Cant figure out whats wrong.

---

## Reply 265
**Author**: Jayaram
**Posted**: 2025-02-09T15:50:47.039Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/280

for second query i am getting this result as row 4 and 5 (Screenshot)… but when testing the results it shows

{"id":"tt22804850","title":"3. The Sand Castle","year":"2024","rating":"4.7"},
{"id":"tt10128846","title":"4. Megalopolis","year":"2024","rating":"4.8"},
{"id":"tt2322441","title":"5. Fifty Shades of Grey","year":"2015","rating":"4.2"},
{"id":"tt4978420","title":"6. Borderlands","year":"2024","rating":"4.6"},

Error: At [4].title: Values don’t match. Expected: “5. Cinquanta sfumature di grigio”. Actual: “5. Fifty Shades of Grey”

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of a user interface, likely from a movie or entertainment listing website or app. It displays information about two movies: "Megalopolis" and "Fifty Shades of Grey." Each movie entry includes a poster image, title, release year, duration, age rating, user rating, the number of ratings, a "Rate" option, Metascore, and a brief synopsis.

**2. Text Content:**

*   **Megalopolis:**
    *   "4. Megalopolis"
    *   "2024"
    *   "2h 18m"
    *   "15"
    *   "4.8 (33K)"
    *   "Rate"
    *   "55 Metascore"
    *   "The city of New Rome faces the duel between Cesar Catilina, a brilliant artist in the mayor Franklyn Cicero. Between them is Julia Cicero, with her loyalty divided bet"

*   **Fifty Shades of Grey:**
    *   "5. Fifty Shades of Grey"
    *   "2015"
    *   "2h 5m"
    *   "18"
    *   "4.2 (344K)"
    *   "Rate"
    *   "46 Metascore"
    *   "Literature student Anastasia Steele's life changes forever when she meets hands"

**3. Context and Purpose:**

The purpose of this UI element is to present movie information to users, allowing them to browse and discover new films. The information provided helps users decide whether they are interested in watching a particular movie. The "Rate" option suggests user interaction and feedback is encouraged.

**4. Technical Details:**

*   The layout suggests a list or grid-based display, common in modern web and app design.
*   The use of icons (star for rating, a plus sign for adding to a list) is typical for user-friendly interfaces.
*   The Metascore is displayed in a distinct colored box (likely yellow or gold), indicating its importance as a critical review metric.
*   The presence of "2h 18m" and "2h 5m

---

## Reply 266
**Author**: Tanya kamboj
**Posted**: 2025-02-09T15:58:59.656Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/281

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a question and what appears to be a JSON-like data structure representing a weather forecast. Below the data structure, there's an error message. The entire block of data and the error message are enclosed in a red border.

**2. Any text content visible:**

*   **Question:** "What is the JSON weather forecast description for Vienna?" (The word "Vienna" is highlighted in red).
*   **JSON-like data:**
    *   `{`
    *   `"2025-02-10": "Sunny and a gentle breeze",`
    *   `"2025-02-11": "Sunny intervals and a gentle breeze",`
    *   `"2025-02-12": "Sunny and a gentle breeze",`
    *   `"2025-02-13": "Light cloud and a moderate breeze",`
    *   `"2025-02-14": "Light cloud and a gentle breeze",`
    *   `}`
*   **Error Message:** "Error: At root: Different number of properties"

**3. The context or purpose of what's displayed:**

The image presents a question about retrieving a weather forecast description in JSON format for Vienna. The provided data structure is intended to be the answer, but the error message suggests that the data is not valid JSON or does not conform to an expected schema. The error message "Different number of properties" is misleading, as the issue is that the JSON is not valid.

**4. Technical details (JSON-like data):**

*   The data structure appears to be a JSON object where the keys are dates in the format "YYYY-MM-DD" (e.g., "2025-02-10").
*   The values associated with each date are strings describing the weather forecast for that day (e.g., "Sunny and a gentle breeze").
*   The error message indicates that there's a problem with the structure of the JSON data. The error "Different number of properties" is misleading, as the issue is that the JSON is not valid.

sir earlier it was correct and now i submit it again after running my code it shows error.  sir i have done it correct two times earlier. but now again as i click on save button it changed. these tasks are taking too much time and creating more difficulties. please look into this @s.anand @Jivraj @Saransh_Saini

---

## Reply 267
**Author**: AnandMurti
**Posted**: 2025-02-09T15:59:12.855Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/282

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of JSON data and an error message. The JSON data appears to represent information about movies or TV shows. The error message indicates a mismatch in values during a comparison or validation process.

**2. Any text content visible:**

*   **Question:** "What is the JSON data?"
*   **JSON Data:**
    *   `"title": "1. The Night Agent"`
    *   `"year": "2023-"`
    *   `"rating": "7.5"`
    *   `},`
    *   `{`
*   **Error Message:** "Error: At \[8].title: Values don't match. Expected: "9. Incorrect answer jalement invités". Actual: "9. You're Cordially Invited""

**3. The context or purpose of what's displayed:**

The image likely comes from a system that is validating or comparing JSON data against an expected format or set of values. The error message indicates that the "title" field at the 8th position (index 8) in a list of JSON objects does not match the expected value. The expected value is "9. Incorrect answer jalement invités", while the actual value is "9. You're Cordially Invited".

**4. Technical details:**

*   **JSON:** The data is formatted as JSON (JavaScript Object Notation), a standard text-based format for representing structured data.
*   **Error Message Structure:** The error message provides specific information about the location of the error (\[8].title) and the expected vs. actual values. This suggests a structured validation process.
*   **Array/List:** The "\[8]" in the error message implies that the JSON data is likely part of an array or list of JSON objects.
*   **Incorrect answer:** The error message contains the text "Incorrect answer" which suggests that the system is evaluating a user's response or input against a correct answer.

Hi Team ,

Are we expecting the result to match exactly as per the benchmark of qa4.

---

## Reply 268
**Author**: Arnav Raj 
**Posted**: 2025-02-09T16:04:51.693Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/283

just edit some of the spellings in answers manually as per errors you get n you are good to go.

---

## Reply 269
**Author**: Madhu
**Posted**: 2025-02-09T16:05:40.244Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/284

22f3002723:

Cinquanta sfumature di grigio

It is just a translation of the same movie… it’s not different

Copy paste the Expected: “title” and click on check

It’ll work

---

## Reply 270
**Author**: B Varun karthik
**Posted**: 2025-02-09T16:09:30.499Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/285

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) of what appears to be an online quiz or assignment platform. It includes elements like:

*   **Timer:** Displaying remaining time.
*   **Score:** Showing the current score.
*   **Buttons:** "Check all" and "Save".
*   **Question:** A question with a statement.
*   **Discussion Link:** A link to a discussion forum.
*   **Bonus Information:** Information about earning bonus marks.
*   **User Information:** Displaying the logged-in user's email.
*   **Logout Button:** A button to log out.
*   **Loading Icon:** A circular loading icon at the bottom.

**2. Text Content:**

*   "02:23:44 left" - Indicates the time remaining.
*   "Score: 0" - Shows the current score is zero.
*   "Check all" - A button to check all answers.
*   "Save" - A button to save progress.
*   "7. It s nackable. It's possible to get the answer to some questions by nacking the code for this quiz. That's allowed." - This is the question/statement. It seems to be a playful acknowledgement that the quiz can be "hacked" to find answers.
*   "Have questions?" - A prompt to ask questions.
*   "Join the discussion on Discourse" - A link to a discussion forum.
*   "Bonus marks for posting on Discourse" - A heading indicating bonus marks can be earned.
*   "To encourage discussions, IITM BS students who reply to the discussion on GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] with a relevant question or reply will get 1 bonus mark on this graded assignment." - Explains the conditions for earning bonus marks.
*   "You are logged in as 23f2001305@ds.study.iitm.ac.in." - Shows the logged-in user's email address.
*   "Logout" - A button to log out.

**3. Context and Purpose:**

The image depicts a student taking an online quiz or assignment

Saved responses are not being displayed and also page keeps refreshing…

---

## Reply 271
**Author**: Naman S. 
**Posted**: 2025-02-09T16:09:48.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/286

@all, in q4 Actually the answer data is sync with current weather description therefore the answer changes. Make sure to update your json file before submitting.

---

## Reply 272
**Author**: Chinnam Goutham Nischay
**Posted**: 2025-02-09T16:10:43.735Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/287

try refreshing the page and re-run the script. as the data gets updated the answer also changes.

---

## Reply 273
**Author**: VIKASH PRASAD
**Posted**: 2025-02-09T16:13:55.561Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/288

refer to the link post,

    [GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/65) Tools in Data Science

    use this [Google Colab](https://colab.research.google.com/drive/1X5IO8K1Xf8Wh7SOZelSrFAfZgRG-mv4A?usp=sharing) with the city name to get the Json Body just change the date format. 
@23f2004752

---

## Reply 274
**Author**: Rohit Garg
**Posted**: 2025-02-09T16:15:41.126Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/290

i 'm here for the bonus marks,

But since i am here. Just want to appreciate the course and your efforts towards this.

We need more “teachers” like you, who really puts an extra effort in the course.

And i have never seen any course cool as this,

like appreciating tweaking things, using dev console to tweak things, keep the code checks on client side (*and as S Anand’s Student i have leveraged that freedom   :sweat_smile: , gave client side answer checks’s code to `o1` and it reverse engineered the minifed code, and lots of question were solved by that only, but really curious on how others are doing this*)
keeping the cutting edge tech in course, like function calling from OpenAI.

( *i have seen some students solutions, they were using regex to solve that problem  :smiling_face_with_tear: *)

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page interface, likely part of an online learning platform or course management system. It includes several UI elements:

*   **Informational boxes:**  These are rectangular areas with text, providing information to the user.
*   **Links:**  Hyperlinks are present, allowing the user to navigate to other pages or resources.
*   **Buttons:**  "Reload" and "Logout" buttons are visible, suggesting interactive functionality.

**2. Text Content:**

The image contains the following text:

*   "Have questions? Join the discussion on Discourse"
*   "Bonus marks for posting on Discourse"
*   "To encourage discussions, IITM BS students who reply to the discussion on GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] with a relevant question or reply will get 1 bonus mark on this graded assignment."
*   "You are logged in as 22f2001394@ds.study.iitm.ac.in."
*   "Logout"
*   "Recent saves (most recent is your official score)"
*   "Reload from 2/9/2025, 9:26:17 PM. Score: 10"
*   "Reload from 2/9/2025, 7:48:07 PM. Score: 8"
*   "Reload from 2/9/2025, 7:44:44 PM. Score: 8"

**3. Context and Purpose:**

The content suggests the following:

*   **Course Platform:** The user is likely logged into a course platform, possibly for an IITM BS (Indian Institute of Technology Madras Bachelor of Science) program.
*   **Discourse Forum:** The platform encourages students to use a Discourse forum for discussions, offering bonus marks for participation.
*   **Graded Assignment:** The bonus marks are tied to a graded assignment.
*   **Save History:** The "Recent saves" section indicates that the user's progress or work is being automatically saved, and the scores for each save are displayed.

**4. Technical Details:**

*   **Email Address:** The user

---

## Reply 275
**Author**: Abhay Mehra
**Posted**: 2025-02-09T16:17:12.810Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/291

why everytime question 2 answer is showing error in json?

---

## Reply 276
**Author**: Rohit Garg
**Posted**: 2025-02-09T16:20:29.219Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/292

What error are you getting @Abhay222 ?

Can you post a screenshot or error details ?

---

## Reply 277
**Author**: Matlin Jeleshiya 
**Posted**: 2025-02-09T16:20:47.342Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/293

Is it safe to skip Q4 for those who got the city named Nur-Sultan, since it has been renamed to Astana, and the answer for Astana is incorrect in the portal?

---

## Reply 278
**Author**: Parth Patel
**Posted**: 2025-02-09T16:23:37.267Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/294

@s.anand

There is possibly wrong evaluation in q6 as it is taking in 2nd latest link as the correct answer. I might be wrong, but the latest one is giving me incorrect evaluation while the 2nd latest is giving me the correct score.

---

## Reply 279
**Author**: Rahul 
**Posted**: 2025-02-09T16:23:43.629Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/295

getting the same issue Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

## Reply 280
**Author**: Abhay Mehra
**Posted**: 2025-02-09T16:25:24.448Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/296

yes this kind errors.

---

## Reply 281
**Author**: Rohit Garg
**Posted**: 2025-02-09T16:29:06.442Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/297

@Abhay222 @22f3002184

if you look closely the expected value is `2024- ` and actual that you are supplying is `2024`.

Difference ? your value does have a `-` and a space at the end.

reason ? you might be scraping it ? `trim()` or maybe using `innerText` to get tag’s text ?

---

## Reply 282
**Author**: Anudeep
**Posted**: 2025-02-09T16:30:02.184Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/298

it seems we are intended to provide country specific versions for Individual students simulating being an analyst for MNC in various locations. Clearly you got Spain and I seem to have gotten France, although it doesn’t seem to be mentioned in the question itself.

---

## Reply 283
**Author**: Saransh Saini
**Posted**: 2025-02-09T16:30:25.035Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/299

Thank you Tanya for pointing out this issue.

Just tell me this, has your city changed? If yes then what was it earlier and what is it now.

---

## Reply 284
**Author**: Yogaswetha
**Posted**: 2025-02-09T16:33:41.438Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/301

any reply regarding this please

---

## Reply 285
**Author**: Debarpita Dash
**Posted**: 2025-02-09T16:34:55.919Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/302

22f2000113:

For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name

the movie may have  different title on IMDb (perhaps in another language) according to region which is why there isnt an exact match u can manually format it to get marks

---

## Reply 286
**Author**: Saransh Saini
**Posted**: 2025-02-09T16:35:18.237Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/303

[GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/171) Tools in Data Science

    We have removed that button, cause it was causing confusion among the students. 
If you have saved your answers on the TDS portal then you need not worry, you will be marked. The button was just there to ensure you saw the assignment on the TDS portal. 
Regards, 
TDS TA

Read this

---

## Reply 287
**Author**: Nayonika Arora
**Posted**: 2025-02-09T16:40:31.628Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/304

Try changing it manually. Some values keep changing due to change in server.

---

## Reply 288
**Author**: Aarsh Sohane
**Posted**: 2025-02-09T16:42:06.985Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/305

Alright so in Q4 of W4, We have to extract weather forecast data from bbc servers for a given city. The city I have been given Nur-Sultan is not present in the bbc data base, it appears the city is now known as Astana and is listed in the bbc database as Astana.

Since Nur-Sultan doesn’t exist in the bbc database, all of my attempts to extract data for it were meet with failure. So I extracted the data for Astana and pasted it in the portal but that doesn’t work as well and throws the following error “TypeError: Cannot read properties of undefined (reading ‘id’)”

What am I suppose to do? @carlton @Jivraj @Saransh_Saini

**Image: Screenshot 2025-02-09 175948**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for a coding challenge or exercise related to weather data retrieval and transformation. It includes instructions, example output, an input area for the user to provide their answer, and a "Check" button. There's also a timer, score, and save button at the top.

**2. Text Content:**

*   **Header:** "06:00:20 left Score: 3/10 Check all Save"
*   **Instructions:**
    *   "1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Nur-Sultan. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city)."
    *   "2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId."
    *   "3. Data Transformation: Extract the issueDate and enhancedweatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each issueDate to its corresponding enhancedweatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedWeatherDescription."
*   **Example Output:**
    *   "The output would look like this:" followed by a JSON-like structure:
        ```json
        {
        "2025-01-01": "Sunny with scattered clouds",
        "2025-01-02": "Partly cloudy with a chance of rain",
        "2025-01-03": "Overcast skies",
        // ... additional days
        }
        ```
*   **Question:** "What is the JSON weather forecast description for Nur-Sultan?"
*   **User Input Area:** Contains a JSON-like structure:
    ```json
    {
    "2025-02-09": "Partly cloudy and a moderate breeze",
    "2025-02-10": "Sunny intervals and a moderate breeze",
    "2025-02

Below is the data for Astana that I was able to extract, Since Nur-Sultan doesn’t exist in the bbc database:

{

“2025-02-09”: “Partly cloudy and a moderate breeze”,

“2025-02-10”: “Sunny intervals and a moderate breeze”,

“2025-02-11”: “Sunny and a gentle breeze”,

“2025-02-12”: “Light snow and a fresh breeze”,

“2025-02-13”: “Light snow and a fresh breeze”,

“2025-02-14”: “Light snow and a gentle breeze”,

“2025-02-15”: “Light snow and a gentle breeze”,

“2025-02-16”: “Light snow and a gentle breeze”,

“2025-02-17”: “Light cloud and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”,

“2025-02-19”: “Light cloud and a gentle breeze”,

“2025-02-20”: “Light cloud and a gentle breeze”,

“2025-02-21”: “Sunny and a moderate breeze”,

“2025-02-22”: “Light snow and a moderate breeze”

}

---

## Reply 289
**Author**: Anvitha
**Posted**: 2025-02-09T16:42:55.994Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/306

same problem, could anyone help what is wrong.

---

## Reply 290
**Author**: Rohit Garg
**Posted**: 2025-02-09T16:48:37.375Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/307

@AnvithaV  check this out

---

## Reply 291
**Author**: Tanya kamboj
**Posted**: 2025-02-09T16:50:23.681Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/308

No the city is same as before. But i think it fetches the latest data. As i saved it yesterday it was correct. But today when i  clicked on save button again it got wrong.

---

## Reply 292
**Author**: Tanya kamboj
**Posted**: 2025-02-09T16:52:32.951Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/309

What error are you getting ?

---

## Reply 293
**Author**: Vidya Bharti
**Posted**: 2025-02-09T16:52:52.617Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/310

how to approach question 8 of ga4

---

## Reply 294
**Author**: Syed Zakiyuddin
**Posted**: 2025-02-09T16:53:06.031Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/311

For question #8. Can I use the .github/workflows that I created for the previous assignments or i need to create a new workflow?

---

## Reply 295
**Author**: Rahul 
**Posted**: 2025-02-09T16:55:01.459Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/312

still the same   {“id”:“tt24871974”,“title”:“12. Subservience”,“year”:“2024”,“rating”:“5.4”},

Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

## Reply 296
**Author**: Baddila Mohan Sai
**Posted**: 2025-02-09T16:55:45.350Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/313

Change the value manually

---

## Reply 297
**Author**: Steven Robert
**Posted**: 2025-02-09T16:55:51.950Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/314

I am still not sure why the github action question is not working for me. I have manually triggered the workflow multiple times but i keep getting the same ‘name’ error even though it has been specified in the code. Can somebody kindly help?

---

## Reply 298
**Author**: Tanya kamboj
**Posted**: 2025-02-09T16:56:34.118Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/315

Have you given your email id in name ?

---

## Reply 299
**Author**: Jash Mevada
**Posted**: 2025-02-09T16:57:04.532Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/316

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Top Bar:** A green bar at the top displays the remaining time ("01:37:59 left"), the score ("Score: 10/10"), a "Check all" button, and a "Save" button. There's also a dark mode toggle icon in the top right.
*   **Login Information:** Below the top bar, it indicates the user is logged in with the email address "23f2003807@ds.study.iitm.ac.in."
*   **Logout Button:** A "Logout" button is present.
*   **Recent Saves Section:** A dark green box displays a list of recent saves. Each save entry includes a "Reload" button, the date and time of the save, and the score at that time.
*   **Questions Section:** Below the recent saves, there's a "Questions" heading. A numbered list of questions follows.

**2. Text Content:**

*   "01:37:59 left"
*   "Score: 10/10"
*   "Check all"
*   "Save"
*   "You are logged in as 23f2003807@ds.study.iitm.ac.in."
*   "Logout"
*   "Recent saves (most recent is your official score)"
*   "Reload" (repeated for each save)
*   "from 2/9/2025, 10:20:36 PM. Score: 10"
*   "from 2/9/2025, 10:20:18 PM. Score: 10"
*   "from 2/9/2025, 9:42:55 PM. Score: 7"
*   "Questions"
*   "1. Import HTML to Google Sheets (1 mark)"

**3. Context/Purpose:**

The image appears to be a screenshot of an online quiz or assessment platform. The user is logged in, has a limited time to complete the quiz, and can save their progress. The "Recent saves" section allows the user to revert

Completed GA4 with 10/10.

I have also use tweak that the some answer and question are check and generate on client side.

---

## Reply 300
**Author**: Tanya kamboj
**Posted**: 2025-02-09T16:57:11.845Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/317

See there is difference of hyphen . Correct it manually.

---

## Reply 301
**Author**: Saransh Saini
**Posted**: 2025-02-09T16:57:35.122Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/318

Just try re-running your code once and paste in the current response. Check if its working or not.

---

## Reply 302
**Author**: Baddila Mohan Sai
**Posted**: 2025-02-09T16:58:00.163Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/319

Change the slight differences manually accordingly with the expected values

---

## Reply 303
**Author**: Ashish
**Posted**: 2025-02-09T17:01:51.864Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/320

I haven’t done MLP and BDM so should I drop TDS now

---

## Reply 304
**Author**: Arulvadivelan V
**Posted**: 2025-02-09T17:06:00.951Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/321

Hi,

I couldn’t able to create markdown from pdf, it showing missing links, but i couldn’t able to find the link in pdf either. I think i’m missing something.

anyone suggest some way how to do pdf to markdown correctly?

---

## Reply 305
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-02-09T17:08:16.185Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/322

if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

---

## Reply 306
**Author**: Steven Robert
**Posted**: 2025-02-09T17:08:23.051Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/323

yes

But still doesnt work

---

## Reply 307
**Author**: Tanya kamboj
**Posted**: 2025-02-09T17:10:40.176Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/324

In q10 i am geeting …missing links- error

Any idea how to correct this

---

## Reply 308
**Author**: Parmeet Singh
**Posted**: 2025-02-09T17:12:23.430Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/326

Beyond the specific tools mentioned (like `IMPORTHTML` in Google Sheets or `httpx` and `lxml` in Python), what are the broader *ethical considerations* when scraping data from websites, and how can developers ensure they are acting responsibly and respecting website owners’ rights and resources?

---

## Reply 309
**Author**: Yogaswetha
**Posted**: 2025-02-09T17:12:57.853Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/327

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a task description and a user interface element for submitting an answer, along with an error message. It appears to be part of an online coding challenge or assignment.

**2. Text Content:**

*   **"Retrieves and returns the link to the most relevant post."** (This is likely a continuation of a previous point)
*   **"Your Task"**
*   **"Search using the Hacker News RSS API for the latest Hacker News post mentioning WebAssembly and having a minimum of 86 points. What is the link that it points to?"** (This is the main task description)
*   **"1. Automate Data Retrieval: Utilize the HNRSS API to fetch the latest Hacker News posts. Use the URL relevant to fetching the latest posts, searching for topics and filtering by a minimum number of points."**
*   **"2. Extract and Present Data: Extract the most recent  from this result. Get the  tag inside it."**
*   **"3. Share the result: Type in just the URL in the answer."**
*   **"What is the link to the latest Hacker News post mentioning WebAssembly having at least 86 points?"** (This is a restatement of the task)
*   **"https://news.ycombinator.com/item?id=38790552"** (This is the user's submitted answer)
*   **"Error: Incorrect link"** (This indicates the submitted answer was wrong)

**3. Context and Purpose:**

The image presents a programming task where the user needs to use the Hacker News RSS API to find a specific post. The task involves:

*   Fetching data from the API.
*   Filtering the data based on keywords ("WebAssembly") and a minimum score (86 points).
*   Extracting the URL associated with the post.
*   Submitting the URL as the answer.

The "Error: Incorrect link" message suggests the user's submitted URL was not the correct one according to the task's criteria.

**4. Technical Details:**

*   **Hacker News RSS API:** This is a public API that provides access to Hacker News content in RSS

is everything fine with the answer format?? i am trying this for so long anything i want to change ??

---

## Reply 310
**Author**: Tanya kamboj
**Posted**: 2025-02-09T17:18:23.735Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/328

What is the error are you facing ?

---

## Reply 311
**Author**: Hemant Singh
**Posted**: 2025-02-09T17:20:50.330Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/329

can someone  help through this error!!

**Image: Capture**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface element, likely a text box or code editor, containing JSON data. The data appears to represent a list of movies or TV shows, with each entry having an ID, title, year, and rating. The text box is highlighted with a red border, indicating an error or issue. There's also a scroll bar on the right side of the text box.

**2. Any text content visible:**

*   **Title:** "What is the JSON data?"
*   **JSON Data:** A series of JSON objects, each representing a movie or TV show. The objects have the following structure:
    *   `"id"`: A string representing the unique identifier of the movie/show (e.g., "tt8999762").
    *   `"title"`: A string representing the title of the movie/show (e.g., "5. The Brutalist").
    *   `"year"`: A string representing the year of release (e.g., "2024").
    *   `"rating"`: A string representing the rating of the movie/show (e.g., "8.0").
    *   Examples of the JSON objects include:
        *   `{"id":"tt8999762","title":"5. The Brutalist","year":"2024","rating":"8.0"}`
        *   `{"id":"tt27657135","title":"6. Saturday Night", "year":"2024","rating":"7.0"}`
        *   `{"id":"tt17526714","title":"7. The Substance","year":"2024","rating":"7.3"}`
        *   `{"id":"tt10919420","title":"8. Squid Game","year":"2021-2025","rating":"8.0"}`
        *   `{"id":"tt21227864","title":"9. Un matrimonio di troppo","year":"2025","rating":"5.5"}`
        *   `"id":"#2658

---

## Reply 312
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-02-09T17:22:36.650Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/330

Check if you have made the query proprly. also, check if you taken the correct link from the item

---

## Reply 313
**Author**: Tanya kamboj
**Posted**: 2025-02-09T17:22:37.064Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/331

in q10 i am getting error- missing links.

can i get any explanation about this error so that i can figure out this ?

@Saransh_Saini  as i left with this question only

---

## Reply 314
**Author**: Jash Mevada
**Posted**: 2025-02-09T17:23:01.174Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/332

Pdf content one link, I think your converting method was unable to convert link into markdown format , add it manual from pdf.

---

## Reply 315
**Author**: Tanya kamboj
**Posted**: 2025-02-09T17:23:44.720Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/333

I have done that also but still getting same error

---

## Reply 316
**Author**: Tanya kamboj
**Posted**: 2025-02-09T17:24:22.138Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/334

The one with blue line must be link here in the pdf.

---

## Reply 317
**Author**: Arulvadivelan V
**Posted**: 2025-02-09T17:25:39.334Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/335

After that it asking to add tables, i added the same but the issue ‘Missing Tables’ exists

---

## Reply 318
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-02-09T17:25:58.086Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/336

23f2000573:

if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

refer to this @21f3000745

 22f3000804:

can someone help through this error!!

if it is saying something has a mismatch, just spot the mismatch one by one and manually change it @22f3000804

---

## Reply 319
**Author**: Sayan Das
**Posted**: 2025-02-09T17:34:04.509Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/338

Here for the bonus marks, it was great solving the GA4.

---

## Reply 320
**Author**: Megha Gupta
**Posted**: 2025-02-09T17:36:09.369Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/339

After you click the link, a page containing all the questions will appear. Attempt them and save it on that particular page using your IITM email ID. Through your ID, submissions will be taken.

---

## Reply 321
**Author**: Tanya kamboj
**Posted**: 2025-02-09T17:39:48.455Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/340

Thankyou , but now i am getting missing code error. What it means? @23f2000573

---

## Reply 322
**Author**: Ian Jem
**Posted**: 2025-02-09T17:41:44.880Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/341

You just have to add a space after a hyphen

---

## Reply 323
**Author**: Saransh Saini
**Posted**: 2025-02-09T17:46:11.087Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/342

Check if you are using table formating where there is a table, also there is perhaps a code block in the pdf where a small section of text is in different font than the rest.

---

## Reply 324
**Author**: Tanya kamboj
**Posted**: 2025-02-09T17:49:43.501Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/343

No there is no code block in the pdf. Now i m getting missing code error. Why this error can arise @Saransh_Saini

---

## Reply 325
**Author**: Sohini Sarkar 
**Posted**: 2025-02-09T17:52:19.318Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/344

I am also facing the same error in this question

---

## Reply 326
**Author**: Vidushi Singh
**Posted**: 2025-02-09T18:00:21.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/345

the answer format is correct the link is probably not the latest one, I had the same issue because my code was working only for the first 100 entries… you should try paginating your code so it can cover more entries

---

## Reply 327
**Author**: Aditya goyal
**Posted**: 2025-02-09T18:00:29.669Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/346

just change the values as itis coming in the error

---

## Reply 328
**Author**: Vidushi Singh
**Posted**: 2025-02-09T18:06:17.921Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/347

change the name manually as the name is diiferent on imdb according to the region, I had the same issue…

---

## Reply 329
**Author**: Arnav Raj 
**Posted**: 2025-02-09T18:06:48.092Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/348

are you able do it now? Reload and check

---

## Reply 330
**Author**: Rahul 
**Posted**: 2025-02-09T18:08:17.696Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/349

yes facing the same thing

---

## Reply 331
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-02-09T18:10:54.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/350

you are missing code block

Normal : print(123)

Code Block : `print(123)`

you can refer to week 2 q1  for the syntax of code block

---

## Reply 332
**Author**: Nishant kaushik
**Posted**: 2025-02-09T18:11:10.464Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/351

**Image: Screenshot 2025-02-09 234028**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code snippet, specifically a JSON data structure, displayed within what appears to be a dark-themed code editor or console. There's also an error message displayed below the JSON data.

**2. Any text content visible:**

*   **Question:** "What is the JSON data?"
*   **JSON Data:** A long string representing an array of JSON objects. Each object seems to contain information about a movie or TV show. The keys in each object are "id", "title", "year", and "rating". The data includes entries for titles like "A Serbian Film", "Sugar Baby", "Madame Web", "The Human Centipede (First Sequence)", "Knock Knock", "Sunray: Fallen Soldier", "Y2K", "The Idol", "Movie 43", and "Striptease".
*   **Error Message:** "TypeError: Cannot read properties of null (reading 'textContent')"

**3. The context or purpose of what's displayed:**

The image likely shows a scenario where someone is trying to display or process JSON data, and an error has occurred. The question "What is the JSON data?" suggests that the data is being presented as part of a task or problem. The error message indicates that the code attempting to access or manipulate the JSON data is encountering a null value where it expects a text content property.

**4. Technical details (code screenshot):**

*   **JSON Structure:** The JSON data is an array of objects. Each object has the following structure:
    *   `id`: A string, likely an IMDb ID (e.g., "tt1273235").
    *   `title`: A string, the title of the movie or show (e.g., "A Serbian Film").
    *   `year`: A string, the release year (e.g., "2010").
    *   `rating`: A string, a rating value (e.g., "4.9").
*   **Error Type:** The error is a `TypeError`, which means that the code is trying to perform an operation on a value of an unexpected type. In this case, it's trying to read the `textContent` property of a null value. This usually happens when

anyone have idea about this error?

---

## Reply 333
**Author**: Rahul 
**Posted**: 2025-02-09T18:13:12.352Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/352

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a section of a user interface, likely from a software application or website. It presents information about the impact of automating the extraction and processing of bounding box data, specifically in the context of a service called "UrbanRide."  Below this, there's a question and an input field, along with an error message.

**2. Text Content:**

*   **Title:** "Impact"
*   **Introductory Text:** "By automating the extraction and processing of bounding box data, UrbanRide can:"
*   **Bullet Points:**
    *   "Optimize Routing: Enhance route planning algorithms with precise geographical boundaries, reducing delivery times and operational costs."
    *   "Improve Fleet Allocation: Allocate vehicles more effectively across defined service zones based on accurate city extents."
    *   "Enhance Market Analysis: Gain deeper insights into regional performance, enabling targeted marketing and service improvements."
    *   "Scale Operations: Seamlessly integrate new cities into their service network with minimal manual intervention, ensuring consistent data quality."
*   **Question:** "What is the maximum latitude of the bounding box of the city Riyadh in the country Saudi Arabia on the Nominatim API? Value of the maximum latitude"
*   **Input Field Value:** "27.7020999"
*   **Error Message:** "Error: Incorrect latitude. Check OSM ID ending with 8390"

**3. Context and Purpose:**

The first part of the image describes the benefits of using UrbanRide's automated bounding box data processing. These benefits are related to optimizing routing, improving fleet allocation, enhancing market analysis, and scaling operations.

The second part appears to be a data validation or testing scenario. The user is prompted to provide the maximum latitude for the bounding box of Riyadh, Saudi Arabia, using the Nominatim API. The provided value "27.7020999" is flagged as incorrect, suggesting a data validation failure. The error message indicates that the user should check an OpenStreetMap (OSM) ID ending with "8390" to find the correct value.

**4. Technical Details:**

*   **Bounding Box Data:** This refers to the geographical boundaries of a specific area (in this case, the city of Riyadh). Bounding boxes

getting this error

---

## Reply 334
**Author**: Tanya kamboj
**Posted**: 2025-02-09T18:13:35.541Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/353

Yes thankyou i noticed that code block.

But now getting missig heading @Saransh_Saini

---

## Reply 335
**Author**: Arnav Raj 
**Posted**: 2025-02-09T18:13:40.353Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/354

@carlton sir what about this question.

---

## Reply 336
**Author**: Ian Jem
**Posted**: 2025-02-09T18:13:51.114Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/355

You have to go to the Settings tab, select Actions from the left panel and choose General from the drop-down list. Then scroll down completely and choose “Read and Write Permission” under the Workflow Permission section

---

## Reply 337
**Author**: Jayaram
**Posted**: 2025-02-09T18:17:00.243Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/356

Getting at root differnt number of properties for below

"2025-02-10": "Sunny intervals and a gentle breeze",
"2025-02-11": "Light rain showers and a gentle breeze",
"2025-02-12": "Thundery showers and a gentle breeze",
"2025-02-13": "Thundery showers and a moderate breeze",
"2025-02-14": "Sunny intervals and a gentle breeze",
"2025-02-15": "Drizzle and a gentle breeze",
"2025-02-16": "Sunny and a gentle breeze",
"2025-02-17": "Sunny intervals and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze"}

---

## Reply 338
**Author**: Katherine Barreto
**Posted**: 2025-02-09T18:18:19.669Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/357

I’m assuming it’s occurring because the text formatting for the JSON is incorrect. Try and put it in the correct format

---

## Reply 339
**Author**: Aarsh Sohane
**Posted**: 2025-02-09T18:20:37.267Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/358

I’ve reloaded a dozen time and even extracted the data again and again to account for any changes but it still doesn’t work.

---

## Reply 340
**Author**: Jayaram
**Posted**: 2025-02-09T18:20:50.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/359

22f3002723:

{"2025-02-10": "Sunny intervals and a gentle breeze",
"2025-02-11": "Light rain showers and a gentle breeze",
"2025-02-12": "Thundery showers and a gentle breeze",
"2025-02-13": "Thundery showers and a moderate breeze",
"2025-02-14": "Sunny intervals and a gentle breeze",
"2025-02-15": "Drizzle and a gentle breeze",
"2025-02-16": "Sunny and a gentle breeze",
"2025-02-17": "Sunny intervals and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze"}

{“2025-02-09”: “Partly cloudy and light winds”,

“2025-02-10”: “Sunny intervals and a gentle breeze”,

“2025-02-11”: “Light rain showers and a gentle breeze”,

“2025-02-12”: “Thundery showers and a gentle breeze”,

“2025-02-13”: “Thundery showers and a moderate breeze”,

“2025-02-14”: “Sunny intervals and a gentle breeze”,

“2025-02-15”: “Drizzle and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny intervals and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”}

---

## Reply 341
**Author**: Katherine Barreto
**Posted**: 2025-02-09T18:23:16.226Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/361

There needs to be two weeks worth of data so if it’s starting from the 9th it should be till the 22nd

---

## Reply 342
**Author**: Shivansh Gupta
**Posted**: 2025-02-09T18:24:45.474Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/362

make the edits clearly in the repository and then open it, the url that is then showed. Just copy and paste it into the box, it will work

---

## Reply 343
**Author**: Mohit Singhal
**Posted**: 2025-02-09T18:25:05.322Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/363

what problem is their in ques 2 and 3

---

## Reply 344
**Author**: Arnav Raj 
**Posted**: 2025-02-09T18:25:08.080Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/364

yeah same for me. seems we were unlucky  :frowning:

---

## Reply 345
**Author**: Raunak Dey
**Posted**: 2025-02-09T18:27:55.976Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/365

What can I refer to for proper steps to solve Question 10?

Thanks!

---

## Reply 346
**Author**: Rohit Bhatia
**Posted**: 2025-02-09T18:30:30.946Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/367

Q10 is giving errors even after doing everything

---

## Reply 347
**Author**: Jayaram
**Posted**: 2025-02-09T18:30:52.842Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/368

23ds3000241:

o if it’s

getting values dont match for below now

{“2025-02-09”: “Partly cloudy and light winds”,

“2025-02-10”: “Sunny intervals and a gentle breeze”,

“2025-02-11”: “Light rain showers and a gentle breeze”,

“2025-02-12”: “Thundery showers and a gentle breeze”,

“2025-02-13”: “Thundery showers and a moderate breeze”,

“2025-02-14”: “Sunny intervals and a gentle breeze”,

“2025-02-15”: “Drizzle and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny intervals and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”,

“2025-02-19”: “Light cloud and a gentle breeze”,

“2025-02-20”: “Sunny intervals and a moderate breeze”,

“2025-02-21”: “Light rain showers and a moderate breeze”,

“2025-02-22”: “Light cloud and a moderate breeze”}

---

## Reply 348
**Author**: Jayaram
**Posted**: 2025-02-09T18:32:09.036Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/369

thanks for the help…

---

## Reply 349
**Author**: Carlton D'Silva
**Posted**: 2025-02-10T05:09:13.069Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/371

@23f3002537, @21f3000745, @Jeleshiya

Anyone who received the Nur-Sultan parameter for this question and at least attempted it will get a mark.

Kind regards

---

## Reply 350
**Author**: Arnav Raj 
**Posted**: 2025-02-10T12:19:48.767Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/372

sir what about bonus marks cuz my score was 9/10 due to q4(Nur-sultan).

---

## Reply 351
**Author**: Carlton D'Silva
**Posted**: 2025-02-11T03:21:36.200Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/373

The bonus mark will be processed afterwards. That is checked before the scores are pushed to portal.

---

## Reply 352
**Author**: vaishnavi
**Posted**: 2025-02-11T08:51:36.710Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/374

Nominatim API gives me the bounding box of the location. How exactly the bounding box helps me to find the details of the location?

---

## Reply 353
**Author**: Rehbar khan
**Posted**: 2025-02-11T08:51:42.895Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/375

I am facing issues in Q9 , can you help me out?

---

## Reply 354
**Author**: Lokessh Rana
**Posted**: 2025-02-11T08:51:45.993Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/376

const movies = ;

document.querySelectorAll(‘.sc-d5ea4b9d-0.ejavrk’).forEach((item, index) => {

if (index >= 25) return; // Stop after collecting 25 movies

const titleElement = item.querySelector('.ipc-title__text');
const yearElement = item.querySelector('.sc-d5ea4b9d-7.URyjV.dli-title-metadata-item');
const ratingElement = item.querySelector('.ipc-rating-star--rating');

if (titleElement && yearElement) {
    const idMatch = item.querySelector('a[href*="/title/tt"]')?.href.match(/tt(\d+)/);
    const id = idMatch ? `tt${idMatch[1]}` : null;
    const title = titleElement.innerText.trim();
    //const yearText = yearElement.innerText.replace(/\D/g, "").trim(); // Remove non-numeric characters
    const yearText = yearElement.innerText.trim();
    const year = yearText ? yearText : null; // Keep year as a string
    const rating = ratingElement ? ratingElement.innerText.trim() : null; // Keep rating as a string

    if (id && title && year && rating && parseFloat(rating) >= 3 && parseFloat(rating) <= 5) {
        movies.push({ id, title, year, rating });
    }
}

});

// Output JSON data with no spaces after colon

console.log(JSON.stringify(movies, (key, value) => typeof value === ‘string’ ? value.trim() : value, 0));

---

## Reply 355
**Author**: HARISH. S
**Posted**: 2025-02-11T16:03:33.614Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/377

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a screenshot of a web application interface, likely related to an online course or assignment. It shows UI elements such as text, buttons, and information displays.

**2. Text Content:**

*   **Top Bar (Red):** "Ended at Sun, 9 Feb, 2025, 11:59 pm IST" "Score: 0" "Check all" "Save"
*   **Green Box:** "Bonus marks for posting on Discourse" "To encourage discussions, IITM BS students who reply to the discussion on GA4 - Data Sourcing - Discussion Thread \[TDS Jan 2025] with a relevant question or reply will get 1 bonus mark on this graded assignment."
*   "You are logged in as 23f3000975@ds.study.iitm.ac.in."
*   "Logout"
*   **Green Box:** "Recent saves (most recent is your official score)"
    *   "Reload from 9/2/2025, 8:04:05 pm. Score: 8"
    *   "Reload from 9/2/2025, 8:03:25 pm. Score: 8"
    *   "Reload from 9/2/2025, 4:03:58 pm. Score: 4"

**3. Context and Purpose:**

The interface seems to be for an assignment or assessment within an online course. Key aspects:

*   **Deadline:** The top bar indicates a deadline of February 9, 2025, at 11:59 PM IST.
*   **Scoring:** The current score is 0. There are "Check all" and "Save" buttons, suggesting the user can interact with the assignment and save their progress.
*   **Bonus Marks:** Students can earn bonus marks by participating in a specific discussion thread on "GA4 - Data Sourcing" on the Discourse platform.
*   **Login Information:** The user is logged in with a specific email address.
*   **Recent Saves:** The "Recent saves" section displays a history of saved scores,

sir i have completed and saved the test but it shows score 0. and also

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page or application interface, likely related to an online course or learning platform. It displays a sidebar navigation menu on the left and the main content area on the right. The main content area focuses on a "Graded Assignment 3" and provides information about it.

**2. Any text content visible:**

*   **Sidebar Navigation:**
    *   Development Tools
    *   Module 2: Deployment Tools
    *   Module 3: Large Language Models
    *   Project 1
    *   Module 4: Data Sourcing
        *   Graded Assignment 4
            *   Assignment
    *   Module 5: Data Preparation
*   **Main Content Area:**
    *   Graded Assignment 3
    *   The due date for submitting this assignment has passed.
    *   Due on 2025-02-05, 23:59 IST.
    *   You may submit any number of times before the due date. The final submission will be considered for grading.
    *   If you have any difficulty accessing the Graded Assignment, please check the following causes:
        *   Ad blockers need to be disabled/removed.
        *   The site requires cookies for authentication. So any cookie blocking/tracker blocking extensions or software may prevent access.
        *   Javascript is required for the site to work correctly.
        *   Chrome Browser is the recommended software to access the contents.
        *   Disable any browser extensions that may be interfere with the site from working correctly.
        *   Overly aggressive anti-virus software may also cause similar access problems.
    *   You MUST use your Student Id (eg. 22f3xxxxxx@ds.study.iitm.ac.in) to do the Graded Assignment, otherwise your score will not be considered for evaluation.
    *   Graded Assignment 3 is available at this link: https://exam.sanand.workers.dev/tds-2025-01-ga3. Please attempt it.

**3. The context or purpose of what's displayed:**

The image shows information about a graded assignment within an online course. The main purpose is to inform students

the graded assignment is showing like i didn’t submit it. please check on this.

---

## Reply 356
**Author**: SADIYA MAHEEN SIDDIQUI
**Posted**: 2025-02-11T18:41:15.166Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/378

Your most recent score will be considered, as long as you saved it before the deadline

---

## Reply 357
**Author**: Anand S
**Posted**: 2025-02-13T19:20:06.743Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/379

Here are the Discourse IDs that replied to this post. @carlton could you please add 1 mark to them in the GA (not the overall score)?

Please include only those are enrolled this term, obviously.
If they didn’t attempt GA4, please include them anyway and give them 1/10.
If they got 10/10 already, please add 1 mark anyway and give them 11/10.

21F1005510
21f2000296
21f2000588
21f2000709
21f2001369
21f3000745
21f3001379
21f3001797
21f3001993
21f3002277
22ds2000011
22ds3000157
22f1000120
22f1000535
22f2000008
22f2000113
22f2001590
22f2001640
22f3000079
22f3000519
22f3000586
22f3000639
22f3000657
22f3000804
22f3000910
22f3001011
22f3001315
22f3001754
22f3001840
22f3002034
22f3002175
22f3002184
22f3002723
22f3002771
23ds3000040
23ds3000149
23ds3000241
23f1000299
23f1000422
23f1000625
23f1001126
23f1001174
23f1001231
23f1001301
23f1001839
23f1002534
23f1002571
23f1003139
23f2000098
23f2000237
23f2000573
23f2000926
23f2001177
23f2001286
23f2001305
23f2001413
23f2001738
23f2002291
23f2003268
23f2003717
23f2003751
23f2003853
23f2004042
23f2004636
23f2004644
23f2004752
23f2004907
23f2004941
23f2005138
23f2005275
23f2005419
23f3001208
23f3001601
23f3001752
23f3002537
23F300327
23f3003594
23f3003871
23f3004024
23f3004114
23f3004162
24ds1000082_Vivek
24ds2000024
24ds2000108
24ds3000032
24ds3000090
24f2000695
24f2003130
Abhay222
ABHIJITH_VS
adeepu.here
Adityism
akashkunwar
anu2023
AnvithaV
AryanTikam
Atif01
carlton
daksh76
Deepanshutomar
GIRISH_VISHVESHVAR_B
gouthamnischay
H1Dd3n_xx
Haricharan
HARISH.S
iamsarthak
jashmevada
Jayeshbansal
Jeleshiya
JoelJeffrey
koustubhr
lakshaygarg654
Lokkiii
Megha
mohiit
Namannn28
namanshyamsukha
nayonika
Neelakandan
Nelson
nilaychugh
parthpatel
rabbaniIITB
Rehbar
Rohitb
rohitgarg
roy2003
Rrishit
Sagan
sandeepstele
Saransh_Saini
sarvan108
sha_512_av
ShahbaazSingh
sharma_abhay
ShivaniAdhiyaman
shivanshgupta0007
Siddhu3050
Suhani
swatikap
tanmaysahu295
tarundude02
Udipth
vaishnavi.k
Vedant22
vidushi
vidya19
yasharabhavi

---

## Reply 358
**Author**: Nayonika Arora
**Posted**: 2025-02-18T13:13:08.478Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/381

Hello sir, my name is mentioned here however I did not get the bonus mark.

Warm regards,

Nayonika Arora

24ds1000090

---

## Reply 359
**Author**: Rohit Garg
**Posted**: 2025-02-18T13:26:28.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/382

ig, they have not updated.

not reflected on my portal too

---

## Reply 360
**Author**: Avinash Kumar
**Posted**: 2025-02-18T13:49:29.368Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/383

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a discussion thread, likely from an online learning platform or forum. It shows a question posted by a user ("A") and a code snippet with an error message. The left side of the screen displays a navigation menu with categories like "Topics," "My Posts," "Docs," "Courses," "Operational Issues," "Professionals Corner," and "Tags."

**2. Text Content:**

*   **Title:** "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]"
*   **Course Information:** "Courses," "Tools in Data Science," "announcement," "term1-2025," "graded-assignment," "week-4"
*   **Navigation Menu:** "Topics," "My Posts," "Docs," "More," "CATEGORIES," "Courses," "Operational Issues," "Professionals Corner," "All categories," "TAGS," "clarification"
*   **User Post:**
    *   User ID: "22f2000008"
    *   Message: "I am getting this error again and again after running the code in collab this city Nur-Sultan?"
*   **Error Message:**
    *   "Error: Could not find location ID for Nur-Sultan"
    *   "NameError"
    *   Traceback (most recent call last)
    *   ` in ()`
    *   "33"
    *   "34 # BBC Weather URL"
    *   "---> 35 weather\_url = f'https://www.bbc.com/weather/{location\_id}'"
    *   "36"
    *   "37 # Fetch weather data"
    *   "NameError: name 'location\_id' is not defined"
*   **Other Text:** "Reply," "Jan 31," "10d," "Feb 8," "168 / 360," "14m"

**3. Context and Purpose:**

The image captures a user seeking help with a code

As you can see in this screen shot i already tried this question and getting error so i posted it on discourse. But still i did not get any marks for attempting this question.

i got only 9/10.

---

## Reply 361
**Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA
**Posted**: 2025-02-18T14:12:47.049Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/384

Hello @s.anand @carlton Sir,

As can be seen, my roll number is present in this list (21f2000588) and in GA4 I have got 10/10 but unfortunately, that bonus mark hasn’t been added (as can be seen from the score displayed on the dashboard). So I request you to add that bonus mark to the total kindly.

Hoping for a positive response.

Thanks & Regards

Digvijaysinh Chudasama

21f2000588

---

## Reply 362
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-18T15:43:57.703Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/385

@22f2000008 Your roll number is in the list shared by professor Anand.

---

## Reply 363
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-18T15:44:03.726Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/386

*No content*

---

## Reply 364
**Author**: Avinash Kumar
**Posted**: 2025-02-18T16:50:40.193Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/387

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) of a discussion forum or platform, likely related to an online course. It displays a discussion thread titled "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]". The UI includes a sidebar with navigation elements, a main content area displaying discussion posts, and user profile icons.

**2. Text Content:**

*   **Title:** "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]"
*   **Tags:** "Courses", "Tools in Data Science", "announcement", "term1-2025", "graded-assignment", "week-4", "carlton"
*   **Sidebar Navigation:**
    *   "Topics"
    *   "My Posts"
    *   "Docs"
    *   "More"
    *   "CATEGORIES"
        *   "Courses"
        *   "Operational Issues"
        *   "Professionals Corner"
        *   "All categories"
    *   "TAGS"
        *   "clarification"
*   **Discussion Posts:**
    *   **rohitgarg:** "ig, they have not updated. not reflected on my portal too"
    *   **carlton:** "Course TA"
        *   "@23f3002537, @21f3000745, @Jeleshiya Anyone who received the Nur-Sultan parameter for this question and at least attempted it will get a mark. Kind regards"
    *   **22f2000008:** (No visible text content in the initial view)
*   **Dates/Timestamps:** "3h", "Jan 31", "Feb 18", "1h"
*   **Other Text:** "Reply", "Jump to post", "360 / 364"

**3. Context and Purpose:**

The image captures a discussion thread within an online course or learning platform. The discussion seems to revolve around a graded assignment or a specific question related to the "Nur-Sultan parameter." Users are discussing whether updates have been reflected on their portals

I am not saying anything regarding bonus marks. I am asking GA4 q4  about

Nur-Sultan in this question everyone getting error after post in discourse ,sir say who attempt this question get a marks .But i am not recieved this question marks

---

## Reply 365
**Author**: Sarthak Singh Gaur
**Posted**: 2025-02-18T23:42:37.819Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/388

if a student has 10/10 and his name is in the bonus list, how would that look like in the dashboard?

I don’t think it is added in my case.

---

## Reply 366
**Author**: Carlton D'Silva
**Posted**: 2025-02-19T06:57:41.395Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/389

It will show up as 110  marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon.

Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark.

23f3002537@ds.study.iitm.ac.in

23f3003875@ds.study.iitm.ac.in

21f3002112@ds.study.iitm.ac.in

23f2003437@ds.study.iitm.ac.in

22f3002236@ds.study.iitm.ac.in

22f3001705@ds.study.iitm.ac.in

22f2000008@ds.study.iitm.ac.in

21f1001892@ds.study.iitm.ac.in

23f1002075@ds.study.iitm.ac.in

23f1001126@ds.study.iitm.ac.in

22f3002661@ds.study.iitm.ac.in

22f2000506@ds.study.iitm.ac.in

24f1002149@ds.study.iitm.ac.in

23f2002473@ds.study.iitm.ac.in

Kind regards

---

## Reply 367
**Author**: Carlton D'Silva
**Posted**: 2025-02-19T06:58:58.390Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/390

Please refer to this reply.

    [GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/389) Tools in Data Science

    It will show up as 110  marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon. 
Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark. 
23f3002537@ds.study.iitm.ac.in 
23f3…

Kind regards

---

## Reply 368
**Author**: Andrew David
**Posted**: 2025-02-19T08:10:42.117Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/391

For those who didn’t submit but still need to practice the questions like to check if the answer is right, or cross-check the solutions for GA 4 and GA 5, is there a special link where the portal just checks the answer and says right or wrong. I wasn’t able to do GA4 or even try to attempt GA 5 before deadline, but i would like to go through the process of submitting etc. is there any link or solutions for GA 4 and GA5.

---

## Reply 369
**Author**: Andrew David
**Posted**: 2025-02-24T05:46:12.726Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/392

is there anyway to practice the assignments and check answers even though the deadline for the assignment passes? or is the answer given somewhere just for learning sake. I  understand that each set of students get different questions. @Jivraj @carlton @s.anand

---
