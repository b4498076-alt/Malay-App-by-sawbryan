import streamlit as st
import pandas as pd
import random

# Page Config
st.set_page_config(page_title="Malay Master AI", page_icon="🇲🇾", layout="wide")

# --- DATA LIST ---
vocab_data = [
    {"id": 1, "malay_word": "Saya", "ipa": "/sa.ja/", "pos": "Pronoun", "en": "I / Me", "my": "ကျွန်တော် / ကျွန်မ", "ex": "Nama saya Ali.", "tr": "ကျွန်တော့်နာမည် အလီပါ။"},
    {"id": 2, "malay_word": "Awak", "ipa": "/a.waʔ/", "pos": "Pronoun", "en": "You", "my": "ခင်ဗျား / ရှင်", "ex": "Awak apa khabar?", "tr": "ခင်ဗျား နေကောင်းလား။"},
    {"id": 3, "malay_word": "Makan", "ipa": "/ma.kan/", "pos": "Verb", "en": "To eat", "my": "စားတယ်", "ex": "Saya mahu makan nasi.", "tr": "ကျွန်တော် ထမင်း စားချင်တယ်။"},
    {"id": 4, "malay_word": "Minum", "ipa": "/mi.num/", "pos": "Verb", "en": "To drink", "my": "သောက်တယ်", "ex": "Jom minum air.", "tr": "ရေ သွားသောက်ရအောင်။"},
    {"id": 5, "malay_word": "Ya", "ipa": "/ja/", "pos": "Particle", "en": "Yes", "my": "ဟုတ်ကဲ့", "ex": "Ya, saya faham.", "tr": "ဟုတ်ကဲ့၊ ကျွန်တော် နားလည်တယ်။"},
    {"id": 6, "malay_word": "Tidak", "ipa": "/ti.daʔ/", "pos": "Adverb", "en": "No", "my": "မဟုတ်ဘူး", "ex": "Saya tidak tahu.", "tr": "ကျွန်တော် မသိဘူး။"},
    {"id": 7, "malay_word": "Terima kasih", "ipa": "/tə.ri.ma/", "pos": "Phrase", "en": "Thank you", "my": "ကျေးဇူးတင်ပါတယ်", "ex": "Terima kasih banyak.", "tr": "အများကြီး ကျေးဇူးတင်ပါတယ်။"},
    {"id": 8, "malay_word": "Apa", "ipa": "/a.pa/", "pos": "Pronoun", "en": "What", "my": "ဘာလဲ", "ex": "Ini apa?", "tr": "ဒါ ဘာလဲ။"},
    {"id": 9, "malay_word": "Siapa", "ipa": "/si.a.pa/", "pos": "Pronoun", "en": "Who", "my": "ဘယ်သူလဲ", "ex": "Siapa nama awak?", "tr": "ခင်ဗျားနာမည် ဘယ်သူလဲ။"},
    {"id": 10, "malay_word": "Ada", "ipa": "/a.da/", "pos": "Verb", "en": "Have", "my": "ရှိတယ်", "ex": "Saya ada soalan.", "tr": "ကျွန်တော့်မှာ မေးစရာ ရှိတယ်။"},
    {"id": 11, "malay_word": "Mahu", "ipa": "/ma.hu/", "pos": "Verb", "en": "Want", "my": "ချင်တယ်", "ex": "Saya mahu pulang.", "tr": "ကျွန်တော် ပြန်ချင်တယ်။"},
    {"id": 12, "malay_word": "Pergi", "ipa": "/pər.gi/", "pos": "Verb", "en": "Go", "my": "သွားတယ်", "ex": "Awak pergi mana?", "tr": "ခင်ဗျား ဘယ်သွားမလို့လဲ။"},
    {"id": 13, "malay_word": "Ini", "ipa": "/i.ni/", "pos": "Pronoun", "en": "This", "my": "ဒါ / ဒီ", "ex": "Ini rumah saya.", "tr": "ဒါ ကျွန်တော့်အိမ်ပါ။"},
    {"id": 14, "malay_word": "Itu", "ipa": "/i.tu/", "pos": "Pronoun", "en": "That", "my": "ဟို / အဲဒါ", "ex": "Itu sangat mahal.", "tr": "အဲဒါ သိပ်ဈေးကြီးတယ်။"},
    {"id": 15, "malay_word": "Berapa", "ipa": "/bə.ra.pa/", "pos": "Adverb", "en": "How much", "my": "ဘယ်လောက်လဲ", "ex": "Berapa harga ini?", "tr": "ဒါ ဈေးဘယ်လောက်လဲ။"},
    {"id": 16, "malay_word": "Di", "ipa": "/di/", "pos": "Prep", "en": "At", "my": "မှာ (နေရာပြ)", "ex": "Saya ada di rumah.", "tr": "ကျွန်တော် အိမ်မှာ ရှိတယ်။"},
    {"id": 17, "malay_word": "Tandas", "ipa": "/tan.das/", "pos": "Noun", "en": "Toilet", "my": "အိမ်သာ", "ex": "Di mana tandas?", "tr": "အိမ်သာ ဘယ်နားမှာလဲ။"},
    {"id": 18, "malay_word": "Air", "ipa": "/a.ir/", "pos": "Noun", "en": "Water", "my": "ရေ", "ex": "Tolong bagi air.", "tr": "ရေတစ်ခွက်လောက် ပေးပါ။"},
    {"id": 19, "malay_word": "Tolong", "ipa": "/to.loŋ/", "pos": "Verb", "en": "Help", "my": "ကူညီပါ", "ex": "Tolong saya.", "tr": "ကျွန်တော့်ကို ကူညီပါ။"},
    {"id": 20, "malay_word": "Selamat", "ipa": "/sə.la.mat/", "pos": "Greeting", "en": "Safe", "my": "မင်္ဂလာပါ", "ex": "Selamat pagi.", "tr": "မင်္ဂလာနံနက်ခင်းပါ။"}
]

df = pd.DataFrame(vocab_data)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🇲🇾 Malay Master")
    st.write("Your AI Language Coach")
    mode = st.radio("Select Mode:", ["Learning Hub", "Quiz Arena"])
    st.divider()
    st.info("Developed with Gemini AI")

# --- MAIN APP ---
if mode == "Learning Hub":
    st.header("📚 Learning Hub (လေ့လာရန်)")
    st.caption("Click cards to see details")
    
    for index, row in df.iterrows():
        with st.expander(f"**{row['malay_word']}** ({row['pos']})"):
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"🗣 `{row['ipa']}`")
                st.write(f"🇬🇧 {row['en']}")
                st.subheader(f"🇲🇲 {row['my']}")
            with c2:
                st.info(f"**{row['ex']}**\n\n{row['tr']}")

elif mode == "Quiz Arena":
    st.header("🎮 Quiz Arena (ဉာဏ်စမ်း)")
    
    # Init State
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_data' not in st.session_state: st.session_state.q_data = None
    if 'answered' not in st.session_state: st.session_state.answered = False

    # Score Board
    c1, c2 = st.columns([3, 1])
    c1.metric("Current Score", st.session_state.score)
    
    if c2.button("Reset"):
        st.session_state.score = 0
        st.session_state.q_data = None
        st.session_state.answered = False
        st.rerun()

    st.divider()

    # Question Logic
    def new_question():
        row = df.sample(1).iloc[0]
        correct = row['my']
        distractors = df[df['id'] != row['id']].sample(3)['my'].tolist()
        options = distractors + [correct]
        random.shuffle(options)
        return {"word": row['malay_word'], "correct": correct, "opts": options}

    if st.session_state.q_data is None:
        st.session_state.q_data = new_question()
        st.session_state.answered = False

    q = st.session_state.q_data

    # Display Question
    st.markdown(f"<h1 style='text-align: center; color: #E63946;'>{q['word']}</h1>", unsafe_allow_html=True)
    st.write("Meaning in Burmese?")

    # Display Options
    cols = st.columns(2)
    
    def check(ans):
        if not st.session_state.answered:
            st.session_state.answered = True
            if ans == q['correct']:
                st.session_state.score += 1
                st.toast("Correct! 🎉", icon="✅")
            else:
                st.toast(f"Wrong! It is {q['correct']}", icon="❌")

    for i, opt in enumerate(q['opts']):
        cols[i%2].button(opt, key=f"btn_{i}", on_click=check, args=(opt,), disabled=st.session_state.answered, use_container_width=True)

    # Next Button
    if st.session_state.answered:
        if st.button("Next Question ➡️", type="primary", use_container_width=True):
            st.session_state.q_data = new_question()
            st.session_state.answered = False
            st.rerun()
