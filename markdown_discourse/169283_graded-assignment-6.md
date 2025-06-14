# Graded assignment 6

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1

## Topic Metadata
- **ID**: 169283
- **Slug**: graded-assignment-6
- **Created**: 2025-03-06T13:48:38.931Z
- **Views**: 421
- **Replies**: 21
- **Likes**: 16
- **Tags**: term1-2025, week-6

## Original Post
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-06T13:48:39.245Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1

Please post any questions related to [Graded Assignment 6 - Data Analysis](https://seek.onlinedegree.iitm.ac.in/courses/ns_25t1_se2002?id=25&type=assignment&tab=courses&unitId=23)

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline 2025-03-15T18:30:00Z

---

## Reply 1
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-06T13:49:29.690Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2

*No content*

---

## Reply 2
**Author**: Lovepreet Singh
**Posted**: 2025-03-02T11:45:12.668Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3

The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?

@carlton

---

## Reply 3
**Author**: Sarang Tambe
**Posted**: 2025-03-02T11:57:04.636Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4

@Jivraj @Saransh_Saini

I have similar concern

For Q1, I used the following code:

print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

And got the following output:

Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04

Whereas options are below where none of them are correct.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a user interface element consisting of a list of radio buttons. Each radio button is associated with a text label. One of the radio buttons is selected (filled in with a blue circle).

**2. Any text content visible:**

The text labels associated with the radio buttons are:

*   'Mileage: 0.95'
*   'AvgDistance: -0.05'
*   'Mileage: 0.21'
*   'EngineCapacity: 0.17'

**3. The context or purpose of what's displayed:**

The UI element likely represents a selection of options related to vehicle characteristics or data. The user is presented with a choice between Mileage, Average Distance, and Engine Capacity, each associated with a numerical value. The selected radio button indicates the user's current choice. The single quotes around each label suggest that these are string literals, possibly from a code representation.

**4. Technical details (if applicable):**

The image doesn't show code directly, but the format of the text labels (with single quotes) suggests that this UI element might be generated from code. The values associated with each option could be numerical data being displayed or used in calculations. The negative value for 'AvgDistance' is noteworthy.

Whereas for Q2 (Punjab and Yamaha) I used the following code:

print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

and got the following answers:

Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08

The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a user interface element consisting of a list of radio buttons. Each radio button is associated with a text label. One of the radio buttons is selected (filled in with blue).

**2. Any text content visible:**

The text labels associated with the radio buttons are:

*   'Mileage: 0.95'
*   'AvgDistance: -0.06'
*   'Mileage: 0.24'
*   'EngineCapacity: -0.08'

**3. The context or purpose of what's displayed:**

The UI element likely represents a selection list where the user can choose one option from a set of parameters or features. The values associated with each parameter (e.g., 0.95, -0.06) could represent weights, scores, or some other numerical representation of the importance or relevance of that feature. The fact that one option is already selected suggests that a default value has been chosen or the user has previously made a selection.

**4. Technical details:**

The image shows a standard radio button group. The labels are strings enclosed in single quotes, followed by a colon and a numerical value. The numerical values include both positive and negative numbers. The presence of "Mileage," "AvgDistance," and "EngineCapacity" suggests that the context might be related to vehicle data or analysis.

---

## Reply 4
**Author**: Carlton D'Silva
**Posted**: 2025-03-04T10:11:22.975Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5

@24f2006061 We are looking into it. We will update based on our analysis. Thanks for letting us know.

Kind regards

---

## Reply 5
**Author**: Abhinav
**Posted**: 2025-03-03T18:06:51.395Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6

I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question, likely from an online quiz or assessment. It presents a scenario and asks the user to select the correct answer from a list of options. The question is related to analyzing factors influencing motorcycle resale value.

**2. Any text content visible:**

The image contains the following text:

*   **Question:** "1) As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Delhi. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Yamaha. Use Pearson Correlation Coefficient and price retention is (resale price / original price)."
*   **Point Value:** "1 point"
*   **Answer Options:**
    *   "Mileage: 0.01"
    *   "AvgDistance: 0.00"
    *   "EngineCapacity: 0.13" (This option is currently selected)
    *   "EngineCapacity: 0.95"

**3. The context or purpose of what's displayed:**

The context is an assessment or quiz question related to business analysis, specifically in the automotive industry. The purpose is to test the user's understanding of factors that affect the resale value of motorcycles and their ability to apply statistical concepts like the Pearson Correlation Coefficient. The user is asked to evaluate the impact of mileage, average daily distance traveled, and engine capacity on price retention for Yamaha motorcycles in Delhi.

**4. Technical details if it's a code screenshot or technical diagram:**

This is not a code screenshot or technical diagram. It's a user interface element from a quiz or assessment platform. The radio buttons indicate that only one answer can be selected. The selected radio button for "EngineCapacity: 0.13" suggests that this is the user's current answer.

---

## Reply 6
**Author**: Wasim Ansari
**Posted**: 2025-03-07T17:12:28.199Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7

Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. @carlton @Jivraj @Saransh_Saini

---

## Reply 7
**Author**: Shashannk
**Posted**: 2025-03-08T15:17:03.743Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8

Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out @carlton !

---

## Reply 8
**Author**: RAJ K BOOPATHI
**Posted**: 2025-03-10T07:56:14.493Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9

I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

---

## Reply 9
**Author**: Pradeep Mondal
**Posted**: 2025-03-11T06:42:12.463Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10

Any updates on these? I am too facing the same issue.

@carlton @Jivraj @Saransh_Saini

---

## Reply 10
**Author**: Udipth
**Posted**: 2025-03-11T17:42:32.616Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11

In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question, likely from an online quiz or assessment. It presents a scenario and asks the user to select the best answer from a list of options. The UI elements include:

*   A question number (1)
*   A question prompt
*   Radio buttons for selecting an answer
*   Answer options with text labels

**2. Any text content visible:**

The text content includes:

*   **Question Prompt:** "As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Maharashtra. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Yamaha. Use Pearson Correlation Coefficient and price retention is (resale price / original price)."
*   **Point Value:** "1 point"
*   **Answer Options:**
    *   "'AvgDistance: 0.09'"
    *   "'Mileage: 0.95'"
    *   "'EngineCapacity: -0.02'"
    *   "'Mileage: 0.12'"

**3. The context or purpose of what's displayed:**

The context is a business/data analysis scenario. The question is designed to assess the user's understanding of factors that influence motorcycle resale value and their ability to interpret correlation coefficients. The user is asked to identify which factor (mileage, average distance, or engine capacity) has the greatest positive correlation with price retention, based on the provided correlation coefficients.

**4. Technical details if it's a code screenshot or technical diagram:**

While not a code screenshot or technical diagram, the question involves a statistical concept (Pearson Correlation Coefficient). The coefficients provided (0.09, 0.95, -0.02, 0.12) represent the strength and direction of the linear relationship between each factor and price retention. A coefficient closer to 1 indicates a strong positive correlation, while a coefficient closer to -1 indicates a strong negative correlation. A coefficient close to 0 indicates a weak or no linear correlation. The radio button next to "'Mileage: 0.95'" is selected.

---

## Reply 11
**Author**: Shashannk
**Posted**: 2025-03-12T03:42:05.053Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12

Kindly update us regarding the status of Q1 & Q2 @carlton @Jivraj

---

## Reply 12
**Author**: LAKSHAY
**Posted**: 2025-03-12T11:29:04.042Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13

@Jivraj @carlton @Saransh_Saini

Dear TDS Team,

There are multiple issues in Graded Assignment 6 that require urgent attention:

Questions 1 and 2, along with their options, are ambiguous.
In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.
The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.

The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.

Thank you for your support.

---

## Reply 13
**Author**: Pradeep Mondal
**Posted**: 2025-03-12T13:30:00.912Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14

Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.

For instance:

forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.

but is this talking about the average resale value as no input features are specified?

---

## Reply 14
**Author**: LAKSHAY
**Posted**: 2025-03-12T14:11:15.210Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15

Let’s wait for their response.

I submitted nearby option for Q3 and Q4

---

## Reply 15
**Author**: Vivek Rekha Ashoka
**Posted**: 2025-03-12T14:36:43.739Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16

@Jivraj @carlton @Saransh_Saini

Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).

Thanks

---

## Reply 16
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-13T09:47:03.906Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17

Hi @all

Question intends you to select most correlated one.

Select option which is absolute highest.

---

## Reply 17
**Author**: M v Sunil
**Posted**: 2025-03-14T14:30:12.725Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18

@Jivraj  - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.

Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

---

## Reply 18
**Author**: Shashank Tripathi
**Posted**: 2025-03-14T16:06:48.081Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question, likely from an online quiz or assessment. It presents a scenario and asks the user to select the correct answer from a list of options. The UI elements include:

*   A question prompt.
*   Radio buttons for selecting one of the answer choices.
*   Text labels associated with each radio button, representing the possible answers.

**2. Any text content visible:**

The text content includes:

*   **Question:** "As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Maharashtra. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Honda. Use Pearson Correlation Coefficient and price retention is (resale price / original price)."
*   **Point Value:** "1 point"
*   **Answer Choices:**
    *   'AvgDistance: -0.04'
    *   'AvgDistance: 0.95'
    *   'EngineCapacity: -0.04'
    *   'Mileage: -0.04'

**3. The context or purpose of what's displayed:**

The context is a business/economic analysis scenario. The question is designed to assess the user's understanding of factors affecting motorcycle resale value and their ability to interpret correlation coefficients. The user is asked to analyze the impact of mileage, average daily distance traveled, and engine capacity on price retention for Honda motorcycles in Maharashtra, India. The question specifies the use of the Pearson Correlation Coefficient.

**4. Technical details if it's a code screenshot or technical diagram:**

While not a code screenshot or technical diagram, the question involves a statistical concept (Pearson Correlation Coefficient). The answer choices present correlation values between different factors (average distance, engine capacity, mileage) and price retention. The user needs to understand the meaning of these correlation values (positive, negative, strength) to select the most appropriate answer.

what to do if 3 options have same value -0.04 and all are correct?

---

## Reply 19
**Author**: Khushi Shah
**Posted**: 2025-03-15T05:54:10.148Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20

@carlton @Jivraj

My question 7 for GA6 is :

A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance

Whose options provided are :

10418 meters

12287 meters

10965 meters

11149 meters

However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)

I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)

Kindly look into the question, and let me know about the same (the destination from central command post)

---

## Reply 20
**Author**: Pradeep Mondal
**Posted**: 2025-03-15T06:40:41.714Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/21

Have you succeeded in running the shape file for Q10? It seems to have some error.

@lakshaygarg654

---

## Reply 21
**Author**: LAKSHAY
**Posted**: 2025-03-15T06:52:44.163Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/22

No,

I use google to get MTFCC code for given road segment and  after that mtfcc pdf to classify that road segment.

---

## Reply 22
**Author**: Pradeep Mondal
**Posted**: 2025-03-15T07:29:51.684Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/23

I  downloaded the complete shape file zip from the [census.gov](http://census.gov) site.

Here is the link: [https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip](https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip)

It works fine in QGIS.

@lakshaygarg654

---

## Reply 23
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-03-15T07:50:50.896Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/24

they have not provide all the files needed to read that shp file in the question .

but your link includes them. thanks…

---

## Reply 24
**Author**: LAKSHAY
**Posted**: 2025-03-15T09:26:43.798Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/25

I tried to access shapefile from official website 4-5 days ago, but server was under maintenance. I will check again Q10 after quiz 2.

Thanks for sharing.

---

## Reply 25
**Author**: Kumar Rishabh 
**Posted**: 2025-03-15T15:30:01.842Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/26

My question 9 for GA6 is :

@carlton @Jivraj @Saransh_Saini

**Image: Screenshot 2025-03-15 205444**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code snippet, likely from a Python script, along with the output generated by the script. The code calculates distances between several locations and a central command post, then sorts these locations based on their distance. The output displays the sorted list of locations and their distances from the central command post.

**2. Text Content:**

*   **Code:**
    *   `[26] from haversine import haversine`
    *   `# Define the coordinates of each community and the central command post`
    *   `OakParkTown = (27.0096, -72.3822)`
    *   `EastSpringsSettlement = (27.0769, -72.394)`
    *   `EastFieldsJunction = (27.0961, -72.4248)`
    *   `RedPointTown = (26.9874, -72.426)`
    *   `CentralCommandPostLocation = (27.0552, -72.4893)`
    *   `# Calculate the distances between each community and the central command post`
    *   `distances = {`
    *   `"OakParkTown": haversine(OakParkTown, CentralCommandPostLocation),`
    *   `"EastSpringsSettlement": haversine(EastSpringsSettlement, CentralCommandPostLocation),`
    *   `"EastFieldsJunction": haversine(EastFieldsJunction, CentralCommandPostLocation),`
    *   `"RedPointTown": haversine(RedPointTown, CentralCommandPostLocation)`
    *   `}`
    *   `# Sort the communities based on their distances to the central command post`
    *   `optimal_sequence = sorted(distances, key=distances.get)`
    *   `# Print the optimal evacuation sequence`
    *   `for i, community in enumerate(optimal_sequence, start=1):`
    *   `print(f"{i}. {community} - Distance: {distances[community]:.2f}

**Image: Screenshot 2025-03-15 205456**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question from what appears to be an online quiz or test. The question involves determining the optimal evacuation sequence for four communities based on a "nearest community first" strategy. The image also includes a snippet of Python code.

**2. Text Content:**

*   **Question Text:** "9) If the four communities are: Oak Park Town: (27.0096,-72.3822); East Springs Settlement: (27.0769,-72.394); East Fields Junction: (27.0961,-72.4248); Red Point Town: (26.9874,-72.426) & Central Command Post Location: (27.0552,-72.4893) Using the "nearest community first" evacuation strategy, where the nearest community is determined by the shortest path distance from one community to the other location points, what would be the optimal sequence for evacuating the communities?"
*   **Point Value:** "1 point"
*   **Answer Choices:** Four multiple-choice options, each representing a different evacuation sequence:
    *   ['Start/End', 'East Fields Junction', 'East Springs Settlement', 'Oak Park Town', 'Red Point Town', 'Start/End'] (This option is selected)
    *   ['Start/End', 'Oak Park Town', 'East Fields Junction', 'East Springs Settlement', 'Red Point Town', 'Start/End']
    *   ['Start/End', 'East Springs Settlement', 'Oak Park Town', 'East Fields Junction', 'Red Point Town', 'Start/End']
    *   ['Start/End', 'Red Point Town', 'Oak Park Town', 'East Springs Settlement', 'East Fields Junction', 'Start/End']
*   **Code Snippet:**
    *   `[26] from haversine import haversine`
    *   `# Define the coordinates of each community and the central command post`
    *   `OakParkTown = (27.0096, -72.3822)`

**3. Context and Purpose:**

The question is designed to

I solved it in colab but options are getting mismatched there…kindly clarify this issue..

---

## Reply 26
**Author**: M v Sunil
**Posted**: 2025-03-15T15:45:01.771Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/28

for the above question the options are None of these are matching and answer is around 11.5 kms

3848 meters

6265 meters

4110 meters

5106 meters

---

## Reply 27
**Author**: Amala Natarajan 
**Posted**: 2025-03-15T18:10:33.693Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/29

For 7th Question in GA6 I got the answer 14265.93 Meters but the option I have in 7th are

6069 meters

7687 meters

6106 meters

7035 meters

@carlton @Jivraj

---

## Reply 28
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-03-16T03:40:13.358Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/30

@carlton @Jivraj @Saransh_Saini

for question 4, i have tried `=forecast` and also `=forecast.ets`, both of them are not working. There are two columns for years. One is year of manufacturing, another is year of registration. which one to take.

for question 7, none of the options match. I am selecting the `MOST ACCURATE` among the given options. Hope, it is correct

---

## Reply 29
**Author**: Shashannk
**Posted**: 2025-03-16T08:26:37.649Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/31

Can anyone help me out on how to approach and solve the 10th question please!?

---

## Reply 30
**Author**: LAKSHAY
**Posted**: 2025-03-16T14:22:53.458Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/32

Check the distances of other locations from the central location. One student found **Question 7** of the **GA6 Option Set** based on the distances of other points, which do not match the requirements of Question 7.

---

## Reply 31
**Author**: Vidushi Singh
**Posted**: 2025-03-16T15:42:32.170Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/33

i have the same issue

---

## Reply 32
**Author**: Vidushi Singh
**Posted**: 2025-03-16T15:43:51.901Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/34

yes i have the same issue

and i got the same answer and am give the same options

@carlton sir what to do?

---

## Reply 33
**Author**: Vidushi Singh
**Posted**: 2025-03-16T16:00:21.856Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/35

@Jivraj @Saransh_Saini

For 7th Question in GA6 I got the answer 14265.9275 Meters but the option I have in 7th are

6069 meters

7687 meters

6106 meters

7035 meters

---

## Reply 34
**Author**: Muthupalaniappan
**Posted**: 2025-03-16T18:33:57.063Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/36

Hello Sir,

Can you please check if this is the right answer. As per email received from @carlton sir we should select the absolute maximum value.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question from an online assessment or quiz. It presents a scenario and asks the user to select the correct answer from a list of options. The image also displays feedback indicating that the user's previous answer was incorrect, along with the correct answer.

**2. Text Content:**

*   **Question:** "As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Uttar Pradesh. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Royal Enfield. Use Pearson Correlation Coefficient and price retention is (resale price / original price)."
*   **Point Value:** "1 point"
*   **Answer Options:**
    *   'Mileage: 0.01'
    *   'EngineCapacity: 0.95'
    *   'AvgDistance: -0.13'
    *   'EngineCapacity: 0.09'
*   **Feedback:** "No, the answer is incorrect."
*   **Score:** "Score: 0"
*   **Accepted Answer:** "'EngineCapacity: 0.09'"

**3. Context and Purpose:**

The image is part of an assessment designed to test the user's understanding of factors influencing motorcycle resale value, specifically in the context of Royal Enfield motorcycles in Uttar Pradesh. The question requires the user to apply the concept of Pearson Correlation Coefficient to determine the impact of mileage, average daily distance, and engine capacity on price retention. The feedback indicates whether the user selected the correct answer and provides the correct answer for learning purposes.

**4. Technical Details:**

*   The question involves statistical analysis, specifically the Pearson Correlation Coefficient. This coefficient measures the linear correlation between two variables. In this context, it's used to determine the relationship between factors like mileage, distance, and engine capacity, and the price retention of the motorcycles.
*   The answer options provide correlation values for each factor. The correct answer is the one that represents the most significant correlation between the factor and price retention.
*   The question is likely part of a larger course or training program related to business strategy, market analysis, or the automotive industry.

Example : If we get answers as -0.3 and 0.2 then -0.3 is the right answer as it’s absolut value is maximum.

For the first question the correlation matrix is as follows,

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a correlation matrix visualized as a heatmap. The matrix shows the pairwise correlations between four variables: Mileage (km/l), Average Daily Distance (km), Engine Capacity (cc), and Price Retention (%). The heatmap uses a color gradient, likely from blue to red, to represent the strength and direction of the correlations.  Blue likely indicates negative correlation, and red indicates positive correlation.  Each cell in the matrix contains a numerical value representing the correlation coefficient.  White lines separate the cells.

**2. Any text content visible:**

*   **Variable Names:**
    *   Mileage (km/l)
    *   Avg Daily Distance (km)
    *   Engine Capacity (cc)
    *   Price Retention (%)
*   **Correlation Values:**
    *   0.01 (appears multiple times)
    *   0.04
    *   1.00 (appears twice)
    *   0.09 (appears twice)
    *   -0.13

**3. The context or purpose of what's displayed:**

The image is a visualization of the correlation between different features of a dataset, likely related to cars or vehicles. The purpose is to quickly identify which variables are strongly correlated with each other. For example, a high positive correlation (close to 1) indicates that as one variable increases, the other tends to increase as well. A negative correlation (close to -1) indicates that as one variable increases, the other tends to decrease. A correlation close to 0 indicates a weak or no linear relationship.

**4. Technical details (based on the image):**

*   **Correlation Matrix:** The image represents a correlation matrix, a square table that shows the correlation coefficients between variables.
*   **Heatmap:** The correlation matrix is visualized as a heatmap, where colors represent the magnitude of the correlation.
*   **Correlation Coefficient:** The numbers in the cells are correlation coefficients, which range from -1 to 1.
*   **Perfect Correlation:** The diagonal elements of the matrix are 1.00, indicating a perfect positive correlation of a variable with itself.
*   **Symmetry:** The matrix is likely symmetric, meaning the correlation between variable A and variable B is the same as the correlation between

So shouldn’t it be -0.13?

---

## Reply 35
**Author**: Carlton D'Silva
**Posted**: 2025-03-17T03:43:16.185Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/37

Thanks for the colour picture.

If you read the aforementioned email…

**Image: Screenshot 2025-03-17 at 9.09.55 am**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows an email interface. It displays an email message. The email is a clarification regarding a graded assignment (GA6).

**2. Any text content visible:**

*   **Subject:** \[TDS Jan 25] GA 6 Clarification
*   **Sender:** donot\_reply@study.iitm.ac.in
*   **Recipient:** 25t1\_se2002-announce
*   **Body:**
    *   "Dear Learner,"
    *   "GA6 Question 1 and 2 were not very clear in what was expected."
    *   "The answer we are looking for is the Absolute Maximum Correlation Coefficient."
    *   "eg. If you find -0.3 and 0.2 as the matching options. The correct answer is -0.3"
    *   "Do not worry if the portal marks you as being incorrect. We will still push the right scores on the dashboard if you chose the correct option."
    *   "Kind regards"

**3. The context or purpose of what's displayed:**

The email is a clarification sent to students regarding a graded assignment (GA6). It seems that questions 1 and 2 of the assignment were not clearly worded. The email clarifies that the expected answer involves the "Absolute Maximum Correlation Coefficient." It also addresses a potential issue where the portal might incorrectly mark the correct answer as wrong, assuring students that the correct scores will be reflected on the dashboard.

**4. Technical details:**

*   The email address "donot\_reply@study.iitm.ac.in" suggests that this is an automated email from an educational institution (IITM - likely Indian Institute of Technology Madras).
*   The recipient "25t1\_se2002-announce" is likely a mailing list or group for a specific course or cohort (25t1\_se2002).
*   The mention of a "portal" and "dashboard" indicates that the course likely uses an online learning management system (LMS) for assignments and grading.
*   The email addresses a potential discrepancy between the automated grading system and the intended correct answer, suggesting a known issue with the assignment's evaluation.

Kind regards (in colour  :wink: )

---

## Reply 36
**Author**: M v Sunil
**Posted**: 2025-03-18T17:07:15.417Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/38

Thank you sir. i have got questions 1 and 2 both marked as 0.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question from what appears to be an online assessment or quiz. The question is related to business strategy and data analysis, specifically in the context of a motorcycle dealership. The image also shows the user's answer, feedback on the answer, the score, and the accepted answer.

**2. Any text content visible:**

*   **Question:** "As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Maharashtra. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for KTM. Use Pearson Correlation Coefficient and price retention is (resale price / original price)."
*   **Point Value:** "1 point"
*   **Answer Choices:**
    *   'AvgDistance: 0.01'
    *   'Mileage: 0.03'
    *   'EngineCapacity: -0.06'
    *   'Mileage: 0.95'
*   **Feedback:** "No, the answer is incorrect."
*   **Score:** "Score: 0"
*   **Accepted Answers:** "Accepted Answers:"
*   **Correct Answer:** "'Mileage: 0.03'"

**3. The context or purpose of what's displayed:**

The image is from an assessment where the user is being tested on their understanding of how different factors (mileage, average distance, engine capacity) correlate with the resale value of KTM motorcycles in Maharashtra. The user needs to identify which factor has the strongest positive correlation with price retention, based on the provided Pearson Correlation Coefficients. The user selected 'AvgDistance: 0.01' which was incorrect. The correct answer was 'Mileage: 0.03'.

**4. Technical details if it's a code screenshot or technical diagram:**

The image is not a code screenshot or technical diagram. It's a screenshot of a user interface, likely from an online learning platform or assessment tool. The numbers associated with each factor are Pearson Correlation Coefficients, which are statistical measures of the linear correlation between two variables. A value closer to 1 indicates a strong positive correlation, a value closer to -1 indicates a strong negative correlation

In my case Please note the above two questions are asked to calculate pearson correlation coefficient for KTM brand and for maharashtra and Karnataka states.

I have used excel to calculate the pearson correlation coefficient. Below the values I got for each question. Please verify.

|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for Karnataka||

-0.026685695

|pearson correlation coefficient between average distance travelled and Price retention for kTM for karnataka||

0.003953219

|pearson correlation coefficient between average Engine capacity and Price retention for kTM for karnataka||

-0.010839295

|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for maharashta||

0.029128825

|pearson correlation coefficient between average distance travelled and Price retention for kTM for Maharashtra||

0.013019585

|pearson correlation coefficient between average Engine capacity and Price retention for kTM for Maharashtra||

-0.056866212

---

## Reply 37
**Author**: M v Sunil
**Posted**: 2025-03-18T17:14:25.559Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/39

@Jivraj @carlton

Dear sirs,

I have question no 7 got marked as 0. Please check the question below and the haversine distance for the given post comes to around 11.5 kms which is not matccing with any of the options and I have selected the closest answer. please check and let me know.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question from what appears to be an online quiz or test. It presents a scenario involving a wildfire and the need to calculate distances for evacuation routes. The question is followed by four possible answers, presented as radio buttons. Below the answer choices, there's feedback indicating that the previous answer was incorrect, the score is 0, and the accepted answer is provided.

**2. Text Content:**

*   **Question:** "7) A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction: (26.5596,-99.5336); Maple Fields Station: (26.4212,-99.4597); South Glen Crossing: (26.5962,-99.5243); Cedar Creek Retreat: (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance"
*   **Possible Answers:**
    *   "3848 meters"
    *   "6265 meters" (This option is selected)
    *   "4110 meters"
    *   "5106 meters"
*   **Feedback:**
    *   "No, the answer is incorrect."
    *   "Score: 0"
*   **Accepted Answer:**
    *   "Accepted Answers:"
    *   "5106 meters"
*   **Point Value:** "1 point"

**3. Context and Purpose:**

The context is a scenario-based question likely related to emergency management, geography, or mathematics. The purpose is to assess the test-taker's ability to:

*   Understand a real-world problem.
*   Apply a specific method (Haversine package) to calculate distances

---

## Reply 38
**Author**: Khushi Shah
**Posted**: 2025-03-19T17:09:05.009Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/40

@carlton @Jivraj

I did raise the question 2 days before the GA6 Deadline and doing so again after being marked as incorrect

My question 7 was A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance

10418 meters

12287 meters

10965 meters

11149 meters

Whose right answer turned out 6873, however the answer pushed is 12287 meters, which is nowhere near the closest options (it would’ve been correct if the destination was summit shores village which isn’t the case with this question)

Also, my question 4 was :

As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Kawasaki - Ninja 300 in Tamil Nadu, using historical data.

134483

94774

150666

199711

Whose correct option (through different methods and algorithms) was approximately closest to 94774 and again answer pushed is 150666 which again turns out to be incorrect

So is the case with questions 1 and 2 (where answers aren’t pushed according to absolute values, but as conveyed earlier, I believe this shall be resolved)

Kindly look into it

Thanks and Regards

---

## Reply 39
**Author**: PREMDEEP MAITI
**Posted**: 2025-03-20T14:49:56.474Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/41

@carlton @Jivraj @Saransh_Saini

In Q4 , neither which regression model to use is given nor the what random state to use is given. I tried linear regression, random forest regression but it is giving   answer which vary each time I compute, also, the option values are quite close.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question, likely from an online quiz or assessment. It presents a scenario and asks the user to select the correct answer from a list of options. The UI elements include:

*   A question prompt.
*   Radio buttons for selecting one of the multiple-choice answers.
*   A feedback message indicating that the selected answer was incorrect.
*   A score display.

**2. Any text content visible:**

*   **Question:** "4) As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Hero - HF Deluxe in Punjab, using historical data."
*   **Answer Options:**
    *   194515
    *   185108
    *   142646
    *   152609
*   **Feedback:** "No, the answer is incorrect."
*   **Score:** "Score: 0"

**3. The context or purpose of what's displayed:**

The image is part of an assessment or quiz related to investment analysis and forecasting. The question requires the user to apply their knowledge of forecasting models, considering factors like seasonality and long-term trends, to predict the resale value of a specific motorcycle model in a particular region. The feedback and score indicate that the user has attempted the question and received an incorrect answer.

**4. Technical details (if it's a code screenshot or technical diagram):**

There is no code or technical diagram in the image. It's a UI screenshot of a quiz question.

---

## Reply 40
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-22T12:34:00.092Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/43

@all

we are looking into problems with question 4, 6 and 10.

---

## Reply 41
**Author**: Swati Kapoor
**Posted**: 2025-04-11T07:29:18.139Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/44

Hi,

Have the corrections been done on GA6 marks?

---

## Reply 42
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-11T09:33:15.884Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/45

Yes, corrections have been done in Ga6 marks.

---

## Reply 43
**Author**: Swati Kapoor
**Posted**: 2025-04-11T16:31:37.494Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/46

Just to confirm, were the answers shown on the portal correct because I’m getting the same score as shown in the portal.

---
