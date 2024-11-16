import streamlit as st
import json
from pathlib import Path

# Ruta al archivo JSON con los participantes
DATA_FILE = Path("/home/raxo/Documents/GitHub/Datathon-2024/data/datathon_participants.json")

# Función para cargar participantes
def load_participants():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Función para asignar equipos
def assign_teams(participants, teams):
    # Limpiar equipos previos
    for participant in participants:
        participant["team"] = None

    # Asignar nuevos equipos
    for team in teams:
        for participant_id in team:
            participant = next((p for p in participants if p["id"] == participant_id), None)
            if participant:
                # Añadir nombres de los compañeros al atributo "team"
                participant["team"] = [
                    p["name"] for p in participants if p["id"] in team and p["id"] != participant_id
                ]

# Cargar datos
participants = load_participants()

# Estilo personalizado
st.markdown(
    """
    <style>
    header { 
        background-color: transparent; 
        color: white; 
        text-align: center; 
        font-size: 30px; 
        font-weight: bold;
        padding: 10px 0;
    }
    .search-box input {
        border: 1px solid #800000;
        padding: 5px;
        border-radius: 5px;
        width: 100%;
    }
    .line-divider {
        border-top: 1px solid #800000;
        margin: 20px 0;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
    }
    .load-more-button, .show-less-button {
        background: none;
        border: 1px solid #800000;
        color: #800000;
        padding: 5px 15px;
        border-radius: 5px;
        font-size: 14px;
        margin-right: 5px;
    }
    .load-more-button:hover, .show-less-button:hover {
        background-color: #800000;
        color: white;
    }
    .participant-count {
        font-size: 12px;
        color: #555555;
        margin-bottom: 10px;
    }
    .create-teams-button {
        background-color: #800000;
        color: white;
        padding: 10px 30px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        margin-top: 30px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 100%;
    }
    .create-teams-button:hover {
        background-color: #660000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<header>Datathon FME Team Maker</header>", unsafe_allow_html=True)

# Inicializar estado
if "page" not in st.session_state:
    st.session_state["page"] = "home"
    st.session_state["show_more_count"] = 9  # Mostrar 3 líneas (9 participantes) por defecto
    st.session_state["last_update"] = None  # Evitar múltiples actualizaciones rápidas
    st.session_state["teams"] = []  # Equipos creados

# Manejo de eventos
def set_page(page_name, participant=None):
    st.session_state["page"] = page_name
    if participant:
        st.session_state["selected_participant"] = participant

# Asignar equipos si ya existen
if st.session_state["teams"]:
    assign_teams(participants, st.session_state["teams"])

# Búsqueda
if st.session_state["page"] == "home":
    # Mostrar el número total de participantes en el placeholder
    total_participants = len(participants)
    search_query = st.text_input(
        f"Search participant ({total_participants} in total)", 
        placeholder="Search participants...", 
        key="search_query"
    )
    
    # Mostrar solo la línea de separación si hay contenido
    if search_query or st.session_state["teams"]:
        st.markdown('<div class="line-divider"></div>', unsafe_allow_html=True)

    # Mostrar número de participantes encontrados solo si hay búsqueda
    if search_query:
        # Filtrar participantes
        filtered_participants = [
            p for p in participants if search_query.lower() in p["name"].lower()
        ]

        # Mostrar número de participantes encontrados
        st.markdown(f'<div class="participant-count">{len(filtered_participants)} participants found</div>', unsafe_allow_html=True)

        # Mostrar participantes solo si hay resultados
        if filtered_participants:
            # Grid de tarjetas
            columns = st.columns(3)
            for idx, participant in enumerate(filtered_participants):
                col = columns[idx % 3]
                with col:
                    if st.button(
                        f"{participant['name']} ({participant['year_of_study']})",
                        key=f"participant_{participant['id']}",
                        on_click=set_page,
                        args=("details", participant),
                    ):
                        pass  # El manejo ocurre con la función `set_page`

            # Botón para crear equipos
            st.markdown('<div class="line-divider"></div>', unsafe_allow_html=True)
            if st.button("Create Teams", key="create_teams", use_container_width=True):
                # Ejemplo: Crear equipos con IDs
                st.session_state["teams"] = [
                    ["1", "2", "3"],  # Ejemplo de equipos (IDs de participantes)
                    ["4", "5", "6"],
                ]
                assign_teams(participants, st.session_state["teams"])
                st.experimental_rerun()

    else:
        # Si no hay búsqueda, solo mostrar la línea de separación y el botón "Create Teams"
        st.markdown('<div class="line-divider"></div>', unsafe_allow_html=True)
        if st.button("Create Teams", key="create_teams", use_container_width=True):
            # Ejemplo: Crear equipos con IDs
            st.session_state["teams"] = [
                ["1", "2", "3"],  # Ejemplo de equipos (IDs de participantes)
                ["4", "5", "6"],
            ]
            assign_teams(participants, st.session_state["teams"])
            st.experimental_rerun()

# Página de detalles
elif st.session_state["page"] == "details":
    participant = st.session_state["selected_participant"]
    st.markdown(f"<header>{participant['name']}</header>", unsafe_allow_html=True)
    st.markdown('<div class="line-divider"></div>', unsafe_allow_html=True)

    # Mostrar detalles
    st.markdown(f"### {participant['name']}")
    st.markdown(f"**{participant['year_of_study']} student at {participant['university']}**")
    st.markdown(f"- **Age**: {participant['age']}")
    st.markdown(f"- **Programming Skills**: {', '.join([f'{k} (Level {v})' for k, v in participant['programming_skills'].items()])}")
    st.markdown(f"- **Objective**: {participant['objective']}")
    st.markdown(f"- **Preferred Role**: {participant['preferred_role']}")

    # Atributo del equipo
    if participant.get("team"):
        st.markdown(f"- **Team**: {', '.join(participant['team'])}")
    else:
        st.markdown("- **Team**: None")

    # Botón para volver
    if st.button("Back to Participants", key="back_to_participants", on_click=set_page, args=("home",)):
        pass
