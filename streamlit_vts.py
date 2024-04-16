import streamlit as st
import requests
import openai
from openai import OpenAI


# make streamlit app look better: https://medium.com/international-school-of-ai-data-science/make-your-streamlit-web-app-look-better-14355c2db871

# Setting the app to be in wide mode
st.set_page_config(layout="wide")

# #A9A9A9, #D8BFD8, #5F9EA0, #6495ED, #DCDCDC, #D3D3D3, #A52A2A, #8B0000
# Function to change the sidebar color
def change_sidebar_color():
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                background-color: #8B0000;
            }
        </style>
        """, unsafe_allow_html=True)
# Call the function to change the sidebar color
change_sidebar_color()


# Indiana University Logo and Details
profile_image_url = "https://raw.githubusercontent.com/vamado09/Virtual-Tissue-Simulation/main/IU_logo4.png" 
html_profile = f'''
    <div style="display: flex; flex-direction: column; align-items: center; color: white;">
        <img src="{profile_image_url}" style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover; display: block; margin-left: auto; margin-right: auto;">
        <div style="text-align: center;"><b>Indiana University Bloomington</b></div>
        <div style="text-align: center; font-size: 14px; padding: 0 10px;"><b>Luddy School of Informatics, Computing, and Engineering</b></div>
        <div style="text-align: center;">Virtual Tissue Simulation Project</div>
    </div>
'''
st.sidebar.markdown(html_profile, unsafe_allow_html=True)
# Space between Menu and Profile
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)


# Function to fetch markdown from GitHub
def fetch_markdown_from_github(file_path):
    # Base GitHub URL for the raw files
    github_base_url = "https://raw.githubusercontent.com/vamado09/Virtual-Tissue-Simulation/main/"
    markdown_url = f"{github_base_url}{file_path}"
    response = requests.get(markdown_url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Could not retrieve content. Status code: {response.status_code}"


# Sidebar for package selection
packages = ["About Us", "GPT Model (OpenAI) 🧠", "Text Summarizer 📄", "Artistoo", "CompuCell3D", "PhysiCell", "Morpheus", "CHASTE", "Tissue Forge"]
selected_package = st.sidebar.selectbox("Select information about:", packages)
# Display the selected package title
st.title(selected_package)


# Handle the "About Us" section
if selected_package == "About Us":
    # First image stretched across the full width of the screen
    col1, col2, col3 = st.columns([1, 2, 1]) # 1,2,1
    with col2:        
        group_image_url = "https://raw.githubusercontent.com/vamado09/Virtual-Tissue-Simulation/main/Group.png"
        st.image(group_image_url, use_column_width=True)
    tissue_home_url = "https://raw.githubusercontent.com/vamado09/Virtual-Tissue-Simulation/main/cells.png"
    st.image(tissue_home_url, use_column_width='always')  # This will make the image use the full width available
    about_us_content = fetch_markdown_from_github("AboutUs_Test.md")
    st.markdown(about_us_content, unsafe_allow_html=True)
    

elif selected_package == "GPT Model (OpenAI) 🧠":
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        # Create a button for the OpenAI API key
        openai_api_key_url = "https://platform.openai.com/account/api-keys"
        html_openai_key = '''
            <a href="{0}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #F8F8FF; color: black; padding: 10px; text-align: center; border-radius: 5px; margin-top: 10px;">
                    <span style="margin-left: 5px;">Get an OpenAI API key</span>
                </div>
            </a>
        '''.format(openai_api_key_url)
        st.sidebar.markdown(html_openai_key, unsafe_allow_html=True)

    st.markdown("**Important: You will need to generate an OpenAI API Key to try our ChatBot.**")
    st.write("**Model = gpt-3.5-turbo**")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you? Ask anything related to Virtual Tissue Simulation."}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
        
 
# Text Summarizer 📄"
elif selected_package == "Text Summarizer 📄":
    # Text Summarizer Code
    st.title("📄 Text Summarizer")

    # Sidebar for OpenAI API key input
    openai_api_key = st.sidebar.text_input("OpenAI API Key", key="openai_api_key", type="password")

    # Main app interface for text summarizer
    article_text = st.text_area("Enter your scientific texts to summarize")
    output_size = st.radio("What kind of output do you want?", ["To-The-Point", "Concise", "Detailed"])

    # Set output tokens based on user selection
    if output_size == "To-The-Point":
        out_token = 50
    elif output_size == "Concise":
        out_token = 128
    else:
        out_token = 516

    # Button to generate summary
    if st.button("Generate Summary"):
        if len(article_text) > 100:
            if openai_api_key:
                # Set the OpenAI API key
                openai.api_key = openai_api_key

                # Corrected use of GPT-3 to generate a summary of the article
                response = openai.completions.create(
                    model="gpt-3.5-turbo-instruct",  # Specifying the model
                    prompt=f"Please summarize this scientific article for me in a few sentences: {article_text}",
                    max_tokens=out_token,
                    temperature=0.5
                )

                # Display the generated summary
                res = response.choices[0].text.strip()
                st.success(res)

                # Option to download the result
                st.download_button('Download result', res)
            else:
                st.error("Please enter your OpenAI API key to generate a summary.")
        else:
            st.warning("Please enter more text to summarize (at least 100 words).")


# Handle tabs for "Artistoo" package
elif selected_package == "Artistoo":
    artistoo_home_image_url = "https://raw.githubusercontent.com/vamado09/Virtual-Tissue-Simulation/main/Artistoo_Logo.png"
    st.image(artistoo_home_image_url, use_column_width=True) # This will make the image use the full width available
    tab_titles = ["Content", "Documentation", "Images", "Sources"]
    artistoo_files = {
        "Content": "Artistoo_Test.md",
        "Documentation": "Data_Curation.md",
        "Images": "Artistoo_Images.md",
        "Sources": "Sources_file_name.md"
    }
    tabs = st.tabs(tab_titles)
    for tab, title in zip(tabs, tab_titles):
        with tab:
            st.header(title)
            tab_content = fetch_markdown_from_github(artistoo_files[title])
            st.markdown(tab_content, unsafe_allow_html=True)



    

