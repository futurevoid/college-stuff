import streamlit as st
import requests


st.set_page_config(
         page_title="CS101 session2 HDD VS SSD",
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
  table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
  }

  td, th {
    border: 1px solid #696969;
    text-align: left;
    padding: 8px;
  }

  tr:nth-child(even) {
    background-color: #696969;
  }
  </style>""",unsafe_allow_html=True)


title = st.markdown(f"<h1>CS101 Computer Science Fundamentals<br>Taught by DR. Heba Elhadidi</h1>",unsafe_allow_html=True)

Bio = st.markdown("<h3>من قبل تامر السعيد شوقي الحسيني الكوش</h3>",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

title2 = st.markdown ("<h2>Dynamic Random Access Memory(DRAM) vs Static Random-Access Memory(SRAM)</h2>",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)\

H1= st.markdown("""
<h4>Dynamic Random Access Memory(DRAM)</h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
Data is stored in capacitors. 
Capacitors that store data in DRAM gradually discharge energy, no energy means the data has been lost. 
So, a periodic refresh of power is required in order to function. 
DRAM is called dynamic as constant change or action(change is continuously happening) i.e. refreshing is needed to keep the data intact. 
It is used to implement main memory. """,unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H2= st.markdown("""
<h4>Static Random-Access Memory(SRAM)<br></h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>Data is stored in transistors and requires a constant power flow. 
Because of the continuous power, SRAM doesn’t need to be refreshed to remember the data being stored. 
SRAM is called static as no change or action i.e. refreshing is not needed to keep the data intact. 
It is used in cache memories.&nbsp;</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

T1=st.markdown("""<table>
  <thead>
    <tr>
      <th></th>
      <th>Dynamic random-access memory</th>
        <th>Static random-access memory</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Introduction</th>
      <td>Dynamic random-access memory is a type of random-access memory that stores each bit of data in a separate capacitor within an integrated circuit.</td>
      <td>Static random-access memory is a type of semiconductor memory that uses bistable latching circuitry to store each bit. The term static differentiates it from dynamic RAM (DRAM) which must be periodically refreshed.</td>
    </tr>
    <tr>
      <th>Typical applications</th>
      <td>Main memory in a computer (e.g. DDR3). Not for long-term storage.</td>
      <td>L2 and L3 cache in a CPU</td>
    </tr>
    <tr>
      <th>Typical sizes</th>
      <td>1GB to 2GB in smartphones and tablets; 4GB to 16GB in laptops</td>
      <td>1MB to 16MB</td>
    </tr>
    <tr>
      <th>Place Where Present</th>
      <td>Present on motherboard.</td>
      <td>Present on Processors or between Processor and Main Memory.</td>
    </tr>
  </tbody>
</table>""",unsafe_allow_html=True)


