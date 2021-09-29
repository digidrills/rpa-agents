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



