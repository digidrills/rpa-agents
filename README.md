# RPA Agents - RPA, Power Automate, Virtual Agent related work.

### Power Automate

Contains assistive flows to automate working with Files on OneDrive via the Microsoft Graph and Azure API.<br>
<br><b>Power Automate Desktop</b> is used to remove comments from PDFs, some comments obstruct important data present in the PDFs therefore it was deemed necessary that all comments are to be removed in order to properly process the data.
<br><br><b>Power Automate Cloud</b> is used to generate a link when a batch of files are to be uploaded to a file on OneDrive. It is also used to display the status of the files that are processed in real time using event triggers on Azure Event Grid.
While the chatbot uses Power Virtual Agents for the front-end, the back-end is handled by Power Automate Cloud Flows. 

### Virtual Agents

Contains a flow for creating an interactive Chatbot on Microsoft Teams using Microsoft Power Virtual Agents.<br>
The chatbot is triggered using keywords such as 'upload','invoice' & 'files'. Once triggered the chabot sends a link to the user to upload the files to be processed. After the user confirms that they are done uploading all the files. The chatbot then displays the number of files that are processed at regular intervals and finally confirms that all the files have been processed succesfully.
