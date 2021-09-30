# RPA Agents - RPA, Power Automate, Virtual Agent related work.

### Power Automate

Contains assistive flows to automate working with Files on OneDrive via the Microsoft Graph and Azure API.<br>
<br><b>Power Automate Desktop</b> is used to remove comments from PDFs, some comments obstruct important data present in the PDFs therefore it was deemed necessary that all comments are to be removed in order to properly process the data.
<br><br><b>Power Automate Cloud</b> is used to generate a link when a batch of files are to be uploaded to a file on OneDrive. It is also used to display the status of the files that are processed in real time using event triggers on Azure Event Grid.
While the chatbot uses Power Virtual Agents for the front-end, the back-end is handled by Power Automate Cloud Flows. 

### Virtual Agents

Contains a flow for creating an interactive Chatbot on <b>Microsoft Teams</b> using Microsoft Power Virtual Agents.<br>
The chatbot is triggered using keywords such as 'upload','invoice' & 'files'. Once triggered the chabot sends a link to the user to upload the files to be processed. After the user confirms that they are done uploading all the files. The chatbot then displays the number of files that are processed at regular intervals and finally confirms that all the files have been processed succesfully.

## How to add the chatbot from power virtual agents to MS Teams
<ul>
  <li>Publish the latest bot content<br>
After creating a chatbot in the Power Virtual Agents portal, you must publish your bot before Teams users can interact with it. </li>
  <li>After publishing your bot, add the Teams channel to make the bot available to Teams users. This can be done by going to the section under optimize your bot and click on <b>Go to channels</b> and select Microsoft Teams and add the bot to Teams. </li>  
  <li>To share the bot to your entire organization, you have to click on the button that says 'Submit for admin approval'</li> 
</ul><br>  

## How does the admin approve the bot
The admin must first log in to Microsoft 365 admin center for MS Teams <code>https://admin.teams.microsoft.com/</code>
<br>On the left side action bar click on Teams App and go to the permission policies under it. Scroll through the list of pending policies and once you find the pending request for the chatbot change its status from submitted to published.

  
