import streamlit as st
import pandas as pd
import plotly.express as px
from dados import billing, metrics

st.set_page_config(layout="wide")

# Converte listas em DataFrames
billing = pd.DataFrame(billing)
metrics = pd.DataFrame(metrics)

# Lista de clientes (normalizada com .title() só para visual)
clientes = ["Todos"] + sorted(billing["customer_name"].str.title().unique())

# Selectbox
option = st.selectbox("Cliente", clientes)

# Normaliza para comparação
if option == "Todos":
    dados_filtrados = billing
    metrics_filtrados = metrics
else:
    option_lower = option.lower()
    dados_filtrados = billing[billing["customer_name"].str.lower() == option_lower]
    metrics_filtrados = metrics[metrics["customer_name"].str.lower() == option_lower]

# Tabs: Dados e Gráficos
aba_dados, aba_graficos = st.tabs(["📋 Dados", "📊 Gráficos"])

# Abas de dados
with aba_dados:
    st.subheader("Billing Mensal")
    st.dataframe(dados_filtrados, use_container_width=True)

    st.subheader("Metrica Diária")
    st.dataframe(metrics_filtrados, use_container_width=True)

# Aba de gráficos
with aba_graficos:
    st.subheader("Gráfico de Voice Total Geral")
    
    if not metrics_filtrados.empty and "voice_total_geral" in metrics_filtrados.columns:
        # Caso haja mais de um registro (ex: por mês), usa eixo x com data ou mês
        eixo_x = "metric_date" if "metric_date" in metrics_filtrados.columns else metrics_filtrados.index

        fig = px.bar(
            metrics_filtrados,
            x=eixo_x,
            y="voice_total_geral",
            title=f"Voice Total Geral - {option}",
            labels={"voice_total_geral": "Total de Voz"},
            text="voice_total_geral",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Nenhum dado disponível para gerar o gráfico.")
