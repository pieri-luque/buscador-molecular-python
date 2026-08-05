# Buscador Científico y Analizador Molecular en Python (PROTOTIPO) (Acepto Correcciones ✍️)

## 🧪 El Problema Químico
En las etapas iniciales de la investigación analítica, los científicos necesitan consultar rápidamente las propiedades fisicoquímicas y estructurales de miles de compuestos. Ir base de datos por base de datos buscando manualmente los datos necesarios consume demasiado tiempo y fragmenta el flujo de trabajo.

## 💻 La Solución Tecnológica
Desarrollé una aplicación web científica interactiva utilizando **Streamlit** que automatiza esta búsqueda:
1. **Conexión con APIs**: Se conecta en tiempo real a la base de datos pública **PubChem** mediante peticiones HTTP ("requests") para extraer datos estructurales estructurados en formato JSON.
2. **Quimioinformática avanzada**: Utiliza la librería **RDKit** para procesar los códigos de estructura molecular SMILES y calcular descriptores clave en segundos.

## 🛠️ Tecnologías Utilizadas
* **Python 3**
* **Streamlit**: Desarrollo ágil de la interfaz web para científicos.
* **RDKit**: Procesamiento avanzado de datos químicos y descriptores.
* **Requests**: Consumo de APIs REST (PubChem).

## 🚀 Impacto del Proyecto
* Permite centralizar la búsqueda de datos estructurales básicos en una sola herramienta libre de hojas de cálculo.
* Sirve como base para automatizar bases de datos moleculares completas.
