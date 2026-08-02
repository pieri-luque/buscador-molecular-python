import streamlit as st
import requests
from rdkit import Chem
from rdkit.Chem import Descriptors

st.set_page_config(page_title="Buscador Molecular 3D", page_icon="🧪", layout="wide")

st.title("🧪 Buscador y Analizador de Propiedades Moleculares")
st.write("Introduce el nombre de un compuesto químico en inglés (ej. *aspirin, caffeine, ethanol*).")

nombre_compuesto = st.text_input("Nombre del compuesto:", "caffeine").strip().lower()

if nombre_compuesto:
    # URL limpia y directa
    url = f"https://nih.gov/{nombre_compuesto}/property/CanonicalSMILES,MolecularFormula,MolecularWeight/JSON"
    
    # ESTA LÍNEA ES PARA REVISAR: Nos mostrará la URL real en la página web
    st.info(f"Buscando en: {url}")
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            datos = response.json()
            lista_propiedades = datos.get("PropertyTable", {}).get("Properties", [])
            
            if lista_propiedades:
                propiedades = lista_propiedades[0]
                
                # ¡OJO AQUÍ! Estas líneas ahora tienen 4 espacios más hacia la derecha
                smiles = propiedades.get("CanonicalSMILES", "")
                formula = propiedades.get("MolecularFormula", "")
                peso = propiedades.get("MolecularWeight", 0)
                
                if smiles:
                    mol = Chem.MolFromSmiles(smiles)
                    logp = Descriptors.MolLogP(mol)
                    h_donors = Descriptors.NumHDonors(mol)
                    h_acceptors = Descriptors.NumHAcceptors(mol)
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("📊 Propiedades Químicas")
                        st.metric("Fórmula Molecular", formula)
                        st.metric("Peso Molecular", f"{peso} g/mol")
                        st.text(f"Código SMILES: {smiles}")
                        
                    with col2:
                        st.subheader("🧬 Descriptores Lipinski")
                        st.metric("LogP (Lipofilicidad)", f"{logp:.2f}")
                        st.metric("Donadores de H", h_donors)
                        st.metric("Aceptores de H", h_acceptors)
                else:
                    st.error("No se pudo generar la estructura química.")
            else:
                st.error("La base de datos no devolvió propiedades.")
        else:
            st.error(f"Compuesto no encontrado (Código HTTP: {response.status_code}). Intenta otro nombre en inglés.")
            
    except Exception as e:
        st.error(f"Error en la petición: {e}")



### EJECUCIÓN: streamlit run app_molecular.py
