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
  text-align: left; !important
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

title2 = st.markdown ("""<h2>Register Types<br></h2>""",unsafe_allow_html=True)

H1= st.markdown("""
<h4>Accumulator</h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
This is the most frequently used register used to store data taken from memory. 
It is in variable numbers in a variety of microprocessors.</p>"""
,unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H2= st.markdown("""
<h4>Memory Data Registers (MDR)<br></h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>
It contains data to be written into or to be read out from the addressed location.""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H3= st.markdown("""
<h4>Memory Address Registers (MAR)<br></h4>
""",unsafe_allow_html=True)

P3= st.markdown("""<p>
It holds the address of the location to be accessed from memory. 
MAR and MDR (Memory Data Register) together facilitate the communication of the CPU and the main memory.</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H4= st.markdown("""
<h4>General Purpose Registers<br></h4>""",unsafe_allow_html=True)

P4= st.markdown("""<p>
These are numbered as R0, R1, R2….Rn-1, and used to store temporary data during any ongoing operation. 
Its content can be accessed by assembly programming. 
Modern CPU architectures tends to use more GPR so that register-to-register addressing can be used more, 
which is comparatively faster than other addressing modes.</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H5= st.markdown("""
<h4>Program Counter (PC)<br></h4>
""",unsafe_allow_html=True)

P5= st.markdown("""<p>
Program Counter (PC) is used to keep the track of execution of the program. 
It contains the memory address of the next instruction to be fetched. 
PC points to the address of the next instruction to be fetched from the main memory when the previous instruction has been successfully completed. 
Program Counter (PC) also functions to count the number of instructions. 
The incrementation of PC depends on the type of architecture being used. 
If we are using 32-bit architecture, the PC gets incremented by 4 every time to fetch the next instruction.</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H6= st.markdown("""
<h4>I/O Buffer Registers<br></h4>
""",unsafe_allow_html=True)

P6= st.markdown("""<p>
These registers are used to store data temporarily during the input/output operations.
</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H7= st.markdown("""
<h4>Instruction Register (IR)<br></h4>
""",unsafe_allow_html=True)

P7= st.markdown("""<p>
The IR holds the instruction which is just about to be executed. 
The instruction from PC is fetched and stored in IR. 
As soon as the instruction in placed in IR, 
the CPU starts executing the instruction and the PC points to the next instruction to be executed.
</p>""",unsafe_allow_html=True)


st.markdown("<hr>",unsafe_allow_html=True)


