# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:44:31 2020

@author: kolhe
"""

import streamlit as st
import streamlit.components.v1 as components
import random
import SessionState
import EmailSender as es
import wolframalpha
app_id = "94LP3R-RAVYXL4323"
client = wolframalpha.Client(app_id) 

session_state = SessionState.get(r1 = random.randint(1, 99),\
                                 r2 = random.randint(1, 99),\
                                 r3 = random.randint(1, 99),\
                                 r4 = random.randint(1, 99),\
                                 r5 = random.randint(1, 99),\
                                 r6 = random.randint(1, 50),\
                                 r7 = random.randint(51, 99),\
                                 r8 = random.randint(1, 99),\
                                 r9 = random.randint(1, 99),\
                                 r10 = random.randint(1, 99),\
                                 r11 = random.randint(1, 30),\
                                 r12 = random.randint(31, 99),\
                                 r13 = random.randint(1, 10),\
                                 r14 = random.randint(1, 10),\
                                 r15 = random.randint(1, 10),\
                                 r16 = random.randint(1, 10),
                                 name = ''
                                 )

count = 0
    
menu = ["Maths", "English To Marathi", "Marathi To English"]
choice = st.sidebar.selectbox("Menu", menu)

@st.cache
def get_result(question):
    res = client.query(question) 
    answer = next(res.results).text 
    return(answer) 

# Select elements from a sidebar
if(choice == 'English To Marathi'):
    html_code = """
        <div style="background-color: #1abc9c; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">English To Marathi</h1>
        </div>
        """
    components.html(html_code)
    
    st.success("Nanavati")
    answer = st.selectbox("Answer", ['Dancing', 'Reading', 'Sports'])
    st.write("Your hobby is: ", answer)

elif(choice == 'Marathi To English'):
    html_code = """
        <div style="background-color: #1abc9c; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">Marathi To English</h1>
        </div>
        """
    components.html(html_code)
    

elif(choice == 'Maths'):
    html_code = """
        <div style="background-color: #1abc9c; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">Maths</h1>
        </div>
        """
    components.html(html_code)
    
    name = st.text_input("Your Name")
    session_state.name = name.title()
    st.success('Hello {}'.format(session_state.name))
    
    answers_list = []
    
    
    # Q1.    
    q1 = "{} + {} + {}".format(session_state.r1, session_state.r2, session_state.r3)
    st.warning("Q1. {} = ".format(q1))
    answer1 = st.text_input("Answer 1")
    answer1 = answer1.title()
    ac1 = get_result(q1)
    a1 = st.empty()
        
    # Q2.
    q2 = "{} + {}".format(session_state.r4, session_state.r5)
    st.warning("Q2. {} = ".format(q2))
    answer2 = st.text_input("Answer 2")
    answer2 = answer2.title()
    ac2 = get_result(q2)
    a2 = st.empty()
    
    # Q3.
    q3 = "{} - {}".format(session_state.r7, session_state.r6)
    st.warning("Q3. {} = ".format(q3))
    answer3 = st.text_input("Answer 3")
    answer3 = answer3.title()
    ac3 = get_result(q3)
    a3 = st.empty()
    
    # Q4.
    q4 = "{} + {} + {}".format(session_state.r8, session_state.r9, session_state.r10)
    st.warning("Q4. {} = ".format(q4))
    answer4 = st.text_input("Answer 4")
    answer4 = answer4.title()
    ac4 = get_result(q4)
    a4 = st.empty()
    
    # Q5.
    q5 = "{} - {}".format(session_state.r12, session_state.r11)
    st.warning("Q5. {} = ".format(q5))
    answer5 = st.text_input("Answer 5")
    answer5 = answer5.title()
    ac5 = get_result(q5)
    a5 = st.empty()
    
    # Q6. 
    q6 = "{} - {}".format(session_state.r7, session_state.r11)
    st.warning("Q6. {} = ".format(q6))
    answer6 = st.text_input("Answer 6")
    answer6 = answer6.title()
    ac6 = get_result(q6)
    a6 = st.empty()
    
    
    # Q7.
    q7 = "{} + {}".format(session_state.r4, session_state.r9)
    st.warning("Q7. {} = ".format(q7))
    answer7 = st.text_input("Answer 7")
    answer7 = answer7.title()
    ac7 = get_result(q7)
    a7 = st.empty()
    
    # Q8.
    q8 = "{} + {} + {}".format(session_state.r2, session_state.r5, session_state.r7)
    st.warning("Q8. {} = ".format(q8))
    answer8 = st.text_input("Answer 8")
    answer8 = answer8.title()
    ac8 = get_result(q8)
    a8 = st.empty()
    
    # Q9.
    q9 = "{} * {}".format(session_state.r13, session_state.r14)
    st.warning("Q9. {} = ".format(q9))
    answer9 = st.text_input("Answer 9")
    answer9 = answer9.title()
    ac9 = get_result(q9)
    a9 = st.empty()
    
    # Q10.
    q10 = "{} * {}".format(session_state.r15, session_state.r16)
    st.warning("Q10. {} = ".format(q10))
    answer10 = st.text_input("Answer 10")
    answer10 = answer10.title()
    ac10 = get_result(q10)
    a10 = st.empty()
    
    
    if(st.button("Check")):
        if(answer1==str(ac1)):
            a1.success('Correct Answer')
            count = count + 1
            q1 = ''
        else:
            a1.error('Wrong Answer')
            
        if(answer2==str(ac2)):
            a2.success('Correct Answer')
            count = count + 1
            q2=''
        else:
            a2.error('Wrong Answer')
        
        if(answer3==str(ac3)):
            a3.success('Correct Answer')
            count = count + 1
            q3=''
        else:
            a3.error('Wrong Answer')
            
        if(answer4==str(ac4)):
            a4.success('Correct Answer')
            count = count + 1
            q4=''
        else:
            a4.error('Wrong Answer')
            
        if(answer5==str(ac5)):
            a5.success('Correct Answer')
            count = count + 1
            q5=''
        else:
            a5.error('Wrong Answer')
        
        if(answer6==str(ac6)):
            a6.success('Correct Answer')
            count = count + 1
            q6=''
        else:
            a6.error('Wrong Answer')
            
        if(answer7==str(ac7)):
            a7.success('Correct Answer')
            count = count + 1
            q7=''
        else:
            a7.error('Wrong Answer')
            
        if(answer8==str(ac8)):
            a8.success('Correct Answer')
            count = count + 1
            q8=''
        else:
            a8.error('Wrong Answer')
        
        if(answer9==str(ac9)):
            a9.success('Correct Answer')
            count = count + 1
            q9=''
        else:
            a9.error('Wrong Answer')
            
        if(answer10==str(ac10)):
            a10.success('Correct Answer')
            count = count + 1
            q10 =''
        else:
            a10.error('Wrong Answer')
            
        es.emailsender(session_state.name, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    
    if(count == 10):
        st.balloons()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    