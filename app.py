import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
from palmerpenguins import load_penguins
from shiny import render, reactive, req
from shinywidgets import render_widget
import seaborn as sns
import palmerpenguins  # This package provides the Palmer Penguins dataset
# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Penguin Data by Aaron", fillable=True)
#with ui.layout_columns():

#    @render_plotly
#    def plot1():
 #       return px.histogram(px.data.tips(), y="tip")

#    @render_plotly
#    def plot2():
 #       return px.histogram(px.data.tips(), y="total_bill")

# Add a Shiny UI sidebar for user interaction
with ui.sidebar():
# Set the open parameter to "open" to make the sidebar open by default
# Use a with block to add content to the sidebar

# Use the ui.h2() function to add a 2nd level header to the sidebar
    ui.h2("Sidebar")
#   pass in a string argument (in quotes) to set the header text to "Sidebar"

    ui.input_selectize("selected_attribute","Penguin's Characteristics",
                      ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]) # to create a dropdown input to choose a column
#   pass in three arguments:
#   the name of the input (in quotes), e.g., "selected_attribute"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) 
#   e.g. ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

    ui.input_numeric("plotly_bin_count", "Number of Bins",0) #to create a numeric input for the number of Plotly histogram bins
#   pass in two arguments:
#   the name of the input (in quotes), e.g. "plotly_bin_count"
#   the label for the input (in quotes)

    ui.input_slider("seaborn_bin_count","Choose number of bars",0,100,20) # to create a slider input for the number of Seaborn bins
#   pass in four arguments:
#   the name of the input (in quotes), e.g. "seaborn_bin_count"
#   the label for the input (in quotes)
#   the minimum value for the input (as an integer)
#   the maximum value for the input (as an integer)
#   the default value for the input (as an integer)

    ui.input_checkbox_group("selected_species_list","Species",
                           ["Adelie", "Gentoo", "Chinstrap"],selected=["Gentoo"],inline="True") #to create a checkbox group input to filter the species
#   pass in five arguments:
#   the name of the input (in quotes), e.g.  "selected_species_list"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) as ["Adelie", "Gentoo", "Chinstrap"]
#   a keyword argument selected= a list of selected options for the input (in square brackets)
#   a keyword argument inline= a Boolean value (True or False) as you
    ui.hr() #to add a horizontal rule to the sidebar
    ui.a("Link to my GitHub",href="https://github.com/hrawp/cintel-03-reactive",target= "_blank") #to add a hyperlink to the sidebar
#   pass in two arguments:
#   the text for the hyperlink (in quotes), e.g. "GitHub"
#   a keyword argument href= the URL for the hyperlink (in quotes), e.g. your GitHub repo URL
#   a keyword argument target= "_blank" to open the link in a new tab

# When passing in multiple arguments to a function, separate them with commas.


#ui.h6("Palmer Penguins Grid View")

with ui.layout_columns():
    with ui.card():        
        ui.card_header("Palmer Penguins Seaborn Histogram") 
        @render.plot(alt="A Seaborn histogram on penguin body mass in grams.")  
        def plot_histogram():  
            ax = sns.histplot(filtered_data(), x="body_mass_g", bins=input.seaborn_bin_count())  
            ax.set_title("Penguin Mass")
            ax.set_xlabel("Mass (g)")
            ax.set_ylabel("Count")
            return ax 
        


#ui.h4("Palmer Penguins Plotly Histogram")
with ui.layout_columns():
    with ui.card():        
        ui.card_header("Palmer Penguins Plotly Histogram")    
        @render_widget  
        def create_histogram_plot():  
            scatterplot = px.histogram(
                data_frame=filtered_data(),
                x="body_mass_g",
                nbins=input.plotly_bin_count(),
            ).update_layout(
                title={"text": "Penguin Mass", "x": 0.5},
                yaxis_title="Count",
                xaxis_title="Body Mass (g)",
            )    
            return scatterplot  



#ui.h4("Palmer Penguins Seaborn Histogram")
    with ui.card():        
        ui.card_header("Palmer Penguins Grid View") 
        @render.data_frame  
        def penguins_Grid_df():
            return render.DataGrid(filtered_data()) 
    
#    with ui.card():        
#        ui.card_header("Palmer Penguins Total Bill")
 #       @render_plotly
#        def plot2():
#            return px.histogram(px.data.tips(), y="total_bill")


with ui.layout_columns():
    with ui.card():        
        ui.card_header("Plotly Scatterplot: Species")
        @render_plotly
        def plotly_scatterplot():
                return px.scatter(filtered_data(),
                    x=input.selected_attribute(),
                    y="body_mass_g",
                    color="species",
                    title="Penguins Plot (Plotly Express)",
                    labels={
                        "bill_length_mm": "Bill Length (mm)",
                        "body_mass_g": "Body Mass (g)",
                    },
                    size_max=8, # set the maximum marker size
                )

#ui.h6("Palmer Penguins Table View")
    with ui.card():
        ui.card_header("Palmer Penguins Table View")
        @render.data_frame  
        def penguins_table_df():
            return render.DataTable(filtered_data()) 

#    with ui.card():
#        ui.card_header("Palmer Penguins Tips")            
#        @render_plotly
#        def plot1():
#            return px.histogram(px.data.tips(), y="tip")


# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------

# Add a reactive calculation to filter the data
# By decorating the function with @reactive, we can use the function to filter the data
# The function will be called whenever an input functions used to generate that output changes.
# Any output that depends on the reactive function (e.g., filtered_data()) will be updated when the data changes.

#@reactive.calc
#def filtered_data():
#    return penguins_df


@reactive.calc
def filtered_data():

    # The required function req() is used to ensure that
    # the input.selected_species_list() function is not empty.
    req(input.selected_species_list())

    # If empty, req() will stop the execution and 
    # we'll just wait until the associated input changes to not empty.
    # If not empty, we'll continue and filter the data.
    isSpeciesMatch = penguins_df["species"].isin(input.selected_species_list())

    return penguins_df[isSpeciesMatch]
