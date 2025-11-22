import streamlit as st
import pandas as pd
import random

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Malay Master AI",
    page_icon="🇲🇾",
    layout="wide"
)

# --- 2. The Data (Bulletproof Method) ---
# Using direct Python list to prevent CSV parsing errors
vocab_data = [
    {"id": 1, "malay_word": "Saya", "ipa_pronunciation": "/sa.ja/", "part_of_speech": "Pronoun", "english_meaning": "I / Me", "burmese_meaning": "ကျွန်တော် (male) / ကျွန်မ (female)", "malay_example_sentence": "Nama saya Ali.", "burmese_example_translation": "ကျွန်တော့်နာမည် အလီပါ။"},
    {"id": 2, "malay_word": "Awak", "ipa_pronunciation": "/a.waʔ/", "part_of_speech": "Pronoun", "english_meaning": "You", "burmese_meaning": "ခင်ဗျား (to male) / ရှင် (to female)", "malay_example_sentence": "Awak apa khabar?", "burmese_example_translation": "ခင်ဗျား နေကောင်းလား။"},
    {"id": 3, "malay_word": "Makan", "ipa_pronunciation": "/ma.kan/", "part_of_speech": "Verb", "english_meaning": "To eat", "burmese_meaning": "စားတယ်", "malay_example_sentence": "Saya mahu makan nasi.", "burmese_example_translation": "ကျွန်တော် ထမင်း စားချင်တယ်။"},
    {"id": 4, "malay_word": "Minum", "ipa_pronunciation": "/mi.num/", "part_of_speech": "Verb", "english_meaning": "To drink", "burmese_meaning": "သောက်တယ်", "malay_example_sentence": "Jom minum air.", "burmese_example_translation": "ရေ သွားသောက်ရအောင်။"},
    {"id": 5, "malay_word": "Ya", "ipa_pronunciation": "/ja/", "part_of_speech": "Particle", "english_meaning": "Yes", "burmese_meaning": "ဟုတ်ကဲ့", "malay_example_sentence": "Ya, saya faham.", "burmese_example_translation": "ဟုတ်ကဲ့၊ ကျွန်တော် နားလည်တယ်။"},
    {"id": 6, "malay_word": "Tidak", "ipa_pronunciation": "/ti.daʔ/", "part_of_speech": "Adverb", "english_meaning": "No / Not", "burmese_meaning": "မဟုတ်ဘူး / မ...ဘူး", "malay_example_sentence": "Saya tidak tahu.", "burmese_example_translation": "ကျွန်တော် မသိဘူး။"},
    {"id": 7, "malay_word": "Terima kasih", "ipa_pronunciation": "/tə.ri.ma ka.seh/", "part_of_speech": "Phrase", "english_meaning": "Thank you", "burmese_meaning": "ကျေးဇူးတင်ပါတယ်", "malay_example_sentence": "Terima kasih banyak.", "burmese_example_translation": "အများကြီး ကျေးဇူးတင်ပါတယ်။"},
    {"id": 8, "malay_word": "Apa", "ipa_pronunciation": "/a.pa/", "part_of_speech": "Pronoun", "english_meaning": "What", "burmese_meaning": "ဘာလဲ", "malay_example_sentence": "Ini apa?", "burmese_example_translation": "ဒါ ဘာလဲ။"},
    {"id": 9, "malay_word": "Siapa", "ipa_pronunciation": "/si.a.pa/", "part_of_speech": "Pronoun", "english_meaning": "Who", "burmese_meaning": "ဘယ်သူလဲ", "malay_example_sentence": "Siapa nama awak?", "burmese_example_translation": "ခင်ဗျားနာမည် ဘယ်သူလဲ။"},
    {"id": 10, "malay_word": "Ada", "ipa_pronunciation": "/a.da/", "part_of_speech": "Verb", "english_meaning": "To have / To exist", "burmese_meaning": "ရှိတယ်", "malay_example_sentence": "Saya ada soalan.", "burmese_example_translation": "ကျွန်တော့်မှာ မေးစရာ ရှိတယ်။"},
    {"id": 11, "malay_word": "Mahu", "ipa_pronunciation": "/ma.hu/", "part_of_speech": "Verb", "english_meaning": "To want", "burmese_meaning": "ချင်တယ် / လိုချင်တယ်", "malay_example_sentence": "Saya mahu pulang.", "burmese_example_translation": "ကျွန်တော် ပြန်ချင်တယ်။"},
    {"id": 12, "malay_word": "Pergi", "ipa_pronunciation": "/pər.gi/", "part_of_speech": "Verb", "english_meaning": "To go", "burmese_meaning": "သွားတယ်", "malay_example_sentence": "Awak pergi mana?", "burmese_example_translation": "ခင်ဗျား ဘယ်သွားမလို့လဲ။"},
    {"id": 13, "malay_word": "Ini", "ipa_pronunciation": "/i.ni/", "part_of_speech": "Pronoun", "english_meaning": "This", "burmese_meaning": "ဒါ / ဒီ", "malay_example_sentence": "Ini rumah saya.", "burmese_example_translation": "ဒါ ကျွန်တော့်အိမ်ပါ။"},
    {"id": 14, "malay_word": "Itu", "ipa_pronunciation": "/i.tu/", "part_of_speech": "Pronoun", "english_meaning": "That", "burmese_meaning": "ဟို / အဲဒါ", "malay_example_sentence": "Itu sangat mahal.", "burmese_example_translation": "အဲဒါ သိပ်ဈေးကြီးတယ်။"},
{"id": 15, "malay_word": "Berapa", "ipa_pronunciation": "/bə.ra.pa/", "part_of_speech": "Adverb", "english_meaning": "How much", "burmese_meaning": "ဘယ်လောက်လဲ", "malay_example_sentence": "Berapa harga ini?", "burmese_example_translation": "ဒါ ဈေးဘယ်လောက်လဲ။"},
    {"id": 16, "malay_word": "Di", "ipa_pronunciation": "/di/", "part_of_speech": "Preposition", "english_meaning": "At / In", "burmese_meaning": "မှာ (နေရာပြ)", "malay_example_sentence": "Saya ada di rumah.", "burmese_example_translation": "ကျွန်တော် အိမ်မှာ ရှိတယ်။"},
    {"id": 17, "malay_word": "Tandas", "ipa_pronunciation": "/tan.das/", "part_of_speech": "Noun", "english_meaning": "Toilet", "burmese_meaning": "အိမ်သာ", "malay_example_sentence": "Di mana tandas?", "burmese_example_translation": "အိမ်သာ ဘယ်နားမှာလဲ။"},
    {"id": 18, "malay_word": "Air", "ipa_pronunciation": "/a.ir/", "part_of_speech": "Noun", "english_meaning": "Water", "burmese_meaning": "ရေ", "malay_example_sentence": "Tolong bagi air.", "burmese_example_translation": "ရေတစ်ခွက်လောက် ပေးပါ။"},
    {"id": 19, "malay_word": "Tolong", "ipa_pronunciation": "/to.loŋ/", "part_of_speech": "Verb", "english_meaning": "Help / Please", "burmese_meaning": "ကူညီပါ / ကျေးဇူးပြု၍", "malay_example_sentence": "Tolong saya.", "burmese_example_translation": "ကျွန်တော့်ကို ကူညီပါ။"},
    {"id": 20, "malay_word": "Selamat", "ipa_pronunciation": "/sə.la.mat/", "part_of_speech": "Greeting", "english_meaning": "Safe / Happy", "burmese_meaning": "မင်္ဂလာပါ (နှုတ်ဆက်စကား)", "malay_example_sentence": "Selamat pagi.", "burmese_example_translation": "မင်္ဂလာနံနက်ခင်းပါ။"}
]

# Load Data into DataFrame
df = pd.DataFrame(vocab_data)

# --- 3. Sidebar Design ---
with st.sidebar:
    st.title("🇲🇾 Malay Master")
    st.write("Your AI Language Coach")
    mode = st.radio("Choose Mode:", ["📚 Learning Hub", "🎮 Quiz Arena"])
    st.divider()
    st.info("Developed with Gemini AI")

# --- 4. Main Logic ---

if mode == "📚 Learning Hub":
    st.header("Learning Hub (လေ့လာရန်)")
    st.caption("Click on any card to see details.")
    
    # Display as cards
    for index, row in df.iterrows():
        with st.expander(f"{row['malay_word']} ({row['part_of_speech']})"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"🗣 IPA: {row['ipa_pronunciation']}")
                st.markdown(f"🇬🇧 English: {row['english_meaning']}")
                st.markdown(f"🇲🇲 Myanmar: {row['burmese_meaning']}")
            with c2:
                st.markdown("*Example:*")
                st.info(f"{row['malay_example_sentence']}\n\n{row['burmese_example_translation']}")

elif mode == "🎮 Quiz Arena":
    st.header("Quiz Arena (ဉာဏ်စမ်း)")
    
    # Initialize Session State
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = 0
    if 'current_quiz_data' not in st.session_state:
        st.session_state.current_quiz_data = None
    if 'quiz_answered' not in st.session_state:
        st.session_state.quiz_answered = False

    # Score Display
    col1, col2, col3 = st.columns(3)
    col1.metric("Score", f"{st.session_state.score} / {st.session_state.total_questions}")
    
    # Reset Button
    if col3.button("🔄 Reset Score"):
        st.session_state.score = 0
        st.session_state.total_questions = 0
        st.session_state.current_quiz_data = None
        st.session_state.quiz_answered = False
        st.rerun()

    st.divider()

    # Function to generate question
    def generate_question():
        target_row = df.sample(1).iloc[0]
        correct_answer = target_row['burmese_meaning']
        
        # Get 3 distractors
        distractors = df[df['id'] != target_row['id']].sample(3)['burmese_meaning'].tolist()
options = distractors + [correct_answer]
        random.shuffle(options)
        
        return {
            "word": target_row['malay_word'],
            "correct": correct_answer,
            "options": options,
            "ipa": target_row['ipa_pronunciation']
        }

    # Load Question
    if st.session_state.current_quiz_data is None:
        st.session_state.current_quiz_data = generate_question()
        st.session_state.quiz_answered = False

    quiz = st.session_state.current_quiz_data

    # Question UI
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <h2 style="color: #FF4B4B; font-size: 40px;">{quiz['word']}</h2>
        <p style="color: grey;">What is the Burmese meaning?</p>
    </div>
    """, unsafe_allow_html=True)

    # Display Options
    cols = st.columns(2)
    
    def check_answer(selected_option):
        if st.session_state.quiz_answered:
            return
            
        st.session_state.quiz_answered = True
        st.session_state.total_questions += 1
        
        if selected_option == quiz['correct']:
            st.session_state.score += 1
            st.toast(f"Correct! 🎉 '{quiz['word']}' means '{quiz['correct']}'", icon="✅")
        else:
            st.toast(f"Wrong! It means '{quiz['correct']}'", icon="❌")

    # Render Buttons
    for idx, option in enumerate(quiz['options']):
        col = cols[idx % 2]
        with col:
            def on_click_callback(opt=option):
                check_answer(opt)
            
            disabled = st.session_state.quiz_answered
            if st.button(option, key=f"opt_{idx}", on_click=on_click_callback, disabled=disabled, use_container_width=True):
                pass

    # Next Button
    if st.session_state.quiz_answered:
        if st.button("Next Question ➡️", type="primary", use_container_width=True):
            st.session_state.current_quiz_data = generate_question()
            st.session_state.quiz_answered = False
            st.rerun()                st.markdown(f"🇬🇧 English: {row['english_meaning']}")
                st.markdown(f"🇲🇲 Myanmar: {row['burmese_meaning']}")
            with c2:
                st.markdown("*Example:*")
                st.info(f"{row['malay_example_sentence']}\n\n{row['burmese_example_translation']}")

elif mode == "🎮 Quiz Arena":
    st.header("Quiz Arena (ဉာဏ်စမ်း)")
    
    # Initialize Session State
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = 0
    if 'current_quiz_data' not in st.session_state:
        st.session_state.current_quiz_data = None
    if 'quiz_answered' not in st.session_state:
        st.session_state.quiz_answered = False
# Score Display
    col1, col2, col3 = st.columns(3)
    col1.metric("Score", f"{st.session_state.score} / {st.session_state.total_questions}")
    
    # Reset Button
    if col3.button("🔄 Reset Score"):
        st.session_state.score = 0
        st.session_state.total_questions = 0
        st.session_state.current_quiz_data = None
        st.session_state.quiz_answered = False
        st.rerun()

    st.divider()

    # Function to generate question
    def generate_question():
        target_row = df.sample(1).iloc[0]
        correct_answer = target_row['burmese_meaning']
        
        # Get 3 distractors
        distractors = df[df['id'] != target_row['id']].sample(3)['burmese_meaning'].tolist()
        
        options = distractors + [correct_answer]
        random.shuffle(options)
        
        return {
            "word": target_row['malay_word'],
            "correct": correct_answer,
            "options": options,
            "ipa": target_row['ipa_pronunciation']
        }

    # Load Question
    if st.session_state.current_quiz_data is None:
        st.session_state.current_quiz_data = generate_question()
        st.session_state.quiz_answered = False

    quiz = st.session_state.current_quiz_data

    # Question UI
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <h2 style="color: #FF4B4B; font-size: 40px;">{quiz['word']}</h2>
        <p style="color: grey;">What is the Burmese meaning?</p>
    </div>
    """, unsafe_allow_html=True)

    # Display Options
    cols = st.columns(2)
    
    def check_answer(selected_option):
        if st.session_state.quiz_answered:
            return
            
        st.session_state.quiz_answered = True
        st.session_state.total_questions += 1
        
        if selected_option == quiz['correct']:
            st.session_state.score += 1
            st.toast(f"Correct! 🎉 '{quiz['word']}' means '{quiz['correct']}'", icon="✅")
        else:
            st.toast(f"Wrong! It means '{quiz['correct']}'", icon="❌")

    # Render Buttons
    for idx, option in enumerate(quiz['options']):
        col = cols[idx % 2]
        with col:
            # Button logic
            def on_click_callback(opt=option):
                check_answer(opt)
            
            # Disable if already answered
            disabled = st.session_state.quiz_answered
            
            # If answered, highlight correct/wrong (Visual Cue only works nicely with rerun, keeping simple for now)
            if st.button(option, key=f"opt_{idx}", on_click=on_click_callback, disabled=disabled, use_container_width=True):
                pass

    # Result Message & Next Button
    if st.session_state.quiz_answered:
        if st.button("Next Question ➡️", type="primary", use_container_width=True):
            st.session_state.current_quiz_data = generate_question()
            st.session_state.quiz_answered = False
            st.rerun()
