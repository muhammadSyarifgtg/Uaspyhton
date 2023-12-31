import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# For example, add a title and some content
st.title('Data Penjualan Pakaian Online Shop')
st.write('Data penjualan pakaian online shop. Pilih berkas data di sidebar untuk melihat informasi penjualan.')

# Load data from CSV files
df1 = pd.read_csv('shopping_behavior_updated.csv')
df2 = pd.read_csv('shopping_trends_updated.csv')
df3 = pd.read_csv('shopping_trends.csv')

# Create a Streamlit sidebar with group members' information
st.sidebar.title('Group Members')

# List of group members
group_members = ['Muhammad Syarif', 'Gentar Alam', 'Rizki Ikhza']

# Create a dropdown to select a group member
selected_member = st.sidebar.selectbox('Select Group Member', group_members)

# Dictionary of group members' information
members_info = {
    'Muhammad Syarif': {
        'Email': 'syrf253@gmail.com',
        'Kelas': 'TI21A4',
    },
    'Gentar Alam': {
        'Email': 'gengengen.com',
        'Kelas': 'TI21A4'
    },
    'Rizki Ikhza': {
        'Email': 'rizki190@gmail.com',
        'Kelas': 'TI21A4'
    },
}

if selected_member:
    st.sidebar.markdown(f'**{selected_member}**')
    st.sidebar.markdown(f'Email: {members_info[selected_member]["Email"]}')
    st.sidebar.markdown(f'Kelas: {members_info[selected_member]["Kelas"]}')

# Function to display a colored table with a black background
def colored_table(dataframe):
    # Apply black background color to the entire DataFrame
    return dataframe.style.set_properties(**{'background-color': 'white', 'color': 'black'})

# Add a sidebar selectbox to choose the data file
selected_files = st.sidebar.multiselect('Select Data Files', ['Data from File 1', 'Data from File 2', 'Data from File 3'])

# Display tables with a black background
for selected_file in selected_files:
    st.subheader(selected_file)
    if selected_file == 'Data from File 1':
        st.dataframe(colored_table(df1))
    elif selected_file == 'Data from File 2':
        st.dataframe(colored_table(df2))
    elif selected_file == 'Data from File 3':
        st.dataframe(colored_table(df3))

# Add a checkbox to control the display of the chart
show_chart = st.sidebar.checkbox('Show Chart', value=True)

# Create a pie chart to show the comparison of total purchases based on the checkbox value
if show_chart:
    total_purchase_file1 = df1['Purchase Amount (USD)'].sum()
    total_purchase_file2 = df2['Purchase Amount (USD)'].sum()
    total_purchase_file3 = df3['Purchase Amount (USD)'].sum()

    labels = ['File 1', 'File 2', 'File 3']
    sizes = [total_purchase_file1, total_purchase_file2, total_purchase_file3]
    explode = (0.1, 0, 0)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode=explode, colors=['#ff7f50', '#00ced1', '#98fb98'])
    ax.axis('equal')
    st.sidebar.pyplot(fig)

# Add a home page with an image and a description of online shop clothing sales data
if not selected_files:
    st.image('g1.jpg', use_column_width=True)
    st.write('Data penjualan pakaian online shop. Pilih berkas data di sidebar untuk melihat informasi penjualan. Anda juga dapat menampilkan grafik perbandingan total pembelian.')

# Run the Streamlit app
if __name__ == '__main__':
    st.write('Running the app...')
