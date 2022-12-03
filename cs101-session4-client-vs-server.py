import streamlit as st
import requests


st.set_page_config(
         page_title="Client vs Server",
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

title2 = st.markdown ("""<h2>Client vs Server<br></h2>""",unsafe_allow_html=True)


H1= st.markdown("""
<h4>client</h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
A client can be a device or a program. 
A client device is a machine the end users use to access the web. 
Desktops, laptops, smartphones, tablets are some examples of devices. 
A client program is a program that allows the user to make requests through the web. 
One example is a web browser. 
A user can request for a web page through a web browser. 
Moreover, the programs that can get online support, themes etc. can be also considered as clients.
</p>"""
,unsafe_allow_html=True)


st.markdown("<hr>",unsafe_allow_html=True)

H2= st.markdown("""
<h4>Server<br></h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>
A server is a device that provides services to client requests. These devices run server programs. 
A single server can provide services to multiple clients simultaneously. 
Usually, servers run continuously. 
There can be multiple servers in a single machine. 
For example, there can be both web servers and file servers running at the same time to sever different clients. 
It is also possible to have the client and the server in the same machine.
</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)


T1=st.markdown("""<table cellspacing="0" cellpadding="1" border="1">
  <thead>
    <tr>
      <th> 
        <p style="text-align:center">Client</p>
      </th>
      <th>
        <p style="text-align:center">Server</p>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A Client is a device or a program that requires services via the web.</td>
      <td>A device or a program that responds to the requests of the clients by providing services to them.</td>
    </tr>
    <tr>
      <td>Requests the server for content or service function.</td>
      <td>Provides functions or services to the clients when the client request for services.</td>
    </tr>
    <tr>
      <td>Ex: desktops, laptops, smartphones, tablets and web browsers</td>
      <td>Ex: database servers, file servers, and web servers</td>
    </tr>
  </tbody>
</table>""",unsafe_allow_html=True)


