# cintel-04-local


##  How to Install and Setup Projects

Create a new repo in Git Hub.  Make sure to include README when creating the new repo.

Clone the new repo to your machine.
```
git clone https://github.com/hrawp/datafun-05-sql
```

Add a .gitignore file with:
## Python virtual environment.
```
.venv/
```

## Visual Studio Code settings and workspace.
```
.vscode/
```
added so .venv files will not be sent up to your repo.

## Create a virtual environement by running this command.
```
python -m venv .venv
```

## Activate the environment by running this command.
```
.\.venv\Scripts\activate
```

## Open a terminal and activate the project (anytime you open a new terminal) and run the shiny app.

```
shiny run --reload --launch-browser penguins/app.pycdcd
```
## Update the requirements.txt with libraries that need to be installed.



## Run the three Git commands to stange and transmit files to GitHub.
```
git add .
```
```
git commit -m "initial commit"
```
```
git push origin main
```


## install depedencies from requirements.txt
```
py -m pip install -r requirements.txt
```

After the app is built, serve the app locally from the docs folder to test before publishing to GitHub Pages.
In the terminal, run the following command from the root of the project folder with the project virtual environment active:
```
py -m http.server --directory docs --bind localhost 8008
```

Action 4: Publish GitHub Pages for the Repo
This is a one-time step. We need to set up your GitHub repo (in the cloud) so that it will host with GitHub Pages. 

The first time you set up an app to use Pages, navigate to the repository on GitHub and configure the settings to publish the app with GitHub Pages.
After configuring the repository once, each time you push changes to the main branch, the app will automatically update.

Go to the repository on GitHub and navigate to the **Settings** tab.
Scroll down and click the **Pages** section down the left.
Select branch main as the source for the site.
Change from the root folder to the docs folder to publish from.
Click Save and wait for the site to build.
Eventually, be patient, your app will be published and if you scroll to the top of the Pages tab, you'll see your github.io URL for the hosted web app. Copy this to your clipboard. 
Back on the main repo page, find the About section of the repo (kind of upper right).
Edit the "About" section of the repository to include a link to your hosted web app by using the Pages URL. 
When Finished

When you finish, you should have a working, unique version of a penguin dashboard that you can work with locally on your machine and have published for free on the web. It should have several inputs including a drop down to select a column for display that works and a checkbox group for species that is used to reactively filter the species shown on the charts. It should use a reactive calc to filter the dataframe and use the filtered dataframe for your tables, grids, and charts. 