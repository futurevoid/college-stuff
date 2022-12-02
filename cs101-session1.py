import streamlit as st
import requests

st.set_page_config(
         page_title="CS101 session1",
     page_icon="",
     initial_sidebar_state="collapsed",
 )



remove_menu_footer = """
<style>
#MainMenu {visibility: hidden;}
footer { visibility:hidden; }
</style>
"""

css = st.markdown("""<style>
.list1{
  text-align: center;
  }
  html body div#root div div.withScreencast div div.stApp.css-ffhzg2.eczokvf1 div.appview-container.css-1wrcr25.egzxvld4 section.main.css-k1vhr4.egzxvld3 footer.css-1lsmgbg.egzxvld0{
    visibility: hidden;
  }
  html body div#root div div.withScreencast div div.stApp.css-ffhzg2.eczokvf1 header.css-1avcm0n.e8zbici2 div.css-14xtw13.e8zbici0 span#MainMenu button.css-1rs6os.edgvbvh3{
    visibility: hidden;
  }
  </style>""",unsafe_allow_html=True)


title = st.markdown(f"<h1>CS101 Computer Science Fundamentals<br>Taught by DR. Heba Elhadidi</h1>",unsafe_allow_html=True)

Bio = st.markdown("<h3>من قبل تامر السعيد شوقي الحسيني الكوش</h3>",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)
Q1 = st.markdown("<h4>Types of Computer applications</h4>",unsafe_allow_html=True)

subtitle1 = st.markdown(f"<h5>Types of Computer software applications:</h5>",unsafe_allow_html=True)
list1 = st.markdown("""<ul id=list1>
  <li>Web browsers</li>
  <li>Business software</li>
  <li>Education software</li>
  <li>Multimedia software</li>
  <li>Graphical software</li>
  <li>Video games</li>
  <li>Data entry (Presentation software,Spreadsheet software,Multimedia software)</li>

</ul>  
""",unsafe_allow_html=True)

subtitle2 = st.markdown(f"<h5>Types of Computer hardware applications:</h5>",unsafe_allow_html=True)
list2 = st.markdown("""<ul id=list2>
  <li>Analog computers (continous data)</li>
  <li>Digital computers (discrete data)</li>
  <li>Hybrid computers (continous and discrete data)</li>
  <li>Mainframe computers</li>
  <li>Minicomputers</li>
  <li>Workstation</li>
  <li>Personal computers(PC)/Microcomputers</li>
</ul>  
""",unsafe_allow_html=True)
st.markdown("<hr>",unsafe_allow_html=True)

Q2 = st.markdown("<h4>PC not booting and not making a beep, what to do?</h4>",unsafe_allow_html=True)
list3 = st.markdown("""<ol id=list3>
  <li>Checking the ram DIMMs placement</li>
  <li>Resetting the Bios(Removing the CMOS Battery)</li>
  <li>Checking power supply cables</li>
  <li>Try unplugging all peripherals (keyboard,mouse,speakers and etc.)</li>
  <li>Try replacing The CPU</li>
  <li>Try removing the GPU</li>
  <li>Try replacing the Motherboard</li>
  <li>Try checking PSU cables</li>
  <li>Try replacing the PSU</li>
</ol>  
""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)
Q3 = st.markdown("<h4>Parallel Processing is</h4>",unsafe_allow_html=True)
p1 = st.markdown("""<p id=p1>breaking Large operations into small , discrete , often alike parts<br>
executed simultaneously by multiple processors sharing memory</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)
Q4 = st.markdown("<h4>AI stands For</h4>",unsafe_allow_html=True)
p2 = st.markdown("""<p id=p2>Artificial Intelligence</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)
Q5 = st.markdown("<h4>the biggest computer in size is</h4>",unsafe_allow_html=True)
p3 = st.markdown("<p id=p3>The Mainframe computer</p>",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)
Q6 = st.markdown("<h4>Data is converted to Human readable data by</h4>",unsafe_allow_html=True)
p4 = st.markdown("<p id=p4>Output sources</p>",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)
Q7 = st.markdown("<h4>Binary operated computers are</h4>",unsafe_allow_html=True)
p5 = st.markdown("<p id=p5>Digital computers</p>",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)
Q7 = st.markdown("<h4>Hardware can be physically touched</h4>",unsafe_allow_html=True)
p5 = st.markdown("<p id=p5>True</p>",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)
Q7 = st.markdown("<h4>Is not a computer type</h4>",unsafe_allow_html=True)
p5 = st.markdown("<p id=p5>Login computer</p>",unsafe_allow_html=True)
