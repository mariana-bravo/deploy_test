import streamlit as st
import time
import random

# Configurações da página

st.set_page_config(
    page_title="Eimerchen Protocol",
    page_icon="🎄",
    layout="centered"
)

# Funções dos módulos

def cutify_words():
    st.header("🙈 Cutify Stuff (Tradutor Fofo)")
    st.write ("Type a word in English:")

    word = st.text_input("Word:", key="cutify_input")

    # Dicionário de traduções
    dictionary = {
        "celle": "bucket", "marcel": "baby", "mari": "teapot",
        "mariana": "marizinha", "love": "amorzinho", "bucket": "eimerchen",
        "teapot": "teekännchen", "potato": "batatinha", "factory": "fabriquinha",
        "code": "codigozinho", "rock": "rockzinho", "cute": "fofinho(a)",
        "cutie": "fofinho(a)", "wife": "esposinha", "wifey": "esposinha",
        "husband": "maridinho", "hubby": "maridinho", "beauty": "gatinho(a)",
        "gorgeous": "gatinha","handsome": "gatinho", "pretty": "gatinho(a)", "shawty": "gatinho(a)",
        "german": "alemãozinho(a)", "brazilian": "brasileirinho(a)", "carioca": "carioquinha",
        "beer": "cervejinha", "wine": "vinhozinho", "whiskey":"whiskizinho",
        "game": "joguinho", "friends": "amiguinhos", "friend": "amiguinho(a)",
        "food": "comidinha", "water": "aguinha", "baby": "marcel",
        "darling": "querido(a)", "sweetie": "docinho", "love you": "te amo",
        "carrot": "cenourinha", "carrots": "cenourinhas", "home": "casinha", "house": "casinha",
        "kiss": "beijinho", "kisses": "beijinhos", "car": "carrinho", "cuddle": "conchinha",
        "affection": "carinho", "flower": "florzinha"
    }

    if st.button("Translate"):
        if word:
            w_lower = word.lower().strip()

            if w_lower in dictionary:
                translation = dictionary[w_lower]
                st.success(f"In Brazil: **{translation.upper()}**!")
            
            else:
                st.info(f"Humm... must be **{word.capitalize()}inho/a**!")
                st.caption("(Brazil's Universal Rule: just add 'inho' or 'inha' to make it cuter :D)")

def warhammer_wisdom():
    st.header("🗿 The Emperor's Decree")
    st.write("Doubts burden the mind (unless you are a bucket). Consult the Imperial Truth.")

    lines = [
        "Only in death does duty end. (But you can have a pizza today!)",
        "The Emperor protects... but Teapot loves you.",
        "A moment of laxity spawns a lifetime of heresy. Don't forget to drink enough water.",
        "Knowledge is power, guard it well. But Mari's heart is unguarded for you, fofinho.",
        "Knowledge is power. But learning german is pure torture... pain is cleansing!",
        "In the grim darkness of the far future, there is only war... and chess matches with Mari!",
        "An open mind is like a fortress with its gates unbarred and unguarded.",
        "Hope is the first step on the road to disappointment! :D",
        "Innocence proves nothing. But your Grübchen proves everything.",
        "Strategic relocation authorized: From Sector Brazil to Sector Germany. Prepare for deployment!",
        "Even Space Marines need maintenance. Requesting immediate carinho.",
        "Purge the herectic! Burn the unclean! Spoil Mari!",
        "Rations are scarce, but chocolate is essential for morale. Eat some today.",
        "Mari is not late... she was delayed by Warp Storms. (And she misses you.)",
        "Black as the void or white as bone... it matters not. But sugar is Heresy! Stay bitter, fofinho."
        "Warning: Teapotting levels reaching critical mass! Bucket for containment and love needed.",
        "Archived audio-log recovered from Holy Terra. Decrypting... 'It's Britney, Bitch' Protocol: Slay.",
        "Your emotional shields are at 100%, stoic Bucket. Lower them just for Teapot. Initiating kiss sequence."
    ]

    if st.button("Commune with the Machine Spirit"):
        with st.spinner("Reciting binary litanies to the Cogitator..."):
            time.sleep(1.5)
            wisdom = random.choice(lines)
            st.markdown(f"*{wisdom}*")
            st.success("The Emperor approves this message.")

def christmas_card():
    st.header("🎁 From Teapot to Bucket")
    st.snow()
    st.write(f""" ### Frohe Weihnachten, Bucket! 🎄
             
             I wrote this code in a hurry cause my PC broke (true story),

             but I wanted to make it clear that:

             1. Du bist mein Lieblingsmensch.

             2. I can't wait to see you.

             3. The distance is just a bug in the system, we'll fix it soon.

             Te amo!
             Ich liebe dich!
             Love you!
             ❤

             I wish God bless you always, sweetie. 
             In the Name of Jesus Christ.
             """) 

# Login

def check_password():
    st.title("Restricted Access: Christmas Protocol")

    password = st.text_input("Insert password:", type="password")

    if st.button("Access"):
        if password == st.secrets["BUCKETS_PROPERTY"]:
            st.success("Authorized Access! Welcome, Operator.")
            time.sleep(1)
            return True
        elif password == "":
            st.warning("Enter password.")
        else:
            st.error("ACCESS DENIED. You are not Bucket, get away!")
    return False

# Main

def main():

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        if check_password():
            st.session_state["authenticated"] = True
            st.rerun()
    
    # User logged
    else: 
        st.title("Eimerchen OS v1.0")

        menu = st.selectbox(
            "Select module:",
            ["🏠 Home", "🙈 Cutify Stuff (Tradutor Fofo)", "🗿 The Emperor's Decree"]
        )

        if menu == "🏠 Home":
            christmas_card()

        elif menu == "🙈 Cutify Stuff (Tradutor Fofo)":
            cutify_words()

        elif menu == "🗿 The Emperor's Decree":
            warhammer_wisdom()

if __name__ == "__main__":
    main()