import streamlit as st
import hydralit_components as hc

st.set_page_config(
    page_title="FA",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded"
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#can apply customisation to almost all the properties of the card, including the progress bar
theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

cc = st.columns(4)

with cc[0]:
 # can just use 'good', 'bad', 'neutral' sentiment to auto color the card
 hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good',bar_value=77)

with cc[1]:
 hc.info_card(title='Some BAD BAD', content='This is really bad',bar_value=12,theme_override=theme_bad)

with cc[2]:
 hc.info_card(title='Some NEURAL', content='Oh yeah, sure.', sentiment='neutral',bar_value=55)

with cc[3]:
 #customise the the theming for a neutral content
 hc.info_card(title='Some NEURAL',content='Maybe...',key='sec',bar_value=5,theme_override=theme_neutral)
 #####

# define what option labels and icons to display
option_data = [
   {'icon': "bi bi-hand-thumbs-up", 'label':"Agree"},
   {'icon':"fa fa-question-circle",'label':"Unsure"},
   {'icon': "bi bi-hand-thumbs-down", 'label':"Disagree"},
]

# override the theme, else it will use the Streamlit applied theme
over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}
font_fmt = {'font-size':'150%'}

# display a horizontal version of the option bar
op = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,horizontal_orientation=True)

# display a version version of the option bar
#op2 = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,horizontal_orientation=False)

###
# can apply customisation to almost all the properties 0f the progress ba
override_theme_1 = {'bgcolor': '#EFF8F7','progress_color': 'green'}
override_theme_2 = {'bgcolor': 'green','content_color': 'white','progress_color': 'red'}
override_theme_3 = {'content_color': 'red','progress_color': 'orange'}

# can just use 'good', 'bad', 'neutral' sentiment to auto color the bar
hc.progress_bar(25,'Something something')
hc.progress_bar(35,'Something something',sentiment='good')
hc.progress_bar(95,'Something something',sentiment='neutral')
hc.progress_bar(47,'Something something',sentiment='bad')

# customise the the theming for a neutral content
hc.progress_bar(5,'Something something - 1a',key='pa1',override_theme=override_theme_1)
hc.progress_bar(35,'Something something - 2a',key='pa2',sentiment='good',override_theme=override_theme_2)
hc.progress_bar(95,'Something something - 3a',key='pa3',sentiment='neutral')
hc.progress_bar(47,'Something something - 4a',key='pa4',sentiment='bad',override_theme=override_theme_3)
