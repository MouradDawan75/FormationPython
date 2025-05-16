import streamlit as st # pip install streamlit
from pymongo import MongoClient # pip install pymongo
from datetime import datetime # module de base de python
import calendar # module de base de python



from streamlit_option_menu import option_menu # pip install streamlit-option-menu

# Connexion à la base mongo

# Uses st.cache_resource to only run once.
@st.cache_resource
def connexion():
    client = MongoClient('localhost',27017)
    return client

client = connexion()

# Choisir une base de données

db = client.streamlitdb # si base inexistante elle est créée

# Choisir une collection

periode_collection = db.periode # si collection inexistante -> elle est créée 

# ------------------ settings --------------
revenus = ['Salaire','Blog','Autre revenus']
depenses = ['Loyer','Alimentaires','Voiture','Autres dépenses']
currency = 'EURO'

# ---------- Dropdown list pour choisir une période: mois_année

years = [datetime.now().year, datetime.now().year + 1]
months = list(calendar.month_name[1:]) # la première ligne (index 0) contient le nom des colonnes

# ------------- Fonctions pour mongodb ----------

def insert_periode(periode,revenus,depenses,comment):
    document = {
        'key': periode,
        'revenus':revenus,
        'depenses': depenses,
        'comment': comment
    }
    return periode_collection.insert_one(document).inserted_id

# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600) # ttl: time to load
def get_all_periods():
    docs = periode_collection.find({}, {'_id':0})
    periods = []

    for d in docs:
        periods.append(d['key'])

    # comprehension list
    # result = [d['key'] for d in docs]

    return periods

@st.cache_data(ttl=600)
def get_period(periode):
    item = periode_collection.find_one({'key': periode})
    return item

# Bonne pratique: utiliser le cache pour les fonctions de lecture depuis MongoDB

#-------- Menu de navigation (option menu)

selected = option_menu(
    menu_title=None,
    options=['Mongo Databases', 'Data Entry', 'Data Visualization'],
    icons=['database-fill','pencil-fill','bar-chart-fill'], # https://icons.getbootstrap.com -> icones de botstrap
    orientation='horizontal'
    )

if selected == 'Mongo Databases':
    selected_db = st.selectbox('Select DB', client.list_database_names())
    clic = st.button('Show details', type='primary')

    if clic:
        collections = client[selected_db].list_collection_names()
        st.write('Selected DB', selected_db)
        st.write('Collections:')
        st.table(collections)

        for c in collections:
            st.write('Collection:', c, ' Nombre de documents: ', client[selected_db][c].count_documents({}))


if selected == 'Data Entry':
    st.header(f'Data Entry in {currency}')

    with st.form('entry_form', clear_on_submit=True):

        #'--- periode -----'
        col1,col2 = st.columns(2)
        col1.selectbox('Select month', months, key='month') # streamlit le stocke en session
        col1.selectbox('Select year', years, key='year') # streamlit le stocke en session

        #'--- revenus -----'
        with st.expander("Revenus"):
            for revenu in revenus:
                st.number_input(f'{revenu}:', min_value=0,step=10,key=revenu)

        #'--- depenses -----'
        with st.expander("Dépenses"):
            for depense in depenses:
                st.number_input(f'{depense}:', min_value=0,step=10,key=depense)

        # --- comment
        with st.expander('Comment'):
            comment = st.text_area("", placeholder='Votre commentaire.....')

        submitted = st.form_submit_button('Save data')

        if submitted:
            period = str(st.session_state['year'])+'_'+str(st.session_state['month']) # 2012_janvier
            revenu = {revenu: st.session_state[revenu] for revenu in revenus}
            depense = {depense: st.session_state[depense] for depense in depenses}
            insert_periode(period,revenu,depense,comment)
            st.success('Data saved!')



if selected == 'Data Visualization':
    st.header('Data Visualization')

    with st.form('Saved_periods'):
        period = str(st.selectbox('Select Period', get_all_periods()))
        submited = st.form_submit_button('Period Details')

        if submited:
            period_data = get_period(period) # period_data est un document mongo (dictionnaire)
            comment = period_data.get('comment')
            revenus = period_data.get('revenus')
            depenses = period_data.get('depenses')

            # metrics:
            total_revenus = sum(revenus.values())
            total_depenses = sum(depenses.values())
            budget_restant = total_revenus - total_depenses

            col1,col2,col3 = st.columns(3)
            col1.metric('Total revenus:', f'{total_revenus} {currency}')
            col2.metric('Total dépenses:', f'{total_depenses} {currency}')
            col3.metric('Budget restant:', f'{budget_restant} {currency}')

            st.text(f'Comment: {comment}')
