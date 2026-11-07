from ffglory import auto_accept
async def auto_accept_job(context: ContextTypes.DEFAULT_TYPE):
if guild_data['auto_accept_enabled']:
guild_data['pending_requests'] = mock_get_pending_requests(guild_data['guild_id'])
accepted = 0
for req in guild_data['pending_requests']:
if req['status'] == 'pending' and req['level'] >= guild_data['request_filters']['min_level'] and req['player_id'] not in guild_data['request_filters']['blacklist']:
if mock_accept_request(req['request_id']):
req['status'] = 'accepted'
stats = mock_get_player_stats(req['player_id'])
guild_data['members'].append({'id': req['request_id'], 'username': req['player_id'], 'role': 'Member', 'stats': stats})
accepted += 1
if accepted > 0:
job = context.job
await context.bot.send_message(chat_id=job.chat_id, text=f"Auto-accepted {accepted} join requests.")