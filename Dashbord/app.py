import streamlit as st
import pandas as pd
import plotly.express as px

#configuração da pagina
st.set_page_config(
    page_title="Dashbord de Salários na Área de Dados",
    psge_icon="📊",
    layout="wide",
)

#carregando dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

