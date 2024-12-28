import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load the cleaned dataset
df = pd.read_csv('cleaned_data.csv')

# Convert 'Year' and 'Month' to datetime format and create a 'Date' column
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-01')

# Define relevant categories for visualization
relevant_categories = [
    'Cereals and products', 'Meat and fish', 'Egg', 'Milk and products',
    'Oils and fats', 'Fruits', 'Vegetables', 'Pulses and products',
    'Sugar and Confectionery', 'Spices', 'Non-alcoholic beverages',
    'Prepared meals, snacks, sweets etc.', 'Food and beverages',
    'Pan, tobacco and intoxicants', 'Clothing', 'Footwear',
    'Clothing and footwear', 'Fuel and light',
    'Household goods and services', 'Health',
    'Transport and communication', 'Recreation and amusement',
    'Education', 'Personal care and effects', 'Miscellaneous', 'General index'
]

# Streamlit app title
st.markdown(
    "<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><br><i>ІСЦ тренд по рокам Trends по вказаним параметрам</i></h5>", 
    unsafe_allow_html=True
)
st.write('\n')

# User input for sector, category, and month
selected_sector = st.selectbox('Оберіть сектор', df['Sector'].unique())
selected_category = st.selectbox('Оберіть категорію', relevant_categories)
selected_month = st.selectbox('Вкажіть місяць', df['Month'].unique())

# Filter data based on user input
filtered_data = df[(df['Sector'] == selected_sector) & (df['Month'] == selected_month)]

# Check if category exists in the dataset
if selected_category in filtered_data.columns:
    # Calculate the percentage change in CPI from the previous year
    filtered_data = filtered_data.sort_values(by='Year')
    filtered_data['CPI_Change'] = filtered_data[selected_category].pct_change() * 100

    # Fill NaN values in 'CPI_Change' with 0 (or another placeholder value)
    filtered_data['CPI_Change'].fillna(0, inplace=True)

    # Create combined figure
    fig = go.Figure()

    # Add Bar chart for CPI
    fig.add_trace(go.Bar(
        x=filtered_data['Year'],
        y=filtered_data[selected_category],
        name='CPI',
        marker_color='royalblue',
        texttemplate='%{y:.2f}',
        textposition='outside',
        opacity=0.75,
        yaxis='y1'
    ))

    # Add Line chart for percentage change
    fig.add_trace(go.Scatter(
        x=filtered_data['Year'],
        y=filtered_data['CPI_Change'],
        mode='lines+markers',
        name='Percentage Change',
        line=dict(color='darkorange', width=2),
        marker=dict(size=8, color='darkorange', symbol='circle'),
        yaxis='y2'
    ))

    st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><hr style='height: 4px;background: linear-gradient(to right, #C982EF, #b8b8b8);'><br><i>ІСЦ та відсоткова змінна для категорії {selected_category} в {selected_sector} секторі ({selected_month})</i></h5>", 
        unsafe_allow_html=True
    )
    st.write('\n')

    # Update layout to have two y-axes with enhanced styling
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='CPI Value',
        yaxis=dict(
            title='CPI Value',
            titlefont=dict(color='royalblue'),
            tickfont=dict(color='royalblue'),
            gridcolor='lightgrey',
            zerolinecolor='lightgrey'
        ),
        yaxis2=dict(
            title='Percentage Change (%)',
            titlefont=dict(color='darkorange'),
            tickfont=dict(color='darkorange'),
            overlaying='y',
            side='right',
            gridcolor='rgba(0,0,0,0)'
        ),
        template='plotly_white',
        margin=dict(l=40, r=150, t=40, b=40),  # Adjust margins for wider legend
        width=1200,  # Set plot width to 1200 pixels
        height=600,  # Set plot height to 600 pixels
        legend=dict(
            x=1.05,  # Move legend further to the right
            y=0.99,
            traceorder='normal',
            orientation='v'
        ),
        plot_bgcolor='rgba(245,245,245,0.8)',
        paper_bgcolor='white'
    )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)
    
    # Add recommendations based on the trends
    st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><hr style='height: 4px;background: linear-gradient(to right, #C982EF, #b8b8b8);'><br><i>Рекомендації</i></h5><br>", unsafe_allow_html=True)
    st.write('\n')
    if filtered_data['CPI_Change'].max() > 10:
        st.write("**Зростання**:Лінія відсоткової зміни показує значне збільшення. Це може свідчити про високу інфляцію для цієї категорії в останні роки. Компанії можуть захотіти скорегувати стратегії ціноутворення або споживачі повинні пам’ятати про збільшення витрат.")
    elif filtered_data['CPI_Change'].min() < -10:
        st.write("**Спадання**: Лінія відсоткової зміни показує значне зменшення. Це може свідчити про зниження інфляції або дефляції. Підприємства потенційно можуть використовувати нижчі витрати, тоді як споживачі можуть отримати вигоду від нижчих цін.")
    else:
        st.write("**Стабільний тренд**: Значення CPI та відсоткові зміни є відносно стабільними. Продовжуйте стежити, щоб бути в курсі будь-яких майбутніх значних змін.")
    
else:
    st.write("Обраної категорії немає в заданій вибірці.")
