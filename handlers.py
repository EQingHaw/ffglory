#Copyright(C)-@EQHdev
from ffglory import handlers
application.add_handler(CommandHandler("add_member", add_member))
application.add_handler(CommandHandler("remove_member", remove_member))
application.add_handler(CommandHandler("view_stats", view_stats))
application.add_handler(CommandHandler("announce", announce))
application.add_handler(CommandHandler("generate_report", generate_report))
application.add_handler(CommandHandler("toggle_auto_accept", toggle_auto_accept))
application.add_handler(CommandHandler("view_requests", view_requests))
application.add_handler(CommandHandler("accept_request", accept_request))
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))
