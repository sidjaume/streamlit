import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title="Tu prime",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
option = st.sidebar.selectbox(label='Select a page',options=['Home','Charts','Filter'], index=0)
st.write('You selected: ', option)

df = pd.read_csv(r'data\red_recarga_acceso_publico_2021.csv', sep=";")
df = df.rename(columns={'latidtud':'lat', 'longitud':'lon'})

uploaded_files = st.sidebar.file_uploader("Choose a CSV file", 
                                    accept_multiple_files=False,
                                    type=["csv"])

if uploaded_files:
        df = pd.read_csv(uploaded_files, sep=";")
        st.balloons()


if option == 'Home':
    st.title("Home")
    st.write("This is the home page")

    image = Image.open(r'img\puntos-recarga-madrid.jpg')

    st.title("My First Streamlit APP")
    st.image(image, caption='Sunrise by the mountains', width=300)
    st.map(data=df, zoom=11, )

    with st.expander("Click for details"):
        st.write("App web que muestra puntos de carga en Madrid")

    
    
elif option == 'Charts':
    st.title("Charts")
    st.write("This is the charts page")

    st.bar_chart(data=df, x='DISTRITO', y= 'Nº CARGADORES')
    st.bar_chart(data=df, x='OPERADOR', y= 'Nº CARGADORES')
    
    with st.echo():
        st.dataframe(df)

elif option == 'Filter':
        
        a = df['Nº CARGADORES'].unique().max() +1
        b = df['Nº CARGADORES'].unique().min()
        slider = st.select_slider(label='Desliza para varias el nº de cargadores: ',options= list(range(b,a)))
        
        st.dataframe(df[df['Nº CARGADORES'] == slider])

        filtro_op = st.selectbox(label='Selecciona operador',options=df.OPERADOR.unique(), index=0)
        df_to_show = df[df['OPERADOR'] == filtro_op].copy()
        st.dataframe(df_to_show)
        # if option == 'Minimo':
        #     df = df[['OPERADOR','Nº CARGADORES']].sort_values(by='Nº CARGADORES', ascending=True)
        #     
            
        # elif option == 'Maximo':
        #     df = df[['OPERADOR','Nº CARGADORES']].sort_values(by='Nº CARGADORES', ascending=False)

        #     with st.echo():
        #         st.dataframe(df)