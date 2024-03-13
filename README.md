# StoryVerse
## About this project
StoryVerse is a text-based game platform containing two game themes, a lateral thinking puzzle and a life story generation simulator. 

## Technologies used
- LLM
- Data crawling and storage
- Multiple pages
- HTML in streamlit
- Data visualization

## Problems trying to solve
This web-page serves as a free-time entertainment. People can play games even when they can’t find enough peers and enrich their leisure time.

## How to run

Open the terminal and run the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app_homepage.py
```

**Note:** 
If you want to come back to the homepage from any subpage, just refresh.

## Reflections
### What you learned
- How to use html in streamlit to accomplish custom layout.
- How to achieve page switching by button component in the web-page.
- How to get the most wanted prompt for LLM.
- How to maintain components in stramlit when they are affected by other actions.
- How to use different streamlit components(tab，container, button...etc) to construct complexed functions.
- How to update the value of streamlit web-page components.
### What questions/problems did you face?
- The app is not so stable due to the streamlit, and sometimes it doesn't load the homepage at the first time and run into bug. When that happens, we need to refresh again and again for the correct page.
- While streamlit works well with HTML, it can't use the subpage as a href link. So we had to show the image as a gallery inside.
### Future improvement
- We would like to add user database to store user's login information and play history. For instance, how much time did user take to guess one lateral thinking puzzle. What kind of story ending and begining of lifestory simulator.