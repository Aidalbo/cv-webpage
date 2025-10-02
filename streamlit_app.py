import streamlit as st
from pathlib import Path

st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'lebenslauf.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left,right = st.columns (2)

left.image("aid1.png", width=250)

right.markdown("""
               <h3>Aid Ajdini</h3>
               <em>Ich finde IT faszinierend, weil sich dieser Bereich in den letzten Jahren stark weiterentwickelt hat. 
               Deshalb möchte ich später gerne im IT-Bereich arbeiten </em>
            

               
               """,unsafe_allow_html=True)



right.download_button(
        label="📄 Download CV",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
)

         

st.header("IT-Kompetenzen", anchor=False,divider="blue")

st.markdown("""
          🌎 Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit 
            
          💻 Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            
          📊 Office-Suite: Versierter Umgang mit Microsoft Word und PowerPoint
         
            
            """,unsafe_allow_html=True)

st.header("Schulbildung", anchor=False,divider="blue")

st.subheader("HTL MÖDLING",anchor=False)
st.markdown("""
            **Schwerpunkt**: Elektrontechnik

            **Zeitraum** : 2025-laufend
""")
st.subheader("FMS Schaumburgergasse",anchor=False)
st.markdown("""
            **Schwerpunkt**: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologin und Wirtschaft

            **Zeitraum** : 2024-2025
""")

st.subheader("Mittelschule Georg-Wilhelm-Pabst-Gasse", anchor=False)
st.write("**Zeitraum** : 2020-2024 ")


st.header("Arbeitserfahrung", anchor=False,divider="blue")
st.markdown("""
            📕 Berufspraktische Tage 1: Bei MobiNil von 18. bis 22. Nov. 2024
            
            📕 Berufspraktische Tage 2: Bei AUVA von 24. bis 28. Feb. 2025
         """,unsafe_allow_html=True)

st.header("Zusätzliche Qualifikationen", anchor=False,divider="blue")
st.markdown("""
         🚄 Ich lerne sehr schnell neue Programme und Technologien

         🤼 Ich arbeite gut mit anderen Menschen zusammen.
            
         🗂️ Ich interessiere mich sehr für den IT-Bereich    
            
         ⚖️ Ich bin zuverlässig und erledige meine Aufgaben pünktlich
            
         🏛️ Selbstständiges Arbeiten und Verantwortung übernehmen liegt mir        """)

st.header("Interessen und Hobby", anchor=False,divider="blue")
st.markdown("""
         🚀     Immer was neues lernen
            
         ⌨️ PC : Videospiele spielen und am PC arbeiten
            """)
