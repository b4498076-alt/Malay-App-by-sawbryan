import streamlit as st
import pandas as pd
import io
import random

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Malay Master AI",
    page_icon="🇲🇾",
    layout="wide"
)

# --- 2. The Data (Embedded) ---
# This is the CSV data we generated earlier
csv_data = """id,malay_word,ipa_pronunciation,part_of_speech,english_meaning,burmese_meaning,malay_example_sentence,burmese_example_translation,difficulty_level
1,Saya,/sa.ja/,Pronoun,I / Me,ကျွန်တော် (male) / ကျွန်မ (female),Nama saya Ali.,ကျွန်တော့်နာမည် အလီပါ။,Beginner
2,Awak,/a.waʔ/,Pronoun,You,ခင်ဗျား (to male) / ရှင် (to female),Awak apa khabar?,ခင်ဗျား နေကောင်းလား။,Beginner
3,Makan,/ma.kan/,Verb,To eat,စားတယ်,Saya mahu makan nasi.,ကျွန်တော် ထမင်း စားချင်တယ်။,Beginner
4,Minum,/mi.num/,Verb,To drink,သောက်တယ်,Jom minum air.,ရေ သွားသောက်ရအောင်။,Beginner
5,Ya,/ja/,Particle,Yes,ဟုတ်ကဲ့,Ya, saya faham.,ဟုတ်ကဲ့၊ ကျွန်တော် နားလည်တယ်။,Beginner
6,Tidak,/ti.daʔ/,Adverb,No / Not,မဟုတ်ဘူး / မ...ဘူး,Saya tidak tahu.,ကျွန်တော် မသိဘူး။,Beginner
7,Terima kasih,/tə.ri.ma ka.seh/,Phrase,Thank you,ကျေးဇူးတင်ပါတယ်,Terima kasih banyak.,အများကြီး ကျေးဇူးတင်ပါတယ်။,Beginner
8,Apa,/a.pa/,Pronoun,What,ဘာလဲ,Ini apa?,ဒါ ဘာလဲ။,Beginner
9,Siapa,/si.a.pa/,Pronoun,Who,ဘယ်သူလဲ,Siapa nama awak?,ခင်ဗျားနာမည် ဘယ်သူလဲ။,Beginner
10,Ada,/a.da/,Verb,To have / To exist,ရှိတယ်,Saya ada soalan.,ကျွန်တော့်မှာ မေးစရာ ရှိတယ်။,Beginner
11,Mahu,/ma.hu/,Verb,To want,ချင်တယ် / လိုချင်တယ်,Saya mahu pulang.,ကျွန်တော် ပြန်ချင်တယ်။,Beginner
12,Pergi,/pər.gi/,Verb,To go,သွားတယ်,Awak pergi mana?,ခင်ဗျား ဘယ်သွားမလို့လဲ။,Beginner
13,Ini,/i.ni/,Pronoun,This,ဒါ / ဒီ,Ini rumah saya.,ဒါ ကျွန်တော့်အိမ်ပါ။,Beginner
14,Itu,/i.tu/,Pronoun,That,ဟို / အဲဒါ,Itu sangat mahal.,အဲဒါ သိပ်ဈေးကြီးတယ်။,Beginner
15,Berapa,/bə.ra.pa/,Adverb,How much / How many,ဘယ်လောက်လဲ,Berapa harga ini?,ဒါ ဈေးဘယ်လောက်လဲ။,Beginner
16,Di,/di/,Preposition,At / In,မှာ (နေရာပြ),Saya ada di rumah.,ကျွန်တော် အိမ်မှာ ရှိတယ်။,Beginner
17,Tandas,/tan.das/,Noun,Toilet / Restroom,အိမ်သာ,Di mana tandas?,အိမ်သာ ဘယ်နားမှာလဲ။,Beginner
18,Air,/a.ir/,Noun,Water,ရေ,Tolong bagi air.,ရေတစ်ခွက်လောက် ပေးပါ။,Beginner
19,Tolong,/to.loŋ/,Verb,Help / Please,ကူညီပါ / ကျေးဇူးပြု၍,Tolong saya.,ကျွန်တော့်ကို ကူညီပါ။,Beginner
20,Selamat,/sə.la.mat/,Adjective,Safe (used in greetings),မင်္ဂလာပါ (နှုတ်ဆက်စကား),Selamat pagi.,မင်္ဂလာနံနက်ခင်းပါ။"""

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv(io.StringIO(csv_data))

df = load_data()

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
