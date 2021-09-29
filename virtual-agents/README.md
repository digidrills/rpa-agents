### Introduction
A topic is basically how a chatbot conversation plays out. All the topics mentioned below are conversations built for Microsoft Teams. <br>A chatbot can be triggered by using certain words that are pre-defined.<br> The chatbot will wait 60 minutes for a user to respond before the session is timed out. On the other hand if a cloud flow takes longer than 90 seconds to provide a response to the user, the session times out.  <br><br>It is important to note that chatbots built on power virtual agents are no-code chatbots.

### invoice-conversation-topic
<ul>
<li>Using keywords such as 'upload', 'files' and 'invoices' this conversation topic can be triggered.</li><br>
<li>Once triggered, the bot provides a link to a folder on OneDrive where the user can upload the files to be processed.</li><br>
<li>After the user is done uploading the files to the OneDrive, they should type 'yes' in the chat window, any other response will ask the user to confirm when all files are uploaded.</li>
<br><li> The chatbot will then, at regular intervals, display how many files have been processed. When there are no more files to be processed the chatbot will display the message "All files have been processed".</li>
<br><li> The user can then go back to the link where they have uploaded the files and see that there is a results folder where all processed files are stored.</li></ul>

### status-conversation-topic (deprecated)
This topic is used to display to the user the status of the files that have been already processed in a percentage form. The keyword to trigger this topic is 'status'.

