### pdf-comment-remover.txt
This code is used to automate the removal of comments in a PDF.
To run this file you should install Power Automate Desktop. It can be downloaded here for free (<https://flow.microsoft.com/en-us/desktop/>). 

The file is coded in a language native to power automate called Microsoft Power Fx. 
If the file does not automatically open on power automate desktop, one can copy the contents of the file and paste it in a new flow on the application.  
Before running the flow please check if PDFs open with Adobe Acrobat by default, if not then this flow will not work. <br>
When you run the program, you will get a pop-up message to enter the folder path.<br>It takes approximately 10 seconds to remove all the comments on one file.
Sometimes when you open a PDF you can encounter a pop-up message such as
    <code>Cannot find or create the font 'SansSerif'. Some characters may not display or print correctly.</code><br>
The flow can override one such pop-up per PDF.    

### generate-link.json
This flow has 3 steps
<ul>
  <li>Firstly the flow sends a HTTP post request to the URI below
    <br><code>https://parse-url.azurewebsites.net/api/drivelink?code=jIAp3gXank93ClH9IwbM6YPP0n9gQR5zvkC8NcptqfsinmKDzXE8Ag==</code><br>     
    </li>
  <li>The next step is where the body of the HTTP request is parsed to get two values - folder name and final url.
     <br>Folder name is the unique name created based on the time of creation and final url contains the link generated.</li>
  <li>The flow then creates a folder inside <b>/Hello</b> with the folder name it got from the previous step. </li>
</ul>
The flow pastes the final url link on the chatbot.<br>
Important point to note is that Power automate flow cannot create a folder without any files in said folder. Therefore a dummy file called text.txt is created and then deleted.
So do not be alarmed if the recycle bin contains multiple text.txt files.

### complete-status.json
This flow initializes two variables at the start, the first one being 'processed files' which stores the number of files already processed and a second variable called 'total files' which stores the total number of files to be processed in the folder.
The flow then breaks into two paralell branches,
<br>The left branch sends a HTTP post request to the following URI <br><br><code>https://forms-entities.azurewebsites.net/api/orchestrators/invoice_forms_orch?code=BK4LzMdBIHNgmbkvVSW91yHcoul4TgzU6DCXHoxf5zsbHMqtDf7c3A==</code><br><br>
The body of this post request contains the folder path of the files to be processed.
<br>The right branch waits for an event to be published on the Azure Event Grid notifying that a file has been processed. Once it receives an event the event data is parsed to get the files processed and total files. <br>The following message is an example of the message the flow return to the chatbot. 
<br><code>1/10 files have been processed</code>  

### recursive.json
This flow calculates the number of files to be processed by subtracting the total files by the files that are already processed. The flow receives this data from the Azure Event Grid, the body of JSON file receive from the event grid is parsed and the information about the total files and processed files are received from it and stored in separate variables.


