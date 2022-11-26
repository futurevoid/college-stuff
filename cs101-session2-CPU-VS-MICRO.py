import streamlit as st
import requests


st.set_page_config(
         page_title="CS101 session2 CPU VS Microprocessor",
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

title1 = st.markdown ("<h2>Processors vs Microprocessors</h2>",unsafe_allow_html=True)

H1 = st.markdown("<h4>Processor</h4>",unsafe_allow_html=True)

P1 =st.markdown("""<p>Processor which is also known as Central Processing Unit (CPU) is a chip, assigned with the instructions of performing logical I/O operations and arithmetical functions of the computer.<br> 
Do not confuse the term CPU/processor with the whole system.<br><br>
In fact, processor or CPU is a small chip, which contains millions of tiny transistors to run the system effectively.<br>
It is the duty of processor to monitor the computer.<br> 
Its main function is to perform complex and difficult arithmetic or logical tasks.<br>
It reads and writes the data on CD/DVD, USB or another removable disk and also reads and writes from internal disks like SSDs and HDDs.<br> 
It performs its functions through the ALU and the CU stands for Arithmetic Logic Unit and Control Unit respectively.</p>
<img src =https://diffzi.com/wp-content/uploads/2018/12/Processor-870x435.jpg>""",unsafe_allow_html=True)

H2 = st.markdown("<h4>MicroProcessor</h4>",unsafe_allow_html=True)

P2  = st.markdown("""<p>Microprocessors are the latest form of CPUs.<br> 
A Microprocessors is an IC in a single chip that performs all the CPU functions with a few new circuits.<br>
Its processing speed is so much greater than the Processor's speed.<br>
Today all the latest CPUs are a microprocessor.<br>
Microprocessors are multipurpose devices,which are capable of accepting and storing different types of data and processing and outputting results according to the instructions.<br>
This invention revamped the whole CPUs realm.<br>
The introduction of higher processors power cost increased the processors processing power and speed.<br>
Before microprocessors, medium and small scale circuits were used for small computers.<br>
But now small computers requires one or a few large scale circuits.
</p>
<img src =https://diffzi.com/wp-content/uploads/2018/12/Microprocessor-870x435.jpg>""",unsafe_allow_html=True)

H3 = st.markdown("<H2>Difference Between HDD and SSD</H2>",unsafe_allow_html=True)
T1 = st.markdown("""<br><table>
<tr>
<th>Function</th>
<th>CPU/Processor</th>
<th>Microprocessor</th>
<tr>
<td>Can process logical and arithmetic operations.</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Deals with BIOS/UEFI, memory channels, PCI-E Slots ,and other motherboard components</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Can have GPU units, sound cards, network cards</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Controls the main computer functions like starting the OS ,opening apps, and etc.</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>The brain of the computer</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>the processor of the motherboard(the small chip on the motherboard)</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Can be Microprocessors</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Can be CPUs</td>
<td>✅</td>
<td>❌</td>
</tr>
</table>
<br>
""",unsafe_allow_html=True)
