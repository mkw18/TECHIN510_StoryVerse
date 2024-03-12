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
If you encounter the following issues after running the code:

- Unable to see the main page
- Any errors on the subpages (set_config, 401 Error, list index out of range, etc)

Please **keep refreshing** until you see the correct ![home page]("https://github.com/mkw18/TECHIN510_StoryVerse/blob/main/files/img/homepage.jpg"), then enter the subpages to play the game.

## Reflections
### What you learned
- How to use html in streamlit to accomplish advanced layout.
- How to achieve page switching by button component in the web-page.
- How to get the most wanted prompt for LLM.
- How to maintain components in stramlit when they are affected by other actions.
- How to update the value of streamlit web-page components.
### What questions/problems did you face?
- The app is not so stable due to the streamlit, and sometimes it doesn't load the homepage at the first time and run into bug. When that happens, we need to refresh again and again for the correct page.
- While streamlit works well with HTML, it can't use the subpage as a href link. So we had to show the image as a gallery inside.