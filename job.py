from ffglory import job
#runs every 5 minutes in the chat where /start was called
job_queue = application.job_queue
job_queue.run_repeating(auto_accept_job, interval=300, first=10, chat_id=YOUR_CHAT_ID)  
# Replace YOUR_CHAT_ID with group chat ID