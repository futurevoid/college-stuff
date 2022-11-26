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

Bio = st.markdown("<h3>Made by Tamer saeed shawky elhussieny elkoush</h3>",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

title2 = st.markdown ("""<h2>Double Data Rate Types<br></h2>""",unsafe_allow_html=True)

H1= st.markdown("""
<h4>Double Double Data Synchronous Type 1 Dynamic Random-Access Memory(DDR1 SDRAM)</h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
The next generation of SDRAM is DDR1, which achieves greater bandwidth than the preceding single data rate SDRAM by transferring data on the rising and falling edges of the clock signal (double pumped). 
Effectively, it doubles the transfer rate without increasing the frequency of the clock. 
The transfer rate of DDR SDRAM is the double of SDR SDRAM without changing the internal clock. 
DDR SDRAM, as the first generation of DDR memory, the prefetch buffer is 2bit, which is the double of SDR SDRAM. 
The transfer rate of DDR is between 266~400 MT/s. 
DDR266 and DDR400 are of this type.</p>"""
,unsafe_allow_html=True)

H2= st.markdown("""
<h4>Double Double Data Synchronous Type 2 Dynamic Random-Access Memory(DDR2 SDRAM)<br></h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>
DDR2 SDRAM is the second generation of DDR SDRAM.
Its primary benefit is the ability to operate the external data bus twice as fast as DDR SDRAM. 
This is achieved by improved bus signal. 
The prefetch buffer of DDR2 is 4 bit(double of DDR SDRAM). 
DDR2 memory is at the same internal clock speed (133~200MHz) as DDR, but the transfer rate of DDR2 can reach 533~800 MT/s with the improved I/O bus signal. 
DDR2 533 and DDR2 800 memory types are on the market.""",unsafe_allow_html=True)

H3= st.markdown("""
<h4>Double Double Data Synchronous Type 3 Dynamic Random-Access Memory(DDR3 SDRAM)<br></h4>
""",unsafe_allow_html=True)

P3= st.markdown("""<p>
DDR3 SDRAM is the third generation of DDR SDRAM.""",unsafe_allow_html=True)

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


