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

title2 = st.markdown ("""<h2>Synchronous Dynamic Random Access Memory(SDRAM)<br>
vs <br>
Double Data Rate Synchronous Random Access Memory(DDR SDRAM)</h2>""",unsafe_allow_html=True)

H1= st.markdown("""
<h4>Synchronous Dynamic Random Access Memory(SDRAM)</h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
SDRAM is synchronous, and therefore relies on a clock to synchronize signals, creating predictable orderly cycles of data fetches and writes. 
However, SDRAM transfers data on one edge of the clock. """,unsafe_allow_html=True)

H2= st.markdown("""
<h4>Double Double Data Synchronous Dynamic Random-Access Memory(DDR SDRAM)<br></h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>Double Data Rate Synchronous Dynamic Random Access Memory is a common type of memory used as RAM for most every modern processor. 
First on the scene of this stack of acronyms was Dynamic Random-Access Memory (DRAM), introduced in the 1970s. 
DRAM is not regulated by a clock. DRAM is asynchronous, i.e., not synchronized by any external influence. 
This posed a problem in organizing data as it comes in so it can be queued for the process it’s associated with. 
Because DRAM was asynchronous, it was not going to work as fast with processors that were just getting faster.""",unsafe_allow_html=True)


T1=st.markdown("""</tr></tbody></table><table><tbody><tr>
      <th>SDRAM</th>
      <th>DDR SDRAM</th>
    </tr><tr>
      <th>It refers as synchronous dynamic random access memory</th>
      <th>It refers as Double data rate synchronous dynamic random access memory</th>
    </tr><tr>
      <th>SDRAM has 168 pins and two notches at the connector</th>
      <th>DDR has 184 pins and a single notch at the connector.</th>
    </tr><tr>
      <th>SDRAM was released in 1997</th>
      <th>DDR SDRAM was released in 2000</th>
    </tr><tr>
      <th>SDRAM has less speed in comparison DDR</th>
      <th>DDR can transfer data at roughly twice the speed of SDRAM.</th>
    </tr><tr>
      <th>it’s working on 3.3 volts</th>
      <th>it’s working on 2.5 Volts (standard); 1.8 V (low voltage)</th>
    </tr><tr>
      <th>SDRAM speed is considered as 66 MHz, 100 MHz, 133 MHz</th>
      <th>DDR working on speed as 200 MHz, 266 MHz, 333 MHz, 400 MHz</th>
    </tr><tr>
      <th>SDRAM’s Internal rate range is (100 Mhz-166 Mhz)</th>
      <th>DDR’s Internal rate range is(133 Mhz – 200 Mhz)</th>
    </tr><tr>
      <th>Data rate of SDRAM is (0.8-1.3) GB/s</th>
      <th>Data rate of DDR is (2.1-3.2)</th>
    </tr><tr>
      <th>SDRAM prefetch timing is 1ns</th>
      <th>DDR prefetch timing is 2ns</th>
    </tr><tr>
      <th>SDRAM is waiting wait for the completion of the previous command to be able to do another read/write operation.</th>
      <th>DDR is not waiting wait for the completion of the previous command to be able to do another read/write operation.</th>
    </tr></tbody></table>""",unsafe_allow_html=True)


