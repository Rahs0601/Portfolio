import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# **RAHUL N SHETTIGAR**
''')

image = Image.open('Profile.png')
st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
ECE graduate trying to find an Opportunity to figure in an Exceedingly enjoyable and requesting climate. 
Self-motivated, extremely engaged and diligent applier hoping to develop with the event of the organization by Performing on my skills and knowledge.
''')

####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
#
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #FA8072;">
  <a class="navbar-brand" target="_blank">Rahul N Shettigar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#rahul-n-shettigar">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#internships">Internships</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#extra-curricular-activities">Extra Curricular Activities</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#hobbies">Hobbies</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b):
    col1, col2 = st.columns([4, 4])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


####################
st.markdown('''
## Education
''')

txt('**St Joseph Engineering College**, Mangaluru Karnataka India', '2019-present')
txt('*B. Tech in Electronics and Communication Engineering*', '')
st.markdown('''
- CGPA: `8.21`
''')

txt('**Shri Marikamba Govt. PU College**, Sirsi Karnataka India', '2017-2019')
txt('*P. U. in Electronics*', '')
st.markdown('''
- Percentage: `89%`
''')

txt('**Ave Maria High School**, Sirsi Karnataka India', '2017')
txt('*High School*', '')
st.markdown('''
- Percentage: `80%`
''')

#####################
st.markdown('''
## Projects
''')

st.markdown('''
### Software Projects
''')

txt('**Stock Predication System**', 'Sep 2022')
txt('*https://rahs0601-stock-predication-stock-96s3hp.streamlitapp.com/*', '')
st.markdown('''
- web based Application that predicts the stock price of a company based on the past and the current data of the company.
- The data is fetched from the yahoo finance website.
- The model is trained using the data.
- built using Python, Streamlit, Pandas and Plotly.
''')

txt('**Recommendation System**', 'Aug 2022')
txt('*https://rahs0601-recommdation---system-app-t6lql5.streamlitapp.com*', '')

st.markdown('''
- Web based Application That Recommends Similar Anime, Books, Movies and Music selected.
- Uses Machine Learning to find Similar Items.
- Used NumPy Pandas and Scikit-Learn to perform the Machine Learning Algorithm.
- Used Stream-lit to create the Web Application.
''')

txt('**Price Comparison System**', 'Jun 2022')
txt('*https://github.com/Rahs0601/projects/blob/main/priceCompare.py*', '')
st.markdown('''
- Python Script That Compares Prices of different Websites and gives the Specifications, Prices, and Ratings from Amazon, Flipkart, and Reliance Digital.
- Used BeautifulSoup to parse the HTML and extract the same.
''')

txt('**Virtual Assistant**', 'Jan 2022')
txt('*https://github.com/Rahs0601/projects/blob/main/virutal%20Assistant.py*', '')
st.markdown('''
- Built a basic virtual assistant that can play music tell time and search based on what the user ask for
- Used Pythons Speech Recognition, text to speech, Wikipedia and pywhatkit libraries is used to perform the tasks.
''')

txt('**Bill splitter using Python**', 'Sep 2021')
txt('*https://github.com/Rahs0601/projects/blob/main/bill_splitter.py*', '')
st.markdown('''
- Python Script that splits the bill equally among the people and gives the amount each person must to pay.
- Using Python Dictionary to store the bill details and split the bill among the group people.
''')

st.markdown('''
### Hardware Projects
''')

txt('**Plant Watering Robot**', 'Aug 2022')
st.markdown('''
- Using Arduino Uno, IR sensors,  DC pump and Motor driver L298N Prototype was developed to water plants.
- The Arduino Uno is used to Control Motor Driver and turn on the pump to water the plant.
- The IR sensors are used to detect the plants.
''')

txt('**Self-Balancing Robot**', 'Jan 2022')
st.markdown('''
- Using Arduino UNO, MPU-6050, Motor Driver L298N prototype was developed to balance the robot.
- The MPU-6050 is used to detect the angle of the robot.
- The motor driver is used to control the motor.
''')

txt('**Bluetooth-controlled car**', 'Jan 2019')
st.markdown('''
- Using Arduino UNO, Motor Driver L298N, and Bluetooth module, Bluetooth controlled Robot was developed 
- The Arduino UNO is used to Control Motor Driver.
- The Bluetooth module is used to control the robot.
''')

st.markdown('''
## Internships
''')

txt('**Institute of Electrical and Electronics Engineers**', '')
txt('*Machine Learning Intern*', 'Sep 2022 - Present')
txt('*link*','')
st.markdown('''
- Built a Speech to Speech Translation web application using Machine Learning.
- Used Pytorch to build LSTM and Encoder Decoder Algorithm.
- Used Streamlit to build the Web Application.
''')

txt('**Advanced System design using FPGA**', '')
txt('*Short term training program*', 'Apr 2022 - Sep 2022')
txt('*https://bit.ly/advancedfpga*','')
st.markdown('''
- Using FPGA Built a 4bit Processor.
- Used Verilog to design the processor.
''')

txt('**JPMorgan Chase**', '')
txt('*Software Engineering Virtual Experience*', 'Oct 2021 - Dec 2021')
txt('*https://bit.ly/softwarexp*','')
st.markdown('''
- Interface with a stock price data feed
- Use JPMorgan Chase frameworks and tools
- Display data visually for traders
- Use Python, React and Typescript to develop the application
''')

txt('**NEO Foundation**', '')
txt('*Campus Ambassador*', 'Sep 2021 - Oct 2021')
txt('*https://bit.ly/neocampus*','')
st.markdown('''
- Helped the students to understand NEO exams and be their resource for future help related to exams.
- Using social media helped the students to understand the resources related to NEO exams.
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Verilog`, `MATLAB`, `C`')
txt3('Python Libraries',
     '`Stream-Lit`, `Pandas`, `NumPy`, `Scikit-Learn`, `BeautifulSoup`, `Pywhatkit`, `Pickle`')
txt3('Operating System', '`Windows`, `Linux (GUI)`, `Android`')
txt3('Software', '`VS code`, `Pycharm`, `MATLAB and Simulink`, `Xilinx Vivado` , `Multisim`, ')

st.markdown('''
## Certifications
''')
txt4('**Programming for Everybody**', 'https://bit.ly/rahspythoncertificate')
txt4('**Designing Communication System: Wireless and 5G With MATLAB and Simulink**', 'https://bit.ly/rahsdesigningcomsys')
txt4('**Signal Processing Onramp**', 'https://bit.ly/rahssignalonramp')
txt4('**IUCEE AI for All**', 'https://bit.ly/rahsai')
txt4('**Java Programming**', 'https://bit.ly/rahsjava')
txt4('**Arduino Master Class**', 'https://bit.ly/rahsardunio')
txt4('**Ethical Hacking**', 'https://bit.ly/rahsethical')


st.markdown('''
## Extra Curricular Activities
''')
txt('**Treasurer** of Institute of Electrical and Electronics Engineers (IEEE) SJEC student branch', '')
txt('**Project Manager** of Indo Universal Collaboration for Engineering Education (IUCEE) SJEC student chapter', '')
txt('Member of The National Service Scheme (NSS) SJEC unit', '')


st.markdown('''
## Hobbies
''')
txt('Mobile Photography', '')
txt('Photo editing using Lightroom-Mobile', '')
txt('Reading books', '')

#####################
st.markdown(''' ## Social Media ''')
txt2('LinkedIn', 'https://www.linkedin.com/in/rahul-shettigar-77bb19192/')
txt2('GitHub', 'https://github.com/Rahs0601')
txt2('Instagram', 'https://www.instagram.com/rahs_since2002/')
txt2('Photography ', 'https://bit.ly/rahsclicks')
