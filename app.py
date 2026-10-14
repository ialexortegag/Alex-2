import streamlit as st

st.set_page_config(
    page_title="Match de Mesa",
    page_icon="🎲",
    layout="centered",
    initial_sidebar_state="collapsed",
)

GAMES = [
    ("Sky Team", "Cooperación", "Aterrizad un avión coordinándoos y tomando decisiones juntos.", "✈️"),
    ("Disney Villainous", "Estrategia", "Convertíos en villanos Disney y perseguid vuestro propio objetivo.", "🦹"),
    ("Among Us", "Deducción", "Engaños, sospechas y pequeñas traiciones en la mesa.", "🚀"),
    ("Forest Shuffle", "Naturaleza", "Construid un bosque lleno de árboles y biodiversidad.", "🌳"),
    ("Goat Cheese Pizza", "Cartas · rápido", "Un juego de cartas ágil para entrar en modo competición.", "🐐"),
    ("The Mind", "Cooperación · silencio", "Jugad cartas en orden sin hablar ni hacer señales.", "🧠"),
    ("Azul", "Abstracto · estrategia", "Elegid azulejos y componed el mosaico más bonito.", "🔷"),
    ("Faraway", "Cartas · exploración", "Explorad una región misteriosa y optimizad vuestra puntuación.", "🧭"),
    ("Mysterium", "Cooperación · misterio", "Interpretad visiones para resolver un misterio.", "🔮"),
    ("Hawaii", "Estrategia", "Gestionad recursos y explorad islas en un juego de estrategia.", "🌺"),
    ("UNO", "Cartas · familiar", "El clásico de colores, cambios de sentido y +4 inesperados.", "🟥"),
    ("Dobble", "Observación · rápido", "Encontrad el símbolo común antes que la otra persona.", "👀"),
    ("Throw Throw Burrito", "Acción · caótico", "Combina cartas con divertidos duelos de burritos blandos.", "🌯"),
    ("Cluedo", "Deducción", "Averiguad quién cometió el crimen, dónde y con qué arma.", "🕵️"),
    ("Twister", "Fiesta", "Flexibilidad, equilibrio y posiciones cada vez más absurdas.", "🌀"),
    ("Hanabi", "Cooperación", "Preparad fuegos artificiales viendo las cartas de los demás.", "🎆"),
    ("Agent Avenue", "Faroleo · estrategia", "Un duelo de espías con decisiones y faroleo.", "🕶️"),
    ("El Impostor", "Deducción social", "Descubrid quién no tiene toda la información.", "🎭"),
    ("Eres así", "Conversación", "Descubrid cuánto os conocéis y cómo os veis mutuamente.", "💬"),
    ("Towers", "Estrategia", "Construid y optimizad vuestra posición torre a torre.", "🏰"),
    ("Don't Get Got!", "Misión secreta", "Intentad completar misiones secretas durante el día.", "🤫"),
    ("Sea Salt & Paper", "Cartas · táctico", "Coleccionad criaturas marinas y decidid cuándo cerrar la ronda.", "🐚"),
    ("Saboteur", "Roles ocultos", "Cavad túneles hacia el oro mientras alguien puede sabotearos.", "⛏️"),
    ("Trio", "Memoria · cartas", "Encontrad tríos usando memoria y deducción.", "3️⃣"),
    ("Times Up!", "Fiesta · palabras", "Adivinad personajes en rondas cada vez más frenéticas.", "⏱️"),
    ("Scout", "Cartas · táctico", "Gestionad vuestra mano y superad las jugadas rivales.", "🎪"),
    ("Isla Prohibida", "Cooperación · aventura", "Trabajad juntos para recuperar tesoros y escapar a tiempo.", "🏝️"),
    ("7 Wonders Duel", "Duelo · estrategia", "Desarrollad una civilización en un enfrentamiento para dos.", "🏛️"),
    ("Unstable Unicorns", "Cartas · sabotaje", "Reunid unicornios en vuestro establo y fastidiad al rival.", "🦄"),
]

if "votes" not in st.session_state:
    st.session_state.votes = {"Tú": {}, "Tu pareja": {}}
if "pos" not in st.session_state:
    st.session_state.pos = 0
if "player" not in st.session_state:
    st.session_state.player = "Tú"
if "finished" not in st.session_state:
    st.session_state.finished = False
if "custom_games" not in st.session_state:
    st.session_state.custom_games = []

all_games = GAMES + [
    (g, "Añadido por vosotros", "Juego añadido a vuestra lista.", "🎲")
    for g in st.session_state.custom_games
]

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover">
<style>
:root { color-scheme: light dark; }
.block-container {
  width: 100% !important;
  max-width: 700px !important;
  padding: max(1rem, env(safe-area-inset-top)) 1rem max(2rem, env(safe-area-inset-bottom)) !important;
}
header[data-testid="stHeader"] { background: transparent; }
[data-testid="stAppViewContainer"] { overflow-x: hidden; }
.hero { text-align:center; padding: .25rem 0 .8rem; }
.hero h1 { font-size: clamp(1.9rem, 8vw, 2.7rem); letter-spacing:-1.3px; margin: .1rem 0; }
.sub { color: var(--text-color); opacity:.72; font-size:1rem; }
.gamecard {
  border:1px solid rgba(128,128,128,.28);
  border-radius:24px;
  padding:clamp(20px, 6vw, 32px) 18px;
  text-align:center;
  margin:12px 0 18px;
  background:linear-gradient(145deg, rgba(150,120,255,.13), rgba(255,130,170,.13));
  overflow-wrap:anywhere;
}
.emoji { font-size:clamp(3.7rem, 18vw, 5.2rem); line-height:1.25; }
.tag { font-size:.8rem; border-radius:999px; padding:6px 11px; background:rgba(128,128,128,.16); display:inline-block; margin:8px; }
.gamecard h2 { margin:.4rem 0; font-size:clamp(1.45rem, 6vw, 2rem); line-height:1.15; }
.gamecard p { font-size:1rem; line-height:1.5; }
div.stButton > button {
  border-radius:16px;
  min-height:54px;
  width:100%;
  font-size:1rem;
  font-weight:650;
  touch-action: manipulation;
  white-space:normal;
}
button, a, input { touch-action: manipulation; }
[data-testid="stMetric"] { padding: .7rem; border-radius:16px; background:rgba(128,128,128,.08); }
[data-testid="stProgress"] { margin-bottom:1.2rem; }
[data-testid="stExpander"] { border-radius:14px; }
@media (max-width: 520px) {
  .block-container { padding-left: .85rem !important; padding-right: .85rem !important; }
  .gamecard { border-radius:20px; }
  div[data-testid="stHorizontalBlock"] { gap:.55rem; }
  div.stButton > button { min-height:56px; padding:.65rem .4rem; }
  [data-testid="stMetricValue"] { font-size:1.4rem; }
  h3 { font-size:1.15rem !important; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { scroll-behavior:auto !important; animation:none !important; transition:none !important; }
}
</style>
<div class="hero">
  <div style="font-size:2.1rem">💘 🎲 💘</div>
  <h1>Match de Mesa</h1>
  <div class="sub">Dos gustos. Una próxima partida.</div>
</div>
""", unsafe_allow_html=True)

with st.expander("¿Cómo se juega?"):
    st.write("1. Elegid quién vota primero. 2. Cada persona marca si jugaría a cada juego. 3. Al final, descubrid los que os gustan a los dos.")
    st.caption("Diseñado para usarlo desde Safari en iPhone o Chrome en Android. Podéis pasaros el mismo móvil para votar.")

c1, c2 = st.columns(2)
with c1:
    st.metric("Juegos", len(all_games))
with c2:
    matches_count = sum(
        1 for i in range(len(all_games))
        if st.session_state.votes["Tú"].get(i) is True
        and st.session_state.votes["Tu pareja"].get(i) is True
    )
    st.metric("Matches", matches_count)

if st.session_state.finished:
    st.success("¡Ronda terminada! Estos son vuestros matches.")
    matches = [
        i for i in range(len(all_games))
        if st.session_state.votes["Tú"].get(i) is True
        and st.session_state.votes["Tu pareja"].get(i) is True
    ]
    if matches:
        st.balloons()
        for i in matches:
            name, tag, desc, emoji = all_games[i]
            st.markdown(
                f'<div class="gamecard"><div class="emoji">{emoji}</div>'
                f'<h2>{name}</h2><span class="tag">{tag}</span><p>{desc}</p>'
                '<strong>❤️ ¡Os apetece a los dos!</strong></div>',
                unsafe_allow_html=True
            )
    else:
        st.info("Esta vez no ha habido match. ¡Añadid juegos o probad otra ronda!")
    if st.button("🔄 Volver a empezar", use_container_width=True):
        st.session_state.votes = {"Tú": {}, "Tu pareja": {}}
        st.session_state.pos = 0
        st.session_state.player = "Tú"
        st.session_state.finished = False
        st.rerun()
    st.stop()

player = st.session_state.player
# Move past games this player has already rated.
while st.session_state.pos < len(all_games) and st.session_state.pos in st.session_state.votes[player]:
    st.session_state.pos += 1

if st.session_state.pos >= len(all_games):
    other = "Tu pareja" if player == "Tú" else "Tú"
    if len(st.session_state.votes[other]) < len(all_games):
        st.session_state.player = other
        st.session_state.pos = 0
        st.rerun()
    st.session_state.finished = True
    st.rerun()

idx = st.session_state.pos
name, tag, desc, emoji = all_games[idx]
st.markdown(f"### Turno de: **{player}**")
st.progress(min(idx + 1, len(all_games)) / max(len(all_games), 1), text=f"Juego {idx + 1} de {len(all_games)}")
st.markdown(
    f'<div class="gamecard"><div class="emoji">{emoji}</div>'
    f'<span class="tag">{tag}</span><h2>{name}</h2><p>{desc}</p></div>',
    unsafe_allow_html=True
)
st.write("¿Te apetece jugar a este?")
yes, no = st.columns(2)
def vote(value):
    current = st.session_state.player
    st.session_state.votes[current][idx] = value
    if len(st.session_state.votes[current]) >= len(all_games):
        other = "Tu pareja" if current == "Tú" else "Tú"
        if len(st.session_state.votes[other]) < len(all_games):
            st.session_state.player = other
            st.session_state.pos = 0
        else:
            st.session_state.finished = True
    else:
        st.session_state.pos = idx + 1

with yes:
    if st.button("❤️ Me apetece", type="primary", use_container_width=True):
        vote(True)
        st.rerun()
with no:
    if st.button("👋 Paso", use_container_width=True):
        vote(False)
        st.rerun()

st.divider()
with st.expander("➕ ¿Falta algún juego? Añádelo"):
    new_game = st.text_input("Nombre del juego", placeholder="Ej. Catan")
    if st.button("Añadir juego"):
        cleaned = new_game.strip()
        if cleaned and cleaned.lower() not in [g[0].lower() for g in all_games]:
            st.session_state.custom_games.append(cleaned)
            st.success(f"'{cleaned}' añadido a la lista.")
            st.rerun()
        elif cleaned:
            st.warning("Ese juego ya está en la lista.")

st.caption("Esta versión funciona en el navegador del móvil; no requiere descargar una app. Los votos se mantienen durante la sesión.")
