import streamlit as st
from pathlib import Path
import json
from collect import collect_participants
from group import participant_to_group
from main import algorithm, main
import os

# Ruta al archivo JSON con los participantes
dirname = os.path.dirname(__file__)
DATA_FILE = os.path.join(dirname, '../data/datathon_participants.json')

# Cargar participantes
def load_participants(path: Path):
    try:
        participants = collect_participants(str(path))
        return participants
    except Exception as e:
        st.error(f"Error loading participants: {e}")
        return []

# Asignar equipos a los participantes y guardar el número de equipo, los miembros del equipo y la compatibilidad
def assign_teams(participants, teams, compatibility):
    team_info = {}  # Diccionario para almacenar el número de equipo, los miembros y la compatibilidad

    # Asignamos el equipo correcto a cada participante
    for team_idx, team in enumerate(teams):
        for participant_id in team.ids:
            participant = next((p for p in participants if p.id == participant_id), None)
            if participant:
                # Guardamos el número del equipo, los miembros y la compatibilidad
                team_info[participant.id] = {
                    "team_number": team_idx + 1,  # El número de equipo (empieza desde 1)
                    "team_members": [
                        next((p.name for p in participants if p.id == teammate_id), "Unknown")
                        for teammate_id in team.ids
                        if teammate_id != participant_id
                    ],
                    "compatibility": compatibility[team_idx]  # Asociar la compatibilidad con el equipo
                }

    return team_info  # Devolvemos la información de los equipos

# Inicializar estado
if "page" not in st.session_state:
    st.session_state["page"] = "home"
    st.session_state["teams"] = []
    st.session_state["selected_participant"] = None  # Para almacenar el participante seleccionado
    st.session_state["team_info"] = {}  # Almacenamos la información de los equipos
    st.session_state["compatibility"] = []  # Almacenamos la compatibilidad de los equipos

# Cargar los participantes desde el archivo JSON
participants = load_participants(DATA_FILE)

# Página principal
def main_page():
    # Header en negrita y tamaño aumentado
    st.markdown("<h1 style='font-size: 36px; font-weight: bold;'>Datathon FME Team Maker</h1>", unsafe_allow_html=True)
    st.markdown('<div class="line-divider"></div>', unsafe_allow_html=True)

    # Colocar las dos barras de búsqueda (de participantes y equipos) una al lado de la otra
    col1, col2 = st.columns([2, 1])

    # Barra de búsqueda de participantes
    with col1:
        search_query = st.text_input("Search Participant", "")

    # Barra de búsqueda de equipos
    with col2:
        team_search_query = st.text_input("Search Team Number", "")

    # Filtrar los participantes según la búsqueda
    filtered_participants = [
        p for p in participants if search_query.lower() in p.name.lower()
    ]
    
    # Mostrar el número de participantes en paréntesis, con un tamaño de fuente más pequeño
    st.markdown(f"<h5 style='font-size: 14px;'>Search Participants ({len(filtered_participants)})</h5>", unsafe_allow_html=True)

    # Si hay algo en la barra de búsqueda de participantes
    if search_query:
        if filtered_participants:
            st.markdown("### Participants")
            for participant in filtered_participants:
                if st.button(participant.name, key=participant.id):
                    st.session_state["selected_participant"] = participant
                    st.session_state["page"] = "details"
        else:
            st.markdown("No participants found.")

    # Filtrar y mostrar el equipo si se ingresa un número de equipo
    if team_search_query.isdigit():
        team_number = int(team_search_query)
        teams = st.session_state["teams"]
        team_found = False

        for idx, team in enumerate(teams):
            if idx + 1 == team_number:
                team_found = True
                team_members = [
                    next((p.name for p in participants if p.id == member_id), "Unknown")
                    for member_id in team.ids
                ]
                st.markdown(f"### Team {team_number}")
                st.markdown(f"**Team Members**: {', '.join(team_members)}")
                break

        if not team_found:
            st.markdown("Team not found.")

    # Línea horizontal para separar la búsqueda de la creación de equipos
    st.markdown('<hr>', unsafe_allow_html=True)

    # Botón para crear equipos
    if st.button("Create Teams"):
        with st.spinner('Creating Teams, this might take a while...'):
            try:
                # Convertir participantes a grupos
                g, c, mi, me = main()
                groups = [participant_to_group(participant) for participant in participants]
                # Ejecutar el algoritmo
                st.session_state["teams"] = g
                st.session_state["compatibility"] = c  # Guardamos la compatibilidad
                # Asignar equipos y obtener la información de los equipos
                st.session_state["team_info"] = assign_teams(participants, st.session_state["teams"], st.session_state["compatibility"])
                st.success(f"Teams created successfully! Average Compatibility: {int(mi*100)}%, Median: {int(me*100)}%")
            except Exception as e:
                st.error(f"Error creating teams: {e}")

    # Mostrar equipos si existen
    if st.session_state["teams"]:
        st.markdown('<div class="line-divider"></div>', unsafe_allow_html=True)
        st.markdown("### Teams")
        for idx, team in enumerate(st.session_state["teams"]):
            team_members = [
                next((p.name for p in participants if p.id == member_id), "Unknown")
                for member_id in team.ids
            ]
            team_compatibility = st.session_state["compatibility"][idx]
            st.write(f"**Team {idx + 1}:** {', '.join(team_members)} | **Compatibility**: {int(team_compatibility*100)}%")

# Página de detalles del participante
def details_page():
    participant = st.session_state.get("selected_participant")
    if not participant:
        st.error("No participant selected.")
        return

    # Mostrar detalles del participante
    st.markdown(f"### {participant.name}")
    st.markdown(f"**{participant.year_of_study} student at {participant.university}**")
    st.markdown(f"- **Age**: {participant.age}")
    st.markdown(f"- **Programming Skills**: {', '.join([f'{k} (Level {v})' for k, v in participant.programming_skills.items()])}")
    st.markdown(f"- **Objective**: {participant.objective}")
    st.markdown(f"- **Preferred Role**: {participant.preferred_role}")

    # Obtener la información del equipo desde el diccionario de 'team_info'
    team_data = st.session_state["team_info"].get(participant.id)
    if team_data:
        st.markdown(f"- **Team Members**: {', '.join(team_data['team_members'])}")
        st.markdown(f"- **Team Number**: {team_data['team_number']}")  # Mostrar el número del equipo
        st.markdown(f"- **Team Compatibility**: {int(team_data['compatibility']*100)}%")  # Mostrar la compatibilidad del equipo
    else:
        st.markdown("- **Team**: None")

    # Botón para volver
    if st.button("Back to Participants"):
        st.session_state["page"] = "home"

# Navegación entre páginas
if st.session_state["page"] == "home":
    main_page()
elif st.session_state["page"] == "details":
    details_page()
