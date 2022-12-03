import streamlit as st
import requests


st.set_page_config(
         page_title="Internet vs WWW vs Network vs Web",
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

title2 = st.markdown ("""<h2>Internet vs WWW vs networks vs Web<br></h2>""",unsafe_allow_html=True)


H1= st.markdown("""
<h4>Networks<br></h4>
""",unsafe_allow_html=True)

P1= st.markdown("""<p>
A network is two or more connected computer which can share resource like a printer, an internet connection, application, etc. 
It is a collection of computer systems and devices which are linked together using a wireless network or via communication devices and transmission media.
A network provides connectivity between computers and devices within a restricted range where only one entity is controlled or authorized to manage the entire system.""",unsafe_allow_html=True)


st.markdown("<hr>",unsafe_allow_html=True)

H2= st.markdown("""
<h4>The Internet</h4>
""",unsafe_allow_html=True)

P2= st.markdown("""<p>
The Internet is a global WAN.
The Internet (Interconnected Network) is a global system which use TCP/IP protocol suite to link various types of electric devices worldwide. 
The internet is a collection of interconnected devices which are spread across the globe. 
It is a network of networks that consist of public, private, public, sales, finance, academic, business and government networks. 
</p>"""
,unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H3= st.markdown("""
<h4>The World Wide Web<br></h4>
""",unsafe_allow_html=True)

P3= st.markdown("""<p>
The World Wide Web (WWW) is an internet-based application. It refers to the enormous number of online sites that are linked together. Hyperlinks are used to connect these sites. As a result, the user may effortlessly navigate from one page to the next to find the information they need. A website is a collection of related web pages.

The HTTP protocol and a web browser are used to access web pages or websites on the World Wide Web. 
The HTTP protocol is a collection of rules for moving data across the internet, including text, pictures, audio, video, and other multimedia assets. 
On the World Wide Web, there are many different types of web pages and websites. 
Academic, e-commerce and social networking are some of the most common categories.
</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

H4 = st.markdown("""
<h4>The Web<br></h4>
""",unsafe_allow_html=True)

P4 = st.markdown("""<p>
The Web is the only way to access information through the Internet. 
It’s a system of Internet servers that support specially formatted documents. 
The documents are formatted in a markup language called HTML, or “HyperText Markup Language”, 
which supports a number of features including links and multimedia. 
These documents are interlinked using hypertext links and are accessible via the Internet. 
</p>""",unsafe_allow_html=True)

st.markdown("<hr>",unsafe_allow_html=True)

T1=st.markdown("""<table cellspacing="0" cellpadding="1" border="1">
<tbody>
  <tr>
    <td>
      <strong>Network</strong>
    </td>
    <td>
      <strong>Internet</strong>
    </td>
    <td>
      <strong>WWW</strong>
    </td>
    <td>Web</td>
    
  </tr>
  <tr>
    <td>A network is a collection of computer systems and devices which are linked together using a wireless network or via communication devices and transmission media.</td>
    <td>The Internet allows you to link your computer to any other computer on the planet.&nbsp;</td>
    <td>The World Wide Web is a collection of information accessible through the Internet.</td>
    <td>The Web is the only way to access information through the Internet.</td>
  </tr>
  <tr>
    <td>Connect the system using different parameters.</td>
    <td>The Internet is a worldwide network of interconnected computer networks that connect devices using the TCP/IP protocol.&nbsp;</td>
    <td>The World Wide Web refers to HTML-formatted online material that may be accessed using the HTTP protocol.</td>
    <td>The Web is a model for sharing information using the Internet.</td>
  </tr>
  <tr>
    <td>One entity has administrative rights to manage the network</td>
    <td>The Internet can be compared to a large bookstore.&nbsp;</td>
    <td>The World Wide Web can be considered as a store with a collection of books.</td>
    <td>The protocol used by the web is HTTPS.</td>
  </tr>
  <tr>
    <td>Hundreds or a few thousand number of PC, get linked at one time.</td>
    <td>
      <p>Internet is superset of WWW.</p>
    </td>
    <td>The World Wide Web is a subset of the Internet.</td>
    <td>The Web is accessed by the Web Browser.</td>
  </tr>
  <tr>
    <td>To exchange data and collaborate with peers.</td>
    <td>
      <p>It first appeared in the late 1960s.</p>
    </td>
    <td>Tim Berners-Lee, an English scientist, created the World Wide Web in 1989.</td>
    <td>Accesses documents and online sites through browsers.</td>
  </tr>
  <tr>
    <td>Local Area Network, Wide Area Network, Campus Area Network, and Home Area Network.</td>
    <td>The Internet is mostly based on hardware.</td>
    <td>In comparison to the Internet, the WWW is more software-oriented.</td>
    <td>Also, The Web is a system of Internet servers that support specially formatted documents.</td>
  </tr>
</tbody></table>""",unsafe_allow_html=True)


