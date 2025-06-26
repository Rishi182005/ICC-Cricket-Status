import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
import mysql.connector as x
from ttkthemes import ThemedStyle
import subprocess
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from tkinter.ttk import Progressbar

base_url = 'https://www.cricketworldcup.com/match/'
end = '#overview'

# Create a database connection and cursor
y = x.connect(host="localhost", user="root", password="Rishi2005", database="icc")
z = y.cursor()

# Create the main window
root = tk.Tk()
root.title("Cric Ninja")
root.geometry("1920x1080")

# Load an image
image = Image.open("user_cricket.jpg")
image = ImageTk.PhotoImage(image)


def add_image_label(tab_frame):
    image_label = tk.Label(tab_frame, image=image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the image label to cover the whole tab
    image_label.image = image

def remove_all_widgets(tab_frame):
    for widget in tab_frame.winfo_children():
        if widget != live_score_label :
            widget.destroy()

            
#############################################################################################################################################################
            
# Create a tabbed interface
tab_control = ttk.Notebook(root)

# Create tabs
tab0 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

# Add tabs to the tab control
tab_control.add(tab0, text="Home")
tab_control.add(tab1, text="View Scores")
tab_control.add(tab2, text="View Stats")
tab_control.add(tab3, text="View Results")
tab_control.add(tab4, text="View World Cup - 2023 Details")

#############################################################################################################################################################

# Create content for each tab
for tab_name, tab_frame in zip(["Home", "View Scores", "View Stats", "View Results", "View World Cup - 2023 Details"], [tab0, tab1, tab2, tab3, tab4]):
    if tab_name == "View Scores":
        
        load_label=tk.Label(tab_frame, text="Fetching live matches. Please wait...",font=("Arial", 18))
        load_label.pack(fill="both", expand=False)
        
        live_score_label = tk.Label(tab_frame, text="", font=("Arial", 18))
        live_score_label.pack(fill="both", expand=True)

        no_live_score_label = tk.Label(tab_frame, text="", font=("Arial", 18))
        no_live_score_label.pack(fill="both", expand=True)


    elif tab_name == "View Results":
        # Create a scrollable Text widget for results
        results_load_label=tk.Label(tab_frame, text="Fetching match results. Please wait...",font=("Arial", 18))
        results_load_label.pack(fill="both", expand=False)
        
        results_text = tk.Text(tab_frame, wrap=tk.WORD, width=100, height=30, font=("Arial", 18))
        results_text.pack(fill="both", expand=True)
        results_text.configure(state="disabled")  # Make the Text widget read-only

        no_result_label = tk.Label(tab_frame, text="", font=("Arial", 18))
        no_result_label.pack(fill="both", expand=True)

        
    elif tab_name == "View Stats":
        stat_label = tk.Label(tab_frame, text="Player Stats", font=("Arial", 18))
        stat_label.pack(fill="both", expand=True)
        
        add_image_label(tab_frame)
    else:
        label = tk.Label(tab_frame, text=f"{tab_name}")
        label.pack(fill="both", expand=True)
        add_image_label(tab_frame)

tab_file_paths = {
    "View Player Stats": "view_player_stats.py",
}
current_match_url = None

#############################################################################################################################################################

def update_results_text(results):
    results_text.configure(state="normal")  # Enable the Text widget for writing
    results_text.delete(1.0, tk.END)  # Clear previous results
    results_text.insert(tk.END, results)  # Insert new results
    results_text.configure(state="disabled")

def url_generator():
    for i in range(102720, 102784):
        e = str(i)
        match_url = base_url + e + end
        fetch_data(match_url)

def fetch_data(match_url):
    response = requests.get(match_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        div_with_class = soup.find('div', class_='mc-scorebox__team-flags-container')

        if div_with_class:
            x = div_with_class.text.strip()
            x = x.replace('\n', ' ')
            if "Live" in x:
                if live_score_label.winfo_exists():
                    live_score_label.config(text=x)
                    root.after(600, fetch_data, match_url)  # Refresh every 60 seconds (adjust as needed)
                else:
                    print("Live score label no longer exists.")
            else:
                if no_live_score_label and no_live_score_label.winfo_exists():
                    no_live_score_label.config(text="Currently no live matches are going on")
                else:
                    print("No live score label no longer exists.")


#############################################################################################################################################################
                    
def url_generator1():
    results = []  # Initialize an empty list to store match results

    def fetch_results(match_url):
        response = requests.get(match_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            div_with_class = soup.find('div', class_='mc-scorebox__team-flags-container')
            div_with_class1 = soup.find('div', class_='mc-scorebox__summary js-scorebox-update-content')

            if div_with_class and div_with_class1:
                result1 = div_with_class1.text.strip()
                result = div_with_class.text.strip()
                result1 = result1.replace('\n', ' ')
                result = result.replace('\n', ' ')
                if "Complete" in result:
                    return f"{result1}\n{result}"  # Return the combined result text
        return ""  # Return an empty string if no result or not complete

    for i in range(102720, 102784):
        e = str(i)
        match_url = base_url + e + end
        result = fetch_results(match_url)

        if result and "Complete" in result:
            results.append(result)  # Append the result to the list

    def extract_date(match_entry):
        date_str = match_entry.split(' - ')[0]
        return datetime.strptime(date_str, '%A %d %B %Y')

    sorted_matches = sorted(results, key=extract_date)

    # Assuming 'update_results_text' is a function you have for updating the results text
    combined_results = "\n\n".join(sorted_matches)
    update_results_text(combined_results)

#############################################################################################################################################################
    
# Function to open a Python file when a tab is selected
def tab_selected(event):
    current_tab = tab_control.select()
    tab_name = tab_control.tab(current_tab, "text")
    if tab_name in tab_file_paths:
        open_python_file(tab_file_paths[tab_name])
    elif tab_name == "View Stats":
        tab2_homepage()
    elif tab_name == "View World Cup - 2023 Details":
        icc_menu()
    elif tab_name == "View Results":
        remove_all_widgets(tab4)  # Remove all widgets in the "View Results" tab
        url_generator1()
    elif tab_name == "View Scores": # Remove all widgets in the "View Scores" tab
        url_generator()

############################################################################################################################################################
        
# Function to open a Python file using subprocess
def open_python_file(file_path):
    try:
        subprocess.Popen(["python", file_path])
    except Exception as e:
        print(f"Error: {e}")

# Bind the tab_selected function to the "<<NotebookTabChanged>>" event
tab_control.bind("<<NotebookTabChanged>>", tab_selected)

# Pack the tab control to make it visible
tab_control.pack(fill="y", expand=True)

#############################################################################################################################################################

team_a = tk.StringVar()
team_b = tk.StringVar()

# Create a Treeview widget for displaying results
global tree

# Initialize the Treeview widget as None
def panel():
    global tree
    tree = None
    for widget in tab4.winfo_children():
        widget.destroy()

    add_image_label(tab_frame)
    # Create the Treeview widget if it doesn't exist
    if not tree:
        tree = ttk.Treeview(tab4)
        tree["columns"] = ("Match_Number","Round_Number","Date", "Location", "Home_Team", "Away_Team", "Result")
        tree.heading("#1", text="Match Number")
        tree.heading("#2", text="Round Number")
        tree.heading("#3", text="Date")
        tree.heading("#4", text="Location")
        tree.heading("#5", text="Home Team")
        tree.heading("#6", text="Away Team")
        tree.heading("#7", text="Result")
        tree.pack(pady=20, padx=20, fill="both", expand=True)

    # Clear the previous data in the Treeview

    main_label = ttk.Label(tab4, text="World Cup 2023 Matches", font=("Arial", 24))
    main_label.pack(pady=10)

    A_label = ttk.Label(tab4, text="Team A", font=("Arial", 14))
    A_label.pack(pady=10)

    A_entry = ttk.Entry(tab4, font=("Arial", 14), textvariable=team_a)
    A_entry.pack(pady=10)

    B_label = ttk.Label(tab4, text="Team B", font=("Arial", 14))
    B_label.pack(pady=10)

    B_entry = ttk.Entry(tab4, font=("Arial", 14), textvariable=team_b)
    B_entry.pack(pady=10)

    Back = tk.Button(tab4, text="Go Back", font=("Calibri", 14, "bold"), command=icc_menu)
    Back.pack(pady=10)

    A_entry.bind("<KeyRelease>", records)
    B_entry.bind("<KeyRelease>", records)

def records(event=None):
    for record in tree.get_children():
        tree.delete(record)

    # Retrieve team names from the Entry widgets
    team_a_name = team_a.get()
    team_b_name = team_b.get()

    # Build a SQL query to search for matches containing the input team names
    query = "SELECT * FROM match_schedule WHERE Home_Team LIKE %s AND Away_Team LIKE %s;"
    search_pattern_a = f'{team_a_name}%'
    search_pattern_b = f'{team_b_name}%'
    z.execute(query, (search_pattern_a, search_pattern_b))
    result = z.fetchall()

    # Clear the previous data in the Treeview

    # Insert new data into the Treeview
    for row in result:
        tree.insert("", "end", values=row)

#############################################################################################################################################################
        
global tree1
def points_table():
    global tree1
    tree1=None
    # Clear any existing widgets in tab4
    for widget in tab4.winfo_children():
        widget.destroy()
    
    add_image_label(tab_frame)

    if not tree1:
        # Create a Treeview widget for displaying the points table
        tree1 = ttk.Treeview(tab4)
        tree1["columns"] = ("Pos","Team", "Matches", "Win", "Lose","N/R","Tied", "NRR", "Points")
        tree1.heading("#1", text="Pos")
        tree1.heading("#2", text="Team")
        tree1.heading("#3", text="Matches")
        tree1.heading("#4", text="Win")
        tree1.heading("#5", text="Lose")
        tree1.heading("#6", text="N/R")
        tree1.heading("#7", text="Tied")
        tree1.heading("#8", text="NRR")
        tree1.heading("#9", text="Points")
        tree1.pack(pady=20, padx=20, fill="both", expand=False)

    # URL for the points table data
    table_url = "https://www.cricketworldcup.com/standings"  # Replace with the actual URL

    # Send an HTTP request to fetch the points table data
    response = requests.get(table_url)
    if response.status_code == 200:
        try:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Locate the table containing points table data (adjust based on actual HTML structure)
            table = soup.find('table', {'class': 'table'})
            if table:
                for row in table.find_all('tr'):  # Skip the header row
                    columns = row.find_all('td')
                    if len(columns) >= 9:
                        pos = columns[0].text.strip()
                        team = columns[1].text.strip()
                        matches = columns[2].text.strip()
                        win = columns[3].text.strip()
                        lose = columns[4].text.strip()
                        nr = columns[5].text.strip()
                        tied = columns[6].text.strip()
                        nrr = columns[7].text.strip()
                        points = columns[8].text.strip()

                        # Insert the data into the Treeview widget
                        tree1.insert("", "end", values=(pos,team, matches, win, lose, nr, tied, nrr, points))
            else:
                # Handle the case where the table was not found
                tree1.insert("", "end", values=("Data not found", "", "", "", "", ""))
        except Exception as e:
            # Handle any parsing errors
            tree1.insert("", "end", values=("Error parsing data", "", "", "", "", ""))
    else:
        # Handle the case where the HTTP request failed
        tree1.insert("", "end", values=("Request failed", "", "", "", "", ""))
        
#############################################################################################################################################################

def icc_menu():
    for widget in tab4.winfo_children():
        widget.destroy()
    add_image_label(tab_frame)
    menu = tk.Label(tab4, text="Menu", font=("Arial", 14))
    menu.pack(pady=10)

    tree = None

    Matches = tk.Button(tab4, text="World Cup 2023 Matches", font=("Calibri", 14, "bold"), command=panel)
    Matches.pack(pady=10)

    Table = tk.Button(tab4, text="            Points Table              ", font=("Calibri", 14, "bold"), command=points_table)
    Table.pack(pady=10)

#############################################################################################################################################################

tree3=None

selected_option = tk.StringVar()
selected_option1 = tk.StringVar()
player_name = tk.StringVar()
n = tk.StringVar()

def tab2_homepage():
    global tree3
    def on_select():
        selected_value = selected_option.get()
        selected_value1 = selected_option1.get()
        table_search(player_name.get(), selected_value, selected_value1)
    
    for widget in tab2.winfo_children():
        widget.destroy()
    add_image_label(tab2)

    match_type = ["Select", "ODI", "Test", "T20"]
    innings = ["Select", "Batting", "Bowling"]

    player_label = ttk.Label(tab2, text="Enter Player Name", font=("Arial", 15))
    player_label.place(x=200, y=50)

    player_entry = ttk.Entry(tab2, font=("Arial", 14), textvariable=player_name)
    player_entry.place(x=200, y=100)

    dropdown_label = ttk.Label(tab2, text="Match Type", font=("Arial", 15))
    dropdown_label.place(x=600, y=50)

    dropdown = ttk.Combobox(tab2, textvariable=selected_option, values=match_type)
    dropdown.place(x=600, y=100)

    dropdown1_label = ttk.Label(tab2, text="Innings", font=("Arial", 15))
    dropdown1_label.place(x=850, y=50)

    dropdown1 = ttk.Combobox(tab2, textvariable=selected_option1, values=innings)
    dropdown1.place(x=850, y=100)

    Refresh_button = tk.Button(tab2, text="Refresh", font=("Arial", 15), command=on_select)
    Refresh_button.place(x=1100, y=70)

    selected_option.set("Select")
    selected_option1.set("Select")


def table_search(n,a,b):
    global tree3
    tree3=None
    if a == "ODI" and b == "Batting":
        for widget in tab2.winfo_children():
            widget.destroy()
        add_image_label(tab_frame)
        if not tree3:
            tree3 = ttk.Treeview(tab2)
            tree3["columns"] = ("Player", "Span", "Matches", "Innings", "Not_Out", "Runs","HS", "Average", "BF", "SR", "100s", "50s", "0s")
            tree3.heading("#1", text="Player")
            tree3.heading("#2", text="Span")
            tree3.heading("#3", text="Matches")
            tree3.heading("#4", text="Innings")
            tree3.heading("#5", text="Not Out")
            tree3.heading("#6", text="Runs")
            tree3.heading("#7", text="HS")
            tree3.heading("#8", text="Average")
            tree3.heading("#9", text="BF")
            tree3.heading("#10", text="SR")
            tree3.heading("#11", text="100s")
            tree3.heading("#12", text="50s")
            tree3.heading("#13", text="0s")
            tree3.pack(pady=20, padx=20, fill="both", expand=False)
            for record in tree3.get_children():
                tree3.delete(record)

        name = player_name.get()
        if not name:
            query = "SELECT * FROM odi_batting LIMIT 10"
            z.execute(query)
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        else:
            query = "SELECT * FROM odi_batting WHERE Player LIKE %s"
            search_pattern_a = f'%{name}%'
            z.execute(query, (search_pattern_a,))
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        back_button = tk.Button(tab2, text="Go Back", font=("Arial", 15), command=tab2_homepage)
        back_button.pack(pady=10)
    
    elif a=="ODI" and b=="Bowling":
        for widget in tab2.winfo_children():
            widget.destroy()
        add_image_label(tab_frame)
        if not tree3:
            tree3 = ttk.Treeview(tab2)
            tree3["columns"] = ("Player", "Span", "Matches", "Innings", "Balls", "Runs", "Wickets", "BBI", "Average", "Economy", "SR", "4", "5")
            tree3.heading("#1", text="Player")
            tree3.heading("#2", text="Span")
            tree3.heading("#3", text="Matches")
            tree3.heading("#4", text="Innings")
            tree3.heading("#5", text="Balls")
            tree3.heading("#6", text="Runs")
            tree3.heading("#7", text="Wickets")
            tree3.heading("#8", text="BBI")
            tree3.heading("#9", text="Average")
            tree3.heading("#10", text="Economy")
            tree3.heading("#11", text="SR")
            tree3.heading("#12", text="4")
            tree3.heading("#13", text="5")
            tree3.pack(pady=20, padx=20, fill="both", expand=False)

        name = player_name.get()
        if not name:
            query = "SELECT * FROM odi_bowling LIMIT 10"
            z.execute(query)
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)

        else:
            query = "SELECT * FROM odi_bowling WHERE Player LIKE %s"
            search_pattern = f'%{name}%'
            z.execute(query, (search_pattern,))
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        back_button = tk.Button(tab2, text="Go Back", font=("Arial", 15), command=tab2_homepage)
        back_button.pack(pady=10)
        
    elif a=="Test" and b=="Batting":
        for widget in tab2.winfo_children():
            widget.destroy()
        add_image_label(tab_frame)
        if not tree3:
            tree3 = ttk.Treeview(tab2)
            tree3["columns"] = ("Player", "Span", "Matches", "Innings", "Not_Out", "Runs", "HS", "Average", "100s", "50s", "0s")
            tree3.heading("#1", text="Player")
            tree3.heading("#2", text="Span")
            tree3.heading("#3", text="Matches")
            tree3.heading("#4", text="Innings")
            tree3.heading("#5", text="Not Out")
            tree3.heading("#6", text="Runs")
            tree3.heading("#7", text="HS")
            tree3.heading("#8", text="Average")
            tree3.heading("#9", text="100s")
            tree3.heading("#10", text="50s")
            tree3.heading("#11", text="0s")
            tree3.pack(pady=20, padx=20, fill="both", expand=False)
            for record in tree3.get_children():
                tree3.delete(record)
        
        name = player_name.get()
        if not name:
            query = "SELECT * FROM test_batting LIMIT 10"
            z.execute(query)
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)

        else:
            query = "SELECT * FROM test_batting WHERE Player LIKE %s"
            search_pattern = f'%{name}%'
            z.execute(query, (search_pattern,))
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        back_button = tk.Button(tab2, text="Go Back", font=("Arial", 15), command=tab2_homepage)
        back_button.pack(pady=10)
        
    elif a=="Test" and b=="Bowling":
        for widget in tab2.winfo_children():
            widget.destroy()
        add_image_label(tab_frame)
        if not tree3:
            tree3 = ttk.Treeview(tab2)
            tree3["columns"] = (
                "Player", "Span", "Matches", "Innings", "Balls", "Runs",
                "Wickets", "BBI", "BBM", "Average", "Economy", "SR", "5", "10"
            )

            # Set the column headings
            tree3.heading("#1", text="Player")
            tree3.heading("#2", text="Span")
            tree3.heading("#3", text="Matches")
            tree3.heading("#4", text="Innings")
            tree3.heading("#5", text="Balls")
            tree3.heading("#6", text="Runs")
            tree3.heading("#7", text="Wickets")
            tree3.heading("#8", text="BBI")
            tree3.heading("#9", text="BBM")
            tree3.heading("#10", text="Average")
            tree3.heading("#11", text="Economy")
            tree3.heading("#12", text="SR")
            tree3.heading("#13", text="5")
            tree3.heading("#14", text="10")

            tree3.pack(pady=20, padx=20, fill="both", expand=False)

        name = player_name.get()
        if not name:
            query = "SELECT * FROM test_bowling LIMIT 10"
            z.execute(query)
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        else:       
            query = "SELECT * FROM test_bowling WHERE Player LIKE %s"
            search_pattern_a = f'%{name}%'
            z.execute(query, (search_pattern_a,))
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        back_button = tk.Button(tab2, text="Go Back", font=("Arial", 15), command=tab2_homepage)
        back_button.pack(pady=10)
                
    elif a=="T20" and b=="Batting":
        for widget in tab2.winfo_children():
            widget.destroy()
        add_image_label(tab_frame)   
        if not tree3:
            tree3 = ttk.Treeview(tab2)
            tree3["columns"] = ("Player", "Span", "Matches", "Innings", "Not_Out", "Runs", "HS", "Average", "BF", "SR", "100s", "50s", "0s", "4s", "6s")
            tree3.heading("#1", text="Player")
            tree3.heading("#2", text="Span")
            tree3.heading("#3", text="Matches")
            tree3.heading("#4", text="Innings")
            tree3.heading("#5", text="Not_Out")
            tree3.heading("#6", text="Runs")
            tree3.heading("#7", text="HS")
            tree3.heading("#8", text="Average")
            tree3.heading("#9", text="BF")
            tree3.heading("#10", text="SR")
            tree3.heading("#11", text="100s")
            tree3.heading("#12", text="50s")
            tree3.heading("#13", text="0s")
            tree3.heading("#14", text="4s")
            tree3.heading("#15", text="6s")
            tree3.pack(pady=20, padx=20, fill="both", expand=False)
            for record in tree3.get_children():
                tree3.delete(record)

        name = player_name.get()
        if not name:
            query = "SELECT * FROM t20_batting LIMIT 10"
            z.execute(query)
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        else:
            query = "SELECT Player, Span, Matches, Innings, Not_Out, Runs, HS, Average, BF, SR, 100s, 50s, 0s, 4s, 6s FROM t20_batting WHERE Player LIKE %s"
            search_pattern_a = f'%{name}%'
            z.execute(query, (search_pattern_a,))
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        back_button = tk.Button(tab2, text="Go Back", font=("Arial", 15), command=tab2_homepage)
        back_button.pack(pady=10)
    
    elif a=="T20" and b=="Bowling":
        for widget in tab2.winfo_children():
            widget.destroy()
        add_image_label(tab_frame)
        if not tree3:
            tree3 = ttk.Treeview(tab2)
            tree3["columns"] = (
                "Player", "Span", "Matches", "Innings", "Overs", "Mdns", "Runs", "Wickets", "BBI",
                "Average", "Economy", "SR", "4s", "5s"
            )
            tree3.heading("#1", text="Player")
            tree3.heading("#2", text="Span")
            tree3.heading("#3", text="Matches")
            tree3.heading("#4", text="Innings")
            tree3.heading("#5", text="Overs")
            tree3.heading("#6", text="Mdns")
            tree3.heading("#7", text="Runs")
            tree3.heading("#8", text="Wickets")
            tree3.heading("#9", text="BBI")
            tree3.heading("#10", text="Average")
            tree3.heading("#11", text="Economy")
            tree3.heading("#12", text="SR")
            tree3.heading("#13", text="4s")
            tree3.heading("#14", text="5s")
            tree3.pack(pady=20, padx=20, fill="both", expand=False)
            for record in tree3.get_children():
                tree3.delete(record)
        
        name = player_name.get()
        if not name:
            query = "SELECT * FROM t20_bowling LIMIT 10"
            z.execute(query)
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        else:
            query = "SELECT * FROM t20_bowling WHERE Player LIKE %s"
            search_pattern_a = f'%{name}%'
            z.execute(query, (search_pattern_a,))
            result = z.fetchall()
            for row in result:
                tree3.insert("", "end", values=row)
        back_button = tk.Button(tab2, text="Go Back", font=("Arial", 15), command=tab2_homepage)
        back_button.pack(pady=10)
    
#############################################################################################################################################################

# Create a custom style for the "Search" button
root.style = ttk.Style()
root.style.configure("Custom.TButton", font=("Arial", 14), padding=(10, 5), foreground="blue", background="#007acc")

# Start the main loop
root.mainloop()

