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

title2 = st.markdown ("<h2>Hard Disk Drives(HDD) vs Solid State Drive(SSD)</h2>",unsafe_allow_html=True)

H1= st.markdown("""
<h4>Hard Disk Drive (HDD)</h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
An HDD uses magnetism, which allows you to store data on a rotating platter.<br>
It has a read/write head that floats above the spinning platter for Reading and Writing of the data.<br>
The faster the platter spins, the quicker an HDD can perform.<br>
HDD also consists of an I/O controller and firmware, which tells the hardware what to do and communicates with the remaining system.<br>
The full form of HDD is Hard Disk Drive.</p>
<img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjzdiOv8QaCaLOJEDHAmTWXC_wAOUkPmQnNg&usqp=CAU>""",unsafe_allow_html=True)

H2= st.markdown("""
<h4>Solid State Drive (SSD)<br>/h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>
Solid State Drive (SSD) is a non-volatile storage device that stores and retrieves data constantly on solid-state flash memory.<br>
However, this data is stored on interconnected flash memory chips instead of platters, which makes them faster than HDDs.<br>
It provides better performance compared to HDD.</p>
<img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQstR_b8xL00guiPHJhIKaqcoL7kukmYwE5gA&usqp=CAU>""",unsafe_allow_html=True)

T1=st.markdown("""<table class="table table-striped">
<tbody>
<tr>
<th>Hard Disk Drive(HDD)</th>
<th>Solid State Drive(SSD)</th>
</tr>
<tr>
<td>HDD has longer Read and Write time.</td>
<td>SSD has a shorter Read and Write time.</td>
</tr>
<tr>
<td>HDD has higher latency.</td>
<td>SSD has a lower latency.</td>
</tr>
<tr>
<td>HDD supports fewer I/O operations per second (IOPS).</td>
<td>SSD supports more I/O operations per second(IOPS).</td>
</tr>
<tr>
<td>Over a longer time, and with larger files stored on an HDD, there is a high chance of fragmentation.</td>
<td>Fragmentation doesn’t occur on an SSD drive.</td>
</tr>
<tr>
<td>HDD is available in various different capacities.</td>
<td>An SSD drive offers limited storage capacities.</td>
</tr>
<tr>
<td>HDD stands for Hard Disk Drive.</td>
<td>SSD stands for Solid State Drive.</td>
</tr>
<tr>
<td>HDD offers a slower speed for reading and writing data.</td>
<td>SSD is faster at reading and writing data.</td>
</tr>
<tr>
<td>An HDD weighs more.</td>
<td>SDD drives are lighter than HDD drives as they don’t have the rotating disks spindle, and mirror.</td>
</tr>
<tr>
<td>The performance of HDD drives worsens because of the fragmentation.</td>
<td>SSD drive performance is never impacted by fragmentation.</td>
</tr>
<tr>
<td>The moving parts of HDDs make them vulnerable to crashes and damage because of vibration.</td>
<td>SSD drives can tolerate vibration up to 2000Hz, that is more than HDD.</td>
</tr>
<tr>
<td>HDD contains moving mechanical parts, like the arm.</td>
<td>SSD does not contain mechanical parts, only electronic parts like ICs.</td>
</tr>
<tr>
<td>HDD drive is older and more traditional.</td>
<td>SSD is a newer type of storage drive.</td>
</tr>
<tr>
<td>HDD can produce noise due to mechanical movements.</td>
<td>SSD does not produce noise.</td>
</tr>
<tr>
<td>HDD are usually 3.5″ and 2.5″ size for desktop and laptops.</td>
<td>SDD is available in 2.5 inch, 1.8″ and 1.0″, increasing the available space in a computer, especially desktop or server.</td>
</tr>
<tr>
<td>The HDD has moving part and magnetic platters. With more uses they are prone to fail.</td>
<td>The SDD drive has no moving parts. With more uses they are less likely to fail.</td>
</tr>
</tbody>
</table>""",unsafe_allow_html=True)


