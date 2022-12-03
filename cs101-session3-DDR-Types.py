import streamlit as st
import requests


st.set_page_config(
         page_title="Double Data Rate Types",
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

title2 = st.markdown ("""<h2>Double Data Rate Types<br></h2>""",unsafe_allow_html=True)


H1= st.markdown("""
<h4>Double Data Rate Type 1 Synchronous Dynamic Random-Access Memory(DDR1 SDRAM)</h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
The next generation of SDRAM is DDR1, which achieves greater bandwidth than the preceding single data rate SDRAM by transferring data on the rising and falling edges of the clock signal (double pumped). 
Effectively, it doubles the transfer rate without increasing the frequency of the clock. 
The transfer rate of DDR SDRAM is the double of SDR SDRAM without changing the internal clock. 
DDR SDRAM, as the first generation of DDR memory, the prefetch buffer is 2bit, which is the double of SDR SDRAM. 
The transfer rate of DDR is between 266~400 MT/s. 
DDR266 and DDR400 are of this type.</p>"""
,unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H2= st.markdown("""
<h4>Double Data Rate Type 2 Synchronous Dynamic Random-Access Memory(DDR2 SDRAM)<br></h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>
DDR2 SDRAM is the second generation of DDR SDRAM.
Its primary benefit is the ability to operate the external data bus twice as fast as DDR SDRAM. 
This is achieved by improved bus signal. 
The prefetch buffer of DDR2 is 4 bit(double of DDR SDRAM). 
DDR2 memory is at the same internal clock speed (133~200MHz) as DDR, but the transfer rate of DDR2 can reach 533~800 MT/s with the improved I/O bus signal. 
DDR2 533 and DDR2 800 memory types are on the market.""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H3= st.markdown("""
<h4>Double Data Rate Type 3 Synchronous Dynamic Random-Access Memory(DDR3 SDRAM)<br></h4>
""",unsafe_allow_html=True)

P3= st.markdown("""<p>
DDR3 SDRAM is the third generation of DDR SDRAM.DDR3 memory reduces 40% power consumption compared to current DDR2 modules, allowing for lower operating currents and voltages (1.5 V, compared to DDR2's 1.8 V or DDR's 2.5 V). 
The transfer rate of DDR3 is 800~1600 MT/s.
DDR3's prefetch buffer width is 8 bit, whereas DDR2's is 4 bit, and DDR's is 2 bit. 
DDR3 also adds two functions, such as ASR (Automatic Self-Refresh) and SRT (Self-Refresh Temperature). 
They can make the memory control the refresh rate according to the temperature variation.</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H4= st.markdown("""
<h4>Double Data Rate Type 4 Synchronous Dynamic Random-Access Memory(DDR4 SDRAM)<br></h4>
""",unsafe_allow_html=True)

P4= st.markdown("""<p>
DDR4 SDRAM is the fourth generation of DDR SDRAM.
DDR4 memory is the first memory to support 1.2 V operation, which is 20% lower than DDR3's 1.5 V.
DDR4 adds four new Bank Groups technology. Each bank group has the feature of singlehanded operation. 
DDR4 can process 4 data within a clock cycle, so DDR4's efficiency is better than DDR3 obviously. 
DDR4 also adds some functions, such as DBI (Data Bus Inversion), CRC (Cyclic Redundancy Check) and CA parity. 
They can enhance DDR4 memory's signal integrity, and improve the stability of data transmission/access.</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

img = st.markdown("<img src = https://tl360.b-cdn.net/wp-content/uploads/2020/10/DDR1-vs-DDR2-vs-DDR3-vs-DDR4-RAM-2.jpg></img>",unsafe_allow_html=True)

T1=st.markdown("""<table cellspacing="0" cellpadding="1" border="1">
<tbody><tr><td>&nbsp;</td>
<td>&nbsp;DRAM</td>
<td>&nbsp;DDR1</td>
<td>&nbsp;DDR2</td>
<td>&nbsp;DDR3</td>
<td>&nbsp;DDR4</td>
</tr><tr><td>Prefetch</td>
<td>1 – Bit</td>
<td>2 - Bit</td>
<td>4 - Bit</td>
<td>8 - Bit</td>
<td>8 - Bit</td>
</tr><tr><td>Data Rate (MT/s)</td>
<td>100 - 166</td>
<td>266 - 400</td>
<td>533 - 800</td>
<td>1066 - 1600</td>
<td>2133 - 5100</td>
</tr><tr><td>Transfer Rate (GB/s)</td>
<td>0.8 - 1.3</td>
<td>2.1 - 3.2</td>
<td>4.2 - 6.4</td>
<td>8.5 - 14.9</td>
<td>17 - 25.6</td>
</tr><tr><td>Voltage (V)</td>
<td>3.3</td>
<td>2.5 - 2.6</td>
<td>1.8</td>
<td>1.35 - 1.5</td>
<td>1.2</td>
</tr></tbody></table>""",unsafe_allow_html=True)


