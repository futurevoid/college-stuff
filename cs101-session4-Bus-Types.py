import streamlit as st
import requests


st.set_page_config(
         page_title="Bus types",
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

title2 = st.markdown ("""<h2>Bus Types<br></h2>""",unsafe_allow_html=True)


H1= st.markdown("""
<h4>Control Bus<br></h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
The motherboard's control bus manages the activity in the system. 
The control bus, like the other buses, is simply a set of connections among the parts in the computer.
All parts "agree to recognize" that if one connection carries a voltage and the next one does not, 
it means that the central processor reads from memory. If the connections reverse roles, 
the processor writes to memory. 
Other connections deal with the "chunking" of data 8, 16, 32 or 64 bits at a time. 
Still others determine if data is being shuttled to the central processor from memory or the keyboard. 
This signaling system prevents data from going to the wrong place.
</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H2= st.markdown("""
<h4>Data Bus</h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>
The data bus acts as a conduit for data from the keyboard, memory and other devices. 
It passes information at speeds up to billions of characters per second. 
The central processor reads the data, performs calculations, and moves new data back to memory, 
the hard drive and other locations. 
The control bus determines which direction the data is moving.
</p>"""
,unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H4 = st.markdown("""
<h4>Address Bus<br></h4>
""",unsafe_allow_html=True)

P3= st.markdown("""<p>
The computer must be able to access every character of memory rapidly, 
so every character has its own address number. 
The central processor specifies which addresses it wants to read or write and the address bus carries this information to a memory controller circuit, 
which locates and fetches the information. Some locations, called random-access memory, 
hold program instructions and temporary calculation results. 
Other locations point to the hard drive, mouse and keyboard. 
The control bus specifies which of these two sets of addresses become active for a particular memory operation.
</p>""",unsafe_allow_html=True)


st.markdown("<hr>",unsafe_allow_html=True)

img = st.markdown("<img src = https://electricalacademia.com/wp-content/uploads/2018/11/350px-Computer_system_bus.png></img>",unsafe_allow_html=True)



