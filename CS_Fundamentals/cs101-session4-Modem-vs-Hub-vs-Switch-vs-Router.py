import streamlit as st
import requests


st.set_page_config(
         page_title="Modem vs Hub vs Switch vs Router",
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

title2 = st.markdown ("""<h2>Modem vs Hub vs Switch vs Router<br></h2>""",unsafe_allow_html=True)


H1 = st.markdown("""<p>
<h4>Modem</h4>
</p>""",unsafe_allow_html=True)

P1= st.markdown("""<p>
A Modem (modulator-demodulator) is a device that modulates an analog signal to digital information. 
It also decodes carrier signals to demodulate the transmitted information. 
The main aim of the modem is to produce a signal that can be transmitted easily and 
decoded to reproduce the digital data in its original form. 
Modems are also used for transmitting analog signals, from Light Emitting Diodes (LED) to radio.
</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H2= st.markdown("""
<h4>Hub<br></h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>
A Hub is a networking device that allows you to connect multiple PCs to a single network. 
It is used to connect segments of a LAN. A hub stores various ports, 
so when a packet arrives at one port, it is copied to various other ports. 
Hub works as a common connection point for devices in a network.
</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H3= st.markdown("""
<h4>Switch</h4>
""",unsafe_allow_html=True)

P3= st.markdown("""<p>
A network switch learns the association between the MAC addresses of connected devices and its switched ports. 
A switch only sends data to where it needs to go, thus reducing the amount of data on the network, 
accordingly increasing the overall performance of the connected devices while improving security.
</p>"""
,unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H4 = st.markdown("""
<h4>Router<br></h4>
""",unsafe_allow_html=True)

P4= st.markdown("""<p>
Routers are the multiport devices and more sophisticated as compared to repeaters and bridges. 
It contains a routing table that enables it to make decision about the route 
i.e. to determine which of several possible paths between the source and destination is the best for a particular transmission.
<br></p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

T1=st.markdown("""<table cellspacing="0" cellpadding="1" border="1">
  <thead>
    <tr>
      <th> 
        <p style="text-align:center">Modem</p>
      </th>
      <th>
        <p style="text-align:center">Hub</p>
      </th>
      <th>
        <p style="text-align:center">Switch</p>
      </th>
      <th>
        <p style="text-align:center">Router</p>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A Modem modulates and demodulates signals.</td>
      <td>A Hub works on the basis of broadcasting.</td>
      <td>Switch works on the basis of MAC address.</td>
      <td>A router works on the basis of IP address.</td>
    </tr>
    <tr>
      <td>It is used for accessing the Internet as it connects your computer to the ISP.</td>
      <td>A Hub is a multiport repeater in which a signal introduced at the input of any port appears at the output of the all available ports.</td>
      <td>A Switch is &nbsp;a tele-communication &nbsp;device which receives a message from any device connected to it and then transmits the message only to the device for which the message is intended.</td>
      <td>A router reads the header of incoming packet and forward it to the port for which it is intended there by determines the route. It can also perform filtering and encapsulation.</td>
    </tr>
    <tr>
      <td>The modem does not help to examine the data packet. Therefore, the security threat is always there.</td>
      <td>Hub is not an intelligent device that may include amplifier on repeater.</td>
      <td>A Switch is an intelligent device as it passes on the message to the selective device by inspecting the address.</td>
      <td>A route is more sophisticated and intelligent device as it can read IP address and direct the packets to another network with specified IP address. Moreover routers can built address tables that helps in routing decisions.</td>
    </tr>
    <tr>
      <td>It is placed between a telephone line and a router or directly to the computer.</td>
      <td>At least single network is required to connect.</td>
      <td>At least single network is required to connect.</td>
      <td>Router needs at least two networks to connect.&nbsp;</td>
    </tr>
  </tbody>
</table>""",unsafe_allow_html=True)


